## Marta Vohnoutova - Mao -parallel count k-mer
## https://www.youtube.com/watch?v=7Kue7mIK9tE

## importing lib

import os,sys,time
from joblib import Parallel, delayed
from collections import Counter

## functions

def fasta_indexing(filename):
    infile = open(filename,'rb')

    chunksize = 1024*1024
    filepos = 0
    headstart = list()
    headend = list()

    ## read chunksize
    while True:
        content = infile.read(chunksize)
        if len(content) ==  0:
            break

        ## find headers - start
        chunkpos = 0
        while chunkpos != -1:
            chunkpos = content.find(b'>',chunkpos)
            if chunkpos != -1:
                headstart.append(chunkpos + filepos)
                chunkpos += 1
        ## find headers - end
        for i in range(len(headend),len(headstart)):
            chunkpos = max(0, headstart[i] - filepos)
            chunkpos = content.find(b'\n', chunkpos)
            if chunkpos != -1:
                headend.append(chunkpos + filepos)
        filepos += len(content)

    infile.close()

    ## eliminate wrong headers due to extra > in line
    for i in range(len(headstart) -1,0,-1):
        if headend[i] == headend[i-1]:
            del headstart[i]
            del headend[i]
    headstart.append(filepos)
    fastaindex = list()
    for i in range(len(headend)):
        seq_start = headend[i] + 1
        seq_end = headstart[i+1]-1
        fastaindex.append((seq_start, seq_end, seq_end-seq_start))
        
    ## load balancing
    fastaindex = sorted(fastaindex, key = lambda x: x[2], reverse = False)

    return fastaindex


def indexsequence(seq):
    pointer = 0
    seqindex = list()

    while len(seq) > pointer:
        ## find start of sequence
        potenstart = [seq.find(b'a',pointer),seq.find(b't',pointer),seq.find(b'c',pointer),seq.find(b'g',pointer)]

        realstart = min(potenstart)
        if realstart == -1:
            potenstart = [i for i in potenstart if i > -1]
            if len(potenstart) == 0:
                break
            realstart = min(potenstart)
        realend = seq.find(b'N',realstart)
        if realend == -1:
            realend = len(seq)
        seqindex.append((realstart,realend))
        pointer = realend

    return seqindex

        

def find_kmers(fasta,idx):
    ## read sequence
    infile = open(fasta,'rb')
    infile.seek(idx[0])
    seq =  infile.read(idx[1]-idx[0]+1).translate(transtable,b'\r\n\t')
    infile.close() ## close file after read each part to free memory

    subdict = dict()
    ## skip all unknown NNN letters and read onlz DNA
    seqindex = indexsequence(seq)

    for start,stop in seqindex:
        for i in range(start,stop-kmer_len+1):
            kmer = seq[i:i+kmer_len]
            if kmer not in subdict:
                subdict[kmer] = 1
            else:
                subdict[kmer] += 1

    return subdict

if __name__ == '__main__':

    file = '/JCU/Biopython/Biopython/Biodata/PlasmoDB-9.3_Pfalciparum3D7_Genome.fasta'
    kmer_len = 5
    transtable = bytes.maketrans(b'ATCGMRYKVHDBWmrykvhdbxnsw',b'atcgNNNNNNNNNNNNNNNNNNNNN')
    n_worker = os.cpu_count()

    start = time.time()
    my_index = fasta_indexing(file)
    index_time = time.time()-start

    ## make parallel run
    
    print('Indexing time ',index_time)

    start = time.time()
    
    results = Parallel(n_jobs=n_worker)(delayed(find_kmers)(file,z) for z in my_index)

    count_time = time.time()-start
    print('Count kmers time ',count_time)

        
    
          
     
    f = open('mao_results','w')
    for i in results:
        f.write('Kmer;Occurence\n')
        for k,v in i.items():
            f.write(str(k).lstrip('b')+';'+str(v)+'\n')
       
    f.close()
    del results
   

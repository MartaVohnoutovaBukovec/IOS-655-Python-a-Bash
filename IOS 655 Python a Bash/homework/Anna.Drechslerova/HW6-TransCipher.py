def trans_cipher(k):
  l= len(k)
  sk=sorted(k)
  print("Sorted key : ",sk)
  message="ne Ocpn uo idamihtngdea ry wr,ie hl onIpeeddr ea,w ndkawar e,veyO anrm  qyaantuiad  nuiocrsvou ue lmffoo gttronloe e Wr-ie hl odIne, dderlna apynig,pnsdd uny elhretecme aata  pngpi s ,Afsoo eonm  enegl rtypinap,rag pngpia m t haycbr meor.doTs  ioe smiitvsr Io,mtt urd,eetpp an aig y tmhmbcardoe r Oo-l tnyi ahsdnon hngtimre o   ."
  division_message=[message[i:i+l] for i in range(0, len(message), l)]
  print("Divided message:  ",division_message)  #prints divided message - just to make sure it works correctly
  dmdiv=division_message[0]
  for n in range(len(message)):
      dmdiv= division_message[n]     
      dict_key={sk[0]:dmdiv[0],sk[1]:dmdiv[1],sk[2]:dmdiv[2],sk[3]:dmdiv[3],sk[4]:dmdiv[4]}      
      print(dict_key.values())

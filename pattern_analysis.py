import itertools as it
from collections import OrderedDict as od

# A protein sequence (like your original DNA example)
# A protein sequence (like your original DNA example)
protein = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYHAEVSHHHTQALKFPDPHSHGRLYYVMGAAHDFARNLKALVNLGSSPVGNKSLLAAPLDVRPGLDVQNKWLELEVPGDVGVTFACKFEQTLVKAEEFHTAGTTFVGVEAVGGHPYLKAVNDHMLDALGVWNACFVKVLKGLKTLVKEFLALFLSVVNHDVTECVHANALEVMPLTLGFAGLYVTLQSAFDGAFGPDKVLKLVPASGNEHVFDPASVDTLKLVEHVLKNKHAVAYCFTVLDGFVTADGGREVPAAKALSFNKKHGQKLVPHQRLGATPELNYWVRHKGKHEGMWEG"


# Dictionary to store amino acid patterns
patterns = od()

# Find all 2-amino acid combinations
all_pairs = list(it.combinations(protein, 2))

for pair in all_pairs:
    pattern = ''.join(pair)
    if pattern in protein:
        patterns[pattern] = protein.count(pattern)

print("Common 2-amino acid patterns in hemoglobin:\n")
for pattern, count in sorted(patterns.items(), key=lambda x: x[1], reverse=True):
    print(f'{pattern}: {count} occurrences')
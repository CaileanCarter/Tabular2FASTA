import sys
#Tabular2FASTA converts assembly data in a tabular format and converts it to FASTA. 

try:
    if sys.argv[1].endswith(".txt"): #checks file format is .txt
        TabularData = open(sys.argv[1])
    else:
        SystemExit("File provided is not a .txt file")
except:
    raise SystemExit("No file provided")

FASTA_version = open(sys.argv[1].replace(".txt", ".fasta"), "w")

print("Converting to FASTA now...")

for row in TabularData:
    if row.startswith("S"):
        index, identifier, sequence, *_ = row.split()

        FASTA_version.write(">" + identifier + "\n" + sequence + "\n")

print("Conversion to FASTA format is completed. Your new fasta file is: " + FASTA_version.name)

TabularData.close()
FASTA_version.close()
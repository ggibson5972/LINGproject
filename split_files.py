import os
path = 'pubmed_seg_txts/'
outdir = 'split_pubmed_txts/'

for filename in os.listdir(path):
    base = filename[:13]
    outfile = outdir + base + "_out"
    print("outfile: ", outfile)
    true_file = path + filename
    if true_file.endswith(".txt"):
        command = "split -d -l 50000 " + true_file + " " + outfile
        print(command)
        os.system(command)

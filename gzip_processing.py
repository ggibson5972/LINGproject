import gzip
import shutil


i = 13
while i < 31:
    domain = "pubmed19n00" + str(i)
    gzip_file = domain + ".xml.gz"
    with gzip.open(gzip_file, 'rb') as infile:
        with open(domain + ".xml", 'wb') as outfile:
            shutil.copyfileobj(infile, outfile)
    i += 1

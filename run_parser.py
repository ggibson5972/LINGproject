import benepar
import nltk
import sys
nltk.download('punkt')
benepar.download('benepar_en2')
out_dir = "../../parser_data/parsed_pubmeds/"


assert_message = "Please provide an input file for run_parser.py to parse."
assert len(sys.argv) == 2, assert_message

# sys.argv[1] should be name of text file to parse
outfile = open(out_dir + "parsed_" + sys.argv[1], "w+")
parser = benepar.Parser("benepar_en2")
f = open(sys.argv[1], "r")
line = f.readline()
while line != "":
    line = line.strip().split(' ')
    tree = parser.parse(line)
    tree_str = tree.pformat(margin=10000)
    outfile.write(tree_str + '\n')
    line = f.readline()
    # break
outfile.close()
f.close()

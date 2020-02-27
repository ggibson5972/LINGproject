import os
import subprocess
import time
path = '../envs/local/parser_data/split_pubmed_txts/'
outpath = '../envs/local/parser_data/parsed_rnng_pubmeds/'

with open('start_node_rnng.pbs') as pfile:
    string = pfile.readlines()

for filename in os.listdir(path):
    true_file = path + filename
    if not true_file.endswith(".py"):
        print("Starting computational node for mini-batch...")

        # Run parser on true_file
        out_file = outpath + filename + "_parsed.txt"
        parse_command = "python scripts/bert_parse.py bert_models/english-wwm " + true_file + " --beam_size 10 > " + out_file
        gnu_command = "module load gnu/6.1.0"
        print("Parsing " + true_file + "...")
        new_string = string[:-1] + [gnu_command + '\n'] + [parse_command + '\n']
        # print(new_string)
        with open('temp_pbs_file.pbs', 'w') as tempfile:
            for line in new_string:
                tempfile.write(line)
        subprocess.run(['qsub', 'temp_pbs_file.pbs'])
        print("DONE", true_file)
        time.sleep(0.5)

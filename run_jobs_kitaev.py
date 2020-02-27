import os
import subprocess
path = '../../parser_data/split_pubmed_txts/'


for filename in os.listdir(path):
    true_file = path + filename
    if not true_file.endswith(".py"):
        # Start job on computational node
        #job_command = "qsub -I -l nodes=1:ppn=4,mem=16GB -l walltime=2:00:00"
        print("Starting computational node for mini-batch...")
        subprocess.run(["qsub", "-I", "-l", "nodes=1", "ppn=4", "mem=16GB", "-l", "walletime=2:00:00"])
        #os.system(job_command)
        print("DONE")

        # Start environment to run parsing
        env1_command = "conda init parser"
        env_command = "conda activate parser"
        print("Activating conda environment...")
        os.system(env1_command)
        os.system(env_command)
        print("DONE")

        # Get into parser directory
        dir_command = "cd ../self-attentive-parser/benepar"
        print("Changing to kitaev parser directory...")
        os.system(dir_command)
        print("DONE")

        # Run parser on true_file
        parse_command = "python run_kitaev_parserpy " + true_file
        print("Parsing " + true_file + "...")
        os.system(parse_command)
        print("DONE")

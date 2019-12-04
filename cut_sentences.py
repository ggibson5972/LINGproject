def cut_sentences(infile_name, outfile_name):
    f = open(infile_name, "r", encoding='utf-8')
    output = open(outfile_name, "w+", encoding='utf-8')
    line = f.readline()
    while line != "":
        if len(line) <= 300:
            output.write(line)
        line = f.readline()

    f.close()
    output.close()


def sentence_count(file_name):
    f = open(file_name, "r+")
    line = f.readline()
    count = 1
    while line != "":
        line = f.readline()
        count += 1
    f.close()
    return count


cut_sentences("segmented_pubmed1.txt", "cut-segmented-pubmed1.txt")
sentence_count = sentence_count("cut-segmented-pubmed1.txt")

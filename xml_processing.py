import os
import syntok.segmenter as segmenter
from xml.dom import minidom


def read_xml(source, filename):
    abstracts = source.getElementsByTagName('AbstractText')
    write_to_txt(abstracts, filename)


def write_to_txt(abstracts, filename):
    outfile_name = filename.replace('.xml', '.txt')
    outfile = open("pubmed_txts/" + outfile_name, "a+", encoding='utf-8')
    for elem in abstracts:
        data = elem.firstChild.data
        outfile.write(data)
    outfile.close()
    text_stream = open(outfile_name, "r+", encoding='utf-8').read()
    segout_name = outfile_name.replace('.txt', '_seg.txt')
    segment_abstract(text_stream, segout_name)


def segment_abstract(text_stream, segout_name):
    segmented_outfile = open("pubmed_seg_txts/" + segout_name, "a+", encoding='utf-8')
    for paragraph in segmenter.process(text_stream):
        for sentence in paragraph:
            for token in sentence:
                segmented_outfile.write(token.value + ' ')
            segmented_outfile.write('\n')
        print()
    segmented_outfile.close()


def main():
    for filename in os.listdir("pubmed_xmls"):
        if filename.endswith(".xml"):
            source = minidom.parse(filename)
            read_xml(source, filename)


if __name__ == '__main__':
    main()

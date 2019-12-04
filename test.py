# import re
#
# sentence_begin = re.compile(r'\(S', re.IGNORECASE)
#
# test = '(S (PRN (XX () (XX -) (XX -) (XX ))) (XX -) (NP (XX alpha) (XX Bisabolol)) (VP (XX has) (NP (NP (XX a) (XX primary) (XX antipeptic) (XX action))) (PP (XX depending) (PP (XX on) (NP (XX dosage)))) (XX ,) (SBAR (WHNP (XX which)) (S (VP (XX is) (XX not) (VP (XX caused) (PP (XX by) (NP (NP (XX an) (XX alteration)) (PP (XX of) (NP (XX the) (XX p) (XX H) (XX value)))))))))) (XX .))'
#
# def convert_sentence(sentence):
#     paren_tracker = 0
#     while tracker:
#         if sentence_begin.search(test):
#             print('this has a sentence')
#         else:
good_file = r'C:\Users\grace\PycharmProjects\LINGproject\build\rnng-pubmed-trees.txt'
bad_file = r'C:\Users\grace\PycharmProjects\LINGproject\build\kitaev-pubmed-trees.txt'
# key value dictionary with mapping
# parathenses tracking with while count
with open(bad_file, 'r') as fh:
    with open('test.txt', 'w') as newfile:
        for line in fh:
            #print(line)
            newfile.write(line)

import nltk
from nltk import Tree
from nltk.compat import unicode_repr

rnng_file = open("rnng-pubmed-trees.txt", 'r', encoding='utf-8')
kitaev_file = open()


def traverse_tree(tree_str):
    for subtree in tree_str:
        if type(subtree) == nltk.tree.Tree:
            traverse_tree(subtree)
        break


# def check_span(tree_pos):
#     for span in tree_pos:
#         if t[span].height > 1:
#             print(t[span].label(), t[span].leaves)


s = rnng_file.readline()
while s != "":
    t = nltk.tree.Tree.fromstring(s)
    for s in t.subtrees(lambda t: t.height() == 3):
        print(s.label(), s.leaves())
    tpos = t.treepositions()  # list of child positions
    # for span in t.treepositions():
    #     if t[span].height(
    #     print(t[span].label())
    #     if t[span].height > 1:
    #         print(t[span].label(), t[span].leaves)
    s = ""

rnng_file.close()

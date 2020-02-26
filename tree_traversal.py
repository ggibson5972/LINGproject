import re
import nltk
from nltk.corpus import treebank
# SEMANTICS DON'T MATTER

good_file = r"C:\Users\user\PycharmProjects\LINGproject\rnng_pubmed_trees.txt"
bad_file = r"C:\Users\user\PycharmProjects\LINGproject\parsed_pubmed19n0001_out00"


corr_full_count = 0
corr_sub_count = 0
incorr_full_count = 0
incorr_sub_count = 0


def leaves_to_file(k_tree):
    k_leaves = k_tree.leaves()
    with open("k_leaves.txt", 'a') as k_out:
        k_out.write(str(k_leaves))


def traverse_tree(tk, tr):
    global incorr_sub_count, corr_sub_count
    # check span length when comparing spans from one tree to nested spans in another tree
    for subtree_k, subtree_r in zip(tk, tr):
        if type(subtree_k) == nltk.tree.Tree and type(subtree_r) == nltk.tree.Tree:
            traverse_tree(subtree_k, subtree_r)
    k_leaves = tk.leaves()
    r_leaves = tr.leaves()
    k_label = tk.label()
    r_label = tr.label()
    #TODO: check span size first
    # check words next
    # if both match: find subtrees
    #   recurse(subtrees)
    if len(k_leaves) >= 3 and len(r_leaves) >= 3:
        if k_leaves == r_leaves:
            corr_sub_count += 1
        else:
            incorr_sub_count += 1
        outfile.write("Subtree content is identical: \n")
        # if k_label != r_label:
        #     outfile.write("POS labels are not identical!\n")
        outfile.write(str(k_label) + " ")
        outfile.write(str(k_leaves) + '\n')
        outfile.write(str(r_label) + " ")
        outfile.write(str(r_leaves) + '\n\n')


with open(bad_file, "r") as kitaev:
    with open(good_file, "r") as rnng:
        for line_k in kitaev:
        # line_k = kitaev.readline()
        # line_r = rnng.readline()
        # while line_k != "" and line_r != "":
        #     line_r_ex = re.sub('\(XX [()]+\)', '(XX BRACKET)', line_r)
            #line_k_ex = re.sub('\(XX [()]+\)', '(XX BRACKET)', line_k)
            # try:
        # tree_r = nltk.tree.Tree.fromstring(line_r_ex)
            try:
                tree_k = nltk.tree.Tree.fromstring(line_k)
                print(' '.join(tree_k.leaves()))
            except ValueError:
            #     print(line_r, line_r_ex, line_r.count('('), line_r.count(')'))
                print(line_k, line_k.count('('), line_k.count(')'))
                raise
            # TODO: put kitaev leaves into rnng parser (need to generate files w trees)
            # leaves_to_file(tree_k)
        #     with open("comparison.txt", 'a') as outfile:
        #         outfile.write("kitaev: " + line_k + '\n')
        #         outfile.write("rnng: " + line_r + '\n')
        #         if tree_k.leaves() == tree_r.leaves():
        #             corr_full_count += 1
        #         else:
        #             incorr_full_count += 1
        #         traverse_tree(tree_k, tree_r)
        #     line_k = kitaev.readline()
        #     line_r = rnng.readline()
        # with open("sentence_counts.txt", 'a') as outfile:
        #     outfile.write("Correct full trees: " + str(corr_full_count))
        #     outfile.write("Incorrect full trees: " + str(incorr_full_count))
        #     outfile.write("Total full trees: " + str(full_tree_count))
        #     outfile.write("Correct subtrees: " + str(corr_sub_count))
        #     outfile.write("Incorrect subtrees: " + str(incorr_sub_count))
        #     outfile.write("Total subtrees: " + str(full_subtree_count))
        #     average span size, most common tags,
# kitaev.close()
# rnng.close()


# def check_span(tree_pos):
#     for span in tree_pos:
#         if t[span].height > 1:
#             print(t[span].label(), t[span].leaves)

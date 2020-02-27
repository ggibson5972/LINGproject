import nltk
from nltk.corpus import treebank
# SEMANTICS DON'T MATTER

rnng_file = r"C:\Users\grace\PycharmProjects\LINGproject\pubmed19n0001_out00_parsed.txt"
kitaev_file = r"C:\Users\grace\PycharmProjects\LINGproject\parsed_pubmed19n0001_out00"


corr_full_count = 0
corr_sub_count = 0
incorr_full_count = 0
incorr_sub_count = 0


# def leaves_to_file(k_tree):
#     k_leaves = k_tree.leaves()
#     with open("k_leaves.txt", 'a') as k_out:
#         k_out.write(str(k_leaves))
#
#
# def traverse_tree(tk, tr):
#     global incorr_sub_count, corr_sub_count
#     # check span length when comparing spans from one tree to nested spans in another tree
#     for subtree_k, subtree_r in zip(tk, tr):
#         if type(subtree_k) == nltk.tree.Tree and type(subtree_r) == nltk.tree.Tree:
#             traverse_tree(subtree_k, subtree_r)
#     k_leaves = tk.leaves()
#     r_leaves = tr.leaves()
#     k_label = tk.label()
#     r_label = tr.label()
#     # TODO: check span size first
#     #   check words next
#     #   if both match: find subtrees
#     #   recurse(subtrees)
#     if len(k_leaves) >= 3 and len(r_leaves) >= 3:
#         if k_leaves == r_leaves:
#             corr_sub_count += 1
#         else:
#             incorr_sub_count += 1


def read_files():
    # bad klines:  36
    # bad rlines:  308
    k_leaves = open("k_leaves.txt", 'w')
    good_trees = open("r_trees.txt", 'w')
    with open(kitaev_file, "r") as kitaev, open(rnng_file, "r") as rnng:
        for line_k, line_r in zip(kitaev, rnng):
            try:
                tree_k = nltk.tree.Tree.fromstring(line_k)
                kleaves = ' '.join(tree_k.leaves())
            except ValueError:
                continue
            # try:
            #     tree_r = nltk.tree.Tree.fromstring(line_r)
            #     #rleaves = ' '.join(tree_r.leaves())
            # except ValueError:
            #     continue
                # print(line_k, line_k.count('('), line_k.count(')'))
            if tree_k:
                k_leaves.write(kleaves + '\n')
                good_trees.write(line_r)
    k_leaves.close()
    good_trees.close()
    # TODO: put kitaev leaves into rnng parser (need to generate files w trees)


read_files()

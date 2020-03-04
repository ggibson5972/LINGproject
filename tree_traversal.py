"""
GOAL: Compare and raise flag if formats dont match (e.g.: one has VP(has (JJ test)) vs VP(has) (JJ test)
    Example tree: (S (NP (DET The) (NN cat)) (VP (TV ate) (NP (DET the) (NN food)) (. .))
    Constituents: (DET The), (NN cat),
    Span: (NP (DET the) (NN cat))
"""
import nltk
from nltk.corpus import treebank
import argparse
import collections

# SEMANTICS DON'T MATTER.

COMPARE = lambda x, y: collections.Counter(x) == collections.Counter(y)
# TODO: Possibly expand on constituents list. Note: RNNG lines are less descriptive giving XX as general case for words.
K_TO_R_MAPPING = {'S': 'S', 'PRN': 'PRN', '-LRB- -LRB-': 'XX (', ': -': 'XX -', '-RRB- -RRB-': 'XX )', 'NP': 'NP',
                  'JJ': 'XX', 'NN': 'XX', 'VP': 'VP'}


def read_files(rnng_file, kitaev_file):
    """
    :param rnng_file: Parsed file from rnng parser.
    :param kitaev_file: Parsed file from kitaev parser.
    :return: Outputted files with information regarding exceptions raised and mismatch pairings of Spans.
    """
    # k_trees = open("analysis_output/output_k_trees_data.txt", 'w')  # Already parsed sentences via Grace.
    # r_trees = open("analysis_output/output_r_trees_data.txt", 'w')  # To be transformed parsed sentences...

    # Open files to be written to for analysis and comparison later.
    match = True
    exceptions = open("analysis_output/output_r_trees_data.txt", 'w')  # Report exceptions on parsing with line number.
    mismatch_file = open("analysis_output/mismatch_pairs.txt", 'w')  # Report exceptions on parsing with line number.
    with open(kitaev_file, "r") as kitaev, open(rnng_file, "r") as rnng:
        # Grab the first line of each file respectively & track the line index (the line number in the file).
        for index, (line_k, line_r) in enumerate(zip(kitaev, rnng)):
            mismatch = False
            try:
                # Parse using nltk.tree.Tree model.
                k_nltk_obj = nltk.tree.Tree.fromstring(line_k)
                # Create lists of individually parsed words.
                k_leaves = k_nltk_obj.leaves()

                # Remove filler.
                for x in ['-RRB-', '-LRB-']:  # Not sure what these symbols stand for yet.
                    if x in k_leaves:
                        k_leaves.remove(x)

                # Replace parser-specific constituents with literals.
                k_leaves = ['[' if wd == "-LSB-" else wd for wd in k_leaves]
                k_leaves = [']' if wd == "-RSB-" else wd for wd in k_leaves]

                # Combine list of words to end sentence result.
                k_full_sentence = ' '.join(k_leaves)  # Full sentence as parsed.
            except Exception as e:
                exceptions.write(f'Exception while handling line {index + 1} in kitaev_file with error: {e}')
            try:
                # Same as above but for rnng file.
                r_nltk_obj = nltk.tree.Tree.fromstring(line_r)
                r_leaves = r_nltk_obj.leaves()
                r_full_sentence = ' '.join(r_leaves)  # Full sentence as parsed.
            except Exception as e:
                exceptions.write(f'Exception while handling line {index + 1} in rnng_file with error: {e}.')

            # CHECK IF THERE IS A MISMATCH IN HOW IT WAS PARSED.
            matching = COMPARE(k_leaves, r_leaves)  # This means the lists are NOT identical if false.
            if not matching:
                # Do logic here to raise and write to file data points that don't match.
                mismatch_file.write(
                    f'MISMATCH PARSE FOUND ON LINE {index + 1}: \nKITAEV:\n{str(k_leaves)}\n{k_full_sentence}\n'
                    f'RNNG:\n{str(r_leaves)}\n{r_full_sentence}\n\n\n')
            print(f'Line {index + 1} Scanned, Matching = {str(matching).upper()}')

            # Write sentences to each file.
            # k_trees.write(k_full_sentence + '\n')
            # r_trees.write(r_full_sentence + '\n')
    mismatch_file.close()
    exceptions.close()
    print('Successfully analyzed all lines!')
    # k_trees.close()
    # r_trees.close()


if __name__ == "__main__":
    # In python 'Run' -> 'Edit Configuration', set working directory to project folder.
    parser = argparse.ArgumentParser(description='Script to traverse both trees.')
    parser.add_argument('-r', '--rnng', default='data/parsed_rnng_pubmed_data.txt', help='rnng_file to be used.')
    parser.add_argument('-k', '--kitaev', default='data/parsed_kitaev_pubmed_data.txt', help='kitaev_file to be used.')
    args = parser.parse_args()
    read_files(args.rnng, args.kitaev)

""" Below is test code to be expanded upon later... """
# TODO: put kitaev leaves into rnng parser (need to generate files w trees)
# corr_full_count = 0
# corr_sub_count = 0
# incorr_full_count = 0
# incorr_sub_count = 0
# def leaves_to_file(k_tree):
#     k_leaves = k_tree.leaves()
#     with open("output_k_trees_data.txt", 'a') as k_out:
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
# bad klines:  36
# bad rlines:  308

import re
from collections import Counter


def into_token(inputfile, output='corpus_output.txt'):
    """处理原始文档：去除标点符号和纯数字，以及空行"""
    with open(inputfile, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
        text = ''.join(re.sub(r'(?<=\b)\d+(?=\b)|[^\w\s]', '', line).lower() for line in lines if line != '\n'
                       )  # punctuation marks and numbers between two space  and drop vacuum lines
    with open(output, 'w', encoding='utf-8') as fp:
        fp.write(text)


def vocab_count(file):
    """全文词表  {单词：计数}"""
    vocabulary = list()
    with open(file, 'r', encoding='utf-8') as fp:
        text = fp.read()
        words = text.split()
        vocabulary.extend(words)
        # print(vocabulary)
    words_count = Counter(vocabulary)
    return words_count


def matrix(file):
    line_vocabulary = list()
    max_wordsperline_flag = 0
    with open(file, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    for line in lines:
        max_wordsperline_flag = max_wordsperline_flag if len(line) <= max_wordsperline_flag else len(line)
        words = line.split()
        line_vocabulary.append(words)
    # print(line_vocabulary)

    num_lines = len(lines)
    matrix = [[0] * max_wordsperline_flag for _ in range(num_lines)]

    words_count = all_vocab(file)

    for i, line_liststr in enumerate(line_vocabulary):
        for (j, word) in enumerate(line_liststr):
            matrix[i][j] = words_count[word]

    return matrix, lines

# a = matrix('pg35_corpus.txt')
# print(a[0])
# #print(a[1][0])

# a = all_vocab('pg35_corpus.txt')
# print(a)  # Counter({'the': 2466, 'and': 1296, 'of': 1281, 'i': 1241, 'a': 864, 'to': 760


# import robust_pca
#
# L,S = robust_pca.robust_pca(array,devices="cpu", max_iter_pass=200)
#
# print(L)
# print(S)

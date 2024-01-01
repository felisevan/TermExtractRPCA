import re
from collections import Counter

import matplotlib.pyplot as plt
from wordcloud import WordCloud


def corpus_transform(inputfile, output='corpus_output.txt'):
    """Treatment of the original document: removing the punctuation symbols, pure numbers and the empty lines"""
    with open(inputfile, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
        text = ''.join(re.sub(r'(?<=\b)\d+(?=\b)|[^\w\s]', '', line).lower() for line in lines if line != '\n'
                       )  # punctuation marks and numbers between two space  and drop vacuum lines
    with open(output, 'w', encoding='utf-8') as fp:
        fp.write(text)
    print(output + ' has been transformed')


def vocab_count(file):
    """Full text Words: {word: count}"""
    vocabulary = list()
    with open(file, 'r', encoding='utf-8') as fp:
        text = fp.read()
        words = text.split()
        vocabulary.extend(words)
    words_count = Counter(vocabulary)
    return words_count


def word_cloud(word_dict):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_dict)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

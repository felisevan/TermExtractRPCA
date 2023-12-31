from collections import Counter

import nltk
import sklearn.feature_extraction
import stopwordsiso as stopwords
import torch

import robust_pca


def get_keywords(s):
    sentences = nltk.sent_tokenize(s)
    vectorizer = sklearn.feature_extraction.text.CountVectorizer(
        stop_words=list(stopwords.stopwords("en"))
    )
    L, S = robust_pca.robust_pca(
        torch.tensor(
            vectorizer.fit_transform(sentences).toarray(), dtype=torch.float64
        ),
        max_iter_pass=3,
    )
    return sorted(
        [
            (name, value.item())
            for name, value in zip(vectorizer.get_feature_names_out(), S.sum(dim=0))
        ],
        key=lambda x: x[1],
        reverse=True,
    )


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


if __name__ == "__main__":
    with open("../pg35_corpus.txt", encoding="utf-8") as f:
        data = f.read()
        out = get_keywords(data)
        print(out)

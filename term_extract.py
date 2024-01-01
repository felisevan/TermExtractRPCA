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

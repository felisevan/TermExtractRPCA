import stopwordsiso as stopwords
import sklearn.feature_extraction
import robust_pca
import nltk
import torch


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


if __name__ == "__main__":
    with open("pg35.txt", encoding="utf-8") as f:
        data = f.read()
        out = get_keywords(data)
        print(out)

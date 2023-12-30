from sklearn.feature_extraction.text import CountVectorizer
import re

with open('pg35.txt', 'r') as fp:
    lines = fp.readlines()
    text = ''.join(re.sub(r'(?<=\b)\d+(?=\b)|[^\w\s]', '', line).strip('\n') for line in lines
                   )  # punctuation marks and numbers between two space
with open('pg35_corpus.txt', 'w') as fp:
    fp.write(text)

vectorizer = CountVectorizer(input='filename', decode_error='ignore', lowercase=True, analyzer='word')
vec = vectorizer.fit_transform(['pg35_corpus.txt'])
array = vec.toarray()
feature_names = vectorizer.get_feature_names_out()
print(array)
# print(array.shape) (1,7206)   ???????? 词频矩阵有问题  需要建模整个文章（改建模方式）
print(feature_names)

# import robust_pca
#
# L,S = robust_pca.robust_pca(array,devices="cpu", max_iter_pass=200)
#
# print(L)
# print(S)

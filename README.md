# TermExtractRPCA

A Robust-PCA Approach for Term Extracting


---


_Limited by the algorithm itself, we do not optimize Chinese, and the program can only process at the word level without
considering the semantic level._

Robust-pca is used from [https://github.com/14MBD4/pytorch-RPCA]("https://github.com/14MBD4/pytorch-RPCA")

The corpus is translated from an article from website, and we have been authorized by the original author



---

## usage:

**transforming raw corpus to remove the punctuation symbols, pure numbers and the empty lines**

``python main.py corpus.txt corpus_transform``

**give out terms with values after rpca**

``python main.py corpus_transformed.txt``

**give out words with counts in the article*(with terms and corresponding values)***

``python main.py corpus_transformed.txt vocab_count``

**give out word-cloud figure*(with terms and corresponding values)***

``python main.py corpus_transformed.txt word_cloud``

give out word-cloud figure based on the user's own choices or combination of results

``python main.py self_word_cloud``

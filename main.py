import sys

from functional_tools import corpus_transform, vocab_count, word_cloud
from term_extract import get_keywords

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise IndexError("specified file or functions needed")

    if 'self_word_cloud' in sys.argv and len(sys.argv) == 2:
        word_weight_dict = {}
        while True:
            word = input("word input:（ 'qqq' to quit）: ")
            if word.lower() == 'qqq':
                break
            weight = float(input("weight input: "))
            word_weight_dict[word] = weight
        print("word_weight_dict: ", word_weight_dict)
        word_cloud(word_weight_dict)
        exit()

    if len(sys.argv) > 2 and "corpus_transform" in sys.argv:
        out_name = input("the name of the output file: ")
        corpus_transform(sys.argv[1], out_name)
        exit()

    with open(sys.argv[1], encoding="utf-8") as f:
        data = f.read()
        out = dict(get_keywords(data))
        print(out)

    if len(sys.argv) > 2 and "vocab_count" in sys.argv:
        print('vocab_count: ', vocab_count(sys.argv[1]))

    if len(sys.argv) > 2 and "word_cloud" in sys.argv:
        word_cloud(out)
        exit()

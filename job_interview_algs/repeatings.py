TEXT = """abba com mother bill mother com 
abba dog abba mother com"""


def secuenced_words(txt):
    """
        Function identifies the three words
        most often repeated as a group, regardless of the
        words order in the group
    """
    word_list = txt.split()
    collector = dict()
    for idx in range(1, len(word_list)-1):
        item = frozenset([word_list[idx-1], word_list[idx], word_list[idx+1]])
        if item not in collector:
            collector[item] = 1
        else:
            collector[item] += 1

    return list(sorted(collector)[0])


if __name__ == "__main__":
    print(secuenced_words(TEXT))

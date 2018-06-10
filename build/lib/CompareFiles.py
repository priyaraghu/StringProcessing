from HelpLib.File2Words import File2Words


def compare(file1 , file2):
    words = File2Words(file1)
    dict_words = File2Words(file2)
    return set(words) - set(dict_words)


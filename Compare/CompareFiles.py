from HelpLib.File2Words import File2Words

''' function to check the spellings of words with a dictionary.
   Dictionary is also a file with words with correct spellings
   This function takes 2 arguments file1 is the input file with 
   a list of words and file2 is the dictionary file with the 
   correct spellings '''


def compare(file1 , file2):
    try:
        words = File2Words(file1)
        dict_words = File2Words(file2)
        for word in words:
            if word not in dict_words:
                print(word)
    except FileNotFoundError as e:
        raise
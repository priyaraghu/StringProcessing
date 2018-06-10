def File2Words(filename):
    try:
        with open(filename) as file:
            words = file.read().split()
            return words
    except FileNotFoundError:
        raise





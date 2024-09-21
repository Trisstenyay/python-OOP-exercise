import random # Import the random module for generating random choices


class WordFinder:
    """ Find random words from a file

    >>> wf = WordFinder("/home/trisstenyay/python/python-oo-practice/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    """
    def __init__(self, filepath):
        """Read the file and report the number of words read."""
        self.words = self.read_words(filepath)
        print(f"{len(self.words)} words read")


    def read_words(self, filepath):
        """Read words from the given file and return a list of words."""
        with open(filepath, "r") as file: # Open the file in read mode
            return [line.strip() for line in file] # Strip newlines and create a list
    

    def random(self):
        """Return a random word from the list of words."""
        return random.choice(self.words) # Pick a random word from the words list



wf = WordFinder("/home/trisstenyay/python/python-oo-practice/words.txt")
rw = wf.random()
print(rw)
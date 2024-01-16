import re  # needed to remove punctuation
from nltk.stem import PorterStemmer  # for stemming


class Document:
    def __init__(self, lines):
        self.lines = lines

    # add tokenization: split on whitespace, converts to lower case,  remove punctuation, add stemming
    def tokenize(self) -> list[str]:
        text_to_tokenize = ' '.join(self.lines)  # join the lines into one string
        words = re.split(r'\s+', text_to_tokenize)  # divide at every whitespace
        # words = text_to_tokenize.split()
        words = [word.lower() for word in words]  # lower case

        additional_signs = ".','':'';'!';'?'"  # remove these signs, see also line below
        cleaned_words = [re.sub(f'[{additional_signs}]', '', word) for word in words]
        cleaned_words = list(filter(None, cleaned_words))  # filter out empty bits

        # Create  instance of Porter Stemmer and use it on every word of variable cleaned_words
        porter_stemmer = PorterStemmer()
        stemmed_words = [porter_stemmer.stem(word) for word in cleaned_words]
        return stemmed_words

class Article:
    def __init__(self, author, magazine, title, word_count):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.word_count = word_count
        author.articles.append(self)
        magazine.articles.append(self)

    @property
    def word_count(self):
        return self._word_count
    
    @word_count.setter
    def word_count(self, new_wc):
        if new_wc >= 0:
            self._word_count = new_wc
        else:
            raise ValueError('word count cannot be negative')
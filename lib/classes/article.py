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
    def word_count(self, new_word_count):
        if new_word_count >= 0:
            self._word_count = new_word_count
        else:
            raise ValueError('word_count cannot be negative')
    
    def __repr__(self) -> str:
        return f"<Article {self.title}>"

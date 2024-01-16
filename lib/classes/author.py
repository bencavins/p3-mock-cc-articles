class Author:
    def __init__(self, name):
        self.name = name
        self.articles = []
    
    @property
    def name(self):
        """Getter function for name"""
        return self._name
    
    @name.setter
    def name(self, new_name):
        """Setter function for name"""
        if len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError('name must be more than 0 chars')

    def get_magazines(self):
        result = []
        for article in self.articles:
            result.append(article.magazine)
        return result
        # return [article.magazine for article in self.articles]

    def has_written_for_magazine(self, magazine):
        # for article in self.articles:
        #     if article.magazine == magazine:
        #         return True
        # return False
        return magazine in self.get_magazines()

    def __repr__(self) -> str:
        return f"<Author {self.name}>"

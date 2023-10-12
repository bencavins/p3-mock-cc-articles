class Author:
    def __init__(self, name):
        self.name = name
        self.articles = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError('name must be > 0 chars')

    def get_magazines(self):
        # zines = []
        # for article in self.articles:
        #     if article.magazine not in zines:
        #         zines.append(article.magazine)
        # return zines
        return set([article.magazine for article in self.articles])

    def has_written_for_magazine(self, magazine):
        for article in self.articles:
            if article.magazine == magazine:
                return True
        return False
        # return magazine in self.get_magazines()

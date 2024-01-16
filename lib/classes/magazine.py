class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
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

    def get_authors(self):
        result = []
        for article in self.articles:
            result.append(article.author)
        return result

    def get_article_titles(self):
        pass

    def get_longest_article(self):
        pass

    def get_average_word_count(self):
        pass

    def get_top_contributor(self):
        """Note this method is an optional stretch goal"""
        pass

    def __repr__(self) -> str:
        return f"<Magazine {self.name}>"

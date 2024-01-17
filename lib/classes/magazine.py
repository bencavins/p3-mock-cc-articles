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
        result = []
        for article in self.articles:
            result.append(article.title)
        return result

    def get_longest_article(self):
        if len(self.articles) == 0:
            return None
        longest = self.articles[0]
        for article in self.articles:
            if article.word_count > longest.word_count:
                longest = article
        return longest

    def get_average_word_count(self):
        if len(self.articles) == 0:
            return 0
        total = 0
        count = 0
        for article in self.articles:
            total += article.word_count  # total = total + article.word_count
            count += 1  # count = count + 1
        return total / count

    def get_top_contributor(self):
        """Note this method is an optional stretch goal"""
        author_dict = {}
        for article in self.articles:
            author = article.author
            if author not in author_dict:
                author_dict[author] = 1
            else:
                author_dict[author] += 1  # author_dict[author] = author_dict[author] + 1
        
        top = None
        for author in author_dict:
            article_count = author_dict[author]
            if top is None:
                top = [author, article_count]
            else:
                if top[1] < article_count:
                    top = [author, article_count]
        return top[0]

    def __repr__(self) -> str:
        return f"<Magazine {self.name}>"

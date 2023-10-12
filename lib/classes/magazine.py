class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
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

    def get_authors(self):
        return set([article.author for article in self.articles])

    def get_article_titles(self):
        # titles = []
        # for article in self.articles:
        #     titles.append(article.title)
        # return titles
        return [article.title for article in self.articles]

    def get_longest_article(self):
        if len(self.articles) == 0:
            return None
        longest = self.articles[0]
        for article in self.articles:
            if article.word_count > longest.word_count:
                longest = article
        return longest
        # (article) => article.word_count
        # return max(self.articles, key=lambda article: article.word_count)

    def get_average_word_count(self):
        total = 0
        count = 0
        for article in self.articles:
            total += article.word_count
            count += 1
        return total / count
        # return sum([article.word_count for article in self.articles]) / len(self.articles)

    def get_top_contributor(self):
        """Note this method is an optional stretch goal"""
        author_set = self.get_authors()
        author_list = [article.author for article in self.articles]
        top_dog = None
        total = 0
        for current_author in author_set:
            count = 0
            for auth in author_list:
                if auth == current_author:
                    count += 1
            if count > total:
                top_dog = current_author
                total = count
        return top_dog

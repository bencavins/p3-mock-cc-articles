#!/usr/bin/env python3
import ipdb;

from classes.author import Author
from classes.magazine import Magazine
from classes.article import Article

if __name__ == '__main__':
    author = Author('joe')
    cosmo = Magazine('cosmo', 'x')
    vogue = Magazine('vogue', 'x')

    Article(author, cosmo, 'title', 5)
    Article(author, cosmo, 'title', 5)

    ipdb.set_trace()

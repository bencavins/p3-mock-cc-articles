#!/usr/bin/env python3
import ipdb;

from classes.author import Author
from classes.magazine import Magazine
from classes.article import Article


if __name__ == '__main__':
    author = Author('stephen king')
    a2 = Author('joe')
    mag = Magazine('Cosmo', 'fashion')
    mag2 = Magazine('NatGeo', 'nature')
    mag3 = Magazine('fdsfds', 'fdsfsd')

    article = Article(author, mag, 'sometihgn', 100)
    article2 = Article(author, mag, 'python 101', 500)
    article3 = Article(a2, mag, 'js 101', 5000)

    print(mag.get_top_contributor())


#!/usr/bin/env python3
import ipdb;

from classes.author import Author
from classes.magazine import Magazine
from classes.article import Article


if __name__ == '__main__':
    author = Author('stephen king')
    mag = Magazine('Cosmo', 'fashion')
    mag2 = Magazine('NatGeo', 'nature')
    mag3 = Magazine('fdsfds', 'fdsfsd')

    article = Article(author, mag2, 'sometihgn', 6666)
    article2 = Article(author, mag, 'python 101', 500)

    print(author.has_written_for_magazine(mag3))


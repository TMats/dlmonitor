"""
A class for fetching all sources.
"""

from sources.arxivsrc import ArxivSource
from sources.twittersrc import TwitterSource
from db import Base, engine

def get_source(src_name):
    if src_name == 'arxiv':
        return ArxivSource()
    elif src_name == 'twitter':
        return TwitterSource()
    else:
        raise NotImplementedError

def fetch_sources(src_name, fetch_all=False):
    global Base, engine
    Base.metadata.create_all(engine)
    src = get_source(src_name)
    if fetch_all:
        src.fetch_all()
    else:
        src.fetch_new()

def get_posts(src_name, keywords=None, since=None, start=0, num=100):
    src = get_source(src_name)
    return src.get_posts(keywords=keywords, since=since, start=start, num=num)

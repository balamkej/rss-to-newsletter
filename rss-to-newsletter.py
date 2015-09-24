#!/usr/bin/env python

import feedparser
from bs4 import BeautifulSoup

d = feedparser.parse('http://linguistics.arizona.edu/rss.xml')

# Takes an d.entries[n] item and returns a formatted string 
# with title, date, body, and link of item.
def newsItem(entry):
	soup = BeautifulSoup(entry.description, 'html.parser')
	return entry.title + "\n" + entry.published + "\n\n" + soup.p.get_text() + "\n\n" + entry.link 

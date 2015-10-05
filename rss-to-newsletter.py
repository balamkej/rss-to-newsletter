#!/usr/bin/env python

import time
import feedparser
from bs4 import BeautifulSoup

d = feedparser.parse('http://linguistics.arizona.edu/rss.xml')

# Returns a list of news entries from feed that are less than 15 days old.
def newsList():
	now = time.localtime()
	recent_entries = []
	for entry in d.entries:
		if now.tm_yday - entry.published_parsed.tm_yday < 15:
			recent_entries.append(entry)
	return recent_entries

# Takes an d.entries[n] item and returns a formatted string 
# with title, date, body, and link of item.
def newsItem(entry):
	soup = BeautifulSoup(entry.description, 'html.parser')
	return entry.title + "\n" + entry.published + "\n\n" + soup.p.get_text() + "\n\n" + entry.link 
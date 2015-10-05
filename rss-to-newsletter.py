#!/usr/bin/env python

import time
import feedparser
from bs4 import BeautifulSoup

d = feedparser.parse('http://linguistics.arizona.edu/rss.xml')
f = open('newsfile.txt', 'w')

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
	return entry.title + "\n\n" + soup.p.get_text() + "\n\n" + entry.link + "\n\n\n"

f.write("WHAA as of " + time.strftime('%x') + "\n\n" + "As always, you can catch the latest UA Linguistics news, including photos, at http://linguistics.arizona.edu/news. Below are this edition's highlights:" + "\n\n\n")

for entry in newsList():
	f.write(newsItem(entry))

f.write("Remember that whenever anything is going on in your linguistics life, be sure to send it to rhenderson@email.arizona.edu or submit it at our website: http://linguistics.arizona.edu/eform/submit/news-submitted.")

f.close()
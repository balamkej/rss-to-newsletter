#!/usr/bin/env python

import time
import feedparser
from bs4 import BeautifulSoup

d = feedparser.parse('http://linguistics.arizona.edu/rss.xml')
f = open('newsfile.html', 'w')

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
	return "<h3><a href=\"" + entry.link + "\" style=\"color:rgb(171,5,32); text-decoration:none\">" + entry.title + "</a></h3>" + "\n\n" + "<p>" +soup.p.get_text() + "</p>" + "\n\n\n"

f.write("<a href=\"http://linguistics.arizona.edu\"><img src=\"http://www.powerwarg.com/UASBS_LINGUISTICS_PRIMARY.png\" width=\"400\" height=\"75\"></a>" + "\n" + "<h2><font color=\"rgb(12,35,75)\">WHAAL " + time.strftime('%x') + " Edition</font></h2>" + "\n\n" + "<p>As always, you can catch the latest UA Linguistics news, including photos, at our <a href=\"http://linguistics.arizona.edu/news\" style=\"color:rgb(171,5,32); text-decoration:none\">news feed</a>." + " Remember that whenever anything is going on in your linguistics life, be sure to <a href=\"http://linguistics.arizona.edu/eform/submit/news-submitted\" style=\"color:rgb(171,5,32); text-decoration: none\">submit</a> it to WHAAL." + "\n\n\n")

for entry in newsList():
	f.write(newsItem(entry))

f.close()
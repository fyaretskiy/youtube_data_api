from sys import argv
import urllib
import urllib2
import re

search = argv[1]
number_of_links = argv[2]
list_urls = []


def page_changer(search, number_of_links):
	finished = False
	page = 2
	while not finished:
		search = search + "&page={0}".format(page)
		get_list(search)
		page += 1
		print len(list_urls)
		if len(list_urls) <= number_of_links:
			finished = True


def get_list(search):
	global list_urls
	url = "https://www.youtube.com/results?search_query={0}".format(search)
	a = urllib2.urlopen(url)
	a = a.read()
	a = re.findall("data-context-item-id=[^ \t\n\r\f\v]+", a)
	a.remove(a[0])
	a.remove(a[0])
	a.remove(a[0])

	
	for i in a:
		j = re.findall("=[^ \t\n\r\f\v]+", i)[0]
		j = j.replace("=", "")
		j = j.replace('"', '')
		j = "=" + j
		#j = "https://www.youtube.com/watch?v=" + j
		list_urls.append(j)

	print list_urls


get_list(search)
page_changer(search, number_of_links)




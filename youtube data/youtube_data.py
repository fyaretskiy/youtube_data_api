import api_key, the_lists
import urllib2
import json
import sqlite3
import urllib



key = api_key.api_key
new_list = the_lists.new_list


def return_video_stats(link_id):
	"""Connects to the api and sets variable """
	global name, comment_count, view_count, favorite_count, dislike_count, like_count
	params = {
		"part" : "statistics,snippet",
		"filter" : "commentcount"
	}
	params = urllib.urlencode(params)
	url = "https://www.googleapis.com/youtube/v3/videos?id" + link_id + "&key=" + key + "&" + params
	response = urllib2.urlopen(url)
	response = json.loads(response.read())
	the_stats = response["items"][0]["statistics"]
	the_title_from_snippet = response["items"][0]["snippet"]["title"]
	name = the_title_from_snippet.replace("'", "")
	name = "  '{0}' ".format(name)
	comment_count = the_stats["commentCount"]
	view_count = the_stats["viewCount"]  
	favorite_count = the_stats["favoriteCount"]  
	dislike_count = the_stats["dislikeCount"]    
	like_count = the_stats["likeCount"]  
	
	

	
	
def check_table_stats():
	"""checks if table exists and makes one"""
	conn = sqlite3.connect("youtube_stats.db")
	try:
		conn.execute('''CREATE TABLE STATS
			(ID INT PRIMARY KEY NOT NULL,
			name TEXT NOT NULL,
			comment_count INT NOT NULL,
			view_count INT NOT NULL,
			dislike_count INT NOT NULL,
			like_count INT NOT NULL);''')
	except:
		pass
	conn.close()


def save_to_sql(): 															
 	"""Saves values from return_video_stats to a sql database"""				 
 	conn = sqlite3.connect("youtube_stats.db")
 	get_last_id = conn.execute("SELECT * FROM STATS")
 	new_list = []
 	for i in get_last_id:
		new_list.append(i)
	count = len(new_list)
	id_ = count + 1

	conn.execute("""INSERT INTO STATS (ID,name,comment_count,view_count,dislike_count,like_count) \
		VALUES ({0}, {1}, {2}, {3}, {4}, {5})""".format(id_, name, comment_count, view_count, dislike_count, like_count))
	conn.commit()
	conn.close()

def print_table():
	conn = sqlite3.connect("youtube_stats.db")
	courser = conn.execute("SELECT * FROM STATS")
	for i in courser:
		print "Title:	",i[1],"Comment Count: ",i[2],"View Count: ",i[3],"Dislike Count: ",i[4],"Like Count:",i[5]

def run_program():
	for i in new_list:
		return_video_stats(i)
		check_table_stats()
		save_to_sql()

run_program()
print_table()

"""ok lets start from the beginning. I get add links to another file. 
	first check if this video exists - dont have time for this
	ok I pull data from the api
	then i set data from the api into a few variables -  I got this part fucking finished ###
	then the variables go into a new table
	my id needs to change after I add a new line - this took a while but done!###
	I also need to check if the database exists - motherfucking works! ###
	now i need to do the keyword argument part for multiple videos ### I got this to work for a list of links


	
"""

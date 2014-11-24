import re

new_list = []
list_of_links = ["https://www.youtube.com/watch?v=EkhgaVo6rNM", "https://www.youtube.com/watch?v=-suJs0omadM", 
					"https://www.youtube.com/watch?v=3Fti9SKf0iI", "https://www.youtube.com/watch?v=3q9YeSSwte8",
					"https://www.youtube.com/watch?v=iZN5N5420jM"]

for i in list_of_links:
	a = re.findall("=[^ \t\n\r\f\v]+", i)[0]
	new_list.append(a)
	
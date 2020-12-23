

import webbrowser

def makePage(content):
	# creates/overwrites any pages previously created
	f = open("new-page.html", "w")
	# adds any text passed to it as an <h1> element
	f.write("<html><body><h1>{}</h1></body></html>".format(content))
	f.close()

	# opens created page in new tab
	webbrowser.open_new_tab("C:\\Users\\rhodr\\OneDrive\\Documents\\GitHub\\python-projects\\challenges\\html-page-creation\\new-page.html")



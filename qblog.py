# todo: 
#	come up with a Post class that is used to store parsed data
#	read up on how to read, create files etc.
class Post(object):
	def __init__(self, title, date, time, filepath, preview, body):
		self.title = title
		self.date = date
		self.time = time
		self.filepath = filepath
		self.preview = preview
		self.body = body

	# create html file for this post
	def gen_post_html():
		pass

# given data from a .post file, returns a Post object corresponding to the file
def gen_post(post_data):
	pass

# goes through the /data folder, parsing the files and generating the proper
# HTML files in the proper locations, as well as creating links as required.
def gen_posts():
	pass

# goes through the /data folder, getting post titles, previews, and locations,
# putting a preview for each post on the homepage
def gen_homepage():
	pass
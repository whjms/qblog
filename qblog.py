# 
class Post(object):
	def __init__(self, filename):
		self.data = parse(filename)

	# return a tuple containint title, date, time, file path, preview, and post
	# body. post_data is in the following format:
	# 	post_data = (title, date, time, file_path, preview, body)
	def parse(filename):
		pass

	# create html file for this post
	def gen_post_html(self):
		pass

	# return a specific value from post_data, given either:
	# 	'title', 'date', 'time', 'file_path', 'preview', or 'body'
	def get(value):
		pass

# goes through the /data folder, parsing the files and generating the proper
# HTML files in the proper locations, as well as creating links as required.
def gen_posts():
	pass

# goes through the /data folder, getting post titles, previews, and locations,
# putting a preview for each post on the homepage
def gen_homepage():
	pass
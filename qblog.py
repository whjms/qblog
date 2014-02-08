class Post(object):
	def __init__(self, filename):
		self.parse_data(filename)

	# creates a tuple containing title, date, time, file path, preview, and post
	# body. post_data is in the following format:
	# 	post_data = (title, date, time, file_path, preview, body)
	def parse_data(self, filename):
		f = open(filename, 'r')
		title = f.readline()
		date = f.readline()
		time = f.readline()
		file_path = f.readline()
		preview = f.readline()
		body = f.read()
		f.close()

		# if not (all strings are non-empty)
		if not (title and date and time and file_path and preview and body):
			print("Error parsing post file %d, exiting." (filename))
			sys.exit(1)
		else:
			self.post_data = (title, date, time, file_path, preview, body)

	# create html file for this post
	def gen_post_html(self):
		pass

	# return a specific value from post_data, given either:
	# 	'title', 'date', 'time', 'file_path', 'preview', or 'body'
	# Errors for invalid values.
	def get(self, value):
		idx = ["title", "date", "time", "file_path", "preview",
				"body"].index(value)
		return self.post_data[idx]

# goes through the /data folder, parsing the files and generating the proper
# HTML files in the proper locations, as well as creating links as required.
def gen_posts():
	pass

# goes through the /data folder, getting post titles, previews, and locations,
# putting a preview for each post on the homepage
def gen_homepage():
	pass

def main():
	p = Post(r"H:\documents\qblog\data\test-post.post")
	print(p.get('body'))

if __name__ == "__main__":
	main()
class Post(object):
	def __init__(self, filename):
		self.parse_data(filename)

	# creates a tuple containing title, date, time, file path, preview, and post
	# body. post_data is in the following format:
	# 	post_data = (title, date, time, file_path, preview, body)
	def parse_data(self, filename):
		f = open(filename, 'r')
		lines = f.read().splitlines()
		title = lines[0]
		date = lines[1]
		time = lines[2]
		file_path = lines[3]
		preview = lines[4]
		# join each item in the body, separating them with newlines
		body = "\n".join(lines[5:])
		f.close()

		# if not (all strings are non-empty)
		if not (title and date and time and file_path and preview and body):
			print("Error parsing post file %d, exiting." (filename))
			sys.exit(1)
		else:
			# use a tuple, since there's no reason to ever edit a post
			self.post_data = (title, date, time, file_path, preview, body)

	# create html file for this post
	def gen_post_html(self):
		pass

	# string representation: all values in post_data
	def __str__(self):
		return "\n".join(value for value in self.post_data)

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
	p = Post(r"data\test-post.post")
	print(p)

if __name__ == "__main__":
	main()
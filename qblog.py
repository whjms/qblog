import os
class Post(object):
	def __init__(self, filename):
		self.parse_data(filename)

	# creates a tuple containing title, date, time, file path, preview, and post
	# body. post_data is in the following format:
	# 	post_data = (title, date, time, file_path, preview, body)
	def parse_data(self, filename):
		f = open(filename, "r")
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

# generates all of the HTML files for each post, as well as the homepage
def generate():
	print("Generating posts...")
	# need to deal with running this script outside of the script's directory
	# - this gets the absolute path of this script, appending the subdirs to it
	import os
	script_dir = os.path.dirname(os.path.realpath(__file__))
	page_file = open(script_dir + "/templates/homepage.template", "r")
	post_file = open(script_dir + "/templates/post.template", "r")
	page_template = page_file.read()
	post_template = post_file.read()
	page_file.close()
	post_file.close()

	# generate the list of Posts by looping through /data
	posts = []
	for filename in os.listdir(script_dir + "/data"):
		if filename.endswith(".post"):
			posts.append(Post(script_dir + "/data/" + filename))

	for post in posts:
		gen_post(page_template, post_template, post, script_dir)
	gen_homepage(page_template, post_template, posts, script_dir)

# Generates the html file for the given post, according to the given templates
# page_template: a string representing the template for the entire page
# post_template: a string representing the template for a single post, to be
#                subbed into the page template
# post: the Post to generate this page for
# script_dir: string representation of the absolute path to this script's
#             directory
def gen_post(page_template, post_template, post, script_dir):
	postpath = script_dir + "/web/" + post.get("file_path")
	postdir = os.path.dirname(postpath)
	if not os.path.exists(postdir):
		os.makedirs(postdir)

	# fill out the post template
	post_html = post_template.replace("%%%post-title%%%", post.get("title"))
	post_html = post_html.replace("%%%post-timestamp%%%",
		post.get("date") + ", " + post.get("time"))
	post_html = post_html.replace("%%%post-content%%%", post.get("body"))
	post_html = post_html.replace("%%%full-link%%%", post.get("file_path"))

	# fill out the page template
	page_html = page_template.replace("%%%posts%%%", post_html)

	print(page_html, file=open(postpath, "w"))
	print("\tgenerated \'" + post.get("title") + "\'")

# generates the homepage, putting templates for each post on it
# page_template: the template for the homepage
# post_template: the template for each post
# posts: a list of Posts to generate the homepage for
# script_dir: the absolute path to this script's directory
def gen_homepage(page_template, post_template, posts, script_dir):
	pass

def main():
	generate()

if __name__ == "__main__":
	main()
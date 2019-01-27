import praw
import config

def bot_login():
	r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "cactusBot"
				)
	return r

def crash_gaurd(r):
	for submission in r.subreddit('travis_test').new(limit=30c):
		flair = submission.link_flair_text
		for comment in submission.comments:
			user = comment.author
			if flair != None and user == "cactiBot_" :
				comment.mod.remove()


r = bot_login()
crash_gaurd(r)
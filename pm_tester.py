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

r = bot_login()
messages = r.inbox.messages(limit=1)



for message in messages:
	if message.subject == "qwerty":
		message.reply("Working")
		print "ok"



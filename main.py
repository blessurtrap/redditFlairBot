#Written in PRAW by gummy0 for /r/travisscott
#Python2

import praw
import config
import time
from multiprocessing import Process
noflairList = []
fixedList = []
almost_fixed = []
reList = []

sub = travis_test
userBot = cactiBot_

def bot_login():
	r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "cactusBot"
				)
	return r

def flair_checker(r):

	global noflairList

	for submission in r.subreddit(sub).new(limit=10):
		flair = submission.link_flair_text
		post_id = submission.id
		if flair == None:

			if post_id not in reList:
				noflairList.append(post_id)



def commenter(r):

	global noflairList
	global reList

	for post in noflairList:

		submission = r.submission(id=post)
		submission.mod.remove()
		comment = r.submission(id=post).reply("**Your post has been removed because it has no flair.**\n\n " + "*If you flair your post within 24 hours, it will be automatically approved. Otherwise, you will need to manually re-submit it.*\n\n" + "*This action was done by a bot. If it was done incorrectly, please [message the moderators](https://www.reddit.com/message/compose/?to=/r/travisscott)*")
		comment.mod.distinguish(how='yes', sticky=True)
		reList.append(post)
		time.sleep(0.1)

	noflairList = []



def commentRemover(r):

	global fixedList

	for ID in fixedList:
		submission = r.submission(id=ID)
		submission.mod.approve()
		for comment in submission.comments:
			user = comment.author

			if user == userBot:
				comment.mod.remove()				


def findFixed(r):

	global reList

	global fixedList

	for ID in reList:
			submission = r.submission(id=ID)
			flair_recheck = submission.link_flair_text
			if flair_recheck != None:
				fixedList.append(ID)

	return fixedList



def reListToBackup():
	
	global reList

	for ID in reList:

		open('list.txt', 'w').close()
		txtu = open("list.txt", 'a')
		txtu.write(ID)
		txtu.write('\n')

def backupToRelist():

	global reList

	with open('list.txt') as f:
		reList = f.read().splitlines()

def crash_gaurd(r):
	for submission in r.subreddit(sub).new(limit=20):
		flair = submission.link_flair_text
		for comment in submission.comments:
			user = comment.author
			if flair != None and user == userBot :
				comment.mod.remove()

r = bot_login()




if not reList:
	backupToRelist()

flair_checker(r)


commenter(r)


reListToBackup()


if findFixed(r):
	for ID in fixedList:
		if ID in reList:
			reList.remove(ID)
	reListToBackup()
	
	commentRemover(r)



	


	




import praw

CLIENT_ID = "wJhTFzwd3KwK_A"
SECRET = "sirivbA3hRS97w2exKpozm4mGZU"
REDDIT_PASSWORD = "codingclubiitg"
REDDIT_USERNAME = "totalvirgin"
reddit_url = "https://reddit.com/"

def get_posts():
	reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=SECRET,
                     password=REDDIT_PASSWORD,
                     user_agent='testscript by /u/totalvirgin',
                     username=REDDIT_USERNAME)

	reddit.read_only = False
	submissions = reddit.subreddit('all').hot(limit = 5)

	payload = "The top 5 Reddit posts right now are: \n"

	for submission in submissions:
		payload += (reddit_url + submission.id + "/" + "\n")

	print payload
	return payload

get_posts()

#print reddit.user.me()
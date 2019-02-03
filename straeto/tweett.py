import tweepy

def tweet(lastring):
	a = "kTZZaNL3wSfHhtdvvGMsIuOiW"
	b = "rUtr7HsuMt2UHEG6SmKy7hn2bIrGfL355wHLBkV5J8noqfIiEH"
	c = "1091690812319166464-R2TSAYvjtAcgIAXWzIqsvFcoXy7OxY"
	d = "JANxJHjC5PwwZYG9FSS3tIDODTRDyY6tg4ZO6Sncg86Ii"
	auth = tweepy.OAuthHandler(a, b)

	auth.set_access_token(c,d)

	api = tweepy.API(auth)

	api.update_status(lastring)
	print(api.me())



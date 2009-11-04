from django.core.cache import cache
import urllib2
from urllib2 import URLError, HTTPError
import simplejson as json

base_url = 'http://twitter.com/statuses/user_timeline/'
user_id = 'smithandrobot'
format = 'json'
count = 1

def twitter(request):
	url = base_url + user_id + '.' + format + '?count=' + str(count)
	if cache.get('twitter_status'):
		status = cache.get('twitter_status')
	else :
		try:
			stream = urllib2.urlopen(url)
			status = json.load(stream)[0]['text']
			cache.set('twitter_status', status, 3600)
			if status != cache.get('twitter_coldstatus'):
				cache.set('twitter_coldstatus', status, 3600*24)
		except:
			status = cache.get('twitter_coldstatus')
			if status is None:
				status = 'Twitter is on the fritz.'
	
	return dict(twitter_status = status)
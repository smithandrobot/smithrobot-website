from django.core.cache import cache
import urllib2
from urllib2 import URLError, HTTPError
import simplejson as json

base_url = 'http://twitter.com/statuses/user_timeline/'

class User:
	
	@staticmethod
	def get_timeline(user_id, format='json', count=5):
		url = base_url + user_id + '.' + format + '?count=' + str(count)
		if cache.get('twitter_status'):
			return cache.get('twitter_status')[0]['text']
		else :
			try:
				stream = urllib2.urlopen(url)
				status = json.load(stream)
				cache.set('twitter_status', status, 3600)
				return status[0]['text']
			except (HTTPError, URLError):
				return 'Twitter is having issues'
		
	@staticmethod
	def debug():
		url = base_url + 'smithandrobot.json'
		stream = urllib2.urlopen(url)
		return stream
		
	
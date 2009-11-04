from django.shortcuts import render_to_response
from django.template import RequestContext
from utils.twitter import User

def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))
	
def iphone(request):
	return render_to_response('index_iphone.html')
	
def mobile(request):
	return render_to_response('index_mobile.html')
	
def hide_from_google_analytics(request):
	return render_to_response('tracking_cookie.html')
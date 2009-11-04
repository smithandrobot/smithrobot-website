#!/usr/bin/env python
# encoding: utf-8
"""
mobile_ua_detection.py

Created by David Ford on 2009-03-23.
Copyright (c) 2009 Smith & Robot. All rights reserved.
"""

from django.http import HttpResponseRedirect

# list of mobile User Agents
mobile_uas = [
	'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
	'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
	'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
	'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
	'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
	'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
	'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
	'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
	'wapr','webc','winw','winw','xda','xda-'
	]
	
mobile_ua_hints = [ 'SymbianOS', 'Opera Mini']

class MobileMiddleware:
	
	def process_request(self, request):
		
		# this is here to keep from running an infinit redirect
		# it seems that as soon as you redirect this function is
		# called after the redirect and gets in a loop
		if (request.path == "/iphone/" or request.path == "/mobile/" or request.path.find('media') > 0):
			return
			
		mobile_browser = False
		ua = request.META['HTTP_USER_AGENT'].lower()[0:4]
		
		if (ua in mobile_uas):
			return HttpResponseRedirect('/mobile/')
		else:
			for hint in mobile_ua_hints:
				if request.META['HTTP_USER_AGENT'].find(hint) > 0:
					return HttpResponseRedirect('/mobile/')
					
				if request.META['HTTP_USER_AGENT'].find('iPhone') > 0:
					return HttpResponseRedirect('/iphone/')
					
					
					
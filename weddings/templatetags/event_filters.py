from django import template

register = template.Library()

@register.filter(name='gcal_link')
def gcal_link(event):
	name = event.name
	iso_begin = event.iso_begin
	iso_end = event.iso_end
	description	= event.description
	address = "%(venue)s, %(address)s" % event
	url = reverse_lazy('weddings:event-details', event.id)
 	link = "http://www.google.com/calendar/event?action=TEMPLATE&text={name}&dates={iso_begin}//{iso_end}&details={description}&location={address}&sprop=website:{url}&trp=false".format(locals())
 	return link

	# http://www.google.com/calendar/event?action=TEMPLATE&text=Lunch+%27n+%27Learn+-+50th+Anniversary+Celebration&dates=20160621T120000/20160621T130000&details=%3Cp%3ELunch+%E2%80%98n%E2%80%99+Learn+%40+Charles+H.+MacNider+Art+Museum+from+12%3A00-1%3A00+p.m.+Demonstration+of+Camera+Obscura+by+Tim+Jenison+and+Discussion+of+research+project+that+led+to+the+film+%26%238220%3BTim%E2%80%99s+Vermeer%26%238221%3B.%3C%2Fp%3E%3Cp%3EAlthough+the+Museum%E2%80%99s+actual+anniversary+is+in+January%2C+we+realized+it+was+too+cold+and+the+chance+of+storms+too+great+to+have+the+party+in+winter%21+In+June%2C+the+Museum+will+host+a+week-long+celebration.+The+main+event+will+be+a+celebration+the+week+of+June+20-24.%3C%2Fp%3E%3Cp%3EDuring+this+week+special+guest+Tim+Jenison+will+be+at+the+Museum+for+a+variety+of+special+activities.+Jenison%2C+an+inventor+of+such+notable+computer+applications+such+as+Video+Toaster+and+owner+of+the+software+company+NewTek%2C+became+fascinated+with+the+17th+century+painter+Johnannes+Vermeer.+He+set+out+to+prove+that+Vermeer+used+simple+technology%2C+most+specifically+a+basic+camera+obscura+and+mirrors%2C+to+create+his+master+paintings.+The+journey+of+Jenison%E2%80%99s+findings+were+documented+in+the+2014+film+%26%238220%3BTim%E2%80%99s+Vermeer%26%238221%3B.+Jenis+%28View+Full+Event+Description+Here%3A+http%3A%2F%2Fwww.discovernorthiowa.com%2Fevent%2Flunch-n-learn-50th-anniversary-celebration%2F%29%3C%2Fp%3E&location=303+2nd+St+SE%2C+Mason+City%2C+IA%2C+50401%2C+United+States&sprop=website:http://www.discovernorthiowa.com&trp=false
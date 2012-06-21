from django.conf.urls.defaults import *
from blog.views import archive, post, search
from blog.feeds import RSSFeed

urlpatterns = patterns('blog.views',
	url(r'^comments/', include('django.contrib.comments.urls')),
	url(r'^post/(\d+)/$', post),
	url(r'^search/$', search),
	url(r'^feeds/$', RSSFeed()),
	url(r'^$', archive),

)
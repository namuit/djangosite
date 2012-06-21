from django.contrib.syndication.views import Feed
from blog.models import BlogPost

class RSSFeed(Feed):
	title = "Titolo"
	description = "Descrizione"
	link = "/blog/"
	item_link = link
	def items(self):
		return BlogPost.objects.all()[:10]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.body
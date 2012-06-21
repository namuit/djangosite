# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost
from django.shortcuts import get_object_or_404
from django.core.context_processors import csrf

def archive(request):
	posts = BlogPost.objects.all()
	t = loader.get_template("archive.html")
	c = Context({ 'posts': posts })
	return HttpResponse(t.render(c))

def post(request,id):
	post = get_object_or_404(BlogPost, pk=id)
	t = loader.get_template("post.html")
	c = Context({ 'post': post })
	c.update(csrf(request))
	return HttpResponse(t.render(c))

def search(request):
	if 'q' in request.GET:
		term = request.GET['q']
		t = loader.get_template("search.html")
		posts = BlogPost.objects.filter(body__contains=term)
		c = Context({ 'posts': posts })
		return HttpResponse(t.render(c))
from django import template
from blog.models import Post, Comment, SecondCategory,Scripts,SlideBanner,Banner,Links
from django.shortcuts import render,get_object_or_404


register = template.Library()

@register.inclusion_tag('latest_posts.html')
def latest_posts():

    context = {
        'l_posts': Post.objects.filter(active=True)[0:5],
    }
    return context

@register.inclusion_tag('latest_comments.html')
def latest_comments():
    context = {
        'l_comments': Comment.objects.filter(active=True)[0:5],
    }
    return context

@register.inclusion_tag('latest_categories.html')
def latest_categories():

    context = {
        'l_categorie': SecondCategory.objects.all(),
    }
    return context

@register.inclusion_tag('scripts.html')
def scripts():

    context = {
        'scripts': Scripts.objects.all(),
    }
    return context

@register.inclusion_tag('baner.html')
def baner():

    context = {
        'baner': Banner.objects.all(),
    }
    return context
@register.inclusion_tag('slidebaner.html')
def slidebaner():

    context = {
        'slidebaner': SlideBanner.objects.all(),
    }
    return context

@register.inclusion_tag('links.html')
def links():

    context = {
        'links': Links.objects.all(),
    }
    return context
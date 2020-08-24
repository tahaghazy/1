from django.shortcuts import render,get_object_or_404
from .models import Post,Comment,Category,SecondCategory
from .forms import NewComment,PostCreateForm
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .filters import PostFilter
from django.db.models import Count
from django.views.generic import ListView , DetailView
from django.db.models import F
from django.db.models import Count
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm




def home(request):
    posts = Post.objects.filter(active=True)
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    las_posts=Post.objects.filter(active=True)[0:5]
    myfilter = PostFilter(request.GET,queryset=posts)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_page)
    context = {
        'title': 'الصفحة الرئيسية',
        'posts': posts,
        'page': page,
        'las_posts': las_posts,

    }
    return render(request,'home.html',context)






def about(request):
    context ={
        'title': 'من أنا'}

    return render(request, 'about.html', context)

def post_detail(request,slug):
    post = get_object_or_404(Post,slug=slug,active=True)
    comments = post.comments.filter(active=True)
    Post.objects.filter(pk=post.id).update(views=F('views') + 1)
    views = post.views + 1  # to show valid counter in the template

    #جزء التحقق من التعليقات قبل القيام باي نشاط
    if request.method == 'POST':
        comment_form= NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False )
            new_comment.post = post
            new_comment.save()
            comment_form = NewComment()
    else:
            comment_form = NewComment()

    context={
        'title':post.title,
        'post': post,
        'comments': comments,
        'comment_form':comment_form,
        'views':'views'


    }

    return render(request,'detail.html',context)


def movies(request,slug):
    categories = Category.objects.all()
    movie = get_object_or_404(Category,slug=slug)
    post = movie.posts.filter(active=True)
    #myfilter = PostFilter(request.GET, queryset=post)
    #post = myfilter.qs
    context = {
        'title':'movies',
        'post': post,
        'categories':categories
        #'myfilter': myfilter,

    }

    return render(request, 'movies.html', context)

def secondcategory(request,slug):
    categories = SecondCategory.objects.all()
    movie = get_object_or_404(SecondCategory,slug=slug)
    post = movie.posts.filter(active=True)
    #myfilter = PostFilter(request.GET, queryset=post)
    #post = myfilter.qs
    context = {
        'title':'category',
        'post': post,
        'categories':categories
        #'myfilter': myfilter,

    }

    return render(request, 'secondcategory.html', context)


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'new_post.html'
    form_class = PostCreateForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostCreateForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        success_url = '/profile/'

        if self.request.user == post.author:
            return True

        return False


def most_watched(request):
    posts = Post.objects.all().annotate(
        sku_count=Count('views')).order_by('-views')

    return render(request, 'most-watched.html', context={'posts':posts})

def newest(request):
    posts = Post.objects.all().annotate(
        sku_count=Count('views')).order_by('-post_date')

    return render(request, 'newest.html', context={'posts':posts})

def most_rated(request):
    posts = Post.objects.all().annotate(
        sku_count=Count('views')).order_by('-rate')

    return render(request, 'most-rated.html', context={'posts':posts})



def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(title__icontains=query) | Q(content__icontains=query)

            results= Post.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            messages.success(request, 'تم ارسال الرساله بنجاح')
            try:
                send_mail(subject, message, from_email, ['tahaghazt164@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    return render(request, "contact-us.html", {'form': form})


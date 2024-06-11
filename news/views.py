from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
def news_home(req):
    news = Articles.objects.all()
    return render(req, 'news/news.html', {"news": news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news'
    template_name = 'news/newsDelete.html'
def create(req):
    error = ''
    if req.method == 'POST':
        form = ArticlesForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Wrong data!!!'
    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(req, 'news/create.html', data)

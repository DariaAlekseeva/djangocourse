from django.shortcuts import render
from django.urls import reverse_lazy
from app.models import Article
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)
# Create your views here.

class ArticleListView(ListView):
    template_name = "app/home.html"
    model = Article
    context_object_name = "articles"

class ArticleCreateView(CreateView):
    template_name = "app/article_create.html"
    model = Article
    fields = ["title", "content", "twitter_post", "status"]
    success_url = reverse_lazy("home")


class ArticleUpdateView(UpdateView):
    template_name = "app/article_update.html"
    model = Article
    fields = ["title", "content", "twitter_post", "status"]
    success_url = reverse_lazy("home")
    context_object_name = "article"


class ArticleDeleteView(DeleteView):
    template_name = "app/article_delete.html"
    model = Article
    success_url = reverse_lazy("home")
    context_object_name = "article"  
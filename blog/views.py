from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from .models import Post, Category

class dashboard(View):
    template_name = 'index.html'

    def get(self, request):
        """Desplay all posts"""
        posts = Post.objects.all().order_by("-posted")
        paginator = Paginator(posts, 2)

        try: page = int(request.GET.get("page", '1'))
        except ValueError: page = 1

        try:
            posts = paginator.page(page)
        except (InvalidPage, EmptyPage):
            posts = paginator.page(paginator.num_pages)

        # return render(request, self.template_name, 
        #     {'Category':Category.objects.all(),
        #     'Blog':Post.objects.all()})
        return render(request,'blog/dashboard.html')



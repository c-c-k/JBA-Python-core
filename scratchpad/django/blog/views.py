from django.shortcuts import render
from django.views import View

blog_name = "John Doe's blog"
posts = [
    {
        "text": "My first post",
        "theme": "Easy talk",
        "comments": [
            "My congratulations!!",
            "Looking forward to the second one",
        ],
    },
    {
        "text": "<a href=\"https://hyperskill.org\"> "
                "How to make a post entry with Django</a>",
        "theme": None,
        "comments": None,
    }
]


class MainView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "blog_name": blog_name,
            "posts": posts,
        }
        return render(request, "blog/index.html", context=context)

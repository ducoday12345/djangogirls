from django.shortcuts import render

# Create your views here.

def post_list(request): #post_list url's view
    return render(request, "blog/post_list.html", {})
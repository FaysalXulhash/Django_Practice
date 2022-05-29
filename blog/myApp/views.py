from django.shortcuts import render

# Create your views here.

posts = [

    {
        'author': 'Faisal',
        'title': 'Educational Blog',
        'content': 'Educational Content',
        'post_date': 'October 2 2022'
    },

    {
        'author': 'Aziri',
        'title': 'Food Blog',
        'content': 'Food Content',
        'post_date': 'March 12 2022'
    },


]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'myApp/home.html', context)


def about(request):
    return render(request, 'myApp/about.html', {'title': 'about'})

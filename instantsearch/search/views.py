from django.shortcuts import render

# Create your views here.

def home_page(request):

    if request.method == 'GET':
        # Render home page

        return render(request, 'search_page.html')

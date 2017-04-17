from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.core.serializers.json import DjangoJSONEncoder
import json


from .models import Place

# Create your views here.

def home_page(request):
    return render(request, 'search/search_page.html')


# Used to turn a Place into JSON
class PlaceJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Place):
            return obj.__dict__


def search_place(request):

    place = request.GET.get('query')   # This is sent with the AJAX query.

    if place:
        # DB query
        places = list(Place.objects.filter(name__icontains=place).order_by('name'))
    else:
        # No search query, return everything. Adapt to suit the behavior of your app.
        # Everything could be a lot! You would probably want to limit to (e.g.) the first 30 results
        places = list(Place.objects.all().order_by('name'))

    # Use PlaceJSONEncoder to convert list of Places to JSON. Return JSON object.
    return JsonResponse(places, encoder=PlaceJSONEncoder, safe=False)

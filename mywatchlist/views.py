from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import WatchlistMovie

data_watchlist_movie = WatchlistMovie.objects.all()
context = {
    'list_movie': data_watchlist_movie,
    'nama': 'Monica Oktaviona',
    'id': '2106701210'
}
# Create your views here.
def show_mywatchlist(request):
    return render(request, "mywatchlist.html", context)

def show_xml(request): 
    return HttpResponse(serializers.serialize("xml", data_watchlist_movie), content_type="application/xml")

def show_json(request): 
    return HttpResponse(serializers.serialize("json", data_watchlist_movie), content_type="application/json")

def show_xml_by_id(request, id): 
    data = WatchlistMovie.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id): 
    data = WatchlistMovie.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
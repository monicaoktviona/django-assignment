### Link aplikasi: [HTML](https://pbp-katalog.herokuapp.com/mywatchlist/html/), [XML](https://pbp-katalog.herokuapp.com/mywatchlist/xml/), [JSON](https://pbp-katalog.herokuapp.com/mywatchlist/json/)
## Perbedaan antara JSON, XML, dan HTML!
### HTML
1. Digunakan untuk men-display suatu dokumen ke dalam web browser
2. Data yang ingin ditampilkan di-wrap oleh tag
3. Tag bersifat case insensitive
### XML
1. Digunakan untuk menyimpan dan melakukan pertukaran data
2. Data yang disimpan di-wrap oleh tag
3. Tag bersifat case sensitive
### JSON
1. Digunakan untuk menyimpan dan melakukan pertukaran data
2. Data disimpan dalam bentuk string
3. Lebih mudah untuk digunakan daripada XML dan lebih cepat daripada XML (ketika mengimplementasi AJAX)

## Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan ketika kita ingin memindahkan data dari satu stack ke stack lain. Data tersebut dapat dikirimkan dalam berbagai format seperti HTML, XML, dan JSON. Data delivery memungkinkan terjadinya transfer data sehingga untuk aplikasi yang dikembangkan pada berbagai platform berbeda dapat mengakses data yang _up-to-date_ pada setiap platformnya.

## Cara pengimplementasian _checklist_ pada tugas 3
1. Menjalankan virtual environment di repositori django-assignment dengan perintah
`python -m venv env`
2. Menyalakan virtual environment dengan perintah `env\Scripts\activate.bat`
3. Membuat aplikasi mywatchlist dengan perintah `python manage.py startapp mywatchlist`
4. Menambahkan aplikasi mywatchlist ke dalam variabel INSTALLED_APPS untuk didaftarkan ke dalam proyek Django
`INSTALLED_APPS = [
    ...,
    'mywatchlist',
]`
5. Menambahkan potongan kode berikut ke dalam file models.py
`class WatchlistMovie(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=100)
    rating = models.IntegerField()
    release_date = models.CharField(max_length=100)
    review = models.TextField()
`
6. Menjalankan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam database Django lokal
7. Menjalankan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal
8. Membuat folder bernama fixtures lalu membuat sebuah berkas bernama initial_mywatchlist_data.json yang berisi kode berikut.
`[
    {
        "model":"mywatchlist.watchlistmovie",
        "pk":1,
        "fields":{
            "watched":"True",
            "title":"Little Women",
            "rating": "5",
            "release_date":"December 7, 2019",
            "review":"Such a comfort movie for me."
        }
},
{
        "model":"mywatchlist.watchlistmovie",
        "pk":2,
        "fields":{
            "watched":"True",
            "title":"Extreme Job",
            "rating": "4",
            "release_date":"February 20, 2019",
            "review":"So entertaining!"
        }
    },
    {
        "model":"mywatchlist.watchlistmovie",
        "pk":3,
        "fields":{
            "watched":"True",
            "title":"Knives Out",
            "rating": "5",
            "release_date":"November 27, 2019",
            "review":"A cleverly-constructed movie."
        }
    },
    {
        "model":"mywatchlist.watchlistmovie",
        "pk":4,
        "fields":{
            "watched":"True",
            "title":"The Invisible Guest",
            "rating": "4",
            "release_date":"January 6, 2017",
            "review":"Full of plot twists. A good movie actually."
        }
    },
    {
        "model":"mywatchlist.watchlistmovie",
        "pk":5,
        "fields":{
            "watched":"True",
            "title":"Gone Girl",
            "rating": "4",
            "release_date":"October 3, 2014",
            "review":"This movie gives me the same vibe as Simple Favor since I watched Simple Favor earlier."
        }
    },
    {
        "model":"mywatchlist.watchlistmovie",
        "pk":6,
        "fields":{
            "watched":"True",
            "title":"Interstellar",
            "rating": "5",
            "release_date":"November 6, 2014",
            "review":"The very first Christopher Nolan's movie that i watched and i really love it."
        }
    },
    {
        "model":"mywatchlist.watchlistmovie",
        "pk":7,
        "fields":{
            "watched":"True",
            "title":"The Grand Budapest Hotel",
            "rating": "3",
            "release_date":"March 6, 2014",
            "review":"A movie with the most beautiful cinematography i've ever watched. I love every single frame."
        }
    },
    {
        "model":"mywatchlist.watchlistmovie",
        "pk":8,
        "fields":{
            "watched":"False",
            "title":"Inception",
            "rating": "0",
            "release_date":"July 16, 2010",
            "review":"No review yet"
        }
    },
    {
        "model":"mywatchlist.watchlistmovie",
        "pk":9,
        "fields":{
            "watched":"False",
            "title":"Dunkirk",
            "rating": "0",
            "release_date":"July 20, 2017",
            "review":"No review yet"
        }
    },
    {
        "model":"mywatchlist.watchlistmovie",
        "pk":10,
        "fields":{
            "watched":"False",
            "title":"Oppenheimer",
            "rating": "0",
            "release_date":"July 21, 2023",
            "review":"No review yet"
        }
    }
 
]`
9. Menjalankan perintah `python manage.py loaddata initial_mywatchlist_data.json` untuk memasukkan data tersebut ke dalam database Django lokal.
10. Mengimpor models yang sudah dibuat sebelumnya serta mengimpor HttpResponse dan Serializer ke file views.py dengan menambahkan potongan kode berikut
`from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import WatchlistMovie`
11. Menambahkan variabel data_watchlist_movie dan context ke file views.py yang berfungsi untuk memanggil fungsi query ke model database dan menyimpan query tersebut ke dalam sebuah variabel.
`data_watchlist_movie = WatchlistMovie.objects.all()
context = {
    'list_movie': data_watchlist_movie,
    'nama': 'Monica Oktaviona',
    'id': '2106701210'
}`
12.  Membuat fungsi show_mywatchlist, show_xml, dan show_json untuk mengakses mywatchlist masing-masing dalam format HTML, XML, dan JSON dengan menambahkan potongan kode berikut
`def show_mywatchlist(request):
    return render(request, "mywatchlist.html", context)
def show_xml(request): 
    return HttpResponse(serializers.serialize("xml", data_watchlist_movie), content_type="application/xml")
def show_json(request): 
    return HttpResponse(serializers.serialize("json", data_watchlist_movie), content_type="application/json")
`
13. Menambahkan potongan kode berikut untuk mengembalikan data dalam bentuk JSON/XML berdasarkan id nya
`def show_xml_by_id(request, id): 
    data = WatchlistMovie.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id): 
    data = WatchlistMovie.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")`
14. Membuat berkas di dalam folder aplikasi mywatchlist bernama urls.py untuk melakukan routing terhadap fungsi views yang telah dibuat sehingga nantinya halaman HTML dapat ditampilkan melalui browser. Isi dari views.py adalah.
`from django.urls import path
from mywatchlist.views import show_mywatchlist, show_xml, show_json, show_json_by_id, show_xml_by_id

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
]`
15. Mendaftarkan aplikasi mywatchlist ke dalam urls.py yang ada pada folder django-assignment dengan menambahkan potongan kode berikut.
`path('mywatchlist/', include('mywatchlist.urls')),`
16. Membuat sebuah folder bernama templates dan membuat sebuah berkas bernama mywatchlist.html di dalamnya yang berisi potongan kode berikut.
`{% extends 'base.html' %}
 
{% block content %}
<h1>Tugas 3 PBP/PBD</h1>
<h5>Nama: </h5>
<b>{{nama}}</b>
 
<h5>Student ID: </h5>
<b>{{id}}</b>
 
<table>
    <tr>
    <th>Watched</th>
    <th>Title</th>
    <th>Rating</th>
    <th>Release Date</th>
    <th>Review</th>
    </tr>
   
    {% for movie in list_movie %}
        <tr>
            <th>{{movie.watched}}</th>
            <th>{{movie.title}}</th>
            <th>{{movie.rating}}</th>
            <th>{{movie.release_date}}</th>
            <th>{{movie.review}}</th>
        </tr>
    {% endfor %}
</table>
 
 
{% endblock content %}
`
18. Menambahkan potongan kode `release: sh -c 'python manage.py migrate && python manage.py loaddata initial_mywatchlist_data.json'` ke Procfile
19. Add, push, dan commit ke github
20. Melakukan deployment ke heroku. Jika menggunakan repositori tuga sebelumnya maka langsung _re-deploy_ saja pada halaman github tidak perlu membuat aplikasi baru di heroku.

## Postman
#### http://localhost:8000/mywatchlist/html
![Screenshot Postman HTML](https://github.com/monicaoktviona/django-assignment/blob/main/mywatchlist/postman/html.png)<br>
#### http://localhost:8000/mywatchlist/xml
![Screenshot Postman XML](https://github.com/monicaoktviona/django-assignment/blob/main/mywatchlist/postman/xml.png)<br>
#### http://localhost:8000/mywatchlist/json
![Screenshot Postman JSON](https://github.com/monicaoktviona/django-assignment/blob/main/mywatchlist/postman/json.png)<br>


### Link aplikasi: [todolist](https://pbp-katalog.herokuapp.com/todolist)

### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Pada synchronous programming, task dijalankan satu per satu sehingga pengguna perlu menunggu 
task selesai diproses untuk dapat menjalankan task yang lain. Sementara itu, pada asynchronous programming, 
task dapat dijalankan secara parallel sehingga pengguna tidak perlu menunggu suatu task selesai diproses
untuk dapat menjalankan task yang lain.

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming adalah sebuah paradigma di mana suatu task dijalankan sebagai respon/akibat dari terjadinya suatu event.
Contoh penerapan pada tugas ini adalah adanya button yang digunakan sebagai trigger untuk memunculkan modal. Ketika pengguna 
mengeklik button tersebut, maka modal akan muncul.

### Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan asynchronous programming pada AJAX adalah AJAX memungkinkan adanya update pada halaman web tanpa perlu melakukan refresh keseluruhan halaman.
Hal tersebut dapat dilakukan karena AJAX memisahkan presentation layer dengan data exchange layer sehingga ketika terjadi perubahan data, 
halaman web tetap dapat ditampilkan dan perubahan data yang dilakukan akan diupdate ketika selesai dijalankan tanpa
harus mengupdate keseluruhan halaman. 

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat view baru untuk mengembalikan seluruh data task dalam bentuk JSON dengan menambahkan
potongan kode berikut. <br>
```
@login_required(login_url='/todolist/login/')
def get_todolist_json(request):
    todolist_item = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', todolist_item))
```
2. Menambahkan path `path('get_todolist_json/', get_todolist_json, name='get_todolist_json'),` di `urlpatterns`.<br>
3. Melakukan pengambilan data JSON dan memasukkan masing-masing data ke dalam card (Referensi syntax yang digunakan: https://www.geeksforgeeks.org/how-to-fetch-data-from-json-file-and-display-in-html-table-using-jquery/).<br>
4. Membuat tombol trigger `Add Task` untuk menampilkan model yang berisi form add task. (Referensi syntax yang digunakan:https://getbootstrap.com/docs/5.2/components/modal/).<br>
5. Membuat view baru untuk menambahkan task baru ke database dengan potongan kode berikut:<br>
```
@csrf_exempt
def add_task_async(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        #Get the posted form
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.date = date.today()
            task.save()
    return JsonResponse({"success": "Task is successfully added"}) 
```
6. Menambahkan path `path('add/', add_task_async, name='add_task_async'),` di `urlpatterns`.<br>
7. Menambahkan potongan kode berikut untuk menutup model ketika berhasil menambahkan task.<br>
```
$('#staticBackdrop').hide();
$('.modal-backdrop').hide();
```
8. Membuat function untuk memanggil ajax POST agar setelah task baru ditambahkan, halaman
web bisa langsung menampilkan data tersebut tanpa melakukan refresh halaman. 

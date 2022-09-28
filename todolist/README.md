### Link aplikasi: [todolist](https://pbp-katalog.herokuapp.com/todolist)
Dapat juga diakses melalui:
1. https://pbp-katalog.herokuapp.com/todolist untuk mengakses halaman utama yang memuat tabel task (harus login terlebih dahulu)
2. https://pbp-katalog.herokuapp.com/todolist/login untuk mengakses form login
3. https://pbp-katalog.herokuapp.com/todolist/register untuk mengakses form registrasi akun
4. https://pbp-katalog.herokuapp.com/todolist/create-task untuk mengakses form pembuatan task (harus login terlebih dahulu)
5. https://pbp-katalog.herokuapp.com/todolist/logout berisi mekanisme logout.
<br>

### Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
`{% csrf_token %}` berfungsi melindungi website dari serangan Cross-site request forgery (CSRF) dengan cara men-_generate_ token unik untuk setiap _session_ pengguna.
Setiap pengguna mengirimkan _request_, CSFR token juga akan dikirimkan. Jika CSFR tokennya tidak valid (CSFR token pada _session_ dan _request_-nya tidak sama), maka _request_ tidak akan di-_execute_.
Apabila tidak ada `{% csrf_token %}` pada elemen `<form>`, Cross-site request forgery (CSRF) akan lebih rentan terjadi. 
Dalam hal ini, _attacker_ akan lebih mudah untuk melakukan modifikasi pada `<form>` seperti melakukan _request_ POST karena tidak ada pengecekan CSFR token untuk setiap _session_ dan _request_-nya.
<br>

### Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti (`{{ form.as_table }}`)? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
Elemen `<form>` dapat dibuat secara manual di file html. Sebagai contoh, pada `login.html`, `<form>` dibuat secara manual. Hal tersebut dilakukan dengan memanfaatkan tag `<input>` yang ada di HTML `type` yang disesuaikan dengan kebutuhan, seperti `'text'` untuk textfield. `'password'` untuk field password, `'submit'` untuk button submit, dll.
Untuk `<form>` pada halaman login, dibuat dengan potongan kode berikut.
```
<form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>
  ```
    <br>
### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Ketika pengguna melakukan submisi form, maka akan dibuat _instance_ dari TaskForm yang ada di `forms.py` sesuai dengan input yang dimasukkan pengguna. 
Lalu akan terjadi pengecekan, apabila form tersebut valid, maka semua attribut yang ada pada model akan disesuaikan dengan input pengguna. Data tersebut disimpan ke databse saat
pemanggilan method `.save()`. Saat di-_redirect_ ke halaman HTML, data akan ditampilkan melalui _for loop_ setiap atribut yang ada pada model.
<br>

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
#### 1. Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.
Menjalankan potongan kode `py manage.py startapp todolist` pada direktori `django-assignment`.
#### 2. Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
Menambahkan `'todolist'` pada `INSTALLED_APPS` di file `setting.py` dan menambahkan `path('todolist/', include('todolist.urls'))` pada urlpatterns di file `urls.py` pada folder `project_django`.
#### 3. Membuat sebuah model Task yang memiliki atribut user, date, title, dan description
Menambahkan potongan kode berikut.
```
class Task(models.Model):
    user = models.ForeignKey(User, default=None, blank=True, null=True, on_delete=models.CASCADE)
    date = models.DateField(null=True, auto_now_add=True)
    title = models.CharField(null=True, max_length=350)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title
```
`ForeignKey` digunakan untuk membuat _many-to-one_ _relationship_ (dalam kasus ini, seorang user dapat memiliki banyak task).
Setelah itu, menjalankan potongan kode `py manage.py makemigrations` dan `py manage.py migrate`.
#### 4. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
1. Registrasi
<br>
Pada `views.py`, _import_ `redirect`, `UserCreationForm`, dan `messages`. Lalu, menambahkan potongan kode berikut agar _form_ dapat di-_generate_ secara otomatis.
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)
```
Membuat file `register.html` pada folder `templates` dengan potongan kode berikut.
```
{% extends 'base.html' %}

{% block meta %}
<title>Registrasi Akun</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Formulir Registrasi</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
2. Login
Pada `views.py`, _import_ `authenticate` dan `login`. Lalu, menambahkan potongan kode berikut untuk mengautentikasi pengguna yang akan login.
```
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('todolist:show_todolist')) # membuat response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)
```
Membuat file `login.html` pada folder `templates` dengan potongan kode berikut.
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Belum mempunyai akun? <a href="{% url 'todolist:register' %}">Buat Akun</a>

</div>

{% endblock content %}
```
3. Logout
Pada `views.py`, _import_ `logout`. Lalu menambahkan potongan kode beikut sebagai mekanisme _logout_.
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    return response
```
#### 5. Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.
Membuat file `forms.py` berisi _class_ `TaskForm` dengan model`Task` dan _fields_ `titl`e dan `description` saja karena pada _form_ penambahan _task_ nanti, pengguna hanya perlu memasukkan_ title_ dan _description_-nya saja.
```
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description')
        widgets = {
            'description': forms.Textarea(),
        }
```
Pada `views.py`, menambahkan potongan kode berikut untuk meng-_handle_ _request_ POST pada form yang akan dibuat.
```
@login_required(login_url='/todolist/login/')
def create_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        #Get the posted form
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.date = date.today()
            task.save()
        return redirect("todolist:show_todolist")
    context = {'form':form}
    return render(request, "create-task.html", context)
 ```
 Terakhir, membuat file `create-task.html` untuk menampilkan halaman _form_ pembuatan _task_ dengan potongan kode berikut.
 ```
 {% extends 'base.html' %}

{% block meta %}
<title>Create Task</title>
{% endblock meta %}

{% block content %}

<div class = "create-task">

    <h1>Create Task</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            
        </table>
        <input type="submit" value="Submit"></td>
    </form>
</div>

{% endblock content %}
```
### 5. Membuat routing
Menambahkan beberapa potongan kode ke file `urls.py` sehingga menjadi seperti berikut.
```
from django.urls import path
from todolist.views import register, login_user, logout_user, show_todolist, create_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
]
```
### 6. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat 
Menjalankan perintah `git add`, `git push`, dan `git commit`. Aplikasi akan ter-_deploy_ dengan sendirinya karena telah di-_deploy_ pada tugas sebelumnya.

### 7. Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
Mengakses https://pbp-katalog.herokuapp.com/todolist, lalu mendaftarkan dua akun berikut.
Username 1: user1
Password 1: D:Hgwgsw_9M5q7h
Username 2: user2
Password 2: B-YVz8Z69k!tMmQ

### Link aplikasi: [todolist](https://pbp-katalog.herokuapp.com/todolist)
Dapat juga diakses melalui:
1. https://pbp-katalog.herokuapp.com/todolist untuk mengakses halaman utama yang memuat tabel task (harus login terlebih dahulu)
2. https://pbp-katalog.herokuapp.com/todolist/login untuk mengakses form login
3. https://pbp-katalog.herokuapp.com/todolist/register untuk mengakses form registrasi akun
4. https://pbp-katalog.herokuapp.com/todolist/create-task untuk mengakses form pembuatan task (harus login terlebih dahulu)
5. https://pbp-katalog.herokuapp.com/todolist/logout berisi mekanisme logout.

### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
1. Inline
Style attribute ditambahkan di tag HTML secara langsung tanpa menggunakan selector.
Kelebihan: style atribut dapat langsung ditambahkan tanpa membutuhkan file CSS terpisah.
Kekurangan: Setiap tag pada HTML perlu diterapkan style-nya secara satu per satu sehingga cukup memakan waktu.
2. Internal
Internal CSS ditambahkan dengan cara menyisipkan tag `<style>` pada
`<head>` section di dalam HTML file. 
Kelebihan: dapat menggunakan selector id dan kelas di dalam stylesheet serta tidak membutuhkan
file baru.
Kekurangan: dapat meningkatkan size halaman website dan loading time.
3. External
Menggunakan file terpisah untuk melakukan styling pada website.
Kelebihan: File CSS dapat digunakan untuk styling banyak halaman sekaligus.
Kekurangan: Menggunakan banyak file CSS terpisah dapat meningkatkan proses pengaksesan website.

### Jelaskan tag HTML5 yang kamu ketahui.
1. `<header>` -> merepresentasikan header dari dokumen.
2. `<body>` -> merepresentasikan body dari dokumen.
3. `<footer>` -> merepresentasikan footer dari dokumen.
4. `<nav>` -> merepresentasikan bagian navigasi dari dokumen.
5. `<b>` -> menampilkan text dalam huruf tebal.
6. `<p>` -> merepresentasikan paragraf.
7. `<h1>` sampai `<h6>` -> merepresentasikan heading.
8. `<i>` -> menampilkan text dalam italic.
9. `<ol>` -> menampilkan ordered list.
10. `<ul> -> menampilkan unordered list.

### Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. Element selector
-> Menggunakan tag HTML untuk menerapkan styling.
2. Class selector
-> Menggunakan class untuk menerapkan styling dengan format `.[nama_kelas]`.
3. ID selector
-> Menggunakan id untuk menerapkan styling dengan format `#[id]`.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Menambahkan potongan kode berikut untuk meng-include Bootstrap di bagian `<head>` halaman HTML
```
<meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Create Task</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
```
2. Menerapkan kustomisasi pada keempat halaman HTML seperti mengubah warna tombol, layout halaman, dll.
3. Menggunakan cards untuk menampilkan to do list dan menggunakan display grid dengan value repeat dan auto-fill agar penataan cards lebih fleksibel.
4. Menambahkan efek ketika cards di-hover.

1. Import modul yang dibutuhkan
https://pypi.org/project/pyzbar/

https://pythonslearning.com/2021/04/how-to-build-real-time-opencv-barcode-reader-or-scanner-using-python.html

2. Inisiasi buka webcam laptop/hp dengan 'cap'

3. Buat kumpulan library dengan perintah " pipreqs . "

4. Buat folder templates dan index.html

5. Buat file app.py

6. Dalam file app.py import library, init app, and create routes to index.html

7. Buat debugger :
{
    app.run(debug=True)
}

8. Buat file base.html dan import template dari starter template bootstrap

9. Buat navbar pada file base.html dan tambahkan icon:
{
    <!-- <a href="https://imgbb.com/"><img src="https://i.ibb.co/HP1tYkD/2998.png" alt="2998" border="0"></a> -->
}

10. Buat jinja template.

11. Masuk ke index.html hapus semua code dan import data dari base.html:
{
    {% extends 'base.html' %}{% block content %}

    {% endblock %}
}

12. Isikan judul dan atur tata letaknya pada index html

13. Untuk import frame tambahkan tag <!-- img -->, buat file baru dengan camera.py

14. Buat folder untuk menyimpan folder css style.css di folder templates/static kemudian link ke dalam file base.html 

15. Buat file camera.py untuk menampilkan webcam

16. Import camera.py ke app.py :
{
    from camera import Video
}

17. Buat route baru pada app.py untuk menampilkan webcam dan tambahkan method Response pada library Flask
{
    @app.route('/video')
}

18. Panggil fungsi camera diatas route video
{
    def gen_frames():
}

18. Tambahkan yield di def gen_frames() bawah frame :
{
    b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'
}

19. Kembali ke @app.route('/video') tambahkan code di Response
{
    return Response(gen_frames(),
}

20. Tambahkan MimeType di bawah return Response tadi
{
    mimetype = 'multipart/x-mixed-replace; boundary = frame'
}

21. Masuk ke index.html lalu pada tag <!-- <img> --> tambahkan code:
{
    
}
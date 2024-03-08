from django.shortcuts import render

from movies.models import Category, Movie

kategori_liste=["Macera","Korku","Komedi","Belgesel","Bilim Kurgu","Çizgi Film"]
film_liste = [
    {
        "id": 1,
        "film_adi": "film 1",
        "aciklama": "film 1 açıklama",
        "resim": "1.jpeg",
        # "resim": "https://picsum.photos/id/27/367/267",
        "anasayfa": True
    },
     {
        "id": 2,
        "film_adi": "film 2",
        "aciklama": "film 2 açıklama",
        "resim": "2.jpeg",
        # "resim": "https://picsum.photos/id/24/367/267",
        "anasayfa": False
    },
    {
        "id": 3,
        "film_adi": "film 3",
        "aciklama": "film 3 açıklama",
        "resim": "3.jpeg",
        # "resim": "https://picsum.photos/id/30/367/267",
        "anasayfa": True
    },
    {
        "id": 4,
        "film_adi": "film 4",
        "aciklama": "film 4 açıklama",
        "resim": "4.jpeg",
        #"resim": "https://static.depositphotos.com/storage/file_upload/item_188634220_4f8dd3489dbe1893aa8cffb78f12df2c.jpg?1628253112",
        "anasayfa": True
    }, 
        {
        "id": 5,
        "film_adi": "film 5",
        "aciklama": "film 5 açıklama",
        "resim": "4.jpeg",
        #"resim": "https://static.depositphotos.com/storage/file_upload/item_188634220_4f8dd3489dbe1893aa8cffb78f12df2c.jpg?1628253112",
        "anasayfa": False
    } 
]
# Create your views here.
def home(request):
    data = {
    "kategoriler": Category.objects.all(),
    "filmler":Movie.objects.filter(anasayfa=True)    
    }
    return render(request, "index.html", data)

def movies(request):
    data = {
    "kategoriler": Category.objects.all(),
    "filmler":Movie.objects.all()     
    }
    return render(request, "movies.html",data)

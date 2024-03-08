from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 200)

class Movie(models.Model):
    film_adi = models.CharField(max_length = 300)
    aciklama = models.TextField()
    resim = models.CharField(max_length =100)
    anasayfa = models.BooleanField(default = False)
    eklenme_tarihi = models.DateTimeField(auto_now_add=True)
    güncelleme_tarihi = models.DateTimeField(auto_now =True)
    
    class Meta:
        verbose_name ="Film"
        verbose_name_plural ="Filmler"
    
    def __str__(self) -> str:
        return self.film_adi
    
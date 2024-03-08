from django.contrib import admin
from movies.models import Category, Movie

# Register your models here.

admin.site.register(Category)


# class movieAdmin(admin.ModelAdmin):
#     fields = ("film_adi","aciklama","eklenme_tarihi","güncelleme_tarihi" )

admin.site.register(Movie)
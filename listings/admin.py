from django.contrib import admin
from listings.models import *


class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre')  # liste les champs que nous voulons sur l'affichage de la liste

class NewAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('title', 'content')  # liste les champs que nous voulons sur l'affichage de la liste


admin.site.register(Band, BandAdmin)
admin.site.register(New, NewAdmin)

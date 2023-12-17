from django.contrib import admin


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')  # liste les champs que nous voulons sur l'affichage de la liste

class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'stock', 'price')

admin.site.register(Band, BandAdmin)
admin.site.register(New, NewAdmin)
admin.site.register(Article, ArticleAdmin)

from django.contrib import admin

from ProjectProtect.moviesite.models import MovieModel, Comment


# Register your models here.
@admin.register(Comment)
class Comment(admin.ModelAdmin):
    pass
class AdminMovies(admin.ModelAdmin):
    list_display = ('custom_pk', 'name', 'year', 'genre')


    def custom_pk(self, obj):
        return obj.pk

    custom_pk.short_description = 'ID'


admin.site.register(MovieModel, AdminMovies)

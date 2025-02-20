from django.contrib import admin
from ..models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'name')
    list_display_links = ('id', 'name',)
    list_per_page = 50
    search_fields = ('name',)

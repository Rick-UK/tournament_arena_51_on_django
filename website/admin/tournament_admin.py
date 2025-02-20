from django.contrib import admin
from ..models import Tournament


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'is_active', 'name', 'game', 'published_at', 'start_date')
    list_display_links = ('id', 'name',)
    list_per_page = 50
    search_fields = ('name',)
    list_filter = ('is_active', 'game', 'start_date')

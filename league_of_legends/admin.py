from django.contrib import admin

from django.contrib import admin
from .models import Champion, Plateform, Season, Position, Player, Game, Participant

@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):
    list_display = ['champ_id', 'champ_name']
    search_fields = ['champ_name']

@admin.register(Plateform)
class PlateformAdmin(admin.ModelAdmin):
    list_display = ['id_plateform', 'name_plateform']
    search_fields = ['name_plateform']

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ['id_seasonn', 'season']
    search_fields = ['season']

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['id_position', 'name_position']
    search_fields = ['name_position']

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['player_id', 'name']
    search_fields = ['name']

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['game_id', 'id_plateform', 'id_seasonn', 'duration', 'winner']
    list_filter = ['id_plateform', 'id_seasonn', 'winner']
    search_fields = ['game_id']

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['id_position', 'player_id', 'game_id', 'champ_id', 'date_game']
    list_filter = ['id_position', 'game_id', 'champ_id', 'date_game']
    search_fields = ['player_id', 'champ_id']
    list_editable = ['date_game']

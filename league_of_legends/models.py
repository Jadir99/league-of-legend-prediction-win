# from django.db import models

# class TodoItem(models.Model):
#     title=models.CharField(max_length=255)
#     winn=models.BooleanField()


# class Client(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

from django.db import models

class Champion(models.Model):
    champ_id = models.AutoField(primary_key=True)  # AutoField is usually preferred for primary keys
    champ_name = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'champion'

class Plateform(models.Model):
    id_plateform = models.AutoField(primary_key=True)
    name_plateform = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'plateform'

class Season(models.Model):
    id_seasonn = models.AutoField(primary_key=True)
    season = models.IntegerField(null=True)

    class Meta:
        db_table = 'season'

class Position(models.Model):
    id_position = models.AutoField(primary_key=True)
    name_position = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'position'

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'player'

class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    id_plateform = models.ForeignKey(Plateform, on_delete=models.CASCADE)
    id_seasonn = models.ForeignKey(Season, on_delete=models.CASCADE)
    duration = models.SmallIntegerField(null=True)
    winner = models.SmallIntegerField(null=True)
    first_tower = models.SmallIntegerField(null=True)
    first_blood = models.SmallIntegerField(null=True)
    first_inhibitor = models.SmallIntegerField(null=True)
    first_baron = models.SmallIntegerField(null=True)
    first_dragon = models.SmallIntegerField(null=True)
    first_harry = models.SmallIntegerField(null=True)
    tower_kills = models.IntegerField(null=True)
    inhibitor_kills = models.IntegerField(null=True)
    baron_kills = models.IntegerField(null=True)
    dragon_kills = models.IntegerField(null=True)
    herald_kills = models.IntegerField(null=True)

    class Meta:
        db_table = 'game'

class Participant(models.Model):
    id_position = models.ForeignKey(Position, on_delete=models.CASCADE)
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    champ_id = models.ForeignKey(Champion, on_delete=models.CASCADE)
    date_game = models.DateField(null=True)

    class Meta:
        db_table = 'participant'
        unique_together = ('id_position', 'player_id', 'game_id', 'champ_id')

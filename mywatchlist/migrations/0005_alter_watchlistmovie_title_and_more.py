# Generated by Django 4.1 on 2022-09-21 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0004_alter_watchlistmovie_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlistmovie',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='watchlistmovie',
            name='watched',
            field=models.BooleanField(),
        ),
    ]

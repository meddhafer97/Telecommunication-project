# Generated by Django 3.0.8 on 2020-07-14 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deplacement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tab_bords',
            name='Heure_depart',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Heure_depart'),
        ),
        migrations.AlterField(
            model_name='tab_bords',
            name='Heure_retour',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Heure_retour'),
        ),
    ]
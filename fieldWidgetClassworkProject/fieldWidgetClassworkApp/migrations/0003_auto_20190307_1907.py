# Generated by Django 2.0.6 on 2019-03-07 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fieldWidgetClassworkApp', '0002_auto_20190307_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='superhero',
            old_name='dropDown',
            new_name='richOrSuperpower',
        ),
        migrations.RenameField(
            model_name='superhero',
            old_name='dropDown2',
            new_name='superHeroRating',
        ),
        migrations.RenameField(
            model_name='superhero',
            old_name='radio',
            new_name='whichSuperPower',
        ),
    ]
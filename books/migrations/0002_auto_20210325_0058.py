# Generated by Django 3.1.7 on 2021-03-25 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read all books'), ('go_list', 'Can see the book'), ('can_drive', 'Can drive'), ('can_vote', 'Can vote in elections'), ('can_dr', 'Can dcohol'), ('can_dri', 'Caive'), ('can_vo', 'Can votns')]},
        ),
    ]
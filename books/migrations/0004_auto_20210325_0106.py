# Generated by Django 3.1.7 on 2021-03-25 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210325_0059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read all books'), ('go_list', 'Can see the list of books')]},
        ),
    ]
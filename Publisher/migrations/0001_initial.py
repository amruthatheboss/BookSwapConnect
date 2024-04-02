# Generated by Django 5.0.3 on 2024-03-28 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_paddbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pbook_name', models.CharField(max_length=15)),
                ('pbook_desc', models.CharField(max_length=50)),
                ('pbook_price', models.EmailField(max_length=50)),
                ('pbook_photo', models.FileField(upload_to='Assets/PublisherAddBook/')),
                ('pbook_authname', models.CharField(max_length=15)),
                ('pbook_genre', models.CharField(max_length=15)),
                ('pbook_qty', models.CharField(max_length=15)),
            ],
        ),
    ]
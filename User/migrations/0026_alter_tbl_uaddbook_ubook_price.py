# Generated by Django 5.0.4 on 2024-04-11 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0025_tbl_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_uaddbook',
            name='ubook_price',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-22 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0002_tbl_publisher_user_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_name', models.CharField(max_length=15)),
                ('agent_contact', models.CharField(max_length=10)),
                ('agent_address', models.CharField(max_length=10)),
                ('agent_proof', models.FileField(upload_to='Assets/UserProof/')),
                ('agent_email', models.EmailField(max_length=50)),
                ('agent_password', models.CharField(max_length=10)),
                ('user_status', models.IntegerField(default='0')),
            ],
        ),
    ]

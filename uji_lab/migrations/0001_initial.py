# Generated by Django 3.2.23 on 2024-01-04 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UjiLab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=100)),
                ('nama', models.CharField(max_length=50)),
                ('satuan', models.CharField(max_length=250)),
                ('id_bidang', models.CharField(max_length=100)),
                ('harga', models.CharField(max_length=50)),
            ],
        ),
    ]

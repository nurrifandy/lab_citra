# Generated by Django 3.2.23 on 2023-12-09 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dokter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_dokter', models.CharField(max_length=100)),
                ('nama', models.CharField(max_length=100)),
                ('komisi_belum_dibayar', models.IntegerField(default=0)),
                ('komisi_sudah_dibayar', models.IntegerField(default=0)),
            ],
        ),
    ]
# Generated by Django 3.2.23 on 2024-01-08 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pemeriksaan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=100)),
                ('id_pasien', models.CharField(max_length=100)),
                ('id_bidang', models.CharField(max_length=100)),
                ('id_dokter', models.CharField(max_length=100)),
                ('id_tester', models.CharField(max_length=100)),
                ('tanggal_pemeriksaan', models.DateField()),
                ('total_biaya', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=100)),
                ('diagnosa_awal', models.CharField(max_length=250)),
            ],
        ),
    ]

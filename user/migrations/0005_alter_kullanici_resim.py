# Generated by Django 4.2.3 on 2024-08-01 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_kullanici_kullaniciadi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kullanici',
            name='resim',
            field=models.FileField(blank=True, null=True, upload_to='kullanicilar/', verbose_name='Profil Resmi'),
        ),
    ]

# Generated by Django 4.2.3 on 2024-07-26 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=50)),
                ('resim', models.FileField(upload_to='filmler/', verbose_name='Film Resmi')),
                ('video', models.FileField(upload_to='videolar/', verbose_name='Film Fragmanı')),
            ],
        ),
    ]

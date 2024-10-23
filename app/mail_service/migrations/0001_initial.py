# Generated by Django 5.1.2 on 2024-10-14 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.EmailField(max_length=254, verbose_name='От кого')),
                ('recipient', models.EmailField(max_length=254, verbose_name='Кому')),
                ('message', models.TextField(verbose_name='Текст письма')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
            ],
        ),
    ]

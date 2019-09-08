# Generated by Django 2.2.5 on 2019-09-08 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('uid', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=1024)),
                ('title', models.CharField(max_length=64)),
                ('author', models.CharField(max_length=32)),
                ('published_at', models.DateTimeField()),
                ('content', models.TextField()),
            ],
        ),
    ]

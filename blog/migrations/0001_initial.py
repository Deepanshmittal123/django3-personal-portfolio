# Generated by Django 3.1.3 on 2020-11-12 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='All_blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField()),
            ],
        ),
    ]

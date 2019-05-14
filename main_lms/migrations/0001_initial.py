# Generated by Django 2.2 on 2019-05-14 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BooksInsert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.CharField(max_length=100)),
                ('bname', models.CharField(max_length=500)),
                ('btype', models.CharField(max_length=200)),
                ('bwriter', models.CharField(max_length=400)),
                ('bshelf', models.CharField(max_length=400)),
                ('bcreated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'booksinsert',
            },
        ),
    ]
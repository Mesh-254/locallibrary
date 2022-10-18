# Generated by Django 4.1.2 on 2022-10-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_book_date_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='date_published',
        ),
        migrations.AddField(
            model_name='book',
            name='Language',
            field=models.CharField(blank=True, help_text='Language for this book', max_length=255),
        ),
    ]

# Generated by Django 4.1.4 on 2023-02-18 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_slug',
            field=models.SlugField(allow_unicode=True, max_length=100, unique=True),
        ),
    ]

# Generated by Django 5.0.7 on 2024-08-23 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_category_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_edited',
            field=models.DateTimeField(null=True),
        ),
    ]

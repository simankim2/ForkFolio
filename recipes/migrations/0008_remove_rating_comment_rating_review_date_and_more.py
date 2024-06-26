# Generated by Django 5.0.4 on 2024-04-26 03:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_rating_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='comment',
        ),
        migrations.AddField(
            model_name='rating',
            name='review_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='rating',
            name='review_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]

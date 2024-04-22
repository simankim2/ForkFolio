# Generated by Django 5.0.4 on 2024-04-21 23:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=100)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_text', models.TextField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='recipes.recipe')),
            ],
        ),
    ]
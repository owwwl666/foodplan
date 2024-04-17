# Generated by Django 5.0.4 on 2024-04-17 11:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodplan', '0002_alter_menutype_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='menu_type',
        ),
        migrations.CreateModel(
            name='MenuTypeRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='menu_type_recipes', to='foodplan.menutype', verbose_name='Тип меню')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='menu_type_recipes', to='foodplan.recipe', verbose_name='Рецепт')),
            ],
            options={
                'verbose_name': 'Рецепт - тип меню',
                'verbose_name_plural': 'Рецепты по типам меню',
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='menu_type',
            field=models.ManyToManyField(blank=True, null=True, related_name='recipes', through='foodplan.MenuTypeRecipe', to='foodplan.menutype', verbose_name='Тип меню'),
        ),
    ]
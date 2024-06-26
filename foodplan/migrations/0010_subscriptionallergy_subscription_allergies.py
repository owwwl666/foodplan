# Generated by Django 5.0.4 on 2024-04-18 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodplan', '0009_menutype_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionAllergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subscription_allergies', to='foodplan.allergy', verbose_name='Аллергия')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subscription_allergies', to='foodplan.subscription', verbose_name='Подписка')),
            ],
            options={
                'verbose_name': 'Аллергия в подписке',
                'verbose_name_plural': 'Аллергии в подписке',
            },
        ),
        migrations.AddField(
            model_name='subscription',
            name='allergies',
            field=models.ManyToManyField(related_name='subscriptions', through='foodplan.SubscriptionAllergy', to='foodplan.allergy', verbose_name='Аллергия'),
        ),
    ]

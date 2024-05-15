# Generated by Django 5.0.3 on 2024-05-15 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_alter_watchlist_listingid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='listingid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listingwatchlist', to='auctions.listing'),
        ),
    ]
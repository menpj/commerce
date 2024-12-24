# Generated by Django 5.0.3 on 2024-05-17 09:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_alter_bid_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='commentid',
        ),
        migrations.AddField(
            model_name='comments',
            name='datetim',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 5, 17, 14, 41, 48, 493838), null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]

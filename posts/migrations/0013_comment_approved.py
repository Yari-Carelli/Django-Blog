# Generated by Django 3.2.16 on 2023-01-06 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_remove_comment_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]

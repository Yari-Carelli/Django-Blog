# Generated by Django 3.2.16 on 2023-01-07 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_comment_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved',
        ),
    ]
# Generated by Django 5.1.7 on 2025-03-12 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graviapps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar_content_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2.4 on 2022-08-02 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='github_link',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='member',
            name='position',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='text',
            name='created_at',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='birth',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='member',
            name='image_link',
            field=models.CharField(max_length=100),
        ),
    ]

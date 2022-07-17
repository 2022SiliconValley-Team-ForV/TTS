# Generated by Django 3.2.4 on 2022-07-17 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_rename_model_id_modellink_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modellink',
            name='id',
            field=models.ForeignKey(db_column='model_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='modellink', serialize=False, to='backend.member', unique=True),
        ),
    ]

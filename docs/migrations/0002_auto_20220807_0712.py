# Generated by Django 3.2 on 2022-08-07 07:12

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='doc',
            name='id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-10 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
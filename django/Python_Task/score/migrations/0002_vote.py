# Generated by Django 4.1.2 on 2022-10-19 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('update_datetime', models.DateTimeField(auto_now=True)),
                ('vote', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vote',
            },
        ),
    ]
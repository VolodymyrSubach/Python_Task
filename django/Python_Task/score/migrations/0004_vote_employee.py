# Generated by Django 4.1.2 on 2022-10-19 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0003_menu_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='employee',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee', to='score.menu'),
        ),
    ]
# Generated by Django 3.0.8 on 2020-08-07 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_account', '0004_role_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilemodel',
            name='roles',
            field=models.ManyToManyField(to='cars_account.Role'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
# Generated by Django 4.1.5 on 2023-12-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smanage', '0016_usercredentials_user_alter_customuser_generate_key_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercredentials',
            name='user',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='generate_key',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='usercredentials',
            name='key_field',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usercredentials',
            name='password_field',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 4.1.5 on 2023-06-13 09:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('smanage', '0003_uploadedfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='generated_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]

# Generated by Django 4.2.1 on 2024-02-16 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_roomcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='app.roomcategory'),
            preserve_default=False,
        ),
    ]

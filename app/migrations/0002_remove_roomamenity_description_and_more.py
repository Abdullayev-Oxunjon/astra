# Generated by Django 4.2.1 on 2024-03-13 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomamenity',
            name='description',
        ),
        migrations.RemoveField(
            model_name='roomamenity',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='roomamenity',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='roomamenity',
            name='description_uz',
        ),
        migrations.RemoveField(
            model_name='roomamenity',
            name='image',
        ),
        migrations.RemoveField(
            model_name='roomamenity',
            name='title',
        ),
        migrations.RemoveField(
            model_name='roomamenity',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='roomamenity',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='roomamenity',
            name='title_uz',
        ),
        migrations.AddField(
            model_name='roomamenity',
            name='amenity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='amenities', to='app.features'),
            preserve_default=False,
        ),
    ]
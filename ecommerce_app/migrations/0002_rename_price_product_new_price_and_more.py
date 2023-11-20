# Generated by Django 4.2.5 on 2023-11-19 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='new_price',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image_1',
            field=models.ImageField(default='5', upload_to='product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image_2',
            field=models.ImageField(default='2', upload_to='product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='new',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=2, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='video_file',
            field=models.FileField(default='3', upload_to='videos'),
            preserve_default=False,
        ),
    ]

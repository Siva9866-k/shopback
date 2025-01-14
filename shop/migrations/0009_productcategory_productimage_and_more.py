# Generated by Django 5.1.4 on 2024-12-13 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cat_img', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='additional_images',
            field=models.ManyToManyField(blank=True, to='shop.productimage'),
        ),
    ]

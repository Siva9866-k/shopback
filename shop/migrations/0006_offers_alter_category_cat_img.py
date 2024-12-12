# Generated by Django 5.1.4 on 2024-12-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_category_cat_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('offer_img', models.ImageField(upload_to='img')),
                ('offer', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_img',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
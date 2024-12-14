from django.db import models
from .category import Category
from PIL import Image

class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    cat_img = models.ImageField(upload_to='img')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='img')  # Main image
    desc = models.TextField()
    price = models.IntegerField()
    thumbnail1 = models.ImageField(upload_to='img', blank=True, null=True)  # Thumbnail 1
    thumbnail2 = models.ImageField(upload_to='img', blank=True, null=True)  # Thumbnail 2
    thumbnail3 = models.ImageField(upload_to='img', blank=True, null=True)  # Thumbnail 3

    @staticmethod
    def get_category_id(get_id):
        if get_id:
            return Product.objects.filter(category=get_id)
        else:
            return Product.objects.all()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self._process_main_image(self.image)
        self._process_thumbnail(self.thumbnail1)
        self._process_thumbnail(self.thumbnail2)
        self._process_thumbnail(self.thumbnail3)

    def _process_main_image(self, main_image):
        """Resize the main image to 180x180 pixels."""
        if main_image:
            img_path = main_image.path
            with Image.open(img_path) as img:
                img = img.convert("RGBA")
                img.thumbnail((180, 180))
                background = Image.new("RGBA", (180, 180), (255, 255, 255, 255))
                offset = (
                    (180 - img.size[0]) // 2,
                    (180 - img.size[1]) // 2
                )
                background.paste(img, offset)
                background.convert("RGB").save(img_path, optimize=True, quality=85)

    def _process_thumbnail(self, thumbnail):
        """Resize the thumbnails to 140x140 pixels."""
        if thumbnail:
            img_path = thumbnail.path
            with Image.open(img_path) as img:
                img = img.convert("RGBA")
                img.thumbnail((140, 140))
                background = Image.new("RGBA", (140, 140), (255, 255, 255, 255))
                offset = (
                    (140 - img.size[0]) // 2,
                    (140 - img.size[1]) // 2
                )
                background.paste(img, offset)
                background.convert("RGB").save(img_path, optimize=True, quality=85)

class Offers(models.Model):
    title = models.CharField(max_length=20)
    offer_img = models.ImageField(upload_to='img')
    offer_name = models.CharField(max_length=20, default="Default Offer Name")
    offer = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.offer_img:
            img_path = self.offer_img.path
            with Image.open(img_path) as img:
                img = img.convert("RGBA")
                img.thumbnail((140, 140))
                background = Image.new("RGBA", (140, 140), (255, 255, 255, 255))
                offset = (
                    (140 - img.size[0]) // 2,
                    (140 - img.size[1]) // 2
                )
                background.paste(img, offset)
                background.convert("RGB").save(img_path, optimize=True, quality=85)

    def __str__(self):
        return self.title

from django.db import models
from .category import Category
from PIL import Image

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='img')
    desc = models.TextField()
    price = models.IntegerField()

    # Static method
    @staticmethod
    def get_category_id(get_id):
        if get_id:
            return Product.objects.filter(category=get_id)
        else:
            return Product.objects.all()


# Offers section
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
                # Ensure the image has an RGBA mode (supports alpha channel)
                img = img.convert("RGBA")

                # Resize the image while maintaining aspect ratio
                img.thumbnail((140, 140))

                # Create a new 150x150 image with a white background
                background = Image.new("RGBA", (140, 140), (255, 255, 255, 255))
                # Calculate position to paste the image onto the center of the background
                offset = (
                    (140 - img.size[0]) // 2,  # Center horizontally
                    (140 - img.size[1]) // 2   # Center vertically
                )
                background.paste(img, offset)

                # Save the final image, converting to RGB to drop alpha if not needed
                background.convert("RGB").save(img_path, optimize=True, quality=85)

    def __str__(self):
        return self.title

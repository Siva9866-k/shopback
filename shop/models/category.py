from django.db import models
from PIL import Image, ImageOps

class Category(models.Model):
    name = models.CharField(max_length=20)
    cat_img = models.ImageField(upload_to='img/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.cat_img:
            img_path = self.cat_img.path
            with Image.open(img_path) as img:
                # Ensure the image has an RGBA mode (supports alpha channel)
                img = img.convert("RGBA")

                # Resize the image while maintaining aspect ratio
                img.thumbnail((150, 150))

                # Create a new 150x150 image with a white background
                background = Image.new("RGBA", (150, 150), (255, 255, 255, 255))
                # Calculate position to paste the image onto the center of the background
                offset = (
                    (150 - img.size[0]) // 2,  # Center horizontally
                    (150 - img.size[1]) // 2   # Center vertically
                )
                background.paste(img, offset)

                # Save the final image, converting to RGB to drop alpha if not needed
                background.convert("RGB").save(img_path, optimize=True, quality=85)

    def __str__(self):
        return self.name



'''from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=20)
    cat_img=models.ImageField(upload_to='img', default='media/default.jpg')
    def __str__(self):
       return self.name    '''
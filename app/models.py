from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField(null=False)
    description = models.TextField(null=False)
    price = models.TextField(null=False)

    def __str__(self):
        return self.title
    def mini_title(self, max_char:str=25):
        if len(self.title) > max_char:
            return self.title[:max_char] + "..."
        else:
            return self.title
    def getPrice(self):
        format = f'{int(self.price):,}'.replace(',', '.')
        return f'Rp. {format},-'
    

class Image(models.Model):
    image_uri = models.TextField(null=False)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.image_uri
    

class Comment(models.Model):
    name = models.TextField(null=False)
    comment = models.TextField(null=False)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.comment
    

class Link(models.Model):
    no_wa = models.TextField(null=False)
    web_link = models.TextField(null=False)
    fb_link = models.TextField(null=False)
    ig_link = models.TextField(null=False)
    web_click = models.IntegerField(null=False, default=0)
    fb_click = models.IntegerField(null=False, default=0)
    ig_click = models.IntegerField(null=False, default=0)
    web_checkout = models.IntegerField(null=False, default=0)
    fb_checkout = models.IntegerField(null=False, default=0)
    ig_checkout = models.IntegerField(null=False, default=0)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='links')

    def __str__(self):
        return f"no_wa={self.no_wa}, web_link={self.web_link}, fb_link={self.fb_link}, ig_link={self.ig_link}"
    def total_clicks(self):
        return self.web_click + self.ig_click + self.fb_click
    def total_checkout(self):
        return self.web_checkout + self.ig_checkout + self.fb_checkout


class Date(models.Model):
    platform = models.TextField(null=False)
    date = models.DateTimeField(null=False)
    id_link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name='dates')

    def __str__(self):
        return str(self.date)
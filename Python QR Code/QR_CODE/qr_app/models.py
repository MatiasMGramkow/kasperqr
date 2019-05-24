from django.db import models
import qrcode


class Qr_generate_web(models.Model):
    
    def generate(self, url):
       img_string = qrcode.make(url)
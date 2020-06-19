from django.db import models
from django.contrib.auth import get_user_model
import PIL
from PIL import Image
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, SmartResize, Adjust, ResizeToFit

class Image(models.Model):
    SIZE_TYPES = (
            (1, '600x600'),
            (2, '700x700'),
            (3, '800x800'),
            (4, '900x900'),
            (5, '1000x1000'),
            )
    imag = models.ImageField(verbose_name='Изображение')

    size_type = models.IntegerField(verbose_name = 'Выберите размер для ресайза изображения', choices = SIZE_TYPES, default = '1') 
    imag_one =ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
            ResizeToFit(600,600)], source='imag', options={'quality': 90})
    imag_two =ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
            ResizeToFit(700, 700)], source='imag', options={'quality': 90})
    imag_three =ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
            ResizeToFit(800, 800)], source='imag',options={'quality': 90})
    imag_four =ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
            ResizeToFit(900, 900)], source='imag', options={'quality': 90})
    imag_five =ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
            ResizeToFit(1000, 1000)], source='imag', options={'quality': 90})


    User = get_user_model()
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    
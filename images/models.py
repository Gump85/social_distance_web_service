from django.db import models
from django.urls import reverse
from sorl.thumbnail import ImageField
from exiffield.fields import ExifField


class UploadImage(models.Model):
    """ Модель картинки, загружаемой на сайт пользователем """
    image = models.ImageField('файл изображения', upload_to='images/%Y/%m/%d')
    description = models.TextField('Комментарий к изображению')
    created = models.DateField('Время создания объекта в БД', auto_now_add=True, db_index=True)
    exif = ExifField(source='image',)
    coordinates = models.CharField('Геоданные снимка', max_length=200, null=True)
    social_activity = models.CharField(
        'Количество людей на фотографии',
        max_length=50,
        blank=True,
        null=True
    )

    class Meta:
        """ добавляем порядок сортировки изображений """
        ordering = ['created']

    def __str__(self):
        """ возвращает строковое значение для представления объекта модели """
        return self.coordinates

    def get_absolute_url(self):
        """ возвращает ссылку на изображение """
        return reverse('images:image_detail', args=[self.id])

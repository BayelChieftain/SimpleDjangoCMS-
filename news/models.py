from django.db import models

class Articles(models.Model):
    title = models.CharField("Name", max_length=190)
    annonce = models.CharField('Anounce', max_length=250)
    full_text = models.TextField('article')
    date = models.DateTimeField('date of publication')

    def __str__(self):
        return f'News: {self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'


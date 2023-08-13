from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class Advertisement(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Укажите, возможен ли торг')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField('изображение', upload_to='advertisements/')

    @admin.display(description='дата создания')
    def created_date(self):
        if self.create_at.date() == timezone.now().date():
            created_time = self.create_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.create_at.strftime('%d.%m.%Y')
    
    @admin.display(description='дата обновления')
    def updated_date(self):
        if self.update_at.date() == timezone.now().date():
            upd_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: blue; font-weight: bold;">Обновлено в {}</span>', upd_time 
            )
        return self.update_at.strftime('%d.%m.%Y')

    first_name = models.CharField(max_length=100)

    class Meta:
        db_table = "advertisements"
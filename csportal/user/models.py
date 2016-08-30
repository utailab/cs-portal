from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.pk, filename)


class CustomUser(AbstractUser):
    username = models.CharField(
        'username',
        max_length=16,
        primary_key=True,
        help_text='Required. ID number.',
        validators=[RegexValidator(regex='^[0-9]{9}$',
                    message='Enter a valid ID number.')],
        error_messages={
            'unique': 'A user with that username already exists.',
        },
    )
    first_name = models.CharField('first name', max_length=30)
    last_name = models.CharField('last name', max_length=30)
    email = models.EmailField('email address')

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']


class Student(models.Model):
    user = models.OneToOneField(CustomUser,
                                verbose_name='ID number',
                                on_delete=models.CASCADE)
    bio = models.TextField(verbose_name='bio')
    cv = models.TextField(verbose_name='CV')
    pic = models.ImageField(verbose_name='profile picture',
                            upload_to=user_directory_path)

    def __str__(self):
        return '{}'.format(self.user.get_username())

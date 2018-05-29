from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Ownable(models.Model):
    user = models.ForeignKey('auth.User', verbose_name=_("Author"),
                             on_delete=models.CASCADE,
                             related_name="%(class)ss")

    class Meta:
        abstract = True


class RegisteredUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tracking = models.ManyToManyField('self',
                                      related_name='tracked_by',
                                      blank=True, symmetrical=False)


class FeedItem(Ownable):
    content = models.CharField("Content", max_length=1000,
                               blank=True, null=True)

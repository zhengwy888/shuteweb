from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Transaction(models.Model):
    CHINESE_MED = 'cn_med'
    WESTERN_MED = 'we_med'
    MED_TYPES = (
            (CHINESE_MED, _('Chinese Medicine')),
            (WESTERN_MED, _('Western Medicine')),
            )
    date = models.DateTimeField()
    type = models.CharField(max_length=255, choices = MED_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return self.type + str(self.amount)


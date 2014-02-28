from django.contrib import admin
from revenue.models import Transaction

#admin.site.register(Transaction)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('type', 'amount', 'date')
    list_filter = ('type',)

admin.site.register(Transaction, TransactionAdmin)

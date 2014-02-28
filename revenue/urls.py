from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^incomes/', include('incomes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
    (r'^$', 'revenue.views.index'),
    url(r'^(?P<trans_id>\d+)/del$', 'revenue.views.del_transactions', name="trans-delete"),
    url(r'^add$', 'revenue.views.add_transactions', name="trans-add"),
)

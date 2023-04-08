from django.contrib import admin
from .models.articles import Articles
from .models.customers import Customers
from .models.destinations import Destinations
from .models.opinions import Opinions
from .models.promotions import Promotions

admin.site.register(Articles)
admin.site.register(Customers)
admin.site.register(Destinations)
admin.site.register(Opinions)
admin.site.register(Promotions)

# Register your models here.

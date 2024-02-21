from django.contrib import admin
from .models import Vehicle
from .models import Spare
from .models import CartItem
from .models import WishlistItem


admin.site.register(Vehicle)
admin.site.register(Spare)

admin.site.register(CartItem)
admin.site.register(WishlistItem)

# Register your models here.

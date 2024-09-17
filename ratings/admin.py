from django.contrib import admin

from .models import (
	five_star,
	four_star,
	three_star,
	two_star,
	one_star
)

# Register your models here.

admin.site.register(five_star)
admin.site.register(four_star)
admin.site.register(three_star)
admin.site.register(two_star)
admin.site.register(one_star)

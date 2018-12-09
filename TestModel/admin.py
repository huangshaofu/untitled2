from django.contrib import admin

# Register your models here.
from TestModel.models import Test
from TestModel.models import User
from TestModel.models import User2
# Register your models here.
admin.site.register(Test)
admin.site.register(User)
admin.site.register(User2)
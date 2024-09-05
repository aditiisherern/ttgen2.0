

# Register your models here.
from django.contrib import admin

from .models import subject #model name

admin.site.register(subject)

from .models import sched #model name

admin.site.register(sched)


from .models import teacher #model name

admin.site.register(teacher)

from .models import classs #model name

admin.site.register(classs)

from .models import subthing1

admin.site.register(subthing1)

from .models import nofixed

admin.site.register(nofixed)
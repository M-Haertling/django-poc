# Overview

|Topic|Solution|Notes|
|-|-|-|
|Data Audit|django-auditlog||
|Authentication|OOB||
|Authorization|OOB + djangorestframework||
|File Import|djangorestframework||
|File Export|djangorestframework||
|CRUD REST|djangorestframework||
|Table Views|React MUI + djangorestframework||
|Create/Update Form|React + djangorestframework||
|Validations|djangorestframework||
|Admin|OOB|Permission management, app settings, etc.|
|Change Approval|? custom plugin ?||

|Requirement|Notes|
|-|-|
|Simplicty|Need a clean way to combine all these features into an easy to configure and initialize singular interface|
|Support OIDC||
|Support Excel and CSV upload/download||
|Support non-web-client REST API access||
|||


# Table Display

Consider using a React frontend with mui for tables.

Build nessesary backend APIs with standard Django.

## Install

```
pip install django_tables2
```

## Usage

**settings.py**

```
INSTALLED_APPS += [
    'auditlog',
]
```

**models.py**

```
from django.db import models

class Person(models.Model):
   name = models.CharField(max_length=100)
   salary = models.CharField(max_length=20)
```

**views.py**

```
from .models import Person
import django_tables2 as tables

class PersonTable(tables.Table):
   class Meta:
      model = Person

class PersonView(tables.SingleTableView):
   table_class = PersonTable
   queryset = Person.objects.all()
   template_name = "table_example.html"
```

**person_view.html**

```
{% include 'material/includes/material_css.html' %}
{% include 'material/includes/material_js.html' %}
<!DOCTYPE html>
<html>
   <head>
      <title>TUT</title>
   </head>
   <body>
      # these two will render the table
      {% load django_tables2 %}
      {% render_table table %}
   </body>
</html>
```



# CRUD Framework

# Data Audit

https://django-auditlog.readthedocs.io/en/latest/installation.html#adding-auditlog-to-your-django-application

## Install

```
pip install django-auditlog
python manage.py migrate
```

## Usage

**models.py**

```
from django.db import models
from auditlog.models import AuditlogHistoryField

class Person(models.Model):
    history = AuditlogHistoryField()
    name = models.CharField(blank=True, max_length=100)

auditlog.register(Person)
```

**settings.py**

```
INSTALLED_APPS += [
    'auditlog',
]

MIDDLEWARE += [
    'auditlog.middleware.AuditlogMiddleware',
]
```

## Contexts

```
from auditlog.context import set_actor
actor = get_user(actor_id)
with set_actor(actor):
    pass

from auditlog.context import disable_auditlog
with disable_auditlog():
    # Do things silently here
    pass
```

## Test

```
from auditlog.models import LogEntry
p=Person.objects.first()
p.name = 'Mike'
p.save()
p.history.all()
a = p.history.all().first()
a
a.changes
a.timestamp
a.changes_dict
a.changes_str
```

# Authentication (SSO)

# Authorization

# File Import / Export

See REST section

# REST

https://www.django-rest-framework.org/#installation

**Install**

```
pip install djangorestframework
pip install markdown
pip install django-filter
```

**settings.py**

```
INSTALLED_APPS += [
    'rest_framework',
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
```

**urls.py**

```
urlpatterns += [
    ...
    path('api-auth/', include('rest_framework.urls'))
]
```

**serializers.py**

```
from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
```

**views.py**

```
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
```

**urls.py**

```
from django.urls import include, path
from rest_framework import routers

from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```

## Continued Reading

https://www.django-rest-framework.org/api-guide/pagination/

https://www.django-rest-framework.org/api-guide/filtering/

https://www.django-rest-framework.org/api-guide/permissions/

https://www.django-rest-framework.org/api-guide/parsers/

* JSONParser
* FormParser
* MultiPartParser (for file upload)

https://www.django-rest-framework.org/api-guide/renderers/#renderers

* Look into download capability

https://www.django-rest-framework.org/api-guide/validators/
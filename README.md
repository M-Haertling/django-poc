Install

```
pip install Django
python -m django --version
django-admin startproject mysite .

python manage.py runserver
```

Create polls directory

```
python manage.py startapp polls
```

# Install missing tables

```
python manage.py migrate
```

# Prepare migrations for new model

```
python manage.py makemigrations polls
```

A migration script will be added to mysite/polls/migrations/0001_initial.py

# Migrate the DB

```
echo View migartion script
python manage.py sqlmigrate polls 0001

echo Execute the migration
python manage.py migrate
```

# Interactive python shell

```
python manage.py shell
```

```
from polls.models import Choice, Question, Person
from django.utils import timezone

Question.objects.all()

q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
q.id
q.question_text

Question.objects.filter(question_text__startswith="What")


current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)

Question.objects.get(id=2)
q = Question.objects.get(pk=1)
q.was_published_recently()

q.choice_set.create(choice_text="Not much", votes=0)
q.choice_set.create(choice_text="The sky", votes=0)
c = q.choice_set.create(choice_text="Just hacking again", votes=0)
q.choice_set.all()
c.question

# __ can be used to access a layer down
Choice.objects.filter(question__pub_date__year=current_year)

c = q.choice_set.filter(choice_text__startswith="Just hacking")
c.delete()
```

# Admin

```
python manage.py createsuperuser
```

http://127.0.0.1:8000/admin/

# Run Tests

```
python manage.py test polls
```

# Django Debug Toolbar

https://docs.djangoproject.com/en/5.1/intro/tutorial08/


```
python -m pip install django-debug-toolbar
```

# MUI

```
pip install django-material

```

# CRUD Builder

https://django-crudbuilder.readthedocs.io/en/latest/installation.html

```
pip install django-crudbuilder
```

# Audit

https://django-auditlog.readthedocs.io/en/latest/installation.html#adding-auditlog-to-your-django-application

```
pip install django-auditlog
python manage.py migrate
```

```
from auditlog.context import set_actor
actor = get_user(actor_id)
with set_actor(actor):
    pass

from auditlog.context import disable_auditlog
with disable_auditlog():
    # Do things silently here
    ...
```

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

# Django Tables

```
pip install django-tables2
pip install django-filter
pip install django-bootstrap-v5
```
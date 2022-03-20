### Reference
-  [django / django](https://github.com/django/django/blob/main/django/db/models/base.py)
- LMS video 6

### Bookmark
Line 476
#### latest commit to file base.py in django repository above:
1ea7e3157d1f9b4db71e768d75ea57e47dbd49f9

- [Link to commit](https://github.com/django/django/commit/1ea7e3157d1f9b4db71e768d75ea57e47dbd49f9)

### Relevance

Shows `Model` method defined in the base Django model class
- (in django.db.models.base)

```
class Model(metaclass=ModelBase):
```

#### Part 2:

##### Bookmark
Lines 607-608

##### Content

```
    def __str__(self):
        return "%s object (%s)" % (self.__class__.__name__, self.pk)

```

##### Relevance

Adapted quotation from LMS video 6
"""
- The Post object value in the admin
is coming from the fact that we 
inherited the base Django 
model class, 
when we created our Post model.

- By default,
all models that inherit this base model class
will use its built in string method
to display their class name 
followed by the word object.

- Just so that there's sort of a generic way
to display them.

- see this method defined above 
"""

...

string method above returns object and then the 
primary key,
so that's what we see in the admin panel
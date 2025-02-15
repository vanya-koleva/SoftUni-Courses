# Django Models Basics

## Django Models

-   Every model is a **single separate table** (in most cases).

-   Each attribute of the model represents a **database field** - a column in that table.

-   Models allow us to avoid writing low-level SQL.

-   Create models in **models.py**:

```python
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

-   The resulting table will be named appname_classname. In the example: appname_person

-   An id field is added automatically if we don't specify primary key.

## Fields

-   Field names should not conflict with **reserved words**.

-   Field names cannot have more than one underscore in a row and cannot end with an underscore.

### Field Types

-   **CharField** - Required max_length argument.
-   **TextField** - For large texts. Max Length is not enforced even if specified.
-   **IntegerField**
-   **PositiveIntegerField** - positive int or 0
-   **FloatField** - floating-point numbers; not precise
-   **DecimalField** - fixed-precision numbers;precise; required arguments: max_digits and decimal_place
-   **DateField**
-   **TimeField**
-   **DateTimeField**
-   For Date/Time/DateTime Fields there are optional arguments:
    -   **auto_now** - Automatically set the field to now every time the object is saved.
    -   **auto_now_add** - Automatically set the field to now when the object is first created. Even if you set a value for this field when creating the object, it will be ignored.
    -   auto_now or auto_now_add to True will cause the field to have **editable=False** and **blank=True** set.
    -   will always use the date in the default timezone at the moment of creation or update.
-   **BooleanField**
-   **URLField** - CharField with a built-in URL validator. max_length is **200** by default.
-   **EmailField** - CharField with a built-in email validator. max_length is **254** by default.
-   If primary key is not specified, Django adds a BigAutoField, which is a big integer: `DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'`

## Field Options

-   **default**

    -   🚀 Works only at the **Django level**.

    -   Can be a value or a callable object.

    -   Can’t be a mutable object (model instance, list, set, etc.).

    -   Inserting the data directly in the database (e.g., via SQL) without specifying the column will result in NULL or an error (if null=False).

    -   Best practice: **class attribute**.

    -   If you need a database-level default, use `db_default`

-   **unique**

    -   🚀 ⛁ Works on **both levels**.
    -   Raises IntegrityError.

-   **null**

    -   ⛁ **Database level**.

    -   False by default.

        -   null=False --> NOT NULL
        -   null=True --> can have NULL values.

    -   Use for non-string fields. For strings, it would create two possibilities: NULL, and the empty string.

-   **blank**

    -   🚀 **Django level**

    -   If True, the field is allowed to be blank. Default is False, which makes it a required field.

    -   If а BooleanField is set to allow empty values, it changes from a checkbox to a select box.

-   **primary_key**

    -   read-only field.

    -   If you change the PK of an existing object and save it, a new object will be created alongside the old one.

-   **choices**

    -   🚀 **Django level**

    -   A mapping or iterable to use as choices for this field.

    -   Appears as a select box.

    -   The **first** element is the value to be saved in the **database**, and the **second** element is the **human readable** name.

    -   Best practice: **inner class** or a class in another file.

```python
# In choices.py
from django.db import models

class GenreChoices(models.TextChoices):
    FICTION = "Fi", "Fiction"
    #...


# In models.py
from django.db import models

from main_app.choices import GenreChoices


class Book(models.Model):
    genre = models.CharField(
        max_length=20,
        choices=GenreChoices
    )
```

-   Inner class example:

```python
class Citizen(models.Model):
    class Cities(models.TextChoices):
        SF = "SF", "Sofia"
        # ...

    city = models.CharField(
        max_length=50,
        choices=Cities.choices
    )
```

    - If we need integer choices - IntegerChoices/IntegerField

-   **verbose_name**

    -   A human-readable name for the field.

    -   If the verbose name isn’t given, Django will automatically create it using the field’s attribute name, converting underscores to spaces.

    -   Can also be given as a first positional argument.

```python
first_name = models.CharField(
    "First Name",
    max_length=30
)
```

-   **editable**

    -   Default is True.

    -   If False, the field **disappears** from all forms and is **not able to be filled/ edited**.

    -   Used to hide some fields such as encrypted code, verifications, etc.


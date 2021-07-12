# Lab 27: Django Models

## steps

1. In `models.py` in apps folder 
create your class and inherit it from (models.Model) 
example : 
```
class Snack (models.Model): 
    name = models.CharField(max_length=64)
    description =  models.TextField(max_length=200)

    def __str__ (self):
        return self.name
```
***********************************************
2. in terminal `python manage.py makemigration` then 
`python manage.py migrate `


3. Create super_user 

`python manage.py createsuperuser`
follow the steps .. 
*****************************************
4. register your model in admin app
*******************************
```
from .models import moduleName(class)

admin.site.register(moduleName) 
```
*******************************

5. from browser go to /admin  and add some data .
*******************************
6. go to views.py in app .

import 

` from django.views.generic import TemplateView , ListView , DetailView`

`from .models import ModuleName`

add your class in views with renderd html page ,
you can use list views or detailView depnds on your page.
for example : 
```
    class snackView (ListView): 
        template_name="snack_list.html"  
        model = Snack

```
****************************************
7.  go to urls.py and add your  paths 

import 
```
from django.urls import path
from .views import  <your classes in  views>
```



*******************************************
8. render your data your in html .

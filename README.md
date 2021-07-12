# Lab 27: Django Models
## followed step in lab26

## steps

1. In `models.py` in apps folder 

• create your class and inherit it from (models.Model) 

• add your properties and type of data field.

example : 

```
class ModelName (models.Model): 
    name = models.CharField(max_length=64) 
                
    
    description =  models.TextField(max_length=200)

    def __str__ (self):
        return self.name
```
***********************************************
2. in terminal

`python manage.py makemigrations`
   then 

`python manage.py migrate ` to apply the migration

> this for scan `module.py` run as field in databases

*******************************
3. Create super_user 

`python manage.py createsuperuser`
follow the steps .. 

then go the /admin and add users with user name and pass etc
*****************************************
4. register your model in admin app
*******************************
```
from .models import moduleName(class)

admin.site.register(moduleName) 
```
*******************************

5. from browser go to /admin  and add some data .
will open to you the moduleName .. you can fill the input field.
*******************************
6. go to views.py in app .

import 

` from django.views.generic import TemplateView , ListView , DetailView`

`from .models import ModuleName`

add your class in views with renderd html page ,
you can use list views or detailView depends on your page.
for example : 

ListView : for showing a list

DetailView : for showing  Details
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
from .views import  <your *classes* in  views>
```
add your urls 
```
urlpatterns=[
    path = ('' , classNameIn_Views.as_view(), name= "name")
]
```
if you wanna show details of renderd data use 
for example : 
`path ('book/<int:pk>') `



*******************************************
8. create your html pages that you wanna show the list inside it  .
loop inside object_list
```
{% for i in object_list %}
{{i.name }}
{% endfor %}

in detail page :  
href= "{% url 'detialPage' i.pk %}"{{i.name}}



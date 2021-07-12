from django.urls import path
from .views import  snackView , snack_Detail_View


urlpatterns = [
    # path('', HomeView.as_view(), name='home'), 
    path('', snackView.as_view(), name='view'), 
    path('<int:pk>/', snack_Detail_View.as_view(), name='detailView'), 

]



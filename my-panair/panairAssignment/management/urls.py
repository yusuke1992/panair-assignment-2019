
from django.urls import path
from . import views

app_name = 'management'
urlpatterns = [
    path('home', views.home, name='home'),

    path('users',          views.users_index,   name='user_index'),
    path('users/new',      views.user_edit,      name='user_new'),
    path('users/mod/<int:user_id>/', views.user_edit,  name='user_mod'),
    

    path('records',          views.record_index, name='record_index'),
    path('record/new',      views.record_edit,   name='record_add'),
    path('record/<int:record_id>', views.record_edit,  name='record_mod'),

    path('invoices', views.invoice_index, name='invoice_index'),

    path('reports', views.report_index, name='report_index')
]

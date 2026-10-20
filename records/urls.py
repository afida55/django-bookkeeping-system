from django.urls import path
from .views import *

urlpatterns = [

    path(
        '',
        record_list,
        name='record_list'
    ),

    path(
        'add/',
        add_record,
        name='add_record'
    ),

    path(
        'edit/<int:pk>/',
        edit_record,
        name='edit_record'
    ),

    path(
        'delete/<int:pk>/',
        delete_record,
        name='delete_record'
    ),

    path(
        'ajax/load-categories/',
        load_categories,
        name='ajax_load_categories'
    ),

    path(
        'ajax/load-subcategories/',
        load_subcategories,
        name='ajax_load_subcategories'
    ),

]
from django.urls import path

from .views import *

urlpatterns = [

    path(
        '',
        category_list,
        name='category_list'
    ),

    path(
        'add-main/',
        add_main_category,
        name='add_main_category'
    ),

    path(
        'edit-main/<int:pk>/',
        edit_main_category,
        name='edit_main_category'
    ),

    path(
        'delete-main/<int:pk>/',
        delete_main_category,
        name='delete_main_category'
    ),

    path(
        'add-sub/',
        add_sub_category,
        name='add_sub_category'
    ),

    path(
        'filter-categories/',
        filter_categories,
        name='filter_categories'
    ),

    path(
       'delete-sub/<int:pk>/',
        delete_sub_category,
        name='delete_sub_category'
    ),
]
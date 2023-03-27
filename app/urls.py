from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('lab/', views.lab, name='lab'),
    path('query/', views.query, name='query'),
    path('batch/', views.batch, name='batch'),
    path('benchSheet/', views.bench_sheet, name='benchSheet'),
    path('workOrder/', views.work_order, name='workOrder'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    
    
    path('new_project/', views.new_project, name='new_project'),
    path('all_projects/', views.all_projects, name='all_projects'),
    path('project/<int:pk>', views.project, name='project'),
    path('update_project/<int:pk>', views.update_project, name='update_project'),
    path('delete_project/<int:pk>', views.delete_project, name='delete_project'),
    
    path('new_sample/', views.new_sample, name='new_sample'),
    path('new_sample/<int:add>', views.new_sample, name='new_sample'),
    path('new_samples/', views.new_samples, name='new_samples'),
    path('sample/', views.sample, name='sample'),
    path('sample/<int:pk>', views.sample, name='sample'),
    path('samples/', views.samples, name='samples'),
    path('samples/<str:pn>', views.samples, name='samples'),
    #path('add_sample/', views.add_sample, name='add_sample'),
    #path('updat_samples/', views.new_samples, name='new_samples'),
    
    path('approvals/', views.approvals, name='approvals'),
    path('store/', views.store, name='store'),
    
    path('new_test/', views.new_project, name='new_test'),
    
    path('add/', views.person_create_view, name='person_add'),
    path('list/<int:pk>/', views.person_update_view, name='person_change'),
    
    
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
]

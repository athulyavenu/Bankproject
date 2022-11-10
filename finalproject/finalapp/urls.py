from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.PersonListView.as_view(), name='person_changelist'),
    path('add/', views.PersonCreateView.as_view(), name='person_add'),
    path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),
    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('logout/', views.logout),
    path('application_accepted/', views.application_accepted, name='application_accepted')

]
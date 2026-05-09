from django.urls import include, path
from .views import members,my_view,register


urlpatterns = [
    path('member', members),
    path('my_view',my_view),
    path('reg/',register, name='registration')
]
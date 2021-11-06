from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from BC_scan import views

user_list = views.UserView.as_view({
    'get': 'list',
})

urlpatterns = format_suffix_patterns([
    path('users/', user_list, name='users'),  # for dev
    path('users/<email>', views.UserDetailView.as_view(), name='user-detail'), 
    path('users/<email>/cards/', views.UserBusinessCardListView.as_view(), name='cards'), 
    path('cards/<uuid:id>/', views.BusinessCardDetailView.as_view(), name='card-detail'),
    # path('social/callback', views.SocialView.as_view(), name='social-auth'), 
])
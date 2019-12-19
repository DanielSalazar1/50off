from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from api import views


urlpatterns = [
    #---------------------------#
    # UNPROTECTED API ENDPOINTS #
    # --------------------------#

    # HOMEPAGE
    path('', views.UserLocationAPI.as_view(), name='UserLocationAPI' ),


    # Item
    path('api/categories', views.CategoryListAPI.as_view(), name='CategoryListAPI'),
    path('api/items', views.ItemListAPI.as_view(), name='itemListAPI'),
    path('api/images', views.ImagesListAPI.as_view(), name='ImagesListAPI'),


    # GATEWAY
    # path('register', views.register_page, name='register_page'),
    # path('register/success', views.register_success_page, name='register_success_page'),
    # path('login', views.login_page, name='login_page'),
    path('api/register', views.RegisterAPI.as_view(), name='register_api'),
    path('api/login', obtain_auth_token, name='api_token_auth'),
    # path('logout', views.logout_page, name='logout_page'),
    # path('api/logout', views.post_logout_api, name='logout_api'),

    #-------------------------#
    # PROTECTED API ENDPOINTS #
    #-------------------------#

    # DASHBOARD
    # path('dashboard', views.dashboard_page, name='dashboard_page'),
    path('api/dashboard', views.DashboardAPI.as_view(), name='dashboard_api'),
    path('api/favourites', views.FavouritesAPI.as_view(), name='add_favourites'),

]

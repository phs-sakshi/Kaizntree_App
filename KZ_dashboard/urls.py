from django.urls import path
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Kaizntree Dashboard APIs",
        default_version='v1',
        description="APIs used to create the Kaizntree dashboard",
        terms_of_service="https://www.xyz.com/terms/",
        contact=openapi.Contact(email="phs.sakshi@gmail.com"),
        license=openapi.License(name="xyz License"),
    ),
    public=True,
)

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='kz_dashboard_list'),
    path('home/', views.DashboardView.as_view(), name='kz_dashboard_list'),
    path('signin/', views.signin, name='signin'),
    path('', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('dashboard-api/', views.dashboard_api, name='dashboard_api'),
    path('accounts/logout/', views.signout, name='logout'),
    path('accounts/login/', views.signin, name='login'),
]

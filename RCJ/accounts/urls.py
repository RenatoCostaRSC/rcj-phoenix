from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from RCJ.accounts import views as accounts_views

app_name = 'accounts'
urlpatterns = [
    #path('login/', LoginView.as_view(template_name='accounts/login.html'), name = 'login'),
    path('login/', accounts_views.user_login, name='login'),
    path('logout/', accounts_views.user_logout, name = 'logout'),
    path('usuarios-cadastrados/', accounts_views.list_user, name = 'usuarios-cadastrados'),
    path('cadastrar-usuario/', accounts_views.register_user, name = 'cadastro-usuario'),
    path('editar-usuario/<slug:slug>', accounts_views.edit_user, name = 'editar-usuario'),
    path('deletar-usuario/<slug:slug>', accounts_views.delete_user, name = 'deletar-usuario'),
    #path('admin/', admin.site.urls),
]

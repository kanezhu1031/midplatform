from django.conf.urls import url
from sysconf import views



urlpatterns = [
    url(r'^router/', views.router),
    url(r'^changemailserver/', views.changemailserver),
    url(r'^ossconf/', views.ossconf),
    url(r'^mailserver/', views.mailserver),
    url(r'^getrouter/', views.getrouter),
    url(r'^sysuser/', views.sysuser),
    url(r'^logout/', views.logout),
    url(r'^setPassword/', views.setPassword),
    url(r'^sysRole/', views.sysRole),
    url(r'^sysRoleSelect/', views.sysRoleSelect),
    url(r'^sysRoleMenuSelect/', views.sysRoleMenuSelect),
    url(r'^setPassword/', views.setPassword),
    url(r'^sysusergrant/', views.sysusergrant),
    url(r'^sysuserlogin/', views.sysuserlogin),
    url(r'^codeMsg/', views.codeMsg),
    url(r'^baseConfig/', views.baseConfig),
    url(r'^deployuser/', views.deployuser),
]


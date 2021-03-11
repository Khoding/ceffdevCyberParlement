"""ceffdevCyberP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cyberP.views import IndexView, CyberparlementUpdateView, CyberparlementListView, MemberListView, MemberDeleteView

app_name = 'cyberP'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cyberparlements/', CyberparlementListView.as_view(), name='cyberparlement-list'),
    path('cyberparlements/<int:pk>/update/', CyberparlementUpdateView.as_view(), name='cyberparlement-update'),
    path('cyberparlements/<int:pk>/members/', MemberListView.as_view(), name='cyberparlement-member-list'),
    path('members/<int:pk>/delete/', MemberDeleteView.as_view(), name='cyberparlement-member-confirm-delete'),
]

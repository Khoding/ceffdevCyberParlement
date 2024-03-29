"""cyberparlementProject URL Configuration

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
from django.contrib.auth.decorators import login_required
from django.urls import path, include

from cyberparlementProject.views import IndexView, InitiativeListView, InitiativePropositionView, UserCreateView, CyberparlementListView, UserLoginView, InitiativeValidationView, InitiativeStartPollView, InitiativePollVoteView, InitiativeValidatePollVoteView, InitiativePollDetailView, InitiativeCreateSecondRoundView, CyberparlementUpdateView, CyberparlementCreateView, MemberListView, MemberDeleteView, CyberparlementMoveView, MemberUpdateView, MemberAffiliationView, MemberResetPasswordView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view(), name='index'),

    path('initiatives/<int:id_cyberparlement>', login_required(InitiativeListView.as_view()), name='initiative-list'),
    path('initiative/propose/', login_required(InitiativePropositionView.as_view()), name='initiative-propose'),
    path('initiative/validate/<int:id_initiative>', login_required(InitiativeValidationView.as_view()), name='initiative-validate'),
    path('initiative/start-poll/<int:id_initiative>', login_required(InitiativeStartPollView.as_view()), name='initiative-start-poll'),
    path('initiative/vote-poll/<int:pk>', login_required(InitiativePollVoteView.as_view()), name='initiative-vote-poll'),
    path('initiative/poll-detail/<int:pk>', login_required(InitiativePollDetailView.as_view()), name='initiative-poll-detail'),
    path('initiative/poll-new-round/<int:id_initiative>', login_required(InitiativeCreateSecondRoundView.as_view()), name='initiative-create-new-round'),
    path('initiative/validate-poll-vote/<int:pk>', login_required(InitiativeValidatePollVoteView.as_view()), name='initiative-validate-poll-vote'),
    path('cyberparlements/', CyberparlementListView.as_view(), name='cyberparlement-list'),
    path('cyberparlements/<slug:slug>/update', CyberparlementUpdateView.as_view(), name='cyberparlement-update'),
    path('cyberparlements/<slug:slug>/add', CyberparlementCreateView.as_view(), name='cyberparlement-create'),
    path('cyberparlements/<slug:slug>/move', CyberparlementMoveView.as_view(), name='cyberparlement-move'),
    path('cyberparlements/<slug:slug>/members', MemberListView.as_view(), name='member-list'),
    path('cyberparlements/<slug:slug>/members/<int:pk>/update', MemberUpdateView.as_view(), name='member-update'),
    path('cyberparlements/<slug:slug>/members/<int:pk>/affiliation', MemberAffiliationView.as_view(), name='member-affiliation'),
    path('cyberparlements/<slug:slug>/members/<int:pk>/confirm_delete', MemberDeleteView.as_view(), name='member-delete'),
    path('cyberparlements/<slug:slug>/members/<int:pk>/confirm_reset_password', MemberResetPasswordView.as_view(), name='member-reset-password'),

    # Vues relatives à l'authentification -- à des fins de test
    path('user/create/', UserCreateView.as_view(), name='user-create'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]

from django.urls import path, include
from user import views
from .views import comments_view
from .views import UserListView, UserCreateView
from django.conf.urls.i18n import i18n_patterns
from .views import (
   UserListView,UserCreateView,
    ProblemListView, ProblemCreateView, ProblemDetailView,
    OfferCreateView,
    CommentCreateView,
)


app_name = 'user'
urlpatterns = [

    path('sending-email/', views.SendEmailView.as_view(), name='send_email'),
    path('success/', views.success, name='success'),
    path('login/', views.LoginPageView.as_view(), name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('activation-link/<uidb64>/<token>/', views.activate, name='activate'),
    path('logout/', views.logout_page, name='logout_page'),
    path('comments/', comments_view, name='comments'),
    path('', UserListView.as_view(), name='user_list'),
    path('add/', UserCreateView.as_view(), name='user_add'),
    path('problems/', ProblemListView.as_view(), name='problem_list'),
    path('problems/add/', ProblemCreateView.as_view(), name='problem_add'),
    path('problems/<int:pk>/', ProblemDetailView.as_view(), name='problem_detail'),

    path('problems/<int:pk>/offer/', OfferCreateView.as_view(), name='offer_add'),

    path('problems/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_add'),

]

urlpatterns += i18n_patterns(
    path('', include('user.urls')),
)

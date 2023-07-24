from django.urls import path
from .views import IssueCreateView, issue_list, issue_detail, agent_dashboard,home_view,login,register

app_name = 'myapp'

urlpatterns = [
    path('', home_view, name='home'), 
    path('login/', login, name='login'), 
    path('register/', register, name='register'), 
    path('issue/create/', IssueCreateView.as_view(), name='issue_create'),
    path('issue/list/', issue_list, name='issue_list'),
    path('issue/<int:issue_id>/', issue_detail, name='issue_detail'),
    path('agent/dashboard/', agent_dashboard, name='agent_dashboard'),
]

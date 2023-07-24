from django.shortcuts import render, redirect
from django.views import View
from .models import Issue, Agent, Mechanic
from .forms import IssueForm

class IssueCreateView(View):
    def get(self, request):
        form = IssueForm()
        return render(request, 'myapp/issue_create.html', {'form': form})

    def post(self, request):
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save()
            agents = Agent.objects.order_by('queue')
            agent = agents.first()
            agent.queue += 1
            agent.save()
            return redirect('myapp:issue_detail', issue.issueID)
        return render(request, 'myapp/issue_create.html', {'form': form})

def issue_list(request):
    issues = Issue.objects.all()
    return render(request, 'myapp/issue_list.html', {'issues': issues})

def issue_detail(request, issue_id):
    issue = Issue.objects.get(issueID=issue_id)
    return render(request, 'myapp/issue_detail.html', {'issue': issue})

def agent_dashboard(request):
    agents = Agent.objects.order_by('agentID')
    return render(request, 'myapp/agent_dashboard.html', {'agents': agents})

def home_view(request):
    return render(request, 'myapp/home.html')
def login(request):
    return render(request, 'myapp/login.html')
def register(request):
    return render(request, 'myapp/register.html')

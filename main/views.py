# from django
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# from packages

# from local
from .models import News, Project, Oportunity
from .utils import get_nested_list_includes_triple_lists

from students_and_tuiters.models import MediaMembers
# Create your views here.
@login_required(login_url='login')
def home_view(request):
    """Bosh sahifa"""
    oportunities = Oportunity.objects.all()
    media_members = MediaMembers.objects.all()
    if oportunities.count() > 4:
        oportunities = oportunities[-4:]
    
    context = {
        'active_section': 'home',
        'oportunities': oportunities,
        'media_members': get_nested_list_includes_triple_lists(media_members),
    }
    return render(request, 'index.html', context)


@login_required(login_url='login')
def oportunities_view(request):
    """Imkoniyatlar oynsi"""
    chances = Oportunity.objects.all()
    context = {
        'active_section': 'oportunities',
        'list_chances': get_nested_list_includes_triple_lists(chances),
    }
    return render(request, 'oportunities1.html', context)


@login_required(login_url='login')
def projects_view(request):
    """Loyihalar oynasi"""
    projects = Project.objects.all()    
    context = {
        'active_section': 'projects',
        'projects': get_nested_list_includes_triple_lists(projects),
    }
    return render(request, 'projects.html', context)


@login_required(login_url='login')
def project_detail(request, pk:int):
    user = request.user
    project = get_object_or_404(Project, id=pk)
    if user not in project.viewers.all():
        project.viewers.add(user)
    context = {
        'project': project,
    }
    return render(request, 'project_detail.html', context)


@login_required(login_url='login')
def oportunity_detail(request, pk):
    """Imkoniyatlar haqida batafsil ko'rish
    pk = oportunity_id 
    """
    oportunity = get_object_or_404(Oportunity, id=pk)
    context = {
        'active_section': 'oportunity_detail',
        'oportunity': oportunity,
        }
    return render(request, 'oportunity_detail.html', context)


@login_required(login_url='login')
def news_view(request):
    """Yangiliklar oynasi"""
    news = News.objects.all().order_by('-created_at')
    context = {
        'active_section': 'news',
        'news': news,
    }
    return render(request, 'news.html', context)


@login_required(login_url='login')
def detail_news(request, pk:int):
    user = request.user
    news = get_object_or_404(News, id=pk)
    if user not in news.viewers.all():
        news.viewers.add(user)
    context = {
        'news': news,
    }
    return render(request, 'news_detail.html', context)


@login_required(login_url='login')
def contact_view(request):
    context = {
        'active_section': 'contact'
    }
    return render(request, 'contact.html', context)
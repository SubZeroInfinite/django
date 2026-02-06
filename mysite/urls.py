from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    """NIIMS Homepage"""
    return render(request, 'home.html')

def api_root(request):
    """API Documentation"""
    return JsonResponse({
        'app': 'NICAZ NIIMS',
        'version': '1.0.0',
        'status': 'running',
        'database': 'PostgreSQL',
        'hosting': 'Railway',
        'endpoints': {
            'admin': '/admin/',
            'api_docs': '/api/',
            'health': '/health/'
        }
    })

def health_check(request):
    """Health check endpoint"""
    return JsonResponse({'status': 'healthy', 'service': 'NIIMS API'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root),
    path('health/', health_check),
    path('', home, name='home'),
]

# Customize admin
admin.site.site_header = "NICAZ NIIMS Administration"
admin.site.site_title = "NIIMS Admin Portal"
admin.site.index_title = "Welcome to NIIMS Administration"

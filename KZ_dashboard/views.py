from django.utils.decorators import method_decorator
from django.views.generic import ListView
from .models import KZ_dashboard
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ItemsSerializer


@method_decorator(login_required(login_url='/signin'), name='dispatch')
class DashboardView(ListView):
    model=KZ_dashboard
    context_object_name='items'

    def get_queryset(self):
        queryset = super().get_queryset()
        stock_status = self.request.GET.get('stock_status')
        filter_type = self.request.GET.get('filter_type')  # 'above', 'below', or 'equal'

        if stock_status is not None and filter_type is not None:
            try:
                stock_status = int(stock_status)
                if filter_type == 'above':
                    queryset = queryset.filter(stock_status__gt=stock_status)
                elif filter_type == 'below':
                    queryset = queryset.filter(stock_status__lt=stock_status)
                elif filter_type == 'equal':
                    queryset = queryset.filter(stock_status=stock_status)
                else:
                    pass
            except ValueError:
                pass

        return queryset

@api_view(['GET'])
@swagger_auto_schema(manual_parameters=[
    openapi.Parameter('stock_status', openapi.IN_QUERY, description="Stock status", type=openapi.TYPE_INTEGER),
    openapi.Parameter('filter_type', openapi.IN_QUERY, description="Filter type: 'above', 'below', or 'equal'", type=openapi.TYPE_STRING),
])

@login_required()
def dashboard_api(request):
    queryset = KZ_dashboard.objects.all()
    serializer = ItemsSerializer(queryset, many=True)
    return Response(serializer.data)


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def signout(request):
    logout(request)
    return redirect('signin')

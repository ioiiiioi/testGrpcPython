"""service_versioning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from Version 
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from Version.proto import Versioning_pb2_grpc
from Version.services import VersionsService


urlpatterns = []


def grpc_handlers(server):
    # Version_pb2_grpc.add_VersionsControllerServicer_to_server(VersionsService.as_servicer(), server)
    Versioning_pb2_grpc.add_VersioningServiceServicer_to_server(VersionsService.as_servicer(), server)

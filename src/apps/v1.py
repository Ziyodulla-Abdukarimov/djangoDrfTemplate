from django.urls import path, include

accounts = [
    path('account',include(('src.apps.account.urls','src.apps.account',),namespace='accounts')),

]

urlpatterns = accounts

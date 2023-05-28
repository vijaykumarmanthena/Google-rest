from django.urls import path,include
from rest_framework_social_oauth2.views import TokenView
from cal.views import GoogleCalendarInitView, GoogleCalendarRedirectView,GoogleLoginCallbackView




urlpatterns = [
    # Other URL patterns
    
    #path('auth/', include('rest_framework_social_oauth2.urls')),
    #path('auth/token/', TokenView.as_view(), name='token'),
    path('rest/v1/calendar/init/', GoogleCalendarInitView.as_view(), name='google_calendar_init'),
    path('rest/v1/calendar/redirect/', GoogleCalendarRedirectView.as_view(), name='google_calendar_redirect'),
    #path('auth/login/google/callback/', GoogleLoginCallbackView.as_view(), name='google_login_callback'),

]

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
# Create your views here.


from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import redirect
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build


from rest_framework.permissions import AllowAny


class GoogleCalendarInitView(APIView):
    def get(self,request):
        flow = Flow.from_client_secrets_file(
            'client222.json',
            scopes=['openid', 'https://www.googleapis.com/auth/calendar.events'],
            redirect_uri='http://localhost:8000/rest/v1/calendar/redirect/'
        )
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true'
        )
        request.session['state'] = state
        return redirect(authorization_url)


from rest_framework.permissions import AllowAny

class GoogleCalendarRedirectView(APIView):
    permission_classes = [AllowAny]  # Allow any user to access this view

    def get(self, request):
        # Get the authorization code from the request query parameters
        code = request.query_params.get('code')

        if code:
            # Set up the OAuth 2.0 flow
            flow = Flow.from_client_secrets_file(
            'client222.json',
            scopes=['openid', 'https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/calendar.events'],
        redirect_uri='http://localhost:8000/rest/v1/calendar/redirect/'
        )

            # Exchange the authorization code for an access token
            flow.fetch_token(code=code)

            # Get the access token
            credentials = flow.credentials
            access_token = credentials.token

            # Create a service object for the Google Calendar API
            service = build('calendar', 'v3', credentials=credentials)

            # Retrieve the list of events in the user's calendar
            events_result = service.events().list(calendarId='primary', maxResults=10).execute()
            events = events_result.get('items', [])

            # Return the access token and list of events
            return Response({
                'access_token': access_token,
                'events': events
            })

        # Handle the case when the authorization code is not present
        return Response({'error': 'Authorization code is missing'})




class GoogleLoginCallbackView(APIView):
    def get(self, request):
        # Get the authorization code from the request
        code = request.GET.get('code')

        if code:
            # Process the authorization code and exchange it for an access token
            # (Code for exchanging authorization code for access token)

            # Once you have the access token, you can perform further actions
            # such as retrieving user information or saving the access token

            # Redirect to a success page or perform any other necessary actions
            return redirect('success')
        else:
            # Handle the case when the authorization code is not present
            # Redirect to an error page or perform any other necessary actions
            return redirect('error')
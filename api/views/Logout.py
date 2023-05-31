""" API to create/get Register records
"""
# from django.http import JsonResponse, QueryDict
from rest_framework import views
# from django.db.models import Max
# from backend import models
# from ..serializers import LoginSerializer

from django.db import connection
from django.http import JsonResponse

from datetime import datetime

# from rest_framework import authentication, permissions

class LogoutView(views.APIView):
    """ API view to add login Data """
    
    def post(self, request):
        """ POST method handler to add LogoutView
        """
        
        headervalue = request.META.get('HTTP_VALIDATE')
        
        if headervalue == "":
            return JsonResponse({'Message': 'Authenticate Empty','Status':401, 'Success': 'False'}, status=401)
        
        
        if headervalue == "y2s4pyj52nzr49jnuxxgqk5jtj28cj":
            
            # ID = request.data.get('id')
            UserID = request.data.get('user_id')
            UserName = request.data.get('user_name')
            # LiDatetime = request.data.get('li_datetime')
            # LoDatetime = request.data.get('lo_datetime')
            Role = request.data.get('role')
            # Onetimepass = request.data.get('onetimepass')
            # Freetext = request.data.get('freetext')
            Freetext = "logout"
            
            current_datetime = datetime.now()
            Datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

            
            with connection.cursor() as cursor:
                # Execute an SQL query to fetch the user with matching credentials
                query = f"INSERT INTO admin_users_logs (USERID,USERNAME,DATETIME,ROLE,FREETEXT) VALUES ({UserID},'{UserName}','{Datetime}','{Role}','{Freetext}')"
                print(query)
                cursor.execute(query)

                # Return a success message
                data = {
                            'Message': 'logout successfully',
                            'Status':200,
                            'Success': 'True',
                        }
            
            return JsonResponse(data)
            
        else:
            return JsonResponse({'Message': 'Authenticate Failed', 'Status':401, 'Success': 'False'}, status=401)
        
        
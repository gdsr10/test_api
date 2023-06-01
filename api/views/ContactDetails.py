""" API to Post Sidebar List records """

from rest_framework import views
from django.db import connection
from django.http import JsonResponse

import string
import random
import requests

class ContactDetailsView(views.APIView):
    """ API view to Sidebar List records Data """
    
    def post(self, request):
        """ POST method handler to ContactDetailsView
        """
        
        headervalue = request.META.get('HTTP_VALIDATE')
        
        if headervalue == "":
            return JsonResponse({'Message': 'Authenticate Empty','Status':401, 'Success': 'False'}, status=401)
        
        if headervalue == "y2s4pyj52nzr49jnuxxgqk5jtj28cj":
            
            UserPId = request.data.get('user_id')
            LoctnId = request.data.get('location_id')
        
            with connection.cursor() as cursor:
                # Execute an SQL query to check if the user exists and meets a condition
                query = f"SELECT HMOBILE, WMOBILE, MPHONE FROM sidebar_{LoctnId} WHERE ID = '{UserPId}'"
                # print(query)
                cursor.execute(query)
            
                user = cursor.fetchone()
                
                # print(user)

                if user:
                
                    # Return a success message
                    data = {
                        'Message': 'contact details get successfully',
                        'Status':200,
                        'Success': 'True',
                        'data': [{
                            'HMOBILE': user[0],
                            'WMOBILE': user[1],
                            'MPHONE': user[2]
                        }]
                    }
                    return JsonResponse(data)
                
                else:
                    return JsonResponse({'Message': 'Contact details not found', 'Status':404, 'Success': 'False', 'data':[]}, status=404)
        else:
            return JsonResponse({'Message': 'Authenticate Failed', 'Status':401, 'Success': 'False'}, status=401)
        
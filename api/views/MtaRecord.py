""" API to Post Sidebar List records """

from rest_framework import views
from django.db import connection
from django.http import JsonResponse

import string
import random
import requests

class MtaRecordView(views.APIView):
    """ API view to Sidebar List records Data """
    
    def post(self, request):
        """ PUT method handler to update Employee data
        """
        # headers1 = {key: value for key, value in request.META.items() if key.startswith('HTTP_')}
        
        # Generate a random alphanumeric value
        # random_value = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        # print(random_value)
        
        # Set the random value as a header in the request
        # headers = {'X-Random-Header': random_value}
        # headers = {'X-Validate': random_value}
        # print(headers)
    
        headervalue = request.META.get('HTTP_VALIDATE')
        
        if headervalue == "":
            return JsonResponse({'Message': 'Authenticate Empty','Status':401, 'Success': 'False'}, status=401)
        
        if headervalue == "y2s4pyj52nzr49jnuxxgqk5jtj28cj":
            
            LocationId = request.data.get('location_id')
            PId = request.data.get('p_id')
            MTAData = request.data.get('mta_data')
        
            with connection.cursor() as cursor:
                # Execute an SQL query to check if the user exists and meets a condition
                query = f"SELECT MTAFILEDATA FROM sidebar_{LocationId} WHERE ID = '{PId}'"
            
                cursor.execute(query)
            
                user = cursor.fetchone()

                if user:
                
                    # Execute an SQL query to update the user data
                    cursor.execute(f"UPDATE sidebar_{LocationId} SET MTAFILEDATA = %s WHERE ID = %s", [MTAData, PId])

                    # Return a success message
                    data = {
                        'Message': 'MTA Record updated successfully',
                        'Status':200,
                        'Success': 'True',
                        # 'headers': headers1
                    }
                    return JsonResponse(data)
                
                else:
                    return JsonResponse({'Message': 'MTA Record not found', 'Status':404, 'Success': 'False', 'data':[]}, status=404)
        else:
            return JsonResponse({'Message': 'Authenticate Failed', 'Status':401, 'Success': 'False'}, status=401)
        
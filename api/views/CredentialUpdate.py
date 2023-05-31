""" API to create/get Register records
"""
# from django.http import JsonResponse, QueryDict
from rest_framework import views
# from django.db.models import Max
# from backend import models
# from ..serializers import LoginSerializer


from django.db import connection
from django.http import JsonResponse


class CredentialUpdateView(views.APIView):
    """ API view to add login Data """
    
    def put(self, request):
        """ PUT method handler to update Employee data
        """
        
        headervalue = request.META.get('HTTP_VALIDATE')
        
        if headervalue == "":
            return JsonResponse({'Message': 'Authenticate Empty','Status':401, 'Success': 'False'}, status=401)
        
        
        if headervalue == "y2s4pyj52nzr49jnuxxgqk5jtj28cj":
            
            UserID = request.data.get('id')
            MAILID = request.data.get('mail_id')
            PASSWORD = request.data.get('password')
            
            # print(UserID)
            # print(MAILID)
            # print(PASSWORD)
            
            with connection.cursor() as cursor:
                # Execute an SQL query to check if the user exists and meets a condition
                cursor.execute("SELECT * FROM admin_users WHERE id = %s", [UserID])
                user = cursor.fetchone()

                if user:
                    # Perform the condition check here
                    if user[0]:
                        # Execute an SQL query to update the user data
                        cursor.execute("UPDATE admin_users SET FIELD_MAILID = %s, FIELD_PASSWORD = %s WHERE ID = %s", [MAILID, PASSWORD, UserID])

                        # Return a success message
                        data = {
                            'Message': 'User data updated successfully',
                            'Status':200,
                            'Success': 'True',
                            'data': [
                                {
                                    'MailId': user[2],
                                    'Password': user[4]
                                }
                            ]
                        }
                        return JsonResponse(data)
                    else:
                        return JsonResponse({'Message': 'User is not active'}, status=400)
                else:
                    return JsonResponse({'Message': 'User not found', 'Status':404, 'Success': 'False', 'data':[]}, status=404)
            
        else:
            return JsonResponse({'Message': 'Authenticate Failed', 'Status':401, 'Success': 'False'}, status=401)
        
        
            

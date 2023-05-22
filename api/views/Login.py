""" API to create/get Register records
"""
# from django.http import JsonResponse, QueryDict
from rest_framework import views
# from django.db.models import Max
# from backend import models
# from ..serializers import LoginSerializer

from django.db import connection
from django.http import JsonResponse

class LoginView(views.APIView):
    """ API view to add login Data """
    
    def get(self, _):
        """ GET method handler to add Employee data
        """
        with connection.cursor() as cursor:
            # Execute a SQL query to fetch data from the table
            cursor.execute("SELECT * FROM admin_users")

            # Fetch all rows from the cursor
            rows = cursor.fetchall()
            
            print(rows)

        # Format the data as needed and return as JSON response
        data = {
            'user_details': rows,
        }
        return JsonResponse(data)
    
    
    def post(self, request):
        """ POST method handler to add EntryDetailsView
        """
        MAILID = request.data.get('FIELD_MAILID')
        PASSWORD = request.data.get('FIELD_PASSWORD')
        
        # print(MAILID)
        # print(PASSWORD)
        
        with connection.cursor() as cursor:
            # Execute an SQL query to fetch the user with matching credentials
            cursor.execute("SELECT * FROM admin_users WHERE FIELD_MAILID = %s AND FIELD_PASSWORD = %s", [MAILID, PASSWORD])

            # Fetch the first row from the cursor
            row = cursor.fetchone()

        if row:
            # Successful login
            data = {
                'Message': 'Login successful',
                'Status':200,
                'Success': 'True',
                'data': [{
                    'Id': row[0],
                    'Field_Name': row[1],
                    'Field_Mail_Id': row[2],
                    'Field_User_Name': row[3],
                    'Field_Password': row[4],
                    'Field_Location_Id': row[5],
                    'Field_User_Id': row[6],
                    'Field_Role': row[7],
                }]
                # Include other relevant user data if needed
            }
            return JsonResponse(data)
        else:
            # Invalid credentials
            return JsonResponse({'Message': 'Invalid credentials', 'Status':401, 'Success': 'False', 'data': []}, status=401)
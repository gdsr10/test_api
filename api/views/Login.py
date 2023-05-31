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

class LoginView(views.APIView):
    """ API view to add login Data """
    
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    
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
        
        headervalue = request.META.get('HTTP_VALIDATE')
        
        if headervalue == "":
            return JsonResponse({'Message': 'Authenticate Empty','Status':401, 'Success': 'False'}, status=401)
        
        
        if headervalue == "y2s4pyj52nzr49jnuxxgqk5jtj28cj":
            
            MAILID = request.data.get('mail_id')
            PASSWORD = request.data.get('password')
            
            Freetext = "login"
            
            current_datetime = datetime.now()
            Datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            
            # print(MAILID)
            # print(PASSWORD)
            
            with connection.cursor() as cursor:
                # Execute an SQL query to fetch the user with matching credentials
                cursor.execute("SELECT * FROM admin_users WHERE FIELD_MAILID = %s AND FIELD_PASSWORD = %s", [MAILID, PASSWORD])

                # Fetch the first row from the cursor
                row = cursor.fetchone()

            if row:
                # Successful login
                
                UserID = row[6]
                UserName = row[3]
                Role = row[7]
                
                with connection.cursor() as cursor:
                
                    # Execute an SQL query to fetch the user with matching credentials
                    query = f"INSERT INTO admin_users_logs (USERID,USERNAME,DATETIME,ROLE,FREETEXT) VALUES ({UserID},'{UserName}','{Datetime}','{Role}','{Freetext}')"
                    print(query)
                    cursor.execute(query)
        
                data = {
                    'Message': 'Login successful',
                    'Status':200,
                    'Success': 'True',
                    'data': [{
                        'Id': row[0],
                        'Name': row[1],
                        'MailId': row[2],
                        'UserName': row[3],
                        'Password': row[4],
                        'LocationId': row[5],
                        'UserId': row[6],
                        'Role': row[7],
                    }]
                    # Include other relevant user data if needed
                }
                return JsonResponse(data)
            else:
                # Invalid credentials
                return JsonResponse({'Message': 'Invalid credentials', 'Status':401, 'Success': 'False', 'data': []}, status=401)
            
        else:
            return JsonResponse({'Message': 'Authenticate Failed', 'Status':401, 'Success': 'False'}, status=401)
        
        
""" API to Post Sidebar List records """

from rest_framework import views
from django.db import connection
from django.http import JsonResponse

class FollowUpView(views.APIView):
    """ API view to Sidebar List records Data """
    
    def post(self, request):
        """ POST method handler to add FollowUpView
        """
        LOCATIONID = request.data.get('LOCATIONID')
        FROMDATE = request.data.get('FROMDATE')
        TODATE = request.data.get('TODATE')
        USERID = request.data.get('USERID')
        
        # APTDATE = "2023-05-09"
        # USERID = "39"
        
        # print(MAILID)
        # print(PASSWORD)
        
        with connection.cursor() as cursor:
            # Execute an SQL query to fetch the user with matching credentials
            query = f"SELECT sum( A.BOOKED_APTS ) as ana_booked1, sum( A.FUTURE_APTS) as ana_followup1 FROM analytics_{LOCATIONID} A WHERE A.ANADATE >= %s AND A.ANADATE <= %s AND A.BOOKED_APTS>0 AND A.USERID = %s "
            cursor.execute(query, [FROMDATE, TODATE, USERID])
            
            # print(cursor.execute(query, [APTDATE, USERID]))
            
            # Fetch the first row from the cursor
            rows = cursor.fetchall()
            
        if rows:
            # Successful login
            data = []
            
            for row in rows:
                row_data = {
                    'ANA_BOOKED1': row[0],
                    'ANA_FOLLOWUP1': row[1],
                }
                data.append(row_data)

            # Return the data as a JSON response
            response = {
                'Message': 'FollowUp Data',
                'Status':200,
                'Success': 'True',
                'data': data
            }
            
            return JsonResponse(response)
        else:
            # Invalid credentials
            return JsonResponse({'Message': 'Invalid credentials', 'Status':401, 'Success': 'False', 'data': []}, status=401)
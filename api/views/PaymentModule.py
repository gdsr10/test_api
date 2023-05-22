""" API to Post Sidebar List records """

from rest_framework import views
from django.db import connection
from django.http import JsonResponse

class PaymentModuleView(views.APIView):
    """ API view to Sidebar List records Data """
    
    def post(self, request):
        """ POST method handler to add PaymentModuleView
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
            query = f"SELECT ( SELECT B.LOCATIONNAME FROM locationdetails B WHERE B.LOCATIONID = A.LOCATIONID ) AS ana_location , SUM( A.PAID_PRIVATE ) as PRIVATE , SUM( A.PAID_MEDICARE ) as MEDICARE , SUM( A.PAID_DVA ) as DVA , SUM( A.PAID_OTHERS ) as OTHERS , SUM( A.PAID_GST ) as GST , SUM( A.PAID_TOTAL ) as TOTAL,A.USERID FROM analytics_{LOCATIONID} A WHERE A.ANADATE >= '{FROMDATE}' AND A.ANADATE <= '{TODATE}' AND A.USERID = {USERID}"
            # print(query)
            cursor.execute(query)
            # cursor.execute(query, [FROMDATE, TODATE, USERID])
            
            # print(cursor.execute(query, [FROMDATE, TODATE, USERID]))
            
            # Fetch the first row from the cursor
            rows = cursor.fetchall()
            
            # print(rows)
            
        if rows:
            # Successful login
            data = []
            
            for row in rows:
                row_data = {
                    'ANA_LOCATION': row[2],
                    'PRIVATE': row[1],
                    'MEDICARE': row[2],
                    'DVA': row[3],
                    'OTHERS': row[4],
                    'GST': row[5],
                    'TOTAL': row[6],
                    'USERID': row[7],
                }
                data.append(row_data)

            # Return the data as a JSON response
            response = {
                'Message': 'Payment Module Data',
                'Status':200,
                'Success': 'True',
                'data': data
            }
            
            return JsonResponse(response)
        else:
            # Invalid credentials
            return JsonResponse({'Message': 'Invalid credentials', 'Status':401, 'Success': 'False', 'data': []}, status=401)
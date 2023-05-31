""" API to Post Sidebar List records """

from rest_framework import views
from django.db import connection
from django.http import JsonResponse

class PaymentModuleView(views.APIView):
    """ API view to Sidebar List records Data """
    
    def post(self, request):
        """ POST method handler to add PaymentModuleView
        """
        
        headervalue = request.META.get('HTTP_VALIDATE')
        
        if headervalue == "":
            return JsonResponse({'Message': 'Authenticate Empty','Status':401, 'Success': 'False'}, status=401)
        
        
        if headervalue == "y2s4pyj52nzr49jnuxxgqk5jtj28cj":
            
            LOCATIONID = request.data.get('location_id')
            FROMDATE = request.data.get('fromdate')
            TODATE = request.data.get('todate')
            USERID = request.data.get('user_id')
            
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
                        'AnaLocation': row[2],
                        'Private': row[1],
                        'Medicare': row[2],
                        'Dva': row[3],
                        'Others': row[4],
                        'Gst': row[5],
                        'Total': row[6],
                        'UserId': row[7],
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
                return JsonResponse({'Message': 'Payment Module Data Not Found', 'Status':404, 'Success': 'False', 'data': []}, status=404)
            
        else:
            return JsonResponse({'Message': 'Authenticate Failed', 'Status':401, 'Success': 'False'}, status=401)
        
        
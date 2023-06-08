""" API to Post Sidebar List records """

from rest_framework import views
from django.db import connection
from django.http import JsonResponse

class ItemNumberListView(views.APIView):
    """ API view to Sidebar List records Data """
    
    def post(self, request):
        """ POST method handler to add ItemNumberListView
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
                query = f"SELECT * FROM (SELECT A.ITEMNUM as ana_itemnum, COUNT( A.ITEMNUM ) as ana_count, SUM(CHARGEAMOUNT) as ana_billings,USERID FROM itemnum_{LOCATIONID} A WHERE A.USERID = {USERID} AND A.DATEOFSERVICE >= '{FROMDATE}' AND A.DATEOFSERVICE <= '{TODATE}'  GROUP BY A.ITEMNUM) t"
                # print(query)
                cursor.execute(query)
                # cursor.execute(query, [FROMDATE, TODATE, USERID])
                
                # print(cursor.execute(query, [APTDATE, USERID]))
                
                # Fetch the first row from the cursor
                rows = cursor.fetchall()
                
            if rows:
                # Successful login
                data = []
                
                for row in rows:
                    row_data = {
                        'AnaItemNum': row[0],
                        'AnaCount': row[1],
                        'AnaBillings': int(row[2]),
                        # 'UserId': row[3],
                    }
                    data.append(row_data)

                # Return the data as a JSON response
                response = {
                    'Message': 'Item Number List Data',
                    'Status':200,
                    'Success': 'True',
                    'data': data
                }
                
                return JsonResponse(response)
            else:
                # Invalid credentials
                return JsonResponse({'Message': 'Item Number Not Found', 'Status':404, 'Success': 'False', 'data': []}, status=404)
            
        else:
            return JsonResponse({'Message': 'Authenticate Failed', 'Status':401, 'Success': 'False'}, status=401)
        
        
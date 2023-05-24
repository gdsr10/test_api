""" API to Post Sidebar List records """

from rest_framework import views
from django.db import connection
from django.http import JsonResponse

class ItemNumberListView(views.APIView):
    """ API view to Sidebar List records Data """
    
    def post(self, request):
        """ POST method handler to add ItemNumberListView
        """
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
                    'ANA_ITEMNUM': row[0],
                    'ANA_COUNT': row[1],
                    'ANA_BILLINGS': row[2],
                    'USERID': row[3],
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
            return JsonResponse({'Message': 'No Data Found', 'Status':404, 'Success': 'False', 'data': []}, status=404)
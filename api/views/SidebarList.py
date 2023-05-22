""" API to Post Sidebar List records """

from rest_framework import views
from django.db import connection
from django.http import JsonResponse

class SidebarListView(views.APIView):
    """ API view to Sidebar List records Data """
    
    def post(self, request):
        """ POST method handler to add SidebarListView
        """
        LOCATIONID = request.data.get('LOCATIONID')
        APTDATE = request.data.get('APTDATE')
        USERID = request.data.get('USERID')
        
        # APTDATE = "2023-05-09"
        # USERID = "39"
        
        # print(MAILID)
        # print(PASSWORD)
        
        with connection.cursor() as cursor:
            # Execute an SQL query to fetch the user with matching credentials
            query = f"SELECT PNTNAME,APTTIME,APPTID,HAD,MPD,MP,ID,PNTDOB FROM sidebar_{LOCATIONID} WHERE DATE(APTDATE) = '{APTDATE}' AND USERID = {USERID} AND RECORDSTATUS ='1' ORDER BY APTTIME"
            print(query)
            cursor.execute(query)
            # cursor.execute(query, [APTDATE, USERID])
            
            # print(cursor.execute(query, [APTDATE, USERID]))
            
            # Fetch the first row from the cursor
            rows = cursor.fetchall()
            
        if rows:
            # Successful login
            data = []
            
            for row in rows:
                row_data = {
                    'PNTNAME': row[0],
                    'APTTIME': row[1],
                    'APPTID': row[2],
                    'HAD': row[3],
                    'MPD': row[4],
                    'MP': row[5],
                    'ID': row[6],
                    'PNTDOB': row[7],
                }
                data.append(row_data)

            # Return the data as a JSON response
            response = {
                'Message': 'Sidebar List Data',
                'Status':200,
                'Success': 'True',
                'data': data
            }
            
            return JsonResponse(response)
        else:
            # Invalid credentials
            return JsonResponse({'Message': 'No Data Found', 'Status':404, 'Success': 'False', 'data': []}, status=404)
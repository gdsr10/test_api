""" API to Post Sidebar List records """

from rest_framework import views
from django.db import connection
from django.http import JsonResponse

class SidebarListView(views.APIView):
    """ API view to Sidebar List records Data """
    
    def post(self, request):
        """ POST method handler to add SidebarListView
        """
        
        headervalue = request.META.get('HTTP_VALIDATE')
        
        if headervalue == "":
            return JsonResponse({'Message': 'Authenticate Empty','Status':401, 'Success': 'False'}, status=401)
        
        
        if headervalue == "y2s4pyj52nzr49jnuxxgqk5jtj28cj":
            
            LOCATIONID = request.data.get('location_id')
            APTDATE = request.data.get('aptdate')
            USERID = request.data.get('user_id')
            
            # APTDATE = "2023-05-09"
            # USERID = "39"
            
            # print(MAILID)
            # print(PASSWORD)
            
            with connection.cursor() as cursor:
                # Execute an SQL query to fetch the user with matching credentials
                query = f"SELECT PNTNAME,APTTIME,APPTID,HAD,MPD,MP,ID,PNTDOB,RECALL FROM sidebar_{LOCATIONID} WHERE DATE(APTDATE) = '{APTDATE}' AND USERID = {USERID} AND RECORDSTATUS ='1' ORDER BY APTTIME"
                # print(query)
                cursor.execute(query)
                # cursor.execute(query, [APTDATE, USERID])
                
                # print(cursor.execute(query, [APTDATE, USERID]))
                
                # Fetch the first row from the cursor
                rows = cursor.fetchall()
                
            if rows:
                # Successful login
                data = []
                
                for row in rows:
                    
                    recall_column = row[8]
                    
                    if len(recall_column) > 2 :
                        Recall = 1
                    else :
                        Recall = 0
                        
                    row_data = {
                        'PntName': row[0],
                        'AptTime': row[1],
                        'ApptId': row[2],
                        'Had': row[3],
                        'Mpd': row[4],
                        'Mp': row[5],
                        'Id': row[6],
                        'PntDob': row[7],
                        'Recall' : Recall,
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
                return JsonResponse({'Message': 'Sidebar Data Not Found', 'Status':404, 'Success': 'False', 'data': []}, status=404)
            
        else:
            return JsonResponse({'Message': 'Authenticate Failed', 'Status':401, 'Success': 'False'}, status=401)
        
        
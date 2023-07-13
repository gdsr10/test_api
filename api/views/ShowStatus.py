""" API to Post Sidebar List records """

from rest_framework import views
from django.db import connection
from django.http import JsonResponse

class ShowStatusView(views.APIView):
    """ API view to Sidebar List records Data """
    
    def post(self, request):
        """ POST method handler to add ShowStatusView
        """
        def cal_percentage(num_amount, num_total):
            count1 = num_amount / num_total
            count2 = count1 * 100
            count = round(count2, 2)
            return count
    
        headervalue = request.META.get('HTTP_VALIDATE')
        
        if headervalue == "":
            return JsonResponse({'Message': 'Authenticate Empty','Status':401, 'Success': 'False'}, status=401)
        
        if headervalue == "y2s4pyj52nzr49jnuxxgqk5jtj28cj":
            
            LOCATIONID = request.data.get('location_id')
            FROMDATE = request.data.get('fromdate')
            TODATE = request.data.get('todate')
            USERID = request.data.get('user_id')
            
            showmore = ""
            
            STATUSWher = " WHERE STATUS = 1"
            lopId =0
            
            if showmore == "yes" :
                STATUSWher = ""
            
            with connection.cursor() as cursor:
                # Execute an SQL query to fetch the user with matching credentials
                query = f"SELECT * FROM aa_itemnumber_mbs" + STATUSWher
                # print(query)
                cursor.execute(query)
                rows = cursor.fetchall()
                cursor.close()
            if rows:
                # Successful login
                data = []
                
                for row in rows:
                    
                    value = row[1]
                    ITEMNUM_ID = value
                    
                    ITEMNUMBER_WHERE = " A.ITEMNUM ='" + ITEMNUM_ID + "' AND"
                    
                    with connection.cursor() as cursor:
                        query2 = f"SELECT A.ITEMNUM as ana_itemnum, COUNT( A.ITEMNUM ) as ana_count, SUM(CHARGEAMOUNT) as ana_billings,USERID,(SELECT SUM(B.COMPLETED_APTS) FROM analytics_{LOCATIONID} B WHERE B.ANADATE >='{FROMDATE}' AND B.ANADATE <='{TODATE}' AND B.USERID ='{USERID}') AS TOTALBOOKING,(SELECT SUM(B.COMPLETED_APTS) FROM analytics_{LOCATIONID} B WHERE B.ANADATE >='{FROMDATE}' AND B.ANADATE <='{TODATE}' AND B.USERID IN ( SELECT C.USERID FROM users_{LOCATIONID} C WHERE C.STATUS = 0 AND (C.GROUPCODE=3 OR C.GROUPCODE=4) ) ) AS ALL_TOTALBOOKING,(SELECT COUNT(E.ID) FROM itemnum_{LOCATIONID} E WHERE E.ITEMNUM = A.ITEMNUM AND E.DATEOFSERVICE >='{FROMDATE}' AND E.DATEOFSERVICE <='{TODATE}' AND E.USERID IN ( SELECT D.USERID FROM users_{LOCATIONID} D WHERE D.STATUS = 0 AND (D.GROUPCODE=3 OR D.GROUPCODE=4) )) AS ALL_TOTAL_ITEMNU_BOOKING,(SELECT COUNT(F.ID) AS TOTALCO FROM itemnum_{LOCATIONID} F WHERE F.ITEMNUM =A.ITEMNUM AND F.DATEOFSERVICE BETWEEN '{FROMDATE}' AND '{TODATE}' GROUP BY F.USERID ORDER BY TOTALCO DESC LIMIT 1) AS HightC FROM itemnum_{LOCATIONID} A WHERE {ITEMNUMBER_WHERE} A.USERID ='{USERID}' AND A.DATEOFSERVICE >='{FROMDATE}' AND A.DATEOFSERVICE <='{TODATE}' GROUP BY A.ITEMNUM"
                        # print(query2)
                        cursor.execute(query2)
                        rows2 = cursor.fetchall()
                        
                        for row2 in rows2:
                            
                            overallValue = row2[4]
                            itemana_count = row2[1]
                            new_widthF = cal_percentage(row2[1],overallValue)
                        
                    ITEM_VALUE = float(row[2])
                    ITEM_VALUE = round(ITEM_VALUE, 2)
                    
                    row_data = {
                        # 'output': str(ITEMNUM_ID) + " " + str(new_widthF) + " " + str(ITEM_VALUE),
                        'itemnum_id' : ITEMNUM_ID,
                        'new_widthf' : new_widthF,
                        'item_value' : ITEM_VALUE,
                    }
                    data.append(row_data)   

                    # Return the data as a JSON response
                    response = {
                        'Message': 'Status Data',
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
        
        
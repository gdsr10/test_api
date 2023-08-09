""" API to Post Sidebar List records """

from rest_framework import views
from django.db import connection
from django.http import JsonResponse


class MBSReviewView(views.APIView):
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
            SHOWMORE = request.data.get('showmore')
            
            STATUSWher ="WHERE STATUS = 1"
            
            new_widthF = 0
            
            if SHOWMORE =='yes' :
                STATUSWher =""
                
            def cal_percentage(num_amount, num_total):
                count1 = num_amount / num_total
                count2 = count1 * 100
                count = round(count2,2)
                return count 
                
            with connection.cursor() as cursor:
                query = f"SELECT * FROM aa_itemnumber_mbs {STATUSWher}"
                # print(query)
                cursor.execute(query)
                rows = cursor.fetchall()
                
            if rows:
                data = []
                
                for row in rows:
                    
                    ITEMNUM_ID = row[1]
                    ITEM_VALUE = row[2]
                    ITEMNUMBER_WHERE = f" A.ITEMNUM ='{ITEMNUM_ID}' AND "
                    
                    with connection.cursor() as cursor2:
                        # query2 = f"SELECT A.ITEMNUM as ana_itemnum, COUNT( A.ITEMNUM ) as ana_count, SUM(CHARGEAMOUNT) as ana_billings,USERID,(SELECT SUM(B.COMPLETED_APTS) FROM analytics_{LOCATIONID} B WHERE B.LOCATIONID='{LOCATIONID}' AND DATE(B.ANADATE) >='{FROMDATE}' AND DATE(B.ANADATE) <='{TODATE}' AND B.USERID ='{USERID}') AS TOTALBOOKING,(SELECT SUM(B.COMPLETED_APTS) FROM analytics_{LOCATIONID} B WHERE B.LOCATIONID='{LOCATIONID}' AND DATE(B.ANADATE) >='{FROMDATE}' AND DATE(B.ANADATE) <='{TODATE}' AND B.USERID IN ( SELECT C.USERID FROM users_{LOCATIONID} C WHERE C.LOCATIONID='{LOCATIONID}' AND C.STATUS = 0 AND (C.GROUPCODE=3 OR C.GROUPCODE=4) ) ) AS ALL_TOTALBOOKING,(SELECT COUNT(E.ID) FROM itemnum_{LOCATIONID} E WHERE E.LOCATIONID='{LOCATIONID}' AND E.ITEMNUM = A.ITEMNUM AND DATE(E.DATEOFSERVICE) >='{FROMDATE}' AND DATE(E.DATEOFSERVICE) <='{TODATE}' AND E.USERID IN ( SELECT D.USERID FROM users_{LOCATIONID} D WHERE D.LOCATIONID='{LOCATIONID}' AND D.STATUS = 0 AND (D.GROUPCODE=3 OR D.GROUPCODE=4) )) AS ALL_TOTAL_ITEMNU_BOOKING,(SELECT COUNT(F.ID) AS TOTALCO FROM itemnum_{LOCATIONID} F WHERE F.LOCATIONID='{LOCATIONID}' AND F.ITEMNUM =A.ITEMNUM AND DATE(F.DATEOFSERVICE) BETWEEN '{FROMDATE}' AND '{TODATE}' GROUP BY F.USERID ORDER BY TOTALCO DESC LIMIT 1) AS HightC FROM itemnum_{LOCATIONID} A WHERE {ITEMNUMBER_WHERE} A.USERID ='{USERID}' AND DATE(A.DATEOFSERVICE) >='{FROMDATE}' AND DATE(A.DATEOFSERVICE) <='{TODATE}' AND A.LOCATIONID='{LOCATIONID}'  GROUP BY A.ITEMNUM"
                        query2 = f"SELECT COUNT( A.ITEMNUM ) as ana_count, (SELECT SUM(B.COMPLETED_APTS) FROM analytics_{LOCATIONID} B WHERE B.LOCATIONID='{LOCATIONID}' AND DATE(B.ANADATE) >='{FROMDATE}' AND DATE(B.ANADATE) <='{TODATE}' AND B.USERID ='{USERID}') AS TOTALBOOKING FROM itemnum_{LOCATIONID} A WHERE {ITEMNUMBER_WHERE} A.USERID ='{USERID}' AND DATE(A.DATEOFSERVICE) >='{FROMDATE}' AND DATE(A.DATEOFSERVICE) <='{TODATE}' AND A.LOCATIONID='{LOCATIONID}'  GROUP BY A.ITEMNUM"
                        # print(query2)
                        cursor2.execute(query2)
                        rows2 = cursor2.fetchall()
                
                        for row2 in rows2:
                    
                            itemana_count = row2[0]
                            overallValue = row2[1]
                            new_widthF = cal_percentage(itemana_count, overallValue)
                            
                    row_data = {
                        'Itemnum_Id': ITEMNUM_ID,
                        'Itemnum_Value': ITEM_VALUE,
                        'Value 1': new_widthF,
                    }
                    data.append(row_data)

                # Return the data as a JSON response
                response = {
                    'Message': 'MBSReview Data',
                    'Status':200,
                    'Success': 'True',
                    'data': data
                }
                
                return JsonResponse(response)
            else:
                # Invalid credentials
                return JsonResponse({'Message': 'MBS Data Not Found', 'Status':404, 'Success': 'False', 'data': []}, status=404)
            
        else:
            return JsonResponse({'Message': 'Authenticate Failed', 'Status':401, 'Success': 'False'}, status=401)
        
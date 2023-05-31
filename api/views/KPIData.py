""" API to Post KPI Data records """

from rest_framework import views
from django.db import connection
from django.http import JsonResponse


import datetime
from datetime import timedelta


class KPIDataView(views.APIView):
    """ API view to KPI Data """
        
    
    def post(self, request):
        """ POST method handler to add KPIDataView
        """ 
        
        headervalue = request.META.get('HTTP_VALIDATE')
        
        if headervalue == "":
            return JsonResponse({'Message': 'Authenticate Empty','Status':401, 'Success': 'False'}, status=401)
        
        
        if headervalue == "y2s4pyj52nzr49jnuxxgqk5jtj28cj":
            
            
            LOCATIONID = request.data.get('location_id')
            FROMDATE = request.data.get('fromdate')
            TODATE = request.data.get('todate')
            USERID = request.data.get('user_id')
            
            freeapts = 0
            compapts = 0
            bookedapts = 0
            totalfees = 0
            ppavg = 0
            newpatientcount = 0
            hourly_earning = 0
            doctorhours = 0
            
            def foo(secondss):
                t = round(secondss)
                hours = t // 3600
                minutes = (t % 3600) // 60
                seconds = t % 60
                # return '{:02d}.{:02d}.{:02d}'.format(t//3600, t//60%60, t%60)
                return hours * 10000 + minutes * 100 + seconds
            
            def doctorhoursfun(fdate, tdate, locid, uid):
                dochours = 0
                with connection.cursor() as cursor:
                    # Execute an SQL query to fetch the user with matching credentials
                    query = f"SELECT SUM(LENGTH), SUM(FEES) FROM hourly_{locid} WHERE ADATE >='{fdate}' AND ADATE <= '{tdate}' AND USERID  ='{uid}'"
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    if rows:
                        for row in rows:
                            dochours += foo(int(row[0]))
                    return dochours
                
            def userperpatientaverage(fdate, tdate, locid, uid):
                compapts = 0
                per =0
                earnings =0
                # Get the current date
                current_date = datetime.date.today()
                # Calculate the date 90 days before the current date
                delta = timedelta(days=90)
                NEW_DATE = current_date - delta
                with connection.cursor() as cursor:
                    # Execute an SQL query to fetch the user with matching credentials
                    query = f"(SELECT  SUM(A.TOTAL_FEES), SUM(A.COMPLETED_APTS) FROM analytics_{locid} A WHERE  A.ANADATE >= '{NEW_DATE}' AND A.USERID ='{uid}' GROUP BY A.USERID)"
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    if rows:
                        for row in rows:
                            earnings += row[0]
                            compapts += row[1]
                            if earnings > 0 :
                                per = earnings / compapts
                                per = round(per, 2)
                    return per
            
            
            with connection.cursor() as cursor:
                
                # Execute an SQL query to fetch the user with matching credentials
                query = f"SELECT (SUM(FREE_APTS)-SUM(UNAVAIL_APTS)), SUM(COMPLETED_APTS), SUM(BOOKED_APTS), SUM( TOTAL_FEES ) FROM analytics_{LOCATIONID} WHERE USERID ='{USERID}' AND ANADATE >='{FROMDATE}' AND ANADATE <='{TODATE}' AND BOOKED_APTS>0"
                
                cursor.execute(query)
                
                rows = cursor.fetchall()
                
                
            if rows:
                # Successful login
                data = []
            
                for row in rows:
                    
                    freeapts += row[0]
                    compapts += row[1]
                    bookedapts += row[2]
                    totalfees += row[3]
                    
                    if totalfees > 0 and compapts > 0 :
                        ppavg = totalfees / compapts
                    
                    totalapts = freeapts + bookedapts
                    
                    if bookedapts < 0 :
                        bookedapts = 0
                        
                    doctorhours += doctorhoursfun(FROMDATE, TODATE, LOCATIONID, USERID)
                    
                    if doctorhours > 0 :
                        hourly_earning = totalfees / doctorhours
                    
                    perpatientaverage = userperpatientaverage(FROMDATE, TODATE, LOCATIONID, USERID)
                    
                    PotentialBilling = totalapts * perpatientaverage
                    
                    row_data = {
                        'Bookedapts': bookedapts,
                        'Totalfees': round(totalfees, 0),
                        'Compapts': compapts,
                        'Ppavg': round(ppavg, 2),
                        'Newpntcnt': newpatientcount,
                        'Totalapts': totalapts,
                        'Hourlyerng': round(hourly_earning, 0),
                        'Potentialbllng': round(PotentialBilling, 0),
                    }
                    data.append(row_data)

                # Return the data as a JSON response
                response = {
                    'Message': 'KPI Data',
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
        
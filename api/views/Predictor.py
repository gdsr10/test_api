""" API to Post Sidebar List records """

from rest_framework import views
from django.db import connection
from django.http import JsonResponse

import datetime
from datetime import timedelta

class PredictorView(views.APIView):
    """ API view to Sidebar List records Data """
    
    def post(self, request):
        """ POST method handler to add PredictorView
        """
        
        headervalue = request.META.get('HTTP_VALIDATE')
        
        if headervalue == "":
            return JsonResponse({'Message': 'Authenticate Empty','Status':401, 'Success': 'False'}, status=401)
        
        if headervalue == "y2s4pyj52nzr49jnuxxgqk5jtj28cj":
            
            # Get the current date
            current_date = datetime.date.today()
            
            # Calculate the date 90 days before the current date
            delta = timedelta(days=90)
            
            NEW_DATE = current_date - delta
            
            # print(NEW_DATE)
            
            FROMDATE = request.data.get('fromdate')
            TODATE = request.data.get('todate')
            USERID = request.data.get('user_id')
            LOCATIONID = request.data.get('location_id')
            APTPRE = 90
            PPAVG = 1
            
            with connection.cursor() as cursor:
                
                # Execute an SQL query to fetch the user with matching credentials
                query = f"SELECT SUM( A.BOOKED_APTS ) as ana_booked1,(SUM( A.FREE_APTS)-SUM( A.UNAVAIL_APTS)) as ana_free1, ( SELECT (SUM(D.TOTAL_FEES)/SUM(D.COMPLETED_APTS)) FROM analytics_{LOCATIONID} D WHERE D.LOCATIONID = A.LOCATIONID AND D.USERID=A.USERID AND D.ANADATE>= '{NEW_DATE}' AND D.USERID IN ( SELECT E.USERID FROM users_{LOCATIONID} E WHERE E.STATUS = 0 AND (E.GROUPCODE=3 OR E.GROUPCODE=4) ) ) as ana_average from analytics_{LOCATIONID} A WHERE A.ANADATE >='{FROMDATE}' AND A.ANADATE <='{TODATE}' AND A.USERID = '{USERID}' GROUP BY A.USERID"
                
                cursor.execute(query)
                
                rows = cursor.fetchall()
                
                
            if rows:
                # Successful login
                data = []
                
                # 'ANA_BOOKED1': rows['']
                # 'ANA_FREE1': rows[1]
                # 'ANA_AVERAGE': rows[2]
                
                # for row in rows:
                #     row_data = {
                #         'ANA_BOOKED1': row[0],
                #         'ANA_FREE1': row[1],
                #         'ANA_AVERAGE': row[2],
                #     }
                #     data.append(row_data)
                    
                for row in rows:
                    
                    anaBooked = int(row[0])
                    anaFree = int(row[1])
                    anaAverage = int(row[2])
                    
                    if anaBooked < 0 :
                        anaBooked = 0
                        
                    if anaFree < 0 :
                        anaFree = 0
                        
                    anaBooked += anaFree
                    
                    EARNINGS = anaBooked * anaAverage

                    if APTPRE == "" :
                        APTPRE = 90
                        
                    if PPAVG == "" :
                        PPAVG = 1
                        
                    BOOKEDOUT = anaBooked * APTPRE / 100
                    AVGOUT = anaAverage + PPAVG
                    EARNINGOUT = BOOKEDOUT * AVGOUT
                    
                    row_data = {
                        'Appointments': anaBooked,
                        'PerPatientAverage': format(anaAverage, ".2f"),
                        'TotalEarnings': format(EARNINGS),
                        '%': format(EARNINGS, ".2f"),
                        '%_Appointments': format(BOOKEDOUT, ".0f"),
                        '%_PerPatientAverage': format(AVGOUT, ".2f"),
                        '%_TotalEarnings': format(EARNINGOUT),
                    }
                    
                    # print(anaBooked)
                    # print(anaFree)
                    # print(anaAverage)
                    # print(APTPRE)
                    # print(PPAVG)
                    
                    data.append(row_data)
                    
                # anaBooked = ""
                # anaFree = ""
                # anaAverage = ""
                
                # print(anaBooked = data[0]['ANA_BOOKED1'])

                # Return the data as a JSON response
                response = {
                    'Message': 'Predictor Data',
                    'Status':200,
                    'Success': 'True',
                    'data': data
                }
                
                return JsonResponse(response)
            else:
                # Invalid credentials
                return JsonResponse({'Message': 'Invalid Predictor Data', 'Status':404, 'Success': 'False', 'data': []}, status=404)
            
        else:
            return JsonResponse({'Message': 'Authenticate Failed', 'Status':401, 'Success': 'False'}, status=401)
        
        
""" API to Post Sidebar List records """

from rest_framework import views
from django.db import connection
from django.http import JsonResponse

import datetime
from datetime import timedelta

from random import randint

import requests
from django.conf import settings

class OTPVerifyView(views.APIView):
    """ API view to Sidebar List records Data """
    
    def post(self, request):
        """ POST method handler to add OTPVerifyView
        """
        
        headervalue = request.META.get('HTTP_VALIDATE')
        
        if headervalue == "":
            return JsonResponse({'Message': 'Authenticate Empty','Status':401, 'Success': 'False'}, status=401)
        
        
        if headervalue == "y2s4pyj52nzr49jnuxxgqk5jtj28cj":
            
            OTPNum = request.data.get('otp')
            # MAILID = request.data.get('mail_id')
            # PASSWORD = request.data.get('password')

            
            with connection.cursor() as cursor:
                # Execute an SQL query to check if the user exists and meets a condition
                cursor.execute("SELECT FIELD_MAILID, FIELD_PASSWORD, FIELD_MOBILE FROM admin_users WHERE OTP = %s", [OTPNum])
                user = cursor.fetchone()
                
                # print(user)

                if user:
                    
                    MailId = user[0]
                    Password = user[1]
                    MobileNo = user[2]
                    
                    rtnmsg = self.send_otp_to_mobile(MailId, Password ,MobileNo)
                    
                    if "success" == rtnmsg :
                        data = {
                            'Message': 'user details sent successfully',
                            'Status':200,
                            'Success': 'True'
                        }
                    else:
                        data = {
                            'Message': 'user details sent Failure',
                            'Status':400,
                            'Success': 'False'
                        }
                        
                    return JsonResponse(data)
                    
                else:
                    return JsonResponse({'Message': 'user details not found', 'Status':404, 'Success': 'False', 'data':[]}, status=404)
            
        else:
            return JsonResponse({'Message': 'Authenticate Failed', 'Status':401, 'Success': 'False'}, status=401)
        
    
    def send_otp_to_mobile(self, mail_id, password, mobile_number):
        
        # Implement your code to send the OTP to the mobile number using Burst SMS
        # Make sure to configure Burst SMS credentials in your Django settings
        # Here's an example of using the burst_sms package:
        
        api_key = ""
        api_secret = ""
        sender_id = ""
        
        with connection.cursor() as cursor:
                # Execute an SQL query to check if the user exists and meets a condition
                cursor.execute("SELECT SMSNAME, burstsmsapikey, burstsmssecretkey FROM locationdetails")
                datadet = cursor.fetchone()
                
                if datadet :
                    
                    api_key = datadet[1]
                    api_secret = datadet[2]
                    sender_id = datadet[0]
                    
                else:
                    return JsonResponse({'Message': 'User not found', 'Status':404, 'Success': 'False', 'data':[]}, status=404)
    
                burst_api_key = api_key
                burst_api_secret = api_secret
                burst_sender_id = sender_id
                
                
                headers = {
                'Authorization': 'Basic YzQzNGIyYjk5YTMwNzM5YjJiNmIzNmE3YzNkZTFlYzk6QW1oZXJzdDIwMjE='
                }

                message = f"We have recovered your login credentials of Codd. Username: {mail_id} Password : {password}"
                mob_no = "91" + mobile_number
                
                url = f'https://api.transmitsms.com/send-sms.json?message={message}&from={burst_sender_id}&to={mob_no}'
                
                
                # response = requests.request("POST", url, headers=headers, data=data)
                response = requests.post(url, headers=headers)
                
                if response.status_code == 200:
                    print("SMS sent successfully")
                    return "success"
                else:
                    print("SMS sending failed")
                    return "failure"
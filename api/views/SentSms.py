""" API to Post Sidebar List records """

from rest_framework import views
from django.db import connection
from django.http import JsonResponse

from datetime import datetime

from random import randint

import requests
from django.conf import settings

import requests
import base64


class SentSmsView(views.APIView):
    """ API view to Sidebar List records Data """
    
    def post(self, request):
        """ POST method handler to add SentSmsView
        """
        
        headervalue = request.META.get('HTTP_VALIDATE')
        
        if headervalue == "":
            return JsonResponse({'Message': 'Authenticate Empty','Status':401, 'Success': 'False'}, status=401)
        
        
        if headervalue == "y2s4pyj52nzr49jnuxxgqk5jtj28cj":
            
            RefNo = request.data.get('ref_id')
            LoctnId = request.data.get('loctn_id')
            UsrId = request.data.get('usr_id')
            MobileNo = request.data.get('mobile_no')
            Text = request.data.get('text')
            CrtBy = request.data.get('crt_by')
            
            
            current_datetime = datetime.now()
            Datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            
            CrtDt = Datetime
            
            with connection.cursor() as cursor:
                # Execute an SQL query to check if the user exists and meets a condition
                query = f"INSERT INTO sent_sms (reference_id,location_id,user_id,mobile,text,created_by,created_date) VALUES ('{RefNo}','{LoctnId}','{UsrId}','{MobileNo}','{Text}','{CrtBy}','{CrtDt}')"
                # print(query)
                cursor.execute(query)
                
                rtnmsg = self.send_otp_to_mobile(MobileNo, Text, LoctnId)
                
                if "success" == rtnmsg :
                        data = {
                            'Message': 'Message sent successfully',
                            'Status':200,
                            'Success': 'True',
                            'data': [
                                {
                                    'Text Message': Text
                                }
                            ]
                        }
                else:
                        data = {
                            'Message': 'Message sent Failure',
                            'Status':400,
                            'Success': 'False'
                        }
                        
                return JsonResponse(data)
            
        else:
            return JsonResponse({'Message': 'Authenticate Failed', 'Status':401, 'Success': 'False'}, status=401)
        
    
    def send_otp_to_mobile(self, mobile_number, text, locid):
        
        # Implement your code to send the OTP to the mobile number using Burst SMS
        # Make sure to configure Burst SMS credentials in your Django settings
        # Here's an example of using the burst_sms package:
        
        api_key = ""
        api_secret = ""
        sender_id = ""
        
        with connection.cursor() as cursor:
                # Execute an SQL query to check if the user exists and meets a condition
                cursor.execute("SELECT SMSNAME, burstsmsapikey, burstsmssecretkey FROM locationdetails WHERE LOCATIONID = %s", [locid])
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
                
                # url = 'http://burst.transmitsms.com/register?aff_id=120509'
                # payload={}
                # headers = {
                # 'Authorization': 'Basic YzQzNGIyYjk5YTMwNzM5YjJiNmIzNmE3YzNkZTFlYzk6QW1oZXJzdDIwMjE='
                # }
                # payload='message=This%20is%20my%20message%2C%20click%20on%20my%20link%20%5Btracked-link%5D&list_id=4070887&from=61434008437&tracked_link_url=https%3A%2F%2Fwww.twitter.com%2Ftransmitsms'
                # headers = {}
                message = f"Your text is: {text}"
                mob_no = "91" + mobile_number
                # data = {
                #     'message': message,
                #     'to': mob_no,
                #     'from': burst_sender_id,
                #     'api_key': burst_api_key,
                #     'api_secret': burst_api_secret
                # } 
                
                url = f'https://api.transmitsms.com/send-sms.json?message={message}&from={burst_sender_id}&to={mob_no}'
                
                # print(data)
                print(url)
                
                # Set the basic authorization header in the email message
                encoded_credentials = base64.b64encode(f"{burst_api_key}:{burst_api_secret}".encode('utf-8')).decode('utf-8')
                headers = {'Authorization': f'Basic {encoded_credentials}'}
                
                # response = requests.request("POST", url, headers=headers, data=data)
                response = requests.post(url, headers=headers)
                
                print(response)
                # print(response.json)
            
                if response.status_code == 200:
                    print("SMS sent successfully")
                    return "success"
                else:
                    print("SMS sending failed")
                    return "failure"
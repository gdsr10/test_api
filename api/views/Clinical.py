""" API to Post Sidebar List records """

from rest_framework import views
from django.db import connection
from django.http import JsonResponse

from datetime import datetime, timedelta

class ClinicalView(views.APIView):
    """ API view to Sidebar List records Data """
    
    def post(self, request):
        """ POST method handler to add ClinicalView
        """
        headervalue = request.META.get('HTTP_VALIDATE')
        
        if headervalue == "":
            return JsonResponse({'Message': 'Authenticate Empty','Status':401, 'Success': 'False'}, status=401)
        
        if headervalue == "y2s4pyj52nzr49jnuxxgqk5jtj28cj":
            
            # Get the current date
            current_date = datetime.now().date()
            
            # Calculate the date one year ago
            one_year_ago = current_date - timedelta(days=365)
            
            # print(one_year_ago.strftime("%Y-%m-%d"))
            
            LOCATIONID = request.data.get('location_id')
            ID = request.data.get('id')
        
        
            with connection.cursor() as cursor:
            
                # Execute an SQL query to fetch the user with matching credentials
                query = f"SELECT * FROM sidebar_{LOCATIONID} WHERE ID ='{ID}'"
            
                cursor.execute(query)
            
                rows = cursor.fetchall()
            
                # print(rows)
            
                if rows:
                # Successful login
                    data = []
            
                    for row in rows:
                
                        HAD = str(row[15])
                        MDP = str(row[16])
                        MP = str(row[17])
                
                        HAD_MDP_MP = HAD + " " + MDP + " " + MP
                
                
                        # Start ITEMNO split and check condition
                        ITEMNO_str = str(row[18])
                
                        if "######" in ITEMNO_str:
                            Date_701 = ""
                            Date_703 = ""
                            Date_705 = ""
                            Date_707 = ""
                            Date_721 = ""
                            Date_723 = ""
                            Date_732 = ""
                            ITLastDate = ""
                        else:
                            ITEMNO_str_arr = ITEMNO_str.split("#")
                            ITEMNO_str1 = ITEMNO_str_arr[0]
                            ITEMNO_str2 = ITEMNO_str_arr[1]
                            ITEMNO_str3 = ITEMNO_str_arr[2]
                            ITEMNO_str4 = ITEMNO_str_arr[3]
                            ITEMNO_str5 = ITEMNO_str_arr[4]
                            ITEMNO_str6 = ITEMNO_str_arr[5]
                            ITEMNO_str7 = ITEMNO_str_arr[6]
                            Date_701 = ITEMNO_str1
                            Date_703 = ITEMNO_str2
                            Date_705 = ITEMNO_str3
                            Date_707 = ITEMNO_str4
                            Date_721 = ITEMNO_str5
                            Date_723 = ITEMNO_str6
                            Date_732 = ITEMNO_str7
                            
                            # dates = [Date_701, Date_703, Date_705,Date_707,Date_721,Date_723,Date_732]
                            # print(dates)
                            
                            # ITLastDate = ""
                            ITLastDate_lt = ""
                            
                            if Date_701 == "":
                                ITLastDate = ""
                                ITLastDate_lt = ""
                            else:
                                IT_from_date_str = one_year_ago.strftime("%Y-%m-%d")
                                IT_from_date = datetime.strptime(IT_from_date_str, "%Y-%m-%d")
                                IT_to_date1 = datetime.strptime(Date_701, "%Y-%m-%d")
                                difference11 = IT_from_date - IT_to_date1
                                if difference11 <= timedelta(days=365):
                                    ITLastDate = Date_701
                                else:
                                    ITLastDate += "|" + ""

                                    
                            if Date_703 == "":
                                ITLastDate += "|" + ""
                                ITLastDate_lt += ""
                            else:
                                IT_from_date_str = one_year_ago.strftime("%Y-%m-%d")
                                IT_from_date = datetime.strptime(IT_from_date_str, "%Y-%m-%d")
                                IT_to_date2 = datetime.strptime(Date_703, "%Y-%m-%d")
                                difference12 = IT_from_date - IT_to_date2
                                if difference12 <= timedelta(days=365):
                                    ITLastDate += "|" + Date_703
                                else:
                                    ITLastDate += "|" + ""
                                    
                                    
                            if Date_705 == "":
                                ITLastDate += "|" + ""
                                ITLastDate_lt += ""
                            else:
                                IT_from_date_str = one_year_ago.strftime("%Y-%m-%d")
                                IT_from_date = datetime.strptime(IT_from_date_str, "%Y-%m-%d")
                                IT_to_date3 = datetime.strptime(Date_705, "%Y-%m-%d")
                                difference13 = IT_from_date - IT_to_date3
                                if difference13 <= timedelta(days=365):
                                    ITLastDate += "|" + Date_705
                                else:
                                    ITLastDate += "|" + ""
                                
                                    
                            if Date_707 == "":
                                ITLastDate += "|" + ""
                                ITLastDate_lt += ""
                            else:
                                IT_from_date_str = one_year_ago.strftime("%Y-%m-%d")
                                IT_from_date = datetime.strptime(IT_from_date_str, "%Y-%m-%d")
                                IT_to_date4 = datetime.strptime(Date_707, "%Y-%m-%d")
                                difference14 = IT_from_date - IT_to_date4
                                if difference14 <= timedelta(days=365):
                                    ITLastDate += "|" + Date_707
                                else:
                                    ITLastDate += "|" + ""
                                    
                                    
                            if Date_721 == "":
                                ITLastDate += "|" + ""
                                ITLastDate_lt += ""
                            else:
                                IT_from_date_str = one_year_ago.strftime("%Y-%m-%d")
                                IT_from_date = datetime.strptime(IT_from_date_str, "%Y-%m-%d")
                                IT_to_date5 = datetime.strptime(Date_721, "%Y-%m-%d")
                                difference15 = IT_from_date - IT_to_date5
                                if difference15 <= timedelta(days=365):
                                    ITLastDate += "|" + Date_721
                                else:
                                    ITLastDate += "|" + ""

                                    
                            if Date_723 == "":
                                ITLastDate += "|" + ""
                                ITLastDate_lt += ""
                            else:
                                IT_from_date_str = one_year_ago.strftime("%Y-%m-%d")
                                IT_from_date = datetime.strptime(IT_from_date_str, "%Y-%m-%d")
                                # print(IT_from_date)
                                IT_to_date6 = datetime.strptime(Date_723, "%Y-%m-%d")
                                # print(IT_to_date6)
                                difference16 = IT_from_date - IT_to_date6
                                # print(difference16)
                                if difference16 <= timedelta(days=365):
                                    ITLastDate += "|" + Date_723
                                else:
                                    ITLastDate += "|" + ""
                                    
                                    
                            if Date_732 == "":
                                ITLastDate += "|" + ""
                                ITLastDate_lt += ""
                            else:
                                IT_from_date_str = one_year_ago.strftime("%Y-%m-%d")
                                IT_from_date = datetime.strptime(IT_from_date_str, "%Y-%m-%d")
                                IT_to_date7 = datetime.strptime(Date_732, "%Y-%m-%d")
                                difference17 = IT_from_date - IT_to_date7
                                if difference17 <= timedelta(days=365):
                                    ITLastDate += "|" + Date_732
                                else:
                                    ITLastDate += "|" + ""
                                    
                            # print("itlastdate first : " + ITLastDate)
                            
                            dates_arr = ITLastDate.split("|")
                            dates_arr = [x for x in dates_arr if x != '']
                            dates = [datetime.strptime(date_str, "%Y-%m-%d").date() for date_str in dates_arr]
                            recent_date = max(dates)
                            # index = dates.index(recent_date)
                            
                            ITLastDate = recent_date
                            # ITLastDate = ITLastDate_lt
                            
                            # print("itlastdate second : " + ITLastDate)
                            
                            # if Date_701 == "" and Date_703 == "" and Date_705 == "" and Date_707 == "" and Date_721 == "" and Date_723 == "" and Date_732 == "" :
                            #     ITLastDate = ""
                                
                            # ITLastDate = ""
                            
                            # print(dates_arr)
                            # print(recent_date)
                            # print(index)
                            
                            # End ITEMNO split and check condition
                
                
                        # Start BLOODPRESSURE split and check condition
                        BLOODPRESSURE_str = str(row[21])
                        
                        if "-@" in BLOODPRESSURE_str:
                            Systolic = ""
                            Diastolic = ""
                            BLOODPRESSUREDate = ""
                            BPLastDate = ""
                        else:
                            BLOODPRESSURE_str_arr = BLOODPRESSURE_str.split("@")
                            BLOODPRESSURE_str1_split = BLOODPRESSURE_str_arr[0]
                            BLOODPRESSURE_str1_split_arr = BLOODPRESSURE_str1_split.split("/")
                            BLOODPRESSURE_str1_split_1 = BLOODPRESSURE_str1_split_arr[0]
                            BLOODPRESSURE_str1_split_2 = BLOODPRESSURE_str1_split_arr[1]
                            BLOODPRESSURE_str2 = BLOODPRESSURE_str_arr[1]
                            Systolic = BLOODPRESSURE_str1_split_1
                            Diastolic = BLOODPRESSURE_str1_split_2
                            BLOODPRESSUREDate = BLOODPRESSURE_str2
                            # print(BLOODPRESSUREDate)
                            # BPLastDate = ""
                            BP_from_date_str = one_year_ago.strftime("%d-%m-%Y")
                            BP_from_date = datetime.strptime(BP_from_date_str, "%d-%m-%Y")
                            BP_to_date = datetime.strptime(BLOODPRESSUREDate, "%d-%m-%Y")
                            # Calculate the difference between the dates
                            difference2 = BP_from_date - BP_to_date
                            # Check if the difference is less than or equal to 365 days
                            if difference2 <= timedelta(days=365):
                                BPLastDate = BLOODPRESSUREDate
                            else:
                                BPLastDate = ""
                        # End BLOODPRESSURE split and check condition
                        
                        
                        # Start BMI split and check condition
                        BMI_str = str(row[22])
                        
                        if "-#" in BMI_str:
                            Height = ""
                            Weight = ""
                            BMI = ""
                            BMIDate = ""
                            BMILastDate = ""
                        else:
                            BMI_str_arr = BMI_str.split("#")
                            BMI_str1 = BMI_str_arr[0]
                            BMI_str2 = BMI_str_arr[1]
                            BMI_str3 = BMI_str_arr[2]
                            BMI_str4 = BMI_str_arr[3]
                            Height = BMI_str1
                            Weight = BMI_str2
                            BMI = BMI_str3
                            BMIDate = BMI_str4
                            BMI_from_date_str = one_year_ago.strftime("%d-%m-%Y")
                            BMI_from_date = datetime.strptime(BMI_from_date_str, "%d-%m-%Y")
                            BMI_to_date = datetime.strptime(BMIDate, "%d-%m-%Y")
                            # Calculate the difference between the dates
                            difference3 = BMI_from_date - BMI_to_date
                            # print(difference)
                            # Check if the difference is less than or equal to 365 days
                            if difference3 <= timedelta(days=365):
                                BMILastDate = BMIDate
                            else:
                                BMILastDate = ""
                        # End BMI split and check condition
                        
                        
                        # Start GLUCOSE split and check condition
                        GLUCOSE_str = str(row[24])
                        
                        
                        if "-," in GLUCOSE_str:
                            Glucose = ""
                            GLUCOSEDate = ""
                            GLLastDate = ""
                        else:
                            GLUCOSE_str_arr = GLUCOSE_str.split(" ,")
                            GLUCOSE_str1 = GLUCOSE_str_arr[0]
                            GLUCOSE_str2 = GLUCOSE_str_arr[1]
                            Glucose = GLUCOSE_str1
                            GLUCOSEDate = GLUCOSE_str2
                            # print(GLUCOSEDate)
                            GL_from_date_str = one_year_ago.strftime("%d-%m-%Y")
                            GL_from_date = datetime.strptime(GL_from_date_str, "%d-%m-%Y")
                            GL_to_date = datetime.strptime(GLUCOSEDate, "%d-%m-%Y")
                            # Calculate the difference between the dates
                            difference4 = GL_from_date - GL_to_date
                            # print(difference4)
                            # Check if the difference is less than or equal to 365 days
                            if difference4 <= timedelta(days=365):
                                GLLastDate = GLUCOSEDate
                            else:
                                GLLastDate = ""
                        # End GLUCOSE split and check condition
                        
                        
                        # Start HBA1C split and check condition
                        HBA1C_str = str(row[25])
                        
                        if "-," in HBA1C_str:
                            HBA1C = ""
                            HBA1CDate = ""
                            HBLastDate = ""
                        else:
                            HBA1C_str_arr = HBA1C_str.split(" ,")
                            HBA1C_str1 = HBA1C_str_arr[0]
                            HBA1C_str2 = HBA1C_str_arr[1]
                            HBA1C = HBA1C_str1
                            HBA1CDate = HBA1C_str2
                            # print(HBA1CDate)
                            HB_from_date_str = one_year_ago.strftime("%d-%m-%Y")
                            HB_from_date = datetime.strptime(HB_from_date_str, "%d-%m-%Y")
                            HB_to_date = datetime.strptime(HBA1CDate, "%d-%m-%Y")
                            # Calculate the difference between the dates
                            difference5 = HB_from_date - HB_to_date
                            # print(difference5)
                            # Check if the difference is less than or equal to 365 days
                            if difference5 <= timedelta(days=365):
                                HBLastDate = HBA1CDate
                            else:
                                HBLastDate = ""
                                
                        # End HBA1C split and check condition
                        
                        
                        # Start CHELOSTROL split and check condition
                        CHELOSTROL_str = str(row[23])
                        
                        if "-," in CHELOSTROL_str:
                            Cholestrol = ""
                            HDL = ""
                            LDL = ""
                            Triglyceride = ""
                            Ratio = ""
                            CHELOSTROLDate = ""
                            CHLastDate = ""
                        else:
                            CHELOSTROL_str_arr = CHELOSTROL_str.split(",")
                            CHELOSTROL_str1 = CHELOSTROL_str_arr[0]
                            CHELOSTROL_str2 = CHELOSTROL_str_arr[1]
                            CHELOSTROL_str3 = CHELOSTROL_str_arr[2]
                            CHELOSTROL_str4 = CHELOSTROL_str_arr[3]
                            CHELOSTROL_str5 = CHELOSTROL_str_arr[4]
                            CHELOSTROL_str6 = CHELOSTROL_str_arr[5]
                            Cholestrol = CHELOSTROL_str1
                            HDL = CHELOSTROL_str2
                            LDL = CHELOSTROL_str3
                            Triglyceride = CHELOSTROL_str4
                            Ratio = CHELOSTROL_str5
                            CHELOSTROLDate = CHELOSTROL_str6
                            # print(CHELOSTROLDate)
                            CH_from_date_str = one_year_ago.strftime("%d-%m-%Y")
                            CH_from_date = datetime.strptime(CH_from_date_str, "%d-%m-%Y")
                            CH_to_date = datetime.strptime(CHELOSTROLDate, "%d-%m-%Y")
                            # Calculate the difference between the dates
                            difference6 = CH_from_date - CH_to_date
                            # print(difference6)
                            # Check if the difference is less than or equal to 365 days
                            if difference6 <= timedelta(days=365):
                                CHLastDate = CHELOSTROLDate
                            else:
                                CHLastDate = ""
                        # End CHELOSTROL split and check condition
                        
                        
                        # Start ALCOHOL split and check condition
                        ALCOHOL_str = str(row[27])
                        
                        if "-" in ALCOHOL_str:
                            ALCOHOL = ""
                            Days_Per_Week = ""
                            Drinks_Per_Day = ""
                        else:
                            ALCOHOL_str_arr = ALCOHOL_str.split("|")
                            ALCOHOL_str1 = ALCOHOL_str_arr[0]
                            ALCOHOL = ALCOHOL_str1
                            ALCOHOL_str2_split = ALCOHOL_str_arr[1]
                            ALCOHOL_str2_split_arr = ALCOHOL_str2_split.split(",")
                            ALCOHOL_str2_split_1 = ALCOHOL_str2_split_arr[0]
                            Days_Per_Week = ALCOHOL_str2_split_1
                            ALCOHOL_str2_split_2 = ALCOHOL_str2_split_arr[1]
                            Drinks_Per_Day = ALCOHOL_str2_split_2
                        # End ALCOHOL split and check condition
                        
                        # print(ITEMNO)
                        # print(BLOODPRESSURE_str)
                        # print(BMI)
                        # print(GLUCOSE_str)
                        # print(HBA1C_str)
                        # print(CHELOSTROL_str)
                        # print(ALCOHOL_str)
                        
                        row_data = {
                            'Id': row[0],
                            'ApptId': row[1],
                            'PntName': row[2],
                            'PntId': row[3],
                            'PntDob': row[4],
                            'Email': row[5],
                            'OtherEmail': row[6],
                            'AptTime': row[7],
                            'AptLength': row[8],
                            'AptDate': row[9],
                            'UserId': row[10],
                            'RecordId': row[11],
                            'RecordStatus': row[12],
                            'AptType': row[13],
                            'Reason': row[14],
                            'CareplanDate': row[19],
                            'Reminder': row[20],
                            'Had_Mpd_Mp': HAD_MDP_MP,
                            'ItemNo': { 
                                "701" : Date_701,
                                "703" : Date_703,
                                "705" : Date_705,
                                "707" : Date_707,
                                "721" : Date_721,
                                "723" : Date_723,
                                "732" : Date_732,
                                "lastDate": ITLastDate,
                                # "lastDate": ITLastDate_lt,
                            },
                            'BloodPressure': {
                                "Systolic" : Systolic,
                                "Diastolic" : Diastolic,
                                "Date" : BLOODPRESSUREDate,
                                "lastDate": BPLastDate,
                            },
                            'Bmi': {
                                "Height" : Height,
                                "Weight" : Weight,
                                "BMI" : BMI,
                                "Date" : BMIDate,
                                "lastDate": BMILastDate,
                            },
                            'Glucose': {
                                "Glucose" : Glucose,
                                "Date" : GLUCOSEDate,
                                "lastDate": GLLastDate,
                            },
                            'Hba1c': {
                                "HBA1C" : HBA1C,
                                "Date" : HBA1CDate,
                                "lastDate": HBLastDate,
                            },
                            'Cholestrol': {
                                "Cholestrol" : Cholestrol,
                                "HDL" : HDL,
                                "LDL" : LDL,
                                "Triglyceride" : Triglyceride,
                                "Ratio" : Ratio,
                                "Date" : CHELOSTROLDate,
                                "lastDate": CHLastDate,
                            },
                            'Alcohol': {
                                "ALCOHOL" : ALCOHOL,
                                "Days Per Week" : Days_Per_Week,
                                "Drinks Per Day" : Drinks_Per_Day,
                            },
                            'Smoke': row[26],
                            'EmailStatus': row[28],
                            'ArlUpdateStatus': row[29],
                            'HMobile': row[30],
                            'WMobile': row[31],
                            'MPhone': row[32],
                            'InvoiceStatus': row[33],
                            'LastItemNo': row[34],
                        }
                        
                        data.append(row_data)

                    # Return the data as a JSON response
                    response = {
                        'Message': 'Clinical Data',
                        'Status':200,
                        'Success': 'True',
                        'data': data
                    }
                    
                    return JsonResponse(response)
                else:
                    # Invalid credentials
                    return JsonResponse({'Message': 'Invalid Clinical Data', 'Status':404, 'Success': 'False', 'data': []}, status=404)
        else:
            return JsonResponse({'Message': 'Authenticate Failed', 'Status':401, 'Success': 'False'}, status=401)
""" API to Post Sidebar List records """

from rest_framework import views
from django.db import connection
from django.http import JsonResponse

class ClinicalView(views.APIView):
    """ API view to Sidebar List records Data """
    
    def post(self, request):
        """ POST method handler to add ClinicalView
        """
        
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
                # End ITEMNO split and check condition
                
                
                # Start BLOODPRESSURE split and check condition
                BLOODPRESSURE_str = str(row[21])
                
                if "-@" in BLOODPRESSURE_str:
                    Systolic = ""
                    Diastolic = ""
                    BLOODPRESSUREDate = ""
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
                # End BLOODPRESSURE split and check condition
                
                
                # Start BMI split and check condition
                BMI_str = str(row[22])
                
                if "-#" in BMI_str:
                    Height = ""
                    Weight = ""
                    BMI = ""
                    BMIDate = ""
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
                # End BMI split and check condition
                
                
                # Start GLUCOSE split and check condition
                GLUCOSE_str = str(row[24])
                
                
                if "-," in GLUCOSE_str:
                    Glucose = ""
                    GLUCOSEDate = ""
                else:
                    GLUCOSE_str_arr = GLUCOSE_str.split(" ,")
                    GLUCOSE_str1 = GLUCOSE_str_arr[0]
                    GLUCOSE_str2 = GLUCOSE_str_arr[1]
                    Glucose = GLUCOSE_str1
                    GLUCOSEDate = GLUCOSE_str2
                # End GLUCOSE split and check condition
                
                
                # Start HBA1C split and check condition
                HBA1C_str = str(row[25])
                
                if "-," in HBA1C_str:
                    HBA1C = ""
                    HBA1CDate = ""
                else:
                    HBA1C_str_arr = HBA1C_str.split(" ,")
                    HBA1C_str1 = HBA1C_str_arr[0]
                    HBA1C_str2 = HBA1C_str_arr[1]
                    HBA1C = HBA1C_str1
                    HBA1CDate = HBA1C_str2
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
                    'ID': row[0],
                    'APPTID': row[1],
                    'PNTNAME': row[2],
                    'PNTID': row[3],
                    'PNTDOB': row[4],
                    'EMAIL': row[5],
                    'OTHER_EMAIL': row[6],
                    'APTTIME': row[7],
                    'APTLENGTH': row[8],
                    'APTDATE': row[9],
                    'USERID': row[10],
                    'RECORDID': row[11],
                    'RECORDSTATUS': row[12],
                    'APPOINTMENTTYPE': row[13],
                    'REASON': row[14],
                    'CAREPLANDATE': row[19],
                    'REMINDER': row[20],
                    'HAD_MPD_MP': HAD_MDP_MP,
                    'ITEMNO': { 
                        "701" : Date_701,
                        "703" : Date_703,
                        "705" : Date_705,
                        "707" : Date_707,
                        "721" : Date_721,
                        "723" : Date_723,
                        "732" : Date_732,
                    },
                    'BLOODPRESSURE': {
                        "Systolic" : Systolic,
                        "Diastolic" : Diastolic,
                        "Date" : BLOODPRESSUREDate,
                    },
                    'BMI': {
                        "Height" : Height,
                        "Weight" : Weight,
                        "BMI" : BMI,
                        "Date" : BMIDate,
                    },
                    'GLUCOSE': {
                        "Glucose" : Glucose,
                        "Date" : GLUCOSEDate,
                    },
                    'HBA1C': {
                        "HBA1C" : HBA1C,
                        "Date" : HBA1CDate,
                    },
                    'CHELOSTROL': {
                        "Cholestrol" : Cholestrol,
                        "HDL" : HDL,
                        "LDL" : LDL,
                        "Triglyceride" : Triglyceride,
                        "Ratio" : Ratio,
                        "Date" : CHELOSTROLDate,
                    },
                    'ALCOHOL': {
                        "ALCOHOL" : ALCOHOL,
                        "Days Per Week" : Days_Per_Week,
                        "Drinks Per Day" : Drinks_Per_Day,
                    },
                    'SMOKE': row[26],
                    'EMAIL_STATUS': row[28],
                    'ARRIVAL_UPDATE_STATUS': row[29],
                    'HMOBILE': row[30],
                    'WMOBILE': row[31],
                    'MPHONE': row[32],
                    'INVOICE_STATUS': row[33],
                    'LAST_ITEMNO': row[34],
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
            return JsonResponse({'Message': 'Invalid credentials', 'Status':401, 'Success': 'False', 'data': []}, status=401)
from django.contrib.auth.models import User
from rest_framework import serializers

from django.db import connection
from django.http import JsonResponse


class UserSerializer(serializers):

    def my_data_view(request):
        with connection.cursor() as cursor:
            # Execute your raw SQL query
            cursor.execute("SELECT * FROM admin_users")

            # Fetch all the rows from the query result
            rows = cursor.fetchall()

            # Create a list to hold the serialized data
            serialized_data = []

            # Iterate over the rows and serialize each row
            for row in rows:
                data = {
                    'field1': row[3],
                    'field2': row[4],
                    # Add more fields as needed
                }
                serializer = UserSerializer(data)
                serialized_data.append(serializer.data)
                
                print(serialized_data)

        return JsonResponse(serialized_data, safe=False)
from flask_restful import Resource,Api
from flask import jsonify
from call_database import Connect # database connection will be called by function

# import psycopg2
# connection= psycopg2.connect(
#         host='localhost',
#         database='soluvv_1',
#         user='postgres',
#         password='9865197446',
#         port='5432'
#     )
#
# cur=connection.cursor()

#connection to database
cur=Connect()

class Count(Resource):
    def get(self,search_name):
        cur.execute(
            """select a.search_query,count(*) from dim_search_query a join  fact_spoonacular b on a.sid=b.sid where a.search_query=%s group by a.search_query""",
            [search_name])
        # cur.execute("""select a.search_query,count(*) from dim_search_query a join  fact_spoonacular bon a.sid=b.sid where a.search_query=%s group by a.search_query""",[name])
        read = cur.fetchall()
        if read == []:
            count = 0
            result = {
                "Ingredients_name": search_name,
                "count": count
            }
            return jsonify({"Lest's see":result})
        else:
            for lis in read:
                a = lis
                count = a[1]
                result = {
                    "Ingredients_name": search_name,
                    "count": count
                }
            return jsonify({"Lest's see":result})



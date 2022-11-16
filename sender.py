from flask import Flask, render_template, jsonify
from flask_restful import Resource, Api
from count import Count
from store_to_postgress import Send_to_Postgress

# import pika
# import psycopg2
# import os  # talend ko job run garna ko lagi

app = Flask(__name__)
api=Api(app)

# connection to db
# connection = psycopg2.connect(
#     host='localhost',
#     database='soluvv_1',
#     user='postgres',
#     password='9865197446',
#     port='5432'
# )
#
# cur = connection.cursor()


# class send_ingredient_to_postgress():
#     def __init__(self, name_of_ingredient):
#         self.name_of_the_ingredient = name_of_ingredient
#
#     def sending(self):
#         str_1 = self.name_of_the_ingredient
#
#         connect = pika.BlockingConnection(
#             pika.ConnectionParameters(host='localhost'))
#         channel = connect.channel()
#         channel.queue_declare(queue='hello')
#         channel.basic_publish(exchange='', routing_key='hello', body=str_1)
#         channel.queue_declare(queue='etlstart')
#         channel.basic_publish(exchange='', routing_key='hello', body='Hello Etl Start !!!')
#         connect.close()

@app.route("/")
def hello_world():
    return render_template("index.html")  # yeti garda ni templates directory bitra gaera index.html ma access garxa because of render_tempalte hai


# @app.route('/count/<name>')
# def counting_the_ingredient(name):
#     cur.execute("""select a.search_query,count(*) from dim_search_query a join  fact_spoonacular b on a.sid=b.sid where a.search_query=%s group by a.search_query""",[name])
#     # cur.execute("""select a.search_query,count(*) from dim_search_query a join  fact_spoonacular bon a.sid=b.sid where a.search_query=%s group by a.search_query""",[name])
#     read = cur.fetchall()
#     if read == []:
#         count = 0
#         result = {
#             "Ingredients_name": name,
#             "count": count
#         }
#         return result
#     else:
#         for lis in read:
#             a = lis
#             count = a[1]
#             result = {
#                 "Ingredients_name": name,
#                 "count": count
#             }
#         return result
#

 # Endpoints and Resources
api.add_resource(Count, '/count/<string:search_name>')
api.add_resource(Send_to_Postgress,'/send/<string:name_of_the_ingredient>')

# @app.route('/send/<name>')
# def sending(name):
#     s1 = send_ingredient_to_postgress(name)
#     s1.sending()
#     return name + " is send for the check in our list"


# @app.route('/etl_start')
# def Start_etl():
#     os.startfile("Task_1_0.1\Task_1\Task_1_run.bat")
#     return render_template("complete.html")

if __name__ == "__main__":  # hamro program call garnu nabparna ko lagi yo run gareko ho
    app.run(debug=True)  # hami lai port number change garnu parye ko khanda ma cahi (debug=True,port=8000)garney



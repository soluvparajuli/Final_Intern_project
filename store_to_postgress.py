from flask_restful import Resource,Api
import pika


class Send_to_Postgress(Resource):
    def get(self,name_of_the_ingredient):

    # def __init__(self, name_of_ingredient):
    #     self.name_of_the_ingredient = name_of_ingredient
    #
    # def sending(self):
        connect = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connect.channel()
        channel.queue_declare(queue='hello')
        channel.basic_publish(exchange='', routing_key='hello', body=name_of_the_ingredient)
        channel.queue_declare(queue='etlstart')
        channel.basic_publish(exchange='', routing_key='hello', body='Hello Etl Start !!!')
        connect.close()
        return name_of_the_ingredient+ " is searched and saved to postgress"
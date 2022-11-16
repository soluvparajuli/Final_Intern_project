# import pika, sys, os
# import requests
# import json
# import csv
# from config import config
# apikey = config.api_key
# from Templates import api_call1
#
# class get_recipe_by_ingredient:
#     def __init__(self, name_of_the_ingredient):
#         self.name_of_the_ingredient = name_of_the_ingredient
#
#     def run_api(self):
#         payload = {
#             'ingredients': self.name_of_the_ingredient,
#             'number': 2,
#             # can be changed according to required number of receipe we are getting only 2 receipe for now
#             'ranking': 1  # ranking is done by system , I am unknown about the ranking
#         }
#         endpoint = "https://api.spoonacular.com/recipes/findByIngredients"
#         headers = {
#             'x-api-key': apikey
#         }
#         try:
#             observation = requests.get(endpoint, params=payload, headers=headers)
#             observation = observation.json()
#             if len(observation) > 0:
#                 print("run api completed")
#                 return observation
#             else:
#                 print("run completed but failed")
#                 pass
#         except:
#             print("Provide ingredient is not in our any receipe")
#
# # def api_call(name_of_ingredient):
# #     response=api_call(name_of_ingredient)
#
# class convert_observation_to_json_file:
#     def __init__(self, input_for_json_file):
#         self.json_file = input_for_json_file
#
#     def conversion_into_json_file(self):
#         s = json.dumps(self.json_file)
#         with open(".\jsonfiles\data1.json", 'w') as f:
#             f.write(s)
#
#
# # child class to get name of the ingredient
# class convert_json_file_to_csv_file(get_recipe_by_ingredient):
#     def __init__(self, json_file, name_of_the_ingredient):
#         super().__init__(name_of_the_ingredient)
#         self.json_file = json_file
#
#     def converting_into_csv_file(self):
#         missed = "Missed"
#         used = "Used"
#         for obser in self.json_file:
#             for missIngre in obser['missedIngredients']:
#                 fieldnames = ['Search_Query', 'Recipe_id', 'title', 'usedIngredientCount', 'missedIngredientCount',
#                               'ingredients_id', 'ingredients_name', 'aisle', 'MissedorUsed', 'amount', 'unit']
#                 rows = [
#                     {'Search_Query': self.name_of_the_ingredient,
#                      'Recipe_id': obser['id'],
#                      'title': obser['title'],
#                      'usedIngredientCount': obser['usedIngredientCount'],
#                      'missedIngredientCount': obser['missedIngredientCount'],
#                      'ingredients_id': missIngre['id'],
#                      'ingredients_name': missIngre['name'],
#                      'aisle': missIngre['aisle'],
#                      'MissedorUsed': missed,
#                      'amount': missIngre['amount'],
#                      'unit': missIngre['unit']
#                      }
#                 ]
#
#                 with open('./csvfiles/Final.csv', 'r') as infocsv:
#                     reader = [i for i in csv.DictReader(infocsv)]
#                     if len(reader) > 0:
#                         pass
#                     else:
#                         header = ['Search_Query', 'Recipe_id', 'title', 'usedIngredientCount', 'missedIngredientCount',
#                                   'ingredients_id', 'ingredients_name', 'aisle', 'MissedorUsed', 'amount', 'unit']
#                         with open('./csvfiles/Final.csv', 'a', newline='') as f:
#                             dw = csv.DictWriter(f, delimiter=',', fieldnames=header)
#                             dw.writeheader()
#                 with open('./csvfiles/Final.csv', 'a', newline='') as f:
#                     writer = csv.DictWriter(f, fieldnames=fieldnames)
#                     writer.writerows(rows)
#
#             for usedIngre in obser['usedIngredients']:
#                 fieldnames = ['Search_Query', 'Recipe_id', 'title', 'usedIngredientCount', 'missedIngredientCount',
#                               'ingredients_id', 'ingredients_name', 'aisle', 'MissedorUsed', 'amount', 'unit']
#                 rows = [
#                     {'Search_Query': self.name_of_the_ingredient,
#                      'Recipe_id': obser['id'],
#                      'title': obser['title'],
#                      'usedIngredientCount': obser['usedIngredientCount'],
#                      'missedIngredientCount': obser['missedIngredientCount'],
#                      'ingredients_id': usedIngre['id'],
#                      'ingredients_name': usedIngre['name'],
#                      'aisle': usedIngre['aisle'],
#                      'MissedorUsed': used,
#                      'amount': usedIngre['amount'],
#                      'unit': usedIngre['unit']
#                      }
#                 ]
#                 with open('./csvfiles/Final.csv', 'a', newline='') as f:
#                     writer = csv.DictWriter(f, fieldnames=fieldnames)
#                     writer.writerows(rows)
#
#
# def main():
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
#     channel = connection.channel()
#     channel.queue_declare(queue="hello")
#
#     def callback(ch, method, properties, body):
#         name_of_ingredient = body.decode('utf-8')
#         string_of_the_ingredient = name_of_ingredient
#         r1=get_recipe_by_ingredient(string_of_the_ingredient)
#         input_for_json=r1.run_api()
#         print(input_for_json)
#         if input_for_json is not None:
#             c1 = convert_observation_to_json_file(input_for_json)
#             c1.conversion_into_json_file()
#             f = open('./jsonfiles/data1.json')  # open a json file
#             data = json.load(f)
#             print(data)
#             csv_file_generator: convert_json_file_to_csv_file = convert_json_file_to_csv_file(data, name_of_ingredient)
#             csv_file_generator.converting_into_csv_file()
#             print("completed")
#         # print(string_of_the_ingredient)
#         else:
#             print("Invalid search")
#             pass
#
#     channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)
#     print(" [*] Waiting for messages. To exit press CTRL+C ")
#     channel.start_consuming()
#
#
# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os.exit(0)
#

import pika, sys, os
import json
import csv
from config import config
apikey = config.api_key
from Templates import api_call1
# import requests

# class get_recipe_by_ingredient:
#     def __init__(self, name_of_the_ingredient):
#         self.name_of_the_ingredient = name_of_the_ingredient
#
#     def run_api(self):
#         payload = {
#             'ingredients': self.name_of_the_ingredient,
#             'number': 2,
#             # can be changed according to required number of receipe we are getting only 2 receipe for now
#             'ranking': 1  # ranking is done by system , I am unknown about the ranking
#         }
#         endpoint = "https://api.spoonacular.com/recipes/findByIngredients"
#         headers = {
#             'x-api-key': apikey
#         }
#         try:
#             observation = requests.get(endpoint, params=payload, headers=headers)
#             observation = observation.json()
#             if len(observation) > 0:
#                 print("run api completed")
#                 return observation
#             else:
#                 print("run completed but failed")
#                 pass
#         except:
#             print("Provide ingredient is not in our any receipe")

# def api_call(name_of_ingredient):
#     response=api_call(name_of_ingredient)

class convert:
    def __init__(self,observation,name_of_the_ingredient):
        self.json_file = observation
        self.name_of_the_ingredient=name_of_the_ingredient

    def conversion_into_json_file(self):
        s = json.dumps(self.json_file)
        with open(".\jsonfiles\data1.json", 'w') as f:
            f.write(s)

    def converting_into_csv_file(self):
        f = open('./jsonfiles/data1.json')  # open a json file
        data = json.load(f)
        missed = "Missed"
        used = "Used"
        for obser in data:
            for missIngre in obser['missedIngredients']:
                fieldnames = ['Search_Query', 'Recipe_id', 'title', 'usedIngredientCount', 'missedIngredientCount',
                              'ingredients_id', 'ingredients_name', 'aisle', 'MissedorUsed', 'amount', 'unit']
                rows = [
                    {'Search_Query': self.name_of_the_ingredient,
                     'Recipe_id': obser['id'],
                     'title': obser['title'],
                     'usedIngredientCount': obser['usedIngredientCount'],
                     'missedIngredientCount': obser['missedIngredientCount'],
                     'ingredients_id': missIngre['id'],
                     'ingredients_name': missIngre['name'],
                     'aisle': missIngre['aisle'],
                     'MissedorUsed': missed,
                     'amount': missIngre['amount'],
                     'unit': missIngre['unit']
                     }
                ]

                with open('./csvfiles/Final.csv', 'r') as infocsv:
                    reader = [i for i in csv.DictReader(infocsv)]
                    if len(reader) > 0:
                        pass
                    else:
                        header = ['Search_Query', 'Recipe_id', 'title', 'usedIngredientCount', 'missedIngredientCount',
                                  'ingredients_id', 'ingredients_name', 'aisle', 'MissedorUsed', 'amount', 'unit']
                        with open('./csvfiles/Final.csv', 'a', newline='') as f:
                            dw = csv.DictWriter(f, delimiter=',', fieldnames=header)
                            dw.writeheader()
                with open('./csvfiles/Final.csv', 'a', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writerows(rows)

            for usedIngre in obser['usedIngredients']:
                fieldnames = ['Search_Query', 'Recipe_id', 'title', 'usedIngredientCount', 'missedIngredientCount',
                              'ingredients_id', 'ingredients_name', 'aisle', 'MissedorUsed', 'amount', 'unit']
                rows = [
                    {'Search_Query': self.name_of_the_ingredient,
                     'Recipe_id': obser['id'],
                     'title': obser['title'],
                     'usedIngredientCount': obser['usedIngredientCount'],
                     'missedIngredientCount': obser['missedIngredientCount'],
                     'ingredients_id': usedIngre['id'],
                     'ingredients_name': usedIngre['name'],
                     'aisle': usedIngre['aisle'],
                     'MissedorUsed': used,
                     'amount': usedIngre['amount'],
                     'unit': usedIngre['unit']
                     }
                ]
                with open('./csvfiles/Final.csv', 'a', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writerows(rows)


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue="hello")

    def callback(ch, method, properties, body):
        name_of_ingredient = body.decode('utf-8')
        string_of_the_ingredient = name_of_ingredient
        # r1=get_recipe_by_ingredient(string_of_the_ingredient)
        input_for_json=api_call1.api_call1(string_of_the_ingredient)
        print(input_for_json)
        # print(string_of_the_ingredient)
        if input_for_json is None:
            # print("Invalid search")
            pass
        else:
            f = open('./jsonfiles/data1.json')  # open a json file
            data = json.load(f)
            c1 = convert(input_for_json,name_of_ingredient)
            c1.conversion_into_json_file()
            c1.converting_into_csv_file()
            print("completed")

    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)
    print(" [*] Waiting for messages. To exit press CTRL+C ")
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os.exit(0)

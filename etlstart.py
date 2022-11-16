import pika, sys, os
import time
def main():
    connection = pika.BlockingConnection (pika.ConnectionParameters (host= 'localhost') )
    channel = connection. channel()
    channel.queue_declare ( queue="etlstart")
    def callback( ch, method, properties , body):
        os.startfile("Task_1_0.1\Task_1\Task_1_run.bat")
        print(" [x] Received %r" %body)
        starttime=time.time()
        print(starttime)
    channel. basic_consume ( queue= "hello", on_message_callback=callback, auto_ack=True)

    print(" [*] Waiting for messages. To exit press CTRL+C ")
    channel. start_consuming ( )
if __name__ == '__main__':
    try:
        main ()
    except KeyboardInterrupt :
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit :
            os.exit(0)
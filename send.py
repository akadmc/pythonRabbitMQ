# pika package required
import pika

# wait for connection before continuing 
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
# get the channel class
channel = connection.channel()
# declare the rabbitMQ queue, create if neccesary. 
channel.queue_declare(queue='test_queue')
# publish message to an queue
# routing_key = queue
# body is message
channel.basic_publish(exchange='',
                      routing_key='test_queue',
                      body='wait a minute mr postman')

# notify and close connection
print("Message Sent")
connection.close()
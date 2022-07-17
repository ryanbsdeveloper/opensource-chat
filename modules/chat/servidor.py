from time import sleep
import pika
import ssl
import json
import os

BASE_DIR = os.path.dirname(__file__)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')

url = f"amqps://ryanl:842684265santos@b-b86d75fd-5111-4c3c-b62c-b999e666760a.mq.us-east-1.amazonaws.com:5671"
parameters = pika.URLParameters(url)
parameters.ssl_options = pika.SSLOptions(context=ssl_context)

conexão = pika.BlockingConnection(parameters)
canal = conexão.channel()

canal.exchange_declare(exchange='chat', exchange_type='direct')
canal.queue_declare(queue='mensagens', exclusive=True)
canal.queue_bind(queue='mensagens', exchange='chat', routing_key='tag_mensagem')

# global saida
# saida = 'nada'
n = 0
def callback(ch, method, properties, body):
    global n
    with open(f'{BASE_DIR}/mensagens.txt', 'w') as file:
        file.write(f'{str(json.dumps(body))}')
    n += 1
    
# def reply():
#     while True:
#         print(saida)
#         sleep(1)

canal.basic_consume(queue='mensagens', on_message_callback=callback, auto_ack=True)
canal.start_consuming() 

# t1 = threading.Thread(target=consuming)
# t2 = threading.Thread(target=reply)
# t1.start()
# t2.start()

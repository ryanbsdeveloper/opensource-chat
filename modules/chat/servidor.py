import pika
import ssl
import json
import os

class Servidor:
    def __init__(self) -> None:
        self.BASE_DIR = os.path.dirname(__file__)

        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')

        url = f"amqps://ryanl:842684265santos@b-b86d75fd-5111-4c3c-b62c-b999e666760a.mq.us-east-1.amazonaws.com:5671"
        parameters = pika.URLParameters(url)
        parameters.ssl_options = pika.SSLOptions(context=ssl_context)

        conexão = pika.BlockingConnection(parameters)
        self.canal = conexão.channel()

        self.canal.exchange_declare(exchange='chat', exchange_type='direct')
        self.canal.queue_declare(queue='mensagens', exclusive=True)
        self.canal.queue_bind(queue='mensagens', exchange='chat', routing_key='tag_mensagem')


    def callback(self, ch, method, properties, body):
        with open(f'{self.BASE_DIR}/mensagens.txt', 'w') as file:
            file.write(f'{json.loads(body)}')
        
    def consuming(self):
        self.canal.basic_consume(queue='mensagens', on_message_callback=self.callback, auto_ack=True)
        self.canal.start_consuming() 


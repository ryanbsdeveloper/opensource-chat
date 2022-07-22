import pika
import ssl
import json


class Dev:
    def __init__(self):
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        ssl_context.set_ciphers('ECDHE+AESGCM:!ECDSA')

<<<<<<< HEAD
        url = f"url"
=======
        url = f"amqps://ryanl:842684265santos@b-b86d75fd-5111-4c3c-b62c-b999e666760a.mq.us-east-1.amazonaws.com:5671"
>>>>>>> f9fa71c (update)
        parameters = pika.URLParameters(url)
        parameters.ssl_options = pika.SSLOptions(context=ssl_context)

        conexão = pika.BlockingConnection(parameters)
        self.canal = conexão.channel()

    def send(self, nome: str, logo: str, message: str, hora: str):

        mensagem = json.dumps(
            {"nome": nome, "logo": logo, "hora": hora, "mensagem": message})

        self.canal.basic_publish(exchange='chat', body=mensagem, routing_key='tag_mensagem',
                                 properties=pika.BasicProperties(delivery_mode=2))
        self.canal.close()
<<<<<<< HEAD
=======


# cliente = Dev()
# cliente.send("fredekel", "java", "Boa tio, ficou show de bola!", "18:43")
>>>>>>> f9fa71c (update)

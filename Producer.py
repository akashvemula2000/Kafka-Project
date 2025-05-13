from confluent_kafka import Producer

if __name__ == "__main__":

    config = {
        'bootstrap.servers': 'pkc-921jm.us-east-2.aws.confluent.cloud:9092',
        'sasl.username': 'BHIOBX5IW2HJQIWD',
        'sasl.password': 'qu2EWK9jBAO6a8woDzzI0C0CeZgkJ6AuvBFzHaLos4R8lk9xIb0vSFyp5SHHw19b',
        'client.id' : 'FirstProducer',
        'security.protocol': 'SASL_SSL',
        'sasl.mechanisms':   'PLAIN',
        'acks': 'all'
    }

    prod = Producer(config)

    topic = 'topic_0'

    prod.produce(topic,'value1','key1')

    prod.flush()
from kafka.admin import KafkaAdminClient, NewTopic

# define topic settings
topic_name = "my_topic1"
num_partitions = 1
replication_factor = 1

# create KafkaAdminClient instance
admin_client = KafkaAdminClient(
    bootstrap_servers=["localhost:9092"]
)

# create new topic
new_topic = NewTopic(
    name=topic_name, 
    num_partitions=num_partitions, 
    replication_factor=replication_factor
)

# create topic using KafkaAdminClient
admin_client.create_topics(new_topics=[new_topic])

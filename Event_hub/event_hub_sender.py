import uuid
import datetime
import random
import json
from azure.servicebus import ServiceBusService

key_name = 'RootManageSharedAccessKey' # SharedAccessKeyName from Azure portal
key_value = 'peKJmccVkBUaOJzMRQfcz/K5g5QJc2jWSbQJhvlAhNA=' # SharedAccessKey from Azure portal
sbs = ServiceBusService('hms-poc',
                        shared_access_key_name=key_name,
                        shared_access_key_value=key_value)
devices = []
for x in range(0, 10):
   devices.append(str(uuid.uuid4()))

for y in range(0,20):
   for dev in devices:
       reading = {'id': dev, 'timestamp': str(datetime.datetime.utcnow()), 'mess_id':y, 'random_number1': random.randint(70, 100), 'random_number2': random.randint(70, 100)}
       s = json.dumps(reading)
       sbs.send_event('hmsdev', s)
   print (y)
   
   
   
   
#SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=peKJmccVkBUaOJzMRQfcz/K5g5QJc2jWSbQJhvlAhNA=
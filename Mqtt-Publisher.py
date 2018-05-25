import paho.mqtt.client as mqttClient
import time
 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected               
        Connected = True               
 
    else:
 
        print("Connection failed")
 
Connected = False   
 
broker_address= ""
port = 
user = ""
password = ""
 
client = mqttClient.Client("MqttClient")             
client.username_pw_set(user, password=password)   
client.on_connect= on_connect                      
client.connect(broker_address, port=port)          
 
client.loop_start()        
 
while Connected != True:    
    time.sleep(0.1)
 
try:
    while True:
 
        value = raw_input('Enter the message:')
        client.publish("sesnor/temp",value)
 
except KeyboardInterrupt:
 
    client.disconnect()
    client.loop_stop()

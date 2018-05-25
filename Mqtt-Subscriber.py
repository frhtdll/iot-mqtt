import paho.mqtt.client as mqttClient
import time
 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                
        Connected = True                
 
    else:
 
        print("Connection failed")
 
def on_message(client, userdata, message):
    print "Message received: "  + message.payload
 
Connected = False   
 
broker_address= ""  			
port =                          
user = ""                   	
passwd = ""          			
 
client = mqttClient.Client("Subscriber")               
client.username_pw_set(user, passwd=passwd)    
client.on_connect= on_connect                      
client.on_message= on_message                      
 
client.connect(broker_address, port=port)         
 
client.loop_start()        
 
while Connected != True:    
    time.sleep(0.1)
 
client.subscribe("temp/50")
 
try:
    while True:
        time.sleep(1)
 
except KeyboardInterrupt:
    print "exiting"
    client.disconnect()
    client.loop_stop()
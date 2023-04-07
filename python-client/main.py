# https://pypi.org/project/paho-mqtt/#usage-and-api

import paho.mqtt.client as mqtt

mqtt = mqtt.Client(client_id="", clean_session=True, userdata=None, protocol="MQTTv311", transport="tcp")

# connect 전 설정해야하는 옵션
mqtt.enable_logger(logger=None)
mqtt.user_data_set("데이터 전송!")

def on_connect(client, userdata, flags, rc):
    print("연결 성공!")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("연결 해제!")

def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)

mqtt.on_connect = on_connect
mqtt.on_disconnect = on_disconnect
mqtt.on_publish = on_publish

mqtt.connect("localhost", port=1883, keepalive=60, bind_address="")

mqtt.publish("apple", payload=None, qos=0, retain=False)

mqtt.disconnect()
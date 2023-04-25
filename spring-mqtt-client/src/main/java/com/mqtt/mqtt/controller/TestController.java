package com.mqtt.mqtt.controller;

import com.mqtt.mqtt.config.MqttConfig;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
public class TestController {

    private final MqttConfig.OutboundGateway outboundGateway;

    @GetMapping("/")
    public void mqttTest(){
        outboundGateway.sendToMqtt("안뇽 ㅎㅎ", "test_topic");
    }
}

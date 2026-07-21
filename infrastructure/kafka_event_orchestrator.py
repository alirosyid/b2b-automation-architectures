def publish_to_kafka_topic(topic, payload):
    print(f"[Infra] Publishing event payload to distributed Kafka topic: {topic}")
    
    # Mocking Kafka Producer
    encoded_payload = str(payload).encode('utf-8')
    print(f"    -> Serialized {len(encoded_payload)} bytes. Dispatching to broker...")
    
    # producer.send(topic, encoded_payload)
    print(f"[+] Event successfully distributed. Downstream consumer groups (CRM, Outreach) alerted asynchronously.")
    return True

if __name__ == "__main__":
    mock_lead_eval = {"status": "FIT", "score": 95, "company": "Stark Industries"}
    publish_to_kafka_topic("b2b.leads.evaluated", mock_lead_eval)

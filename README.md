# Event-Driven Data Pipeline with GCP Pub/Sub

This project demonstrates an event-driven microservice pipeline built using
Google Cloud Run, Pub/Sub messaging, and containerized Python services.

# Event Driven Data Pipeline with GCP Pub/Sub

This project demonstrates an event-driven microservice pipeline built on Google Cloud Platform.

The system uses Pub/Sub messaging to decouple services and Cloud Run to host containerized Python microservices.

## Architecture
```
Client Request
      |
      v
Publisher Service (Cloud Run)
      |
      v
Pub/Sub Topic
      |
      v
Push Subscription
      |
      v
Subscriber Service (Cloud Run)
```
## Message Flow

1. A client sends a POST request to the publisher service.
2. The publisher publishes the message to a Pub/Sub topic.
3. Pub/Sub delivers the message to the push subscription.
4. The subscriber service receives the message and processes it.

## Technologies

Python  
Flask  
Docker  
Google Cloud Run  
Google Cloud Pub/Sub  

## Publisher

The publisher service exposes a REST endpoint `/publish`.

When a POST request is sent to this endpoint, the service publishes a message to a Pub/Sub topic.

## Subscriber

The subscriber service receives Pub/Sub push messages and decodes the base64 payload.

Messages are logged in Cloud Run logs.

## Deployment Steps

Create topic

`gcloud pubsub topics create demo-topic` 

Deploy services

`gcloud run deploy publisher-svc`
`gcloud run deploy subscriber-svc`


Create push subscription
`gcloud pubsub subscriptions create demo-sub`
`--topic demo-topic`
`--push-endpoint=<subscriber-url>`


Send test message
`curl -X POST <publisher-url>/publish`
`-H "Content-Type: application/json"`
`-d '{"text":"pipeline test"}'`



## Result

Messages published by the publisher service are delivered asynchronously to the subscriber service through Pub/Sub.



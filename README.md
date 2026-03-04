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








































                  [ Read 2 lines (converted from DOS format) ]
^G Help      ^O Write Out ^F Where Is  ^K Cut       ^T Execute   ^C Location
^X Exit      ^R Read File ^\ Replace   ^U Paste     ^J Justify   ^/ Go To Line


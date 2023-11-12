## MICROSERVICE ACCESSIBLE WITH NODE.JS & DOCKER / PM2
An example of microservices implementation of a restaurant that process orders and deliveries.

## Requeriments
- Docker
- PM2
<p align="center" style="margin-bottom: 0px !important;">
  <img width="550"  src="images/requirements.png" align="center">
</p>

## Quickstart
### Docker - Developing mode, live-reload changes
```
cd "Microservice Restaurant"
docker-compose up
```

### PM2 - Production process manager,  manage and keep an application online
```
pm2 start food.json
pm2 plus  (this runs the Monitoring Web Interface)
```

const express = require('express')
const bodyParser = require('body-parser')  //body parsing middleware module
const cote = require('cote')  //Zero-configuration microservices module
const axios = require('axios')  //HTTP client module


const app = express()  //create app
app.use(bodyParser.json())  //define the reader type

//requesters for each service (restaurants, orders, deliveries)
const restaurantsRequester = new cote.Requester({ name: 'restaurants requester', key: 'restaurants' })

const orderRequester = new cote.Requester({ name: 'order requester', key: 'orders' })

const deliveryRequester = new cote.Requester({ name: 'delivery requester', key: 'deliveries' })

//get the restaurants registered
app.get('/restaurants', async (req, res) => {
    const restaurants = await restaurantsRequester.send({ type: 'list' }) //get restaurants info
    res.send(restaurants);
})

//create the orders and the deliveries
app.post('/order', async (req, res) => {
    const order = await orderRequester.send({ type: 'create order', order: req.body })
    const delivery = await deliveryRequester.send({ type: 'create delivery', order })

    res.send({ order, delivery })
})

//prints a log once starts listening
app.listen(3000, () => console.log('listening'))

const cote = require('cote')  //Zero-configuration microservices module

//create the responder for the delivery request
const deliveryResponder = new cote.Responder({ name: 'delivery responder', key: 'deliveries' })
deliveryResponder.on('*', req => req.type && console.log(req))

const deliveries = []
let idCounter = 0

//create a delivery and saves it in a list
deliveryResponder.on('create delivery', req => {
    const delivery = { id: idCounter++, orderId: req.order.id, eta: 30, status: 'pending' }

    deliveries.push(delivery)  //saves
    return Promise.resolve(delivery)  //return the delivery request
})

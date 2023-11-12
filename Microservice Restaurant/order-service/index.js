const cote = require('cote')  //Zero-configuration microservices module

//create the responder for the order request
const orderResponder = new cote.Responder({ name: 'order responder', key: 'orders' })
orderResponder.on('*', req => req.type && console.log(req))

const orders = []
let idCounter = 0

//create an order and saves it in a list
orderResponder.on('create order', req => {
    const order = { id: idCounter++, ...req.order, status: 'preparing' }

    orders.push(order)  //saves
    return Promise.resolve(order)  //returns the order request
})

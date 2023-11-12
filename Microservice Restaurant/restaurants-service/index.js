const cote = require('cote')  //Zero-configuration microservices module

//create the responder for the restaurants request
const restaurantsResponder = new cote.Responder({ name: 'restaurants responder', key: 'restaurants' })
restaurantsResponder.on('*', req => req.type && console.log(req))

//Registered restaurants available for "ordering"
const restaurants = [{
    id: 0,
    name: 'Italian Restaurant',
    menu: [{
        id: 0,
        name: 'Pizza',
        price: 14
    }, {
        id: 1,
        name: 'Pasta',
        price: 12
    }]
}, {
    id: 1,
    name: 'American Restaurant',
    menu: [{
        id: 0,
        name: 'Hamburger',
        price: 10
    }, {
        id: 1,
        name: 'Hot dog',
        price: 10
    }]
}]

//prints a log with the info of the restaurants when requested
restaurantsResponder.on(req => req.type && console.log(req))
restaurantsResponder.on('list', req => Promise.resolve(restaurants)) //returns the restaurants request
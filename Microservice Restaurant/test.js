const axios = require('axios')  //HTTP client module

async function main() {
  const restaurants = await axios.get('http://localhost:3000/restaurants')  //access to the service restaurants
  console.log(restaurants.data)  //print the restaurants information

  const orderRequest = {  //sends a order request
    restaurantId: 1,
    menuId: 1,
    address: 'Wall Street 3, 68443'
  }

  //access to the service orders and gives the order created
  const order = await axios.post('http://localhost:3000/order', orderRequest)  
  console.log(order.data)  //print the order information
}

main()
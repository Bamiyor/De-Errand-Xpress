const cartItems = [
    { name: 'Vegetables', description: 'Fresh and organic vegetables', price: 5.00, quantity: 0, image: '/static/images/cart-vegetable.jpg' },
    { name: 'Tomatoes', description: 'Red tomatoes', price: 3.00, quantity: 0, image: '/static/images/cart-Tomato.jpg' },
    { name: 'Onions', description: 'Fresh onions', price: 2.00, quantity: 0, image: '/static/images/cart-onions.jpg' },
    { name: 'Groundnut Oil', description: 'Groundnut oil', price: 8.00, quantity: 0, image: '/static/images/cart-oils.jpg' },
    { name: 'Rice', description: 'Long grain rice', price: 20.00, quantity: 0, image: '/static/images/cart-rice.jpg' },
    { name: 'Beans', description: 'Beans', price: 8.00, quantity: 0, image: '/static/images/cart-Beans.jpg' },
    { name: 'Garri', description: 'Garri', price: 7.00, quantity: 0, image: '/static/images/cart-garri.jpg' },
    { name: 'Apple', description: 'Apple', price: 2.00, quantity: 0, image: '/static/images/cart-apple.jpg' },
    { name: 'Yam', description: 'Yam', price: 5.00, quantity: 0, image: '/static/images/cart-Yam-Export.jpg' },
    { name: 'Cabbage', description: 'Cabbage', price: 5.00, quantity: 0, image: '/static/images/cart-cabbage.jpg' },
    { name: 'Chicken', description: 'Chicken', price: 5.00, quantity: 0, image: '/static/images/cart-chicken.jpg' },
    { name: 'Orange', description: 'Orange', price: 2.00, quantity: 0, image: '/static/images/cart-orange.jpg' },
    { name: 'Irish Potato', description: 'Irish Potato', price: 5.00, quantity: 0, image: '/static/images/cart-irish-potato.jpg' }
];

const cartContainer = document.querySelector('.cart-items');
const subtotalElement = document.querySelector('.subtotal');

function updateSubtotal() {
    const subtotal = cartItems.reduce((acc, item) => acc + (item.price * item.quantity), 0);
    subtotalElement.textContent = `Subtotal: $${subtotal.toFixed(2)}`;
}

function renderCartItems() {
    cartContainer.innerHTML = '';
    cartItems.forEach((item, index) => {
        const cartItem = document.createElement('div');
        cartItem.className = 'cart-item';

        cartItem.innerHTML = `
            <img src="${item.image}" alt="${item.name}" class="item-image">
            <div class="item-details">
                <h2 class="item-name">${item.name}</h2>
                <p class="item-description">${item.description}</p>
                <p class="item-price">$${item.price.toFixed(2)}</p>
                <div class="item-quantity">
                    <button class="quantity-btn" onclick="updateQuantity(${index}, -1)">-</button>
                    <input type="number" value="${item.quantity}" min="1" class="quantity-input" onchange="changeQuantity(${index}, event)">
                    <button class="quantity-btn" onclick="updateQuantity(${index}, 1)">+</button>
                </div>
            </div>
        `;
        cartContainer.appendChild(cartItem);
    });
    updateSubtotal();
}

function updateQuantity(index, change) {
    const item = cartItems[index];
    item.quantity = Math.max(1, item.quantity + change);
    renderCartItems();
}

function changeQuantity(index, event) {
    const item = cartItems[index];
    const newQuantity = parseInt(event.target.value);
    item.quantity = isNaN(newQuantity) || newQuantity < 1 ? 1 : newQuantity;
    renderCartItems();
}

document.addEventListener('DOMContentLoaded', renderCartItems);


// Function to fetch cart items
function fetchCartItems() {
    fetch('/cart')
      .then(response => response.json())
      .then(data => {
        const cartItems = document.querySelector('.cart-items');
        cartItems.innerHTML = '';
  
        data.forEach(item => {
          const cartItem = document.createElement('div');
          cartItem.classList.add('cart-item');
  
          const itemName = document.createElement('h3');
          itemName.textContent = item.name;
  
          const itemPrice = document.createElement('p');
          itemPrice.textContent = `Price: $${item.price}`;
  
          const itemQuantity = document.createElement('p');
          itemQuantity.textContent = `Quantity: ${item.quantity}`;
  
          cartItem.appendChild(itemName);
          cartItem.appendChild(itemPrice);
          cartItem.appendChild(itemQuantity);
  
          cartItems.appendChild(cartItem);
        });
  
        updateSubtotal(data);
      })
      .catch(error => console.error('Error:', error));
  }
  
  // Function to update the subtotal
  function updateSubtotal(cartItems) {
    const subtotal = cartItems.reduce((total, item) => total + item.price * item.quantity, 0);
    const subtotalElement = document.querySelector('.subtotal');
    subtotalElement.textContent = `Subtotal: $${subtotal.toFixed(2)}`;
  }
  
  // Call fetchCartItems on page load
  window.addEventListener('load', fetchCartItems);

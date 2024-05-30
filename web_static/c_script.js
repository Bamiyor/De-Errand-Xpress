const cartItems = [
    { name: 'Vegetables', description: 'Fresh and organic vegetables', price: 5.00, quantity: 0, image: '/web_static/images/cart-vegitable.jpg' },
    { name: 'Tomatoes', description: 'Red tomatoes', price: 3.00, quantity: 0, image: '/web_static/images/cart-Tomato.jpg' },
    { name: 'Onions', description: 'Fresh onions', price: 2.00, quantity: 0, image: '/web_static/images/cart-onios.jpg' },
    { name: 'Groundnut Oil', description: 'Groundnut oil', price: 8.00, quantity: 0, image: '/web_static/images/cart-oils.jpg' },
    { name: 'Rice', description: 'Long grain rice', price: 20.00, quantity: 0, image: '/web_static/images/cart-rice.jpg' },
    { name: 'Beans', description: 'Beans', price: 8.00, quantity: 0, image: '/web_static/images/cart-Beans.jpg' },
    { name: 'Gari', description: 'Gari', price: 7.00, quantity: 0, image: '/web_static/images/cart-gari.jpg' },
    { name: 'Apple', description: 'Apple', price: 2.00, quantity: 0, image: '/web_static/images/cart-apple.jpg' },
    { name: 'Yam', description: 'Yam', price: 5.00, quantity: 0, image: '/web_static/images/cart-Yam-Export.jpg' },
    { name: 'Kabege', description: 'Kabege', price: 5.00, quantity: 0, image: '/web_static/images/cart-kabege.jpg' },
    { name: 'Chicken', description: 'Chicken', price: 5.00, quantity: 0, image: '/web_static/images/cart-chiken.jpg' },
    { name: 'Orange', description: 'Orange', price: 2.00, quantity: 0, image: '/web_static/images/cart-orange.jpg' },
    { name: 'Irish Potato', description: 'Irish Potato', price: 5.00, quantity: 0, image: '/web_static/images/cart-irish-potato.jpg' }
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

function removeItem(index) {
    cartItems.splice(index, 1);
    renderCartItems();
}

document.addEventListener('DOMContentLoaded', renderCartItems);
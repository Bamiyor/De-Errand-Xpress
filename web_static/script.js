const products = [
    { id: 1, name: 'Fresh Produce', url: 'product_fresh_produce.html' },
    { id: 2, name: 'Dairy Products', url: 'product_dairy_products.html' },
    { id: 3, name: 'Bakery Items', url: 'product_bakery_items.html' },
    { id: 4, name: 'Household Essentials', url: 'product_household_essentials.html' },
    { id: 5, name: 'Rice, Beans, and more', url: 'product.html#rice-beans' },
    { id: 6, name: 'Tomatoes, Pepe, and more', url: 'product.html#tomatoes-pepe' },
    { id: 7, name: 'Yam, Sweet Potato, and more', url: 'product.html#yam-sweet-potato' },
    { id: 8, name: 'Vegetables of all kinds', url: 'product.html#vegetables' },
    { id: 9, name: 'Cucumber, Cabbage, and more', url: 'product.html#cucumber-cabbage' },
    { id: 10, name: 'Onions, Carrots, and more', url: 'product.html#onions-carrots' },
    { id: 11, name: 'Oils, Chickens, and more', url: 'product.html#oils-chickens' },
    { id: 12, name: 'All Fruits', url: 'product.html#fruits' },
    { id: 13, name: 'All kinds of fishes', url: 'product.html#fishes' }
];

function searchProduct() {
    const input = document.getElementById('searchInput').value.toLowerCase();
    const result = products.find(product => product.name.toLowerCase().includes(input));

    if (result) {
        window.location.href = result.url;
    } else {
        alert('Product not found');
    }
}
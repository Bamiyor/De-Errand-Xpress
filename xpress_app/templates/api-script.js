// Function to fetch all products
function fetchProducts() {
    fetch('/products')
      .then(response => response.json())
      .then(data => {
        const productContainer = document.createElement('div');
        productContainer.classList.add('product-container');
  
        data.forEach(product => {
          const productCard = document.createElement('div');
          productCard.classList.add('product-card');
  
          const productName = document.createElement('h3');
          productName.textContent = product.name;
  
          const productPrice = document.createElement('p');
          productPrice.textContent = `Price: $${product.price}`;
  
          productCard.appendChild(productName);
          productCard.appendChild(productPrice);
          productContainer.appendChild(productCard);
        });
  
        const servicesSection = document.getElementById('services');
        servicesSection.appendChild(productContainer);
      })
      .catch(error => console.error('Error:', error));
  }
  
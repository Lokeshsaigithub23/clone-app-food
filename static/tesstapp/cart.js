document.addEventListener("DOMContentLoaded", () => {
    const cartContainer = document.getElementById("cart-items");
    const cartTotalEl = document.getElementById("cart-total");
    
    let cart = JSON.parse(localStorage.getItem("cart")) || [];

    function renderCart() {
        cartContainer.innerHTML = ""; 
        let total = 0;

        if (cart.length === 0) {
            cartContainer.innerHTML = "<p class='text-gray-600'>Your cart is empty.</p>";
        } else {
            cart.forEach((item, index) => {
                total += Number(item.price);
                const div = document.createElement("div");
                div.className = "flex justify-between items-center bg-white p-4 rounded shadow mb-2";
                div.innerHTML = `
                    <span>${item.name} - ₹${Number(item.price).toFixed(2)}</span>
                    <button class="bg-red-500 text-white hover:bg-red-600 px-3 py-1 rounded remove-btn" data-index="${index}">
                        Remove
                    </button>
                `;
                cartContainer.appendChild(div);
            });
        }

        cartTotalEl.textContent = total.toFixed(2);
        localStorage.setItem("cart", JSON.stringify(cart));
    }

    // Remove item from cart
    cartContainer.addEventListener("click", (e) => {
        if (e.target.classList.contains("remove-btn")) {
            const index = e.target.getAttribute("data-index");
            cart.splice(index, 1);
            renderCart(); // re-render dynamically without reload
        }
    });

    renderCart(); // Initial render
});

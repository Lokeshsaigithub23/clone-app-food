document.addEventListener("DOMContentLoaded", () => {
    const cartContainer = document.getElementById("cart-items");
    const cartTotalEl = document.getElementById("cart-total");
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    let total = 0;
    if (cart.length === 0) {
        cartContainer.innerHTML = "<p>Your cart is empty.</p>";
    } else {
        cartContainer.innerHTML = ""; 
        cart.forEach((item, index) => {
            total += item.price;
            const div = document.createElement("div");
            div.className = "flex justify-between items-center bg-white p-4 rounded shadow";
            div.innerHTML = `
                <span>${item.name} - ₹${item.price.toFixed(2)}</span>
                <button class="bg-red-400 hover:bg-red-500 px-3 py-1 rounded remove-btn" data-index="${index}">Remove</button>
            `;
            cartContainer.appendChild(div);
        });
    }
    cartTotalEl.textContent = total.toFixed(2);
    cartContainer.addEventListener("click", (e) => {
        if (e.target.classList.contains("remove-btn")) {
            const index = e.target.getAttribute("data-index");
            cart.splice(index, 1);
            localStorage.setItem("cart", JSON.stringify(cart));
            location.reload();
        }
    });
});

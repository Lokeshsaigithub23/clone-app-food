document.addEventListener("DOMContentLoaded", () => {    
    const buttons = document.querySelectorAll(".add-to-cart-btn");
    buttons.forEach(btn => {
        btn.addEventListener("click", () => {
            const id = btn.getAttribute("data-id");
            const name = btn.getAttribute("data-name");
            const price = parseFloat(btn.getAttribute("data-price"));

            let cart = JSON.parse(localStorage.getItem("cart")) || [];
            
            const existingItem = cart.find(item => item.id === id);
            if (existingItem) {
                alert(name + " is already in the cart!");
                return;
            }
            cart.push({id, name, price});
            localStorage.setItem("cart", JSON.stringify(cart));
            alert(name + " added to cart!");
        });
    });
    const addAllBtn = document.getElementById("add-restaurant-cart");
    if(addAllBtn){
        addAllBtn.addEventListener("click", () => {
            let cart = JSON.parse(localStorage.getItem("cart")) || [];
            const menuItems = document.querySelectorAll("#menu-list .add-to-cart-btn");
            menuItems.forEach(btn => {
                const id = btn.getAttribute("data-id");
                const name = btn.getAttribute("data-name");
                const price = parseFloat(btn.getAttribute("data-price"));

                if (!cart.find(item => item.id === id)) {
                    cart.push({id, name, price});
                }
            });
            localStorage.setItem("cart", JSON.stringify(cart));
            alert("All items added to cart!");
        });
    }
});

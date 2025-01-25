


document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.add-to-cart');
    buttons.forEach(button => {
        button.addEventListener('click', event => {
            event.preventDefault();
            const url = button.dataset.url;
            fetch(url, { method: 'POST', headers: { 'X-CSRFToken': csrfToken } })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('cart-total').innerText = data.total_items;
                })
                .catch(error => console.error('Error:', error));
        });
    });
});

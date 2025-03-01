let addButtons = document.getElementsByClassName('update-cart')

for (i = 0; i < addButtons.length; i++) {
    addButtons[i].addEventListener('click', function () {
        let productId = this.dataset.product
        let action = this.dataset.action
        console.log('ProductId: ', productId, 'action: ', action)
        console.log("User: ", user)
        if (user === 'AnonymousUser') {
            console.log("User is not authenticated")
        } else {
            console.log("User is authenticated")
            updateItemOrder(productId, action)
        }
    })
}

function updateItemOrder(productId, action) {
    console.log("User is logged in. Sending data...")
    let url = '/update-item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    }).then((response) => {
        return response.json()
    }).then((data) => {
        console.log("Data: ", data)
    })

}
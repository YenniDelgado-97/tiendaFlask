(function () {

    const btnsComprarComic = document.querySelectorAll('.btnComprarComic');
    let isbnComicSeleccionado = null;
    const csrf_token = document.querySelector("[name= 'csrf-token']").value;

    btnsComprarComic.forEach((btn) => {
        btn.addEventListener('click', function () {
            isbnComicSeleccionado = this.id;
            confirmarCompra();
        })
    });

    const confirmarCompra = async () => {
        await fetch('http://127.0.0.1:5000/comprarComic', {
            method: 'POST',
            mode: 'same-origin',
            credentials: 'same-origin',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRF-TOKEN': csrf_token
            },
            body: JSON.stringify({
                'isbn': isbnComicSeleccionado
            })


        }).then(response => {
            if (!response.ok) {
                console.error("error!");
            }
            return response.json();
        }).then(data => {
            console.log("Comic Comprado");
        }).catch(error => {
            console.error('Error: ${error}');
        });


    };
})();
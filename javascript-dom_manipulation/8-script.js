async function getHello() {
    try {
        const response = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        if (data && data.hello) {
            return data.hello;
        } else {
            throw new Error('Data not found');
        }
    } catch (err) {
        console.error(err);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const sayHello = document.getElementById('hello');
    getHello().then((hello) => {
        sayHello.textContent = hello;
    })
})
function getHeaders() {
    var url = document.getElementById('urlInput').value;
    fetch('/get_headers', {
        method: 'POST',
        body: new URLSearchParams({'url': url})
    })
    .then(response => response.json())
    .then(data => {
        var output = JSON.stringify(data, null, 2);
        document.getElementById('headersOutput').textContent = output;
    })
    .catch(error => console.error('Error:', error));
}


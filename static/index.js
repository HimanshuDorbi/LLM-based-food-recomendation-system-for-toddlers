document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const productImage = document.getElementById('productImage').files;
    const ageBracket = document.getElementById('ageBracket').value;
    const output = document.getElementById('output');

    if (productImage.length === 0) {
        output.innerHTML = '<p style="color: red;">Please upload at least one image.</p>';
        return;
    }

    const formData = new FormData();
    for (const file of productImage) {
        formData.append('productImage', file);
    }
    formData.append('ageBracket', ageBracket);

    fetch('http://localhost:5000/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            output.innerHTML = '<p style="color: red;">' + data.error + '</p>';
        } else {
            output.innerHTML = '<p>' + data.message + '</p>';
            output.innerHTML += '<p><strong>Analysis:</strong> ' + data.analysis + '</p>';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        output.innerHTML = '<p style="color: red;">Error uploading images. Please try again.</p>';
    });
});

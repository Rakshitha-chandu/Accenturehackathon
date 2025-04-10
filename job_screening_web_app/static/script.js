
document.getElementById('uploadForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    document.getElementById('result').classList.remove('hidden');
    document.getElementById('score').innerText = result.score;
    document.getElementById('parsed').innerText = JSON.stringify(result.parsed_resume, null, 2);
});

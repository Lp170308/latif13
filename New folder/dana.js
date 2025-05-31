document.getElementById('addFundsBtn').addEventListener('click', function() {
    const currentBalance = parseInt(document.getElementById('balance').innerText.replace('Rp ', '').replace('.', ''));
    const newBalance = currentBalance + 100000; // Menambahkan Rp 100.000
    document.getElementById('balance').innerText = 'Rp ' + newBalance.toLocaleString();
    alert('Dana berhasil ditambahkan!');
});
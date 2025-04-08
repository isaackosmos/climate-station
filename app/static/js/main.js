document.addEventListener("DOMContentLoaded", function () {
    fetch('/api/reads')
    .then(res => res.json())
    .then(data => {
        const labels = data.map(d => d.timestamp);
        const temperatures = data.map(d => d.temperature);
        const humidities = data.map(d => d.humidity);

        const tempCtx = document.getElementById('tempChart').getContext('2d');
        new Chart(tempCtx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Temperature (°C)',
                    data: temperatures,
                    borderColor: 'red',
                    backgroundColor: 'rgba(255,0,0,0.1)',
                    tension: 0.3,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                scales: {
                    x: {
                        ticks: { autoSkip: true, maxTicksLimit: 10 }
                    }
                }
            }
        });

        const humidCtx = document.getElementById('humidChart').getContext('2d');
        new Chart(humidCtx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Humidity (%)',
                    data: humidities,
                    borderColor: 'blue',
                    backgroundColor: 'rgba(0,0,255,0.1)',
                    tension: 0.3,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                scales: {
                    x: {
                        ticks: { autoSkip: true, maxTicksLimit: 10 }
                    }
                }
            }
        });
    })
    .catch(err => {
        console.error("Error loading data:", err);
    });
});
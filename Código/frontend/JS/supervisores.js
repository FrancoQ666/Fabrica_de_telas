// Función para actualizar las metas en tiempo real
function updateMetrics() {
    fetch('/api/metrics')
        .then(response => response.json())
        .then(data => {
            // Actualizar producción diaria
            const productionElement = document.querySelector('.meta-item:nth-child(1)');
            const productionValue = productionElement.querySelector('.meta-value');
            const productionBar = productionElement.querySelector('.progress-fill');
            const productionBadge = productionElement.querySelector('.badge');
            
            productionValue.textContent = `${data.production}%`;
            productionBar.style.width = `${data.production}%`;
            
            if (data.production >= 80) {
                productionBadge.className = 'badge badge-success';
                productionBadge.textContent = 'En Meta';
            } else {
                productionBadge.className = 'badge badge-warning';
                productionBadge.textContent = 'Atención';
            }

            // Actualizar calidad
            const qualityElement = document.querySelector('.meta-item:nth-child(2)');
            const qualityValue = qualityElement.querySelector('.meta-value');
            const qualityBar = qualityElement.querySelector('.progress-fill');
            
            qualityValue.textContent = `${data.quality}%`;
            qualityBar.style.width = `${data.quality}%`;

            // Actualizar eficiencia
            const efficiencyElement = document.querySelector('.meta-item:nth-child(3)');
            const efficiencyValue = efficiencyElement.querySelector('.meta-value');
            const efficiencyBar = efficiencyElement.querySelector('.progress-fill');
            
            efficiencyValue.textContent = `${data.efficiency}%`;
            efficiencyBar.style.width = `${data.efficiency}%`;
        })
        .catch(error => console.error('Error al actualizar métricas:', error));
}

// Función para actualizar la tabla de producción
function updateProductionTable() {
    fetch('/api/production/realtime')
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById('productionTable');
            tbody.innerHTML = '';
            
            data.forEach(item => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${item.line}</td>
                    <td>${item.product}</td>
                    <td>${item.quantity}</td>
                    <td><span class="badge ${item.status === 'active' ? 'badge-success' : 'badge-warning'}">
                        ${item.status}
                    </span></td>
                    <td>${item.operator}</td>
                `;
                tbody.appendChild(row);
            });
        })
        .catch(error => console.error('Error al actualizar tabla de producción:', error));
}

// Función para actualizar la tabla de calidad
function updateQualityTable(filter = 'all') {
    fetch(`/api/quality?filter=${filter}`)
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById('qualityTable');
            tbody.innerHTML = '';
            
            data.forEach(item => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${item.product}</td>
                    <td><span class="badge ${item.result === 'approved' ? 'badge-success' : 
                        item.result === 'rejected' ? 'badge-error' : 'badge-warning'}">
                        ${item.result}
                    </span></td>
                    <td>${new Date(item.date).toLocaleString()}</td>
                    <td>${item.inspector}</td>
                `;
                tbody.appendChild(row);
            });
        })
        .catch(error => console.error('Error al actualizar tabla de calidad:', error));
}

// Inicialización
document.addEventListener('DOMContentLoaded', () => {
    // Actualizar datos cada 5 segundos
    setInterval(updateMetrics, 5000);
    setInterval(updateProductionTable, 5000);
    updateQualityTable();

    // Eventos
    document.getElementById('qualityFilter').addEventListener('change', (e) => {
        updateQualityTable(e.target.value);
    });
});
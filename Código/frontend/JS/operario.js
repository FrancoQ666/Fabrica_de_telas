
// operarios.js - Lógica del panel de operarios

// Datos en memoria (por ahora, después se conectará al backend)
let producciones = [
    { hora: '08:30', maquina: 'M001', tipoTela: 'Algodón', cantidad: 120, estado: 'Completado' },
    { hora: '10:15', maquina: 'M002', tipoTela: 'Poliéster', cantidad: 200, estado: 'Completado' }
];

let fallas = [];

// Formulario de Producción
document.getElementById('formProduccion').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const maquina = document.getElementById('maquina').value;
    const tipoTela = document.getElementById('tipoTela').value;
    const cantidad = parseFloat(document.getElementById('cantidad').value);
    const turno = document.getElementById('turno').value;
    
    // Crear nuevo registro
    const nuevaProduccion = {
        hora: obtenerHoraActual(),
        maquina: maquina,
        tipoTela: getTipoTelaText(tipoTela),
        cantidad: cantidad,
        estado: 'Completado'
    };
    
    // Agregar al array
    producciones.push(nuevaProduccion);
    
    // Actualizar tabla
    actualizarTablaProduccion();
    
    // Actualizar metas
    actualizarMetas();
    
    // Limpiar formulario
    this.reset();
    
    // Mostrar mensaje de éxito
    mostrarMensaje('Producción registrada correctamente', 'success');
});

// Formulario de Fallas
document.getElementById('formFallas').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const maquinaFalla = document.getElementById('maquinaFalla').value;
    const tipoFalla = document.getElementById('tipoFalla').value;
    const descripcion = document.getElementById('descripcionFalla').value;
    
    // Crear nuevo reporte de falla
    const nuevaFalla = {
        hora: obtenerHoraActual(),
        maquina: maquinaFalla,
        tipo: getTipoFallaText(tipoFalla),
        descripcion: descripcion,
        estado: 'Pendiente'
    };
    
    // Agregar al array
    fallas.push(nuevaFalla);
    
    // Limpiar formulario
    this.reset();
    
    // Mostrar mensaje de éxito
    mostrarMensaje('Falla reportada correctamente. Se notificará al supervisor.', 'warning');
    
    console.log('Fallas reportadas:', fallas);
});

// Actualizar tabla de producción
function actualizarTablaProduccion() {
    const tbody = document.getElementById('tablaProduccion');
    tbody.innerHTML = '';
    
    producciones.forEach(prod => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${prod.hora}</td>
            <td>${prod.maquina}</td>
            <td>${prod.tipoTela}</td>
            <td>${prod.cantidad}</td>
            <td><span class="badge badge-success">${prod.estado}</span></td>
        `;
        tbody.appendChild(tr);
    });
}

// Actualizar metas
function actualizarMetas() {
    const metaDiaria = 500;
    const produccionActual = producciones.reduce((sum, prod) => sum + prod.cantidad, 0);
    const progreso = Math.min((produccionActual / metaDiaria) * 100, 100);
    
    // Actualizar valores en la UI
    document.querySelector('.metas-container .meta-item:nth-child(2) .meta-value').textContent = 
        `${produccionActual.toFixed(0)} metros`;
    
    document.querySelector('.progress-fill').style.width = `${progreso}%`;
    
    document.querySelector('.metas-container .meta-item:nth-child(3) .meta-value:last-child').textContent = 
        `${progreso.toFixed(0)}%`;
}

// Funciones auxiliares
function obtenerHoraActual() {
    const now = new Date();
    return now.toLocaleTimeString('es-ES', { hour: '2-digit', minute: '2-digit' });
}

function getTipoTelaText(value) {
    const tipos = {
        'algodon': 'Algodón',
        'poliester': 'Poliéster',
        'lana': 'Lana',
        'mezcla': 'Mezcla'
    };
    return tipos[value] || value;
}

function getTipoFallaText(value) {
    const tipos = {
        'mecanica': 'Falla Mecánica',
        'electrica': 'Falla Eléctrica',
        'material': 'Problema con Material',
        'calidad': 'Problema de Calidad'
    };
    return tipos[value] || value;
}

function mostrarMensaje(mensaje, tipo) {
    // Crear elemento de mensaje
    const div = document.createElement('div');
    div.className = `mensaje mensaje-${tipo}`;
    div.textContent = mensaje;
    div.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        background: ${tipo === 'success' ? '#e8f5e9' : '#fff3e0'};
        color: ${tipo === 'success' ? '#2e7d32' : '#f57c00'};
        border-radius: 4px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        z-index: 1000;
        animation: slideIn 0.3s ease;
    `;
    
    document.body.appendChild(div);
    
    // Remover después de 3 segundos
    setTimeout(() => {
        div.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => div.remove(), 300);
    }, 3000);
}

// Agregar animaciones CSS dinámicamente
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Inicializar metas al cargar la página
actualizarMetas();
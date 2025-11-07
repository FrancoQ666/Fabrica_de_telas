package com.alcoyana.fabrica.services;

import com.alcoyana.fabrica.dto.ProduccionRequestDTO;
import com.alcoyana.fabrica.models.Produccion;
import com.alcoyana.fabrica.repositories.ProduccionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

/**
 * Service para la lógica de negocio de producción
 */
@Service
public class ProduccionService {
    
    @Autowired
    private ProduccionRepository produccionRepository;
    
    /**
     * Obtener todas las producciones
     */
    public List<Produccion> obtenerTodas() {
        return produccionRepository.findAll();
    }
    
    /**
     * Obtener producción por ID
     */
    public Optional<Produccion> obtenerPorId(Long id) {
        return produccionRepository.findById(id);
    }
    
    /**
     * Obtener producción por código de lote
     */
    public Optional<Produccion> obtenerPorCodigoLote(String codigoLote) {
        return produccionRepository.findByCodigoLote(codigoLote);
    }
    
    /**
     * Obtener producciones por estado
     */
    public List<Produccion> obtenerPorEstado(String estado) {
        return produccionRepository.findByEstado(estado);
    }
    
    /**
     * Obtener producciones activas de hoy
     */
    public List<Produccion> obtenerProduccionesActivasHoy() {
        return produccionRepository.findProduccionesActivasHoy();
    }
    
    /**
     * Registrar nueva producción
     */
    @Transactional
    public Produccion registrarProduccion(ProduccionRequestDTO dto) {
        // Validar que no exista el código de lote
        if (produccionRepository.findByCodigoLote(dto.getCodigoLote()).isPresent()) {
            throw new RuntimeException("El código de lote ya existe: " + dto.getCodigoLote());
        }
        
        // Crear nueva producción
        Produccion produccion = new Produccion();
        produccion.setCodigoLote(dto.getCodigoLote());
        produccion.setProductoId(dto.getProductoId());
        produccion.setMaquinaId(dto.getMaquinaId());
        produccion.setCantidadPlanificada(dto.getCantidadPlanificada());
        produccion.setCantidadProducida(0.0);
        produccion.setUnidadMedida(dto.getUnidadMedida());
        produccion.setEstado("En Proceso");
        produccion.setTurnoId(dto.getTurnoId());
        produccion.setUsuarioId(dto.getUsuarioId());
        produccion.setSalaId(dto.getSalaId());
        produccion.setObservaciones(dto.getObservaciones());
        produccion.setFechaInicio(LocalDateTime.now());
        
        return produccionRepository.save(produccion);
    }
    
    /**
     * Actualizar cantidad producida
     */
    @Transactional
    public Produccion actualizarCantidadProducida(Long id, Double cantidadProducida) {
        Produccion produccion = produccionRepository.findById(id)
            .orElseThrow(() -> new RuntimeException("Producción no encontrada con ID: " + id));
        
        // Validar que no exceda la cantidad planificada
        if (cantidadProducida > produccion.getCantidadPlanificada()) {
            throw new RuntimeException("La cantidad producida no puede exceder la cantidad planificada");
        }
        
        produccion.setCantidadProducida(cantidadProducida);
        
        // Si alcanzó la cantidad planificada, cambiar estado a Completada
        if (cantidadProducida.equals(produccion.getCantidadPlanificada())) {
            produccion.setEstado("Completada");
            produccion.setFechaFin(LocalDateTime.now());
        }
        
        return produccionRepository.save(produccion);
    }
    
    /**
     * Actualizar estado de producción
     */
    @Transactional
    public Produccion actualizarEstado(Long id, String estado) {
        Produccion produccion = produccionRepository.findById(id)
            .orElseThrow(() -> new RuntimeException("Producción no encontrada con ID: " + id));
        
        produccion.setEstado(estado);
        
        if ("Completada".equals(estado) || "Cancelada".equals(estado)) {
            produccion.setFechaFin(LocalDateTime.now());
        }
        
        return produccionRepository.save(produccion);
    }
    
    /**
     * Eliminar producción
     */
    @Transactional
    public void eliminarProduccion(Long id) {
        if (!produccionRepository.existsById(id)) {
            throw new RuntimeException("Producción no encontrada con ID: " + id);
        }
        produccionRepository.deleteById(id);
    }
    
    /**
     * Obtener últimas 10 producciones
     */
    public List<Produccion> obtenerUltimas() {
        return produccionRepository.findTop10ByOrderByCreatedAtDesc();
    }
}
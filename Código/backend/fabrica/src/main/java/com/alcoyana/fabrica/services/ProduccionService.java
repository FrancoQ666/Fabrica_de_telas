package com.alcoyana.fabrica.services;

import com.alcoyana.fabrica.dto.ProduccionRequestDTO;
import com.alcoyana.fabrica.models.Produccion;
import com.alcoyana.fabrica.repositories.ProduccionRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import jakarta.persistence.EntityNotFoundException;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@Service
public class ProduccionService {

    private final ProduccionRepository produccionRepository;

    public ProduccionService(ProduccionRepository produccionRepository) {
        this.produccionRepository = produccionRepository;
    }

    public List<Produccion> obtenerTodas() {
        return produccionRepository.findAll();
    }

    public Optional<Produccion> obtenerPorId(Long id) {
        return produccionRepository.findById(id);
    }

    public Optional<Produccion> obtenerPorCodigoLote(String codigoLote) {
        return produccionRepository.findByCodigoLote(codigoLote);
    }

    public List<Produccion> obtenerPorEstado(String estado) {
        return produccionRepository.findByEstado(estado);
    }

    public List<Produccion> obtenerProduccionesActivasHoy() {
        LocalDate today = LocalDate.now();
        LocalDateTime start = today.atStartOfDay();
        LocalDateTime end = start.plusDays(1);
        return produccionRepository.findProduccionesActivasHoy(start, end);
    }

    @Transactional
    public Produccion registrarProduccion(ProduccionRequestDTO dto) {
        if (dto.getCodigoLote() != null && produccionRepository.findByCodigoLote(dto.getCodigoLote()).isPresent()) {
            throw new IllegalArgumentException("El código de lote ya existe: " + dto.getCodigoLote());
        }

        Produccion p = new Produccion();
        p.setCodigoLote(dto.getCodigoLote());
        p.setProductoId(dto.getProductoId());
        p.setMaquinaId(dto.getMaquinaId());
        p.setCantidadPlanificada(dto.getCantidadPlanificada());
        p.setCantidadProducida(0.0);
        p.setUnidadMedida(dto.getUnidadMedida());
        p.setEstado("En Proceso");
        p.setTurnoId(dto.getTurnoId());
        p.setUsuarioId(dto.getUsuarioId());
        p.setSalaId(dto.getSalaId());
        p.setObservaciones(dto.getObservaciones());
        p.setFechaInicio(LocalDateTime.now());

        return produccionRepository.save(p);
    }

    @Transactional
    public Produccion actualizarCantidadProducida(Long id, Double cantidadProducida) {
        Produccion produccion = produccionRepository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("Producción no encontrada con ID: " + id));

        if (produccion.getCantidadPlanificada() == null) {
            throw new IllegalStateException("Cantidad planificada no definida para la producción ID: " + id);
        }

        if (Double.compare(cantidadProducida, produccion.getCantidadPlanificada()) > 0) {
            throw new IllegalArgumentException("La cantidad producida no puede exceder la cantidad planificada");
        }

        produccion.setCantidadProducida(cantidadProducida);

        if (Double.compare(cantidadProducida, produccion.getCantidadPlanificada()) == 0) {
            produccion.setEstado("Completada");
            produccion.setFechaFin(LocalDateTime.now());
        }

        return produccionRepository.save(produccion);
    }

    @Transactional
    public Produccion actualizarEstado(Long id, String estado) {
        Produccion produccion = produccionRepository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("Producción no encontrada con ID: " + id));

        produccion.setEstado(estado);

        if ("Completada".equalsIgnoreCase(estado) || "Cancelada".equalsIgnoreCase(estado)) {
            produccion.setFechaFin(LocalDateTime.now());
        }

        return produccionRepository.save(produccion);
    }

    @Transactional
    public void eliminarProduccion(Long id) {
        if (!produccionRepository.existsById(id)) {
            throw new EntityNotFoundException("Producción no encontrada con ID: " + id);
        }
        produccionRepository.deleteById(id);
    }

    public List<Produccion> obtenerUltimas() {
        return produccionRepository.findTop10ByOrderByCreatedAtDesc();
    }
}
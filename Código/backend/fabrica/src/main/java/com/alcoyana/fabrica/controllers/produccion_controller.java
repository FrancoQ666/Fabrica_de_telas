package com.alcoyana.fabrica.controllers;

import com.alcoyana.fabrica.dto.ProduccionRequestDTO;
import com.alcoyana.fabrica.models.Produccion;
import com.alcoyana.fabrica.services.ProduccionService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Controller REST para gestión de producción
 */
@RestController
@RequestMapping("/api/produccion")
@CrossOrigin(origins = {"http://localhost:5500", "http://127.0.0.1:5500"})
public class ProduccionController {
    
    @Autowired
    private ProduccionService produccionService;
    
    /**
     * GET /api/produccion - Obtener todas las producciones
     */
    @GetMapping
    public ResponseEntity<List<Produccion>> obtenerTodas() {
        List<Produccion> producciones = produccionService.obtenerTodas();
        return ResponseEntity.ok(producciones);
    }
    
    /**
     * GET /api/produccion/{id} - Obtener producción por ID
     */
    @GetMapping("/{id}")
    public ResponseEntity<?> obtenerPorId(@PathVariable Long id) {
        return produccionService.obtenerPorId(id)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }
    
    /**
     * GET /api/produccion/lote/{codigoLote} - Obtener por código de lote
     */
    @GetMapping("/lote/{codigoLote}")
    public ResponseEntity<?> obtenerPorCodigoLote(@PathVariable String codigoLote) {
        return produccionService.obtenerPorCodigoLote(codigoLote)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }
    
    /**
     * GET /api/produccion/estado/{estado} - Obtener por estado
     */
    @GetMapping("/estado/{estado}")
    public ResponseEntity<List<Produccion>> obtenerPorEstado(@PathVariable String estado) {
        List<Produccion> producciones = produccionService.obtenerPorEstado(estado);
        return ResponseEntity.ok(producciones);
    }
    
    /**
     * GET /api/produccion/activas - Obtener producciones activas de hoy
     */
    @GetMapping("/activas")
    public ResponseEntity<List<Produccion>> obtenerActivasHoy() {
        List<Produccion> producciones = produccionService.obtenerProduccionesActivasHoy();
        return ResponseEntity.ok(producciones);
    }
    
    /**
     * GET /api/produccion/ultimas - Obtener últimas 10 producciones
     */
    @GetMapping("/ultimas")
    public ResponseEntity<List<Produccion>> obtenerUltimas() {
        List<Produccion> producciones = produccionService.obtenerUltimas();
        return ResponseEntity.ok(producciones);
    }
    
    /**
     * POST /api/produccion - Registrar nueva producción
     */
    @PostMapping
    public ResponseEntity<?> registrarProduccion(@Valid @RequestBody ProduccionRequestDTO dto) {
        try {
            Produccion produccion = produccionService.registrarProduccion(dto);
            
            Map<String, Object> response = new HashMap<>();
            response.put("success", true);
            response.put("message", "Producción registrada exitosamente");
            response.put("data", produccion);
            
            return ResponseEntity.status(HttpStatus.CREATED).body(response);
        } catch (RuntimeException e) {
            Map<String, Object> error = new HashMap<>();
            error.put("success", false);
            error.put("message", e.getMessage());
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(error);
        }
    }
    
    /**
     * PUT /api/produccion/{id}/cantidad - Actualizar cantidad producida
     */
    @PutMapping("/{id}/cantidad")
    public ResponseEntity<?> actualizarCantidad(
        @PathVariable Long id,
        @RequestBody Map<String, Double> body
    ) {
        try {
            Double cantidadProducida = body.get("cantidadProducida");
            Produccion produccion = produccionService.actualizarCantidadProducida(id, cantidadProducida);
            
            Map<String, Object> response = new HashMap<>();
            response.put("success", true);
            response.put("message", "Cantidad actualizada exitosamente");
            response.put("data", produccion);
            
            return ResponseEntity.ok(response);
        } catch (RuntimeException e) {
            Map<String, Object> error = new HashMap<>();
            error.put("success", false);
            error.put("message", e.getMessage());
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(error);
        }
    }
    
    /**
     * PUT /api/produccion/{id}/estado - Actualizar estado
     */
    @PutMapping("/{id}/estado")
    public ResponseEntity<?> actualizarEstado(
        @PathVariable Long id,
        @RequestBody Map<String, String> body
    ) {
        try {
            String estado = body.get("estado");
            Produccion produccion = produccionService.actualizarEstado(id, estado);
            
            Map<String, Object> response = new HashMap<>();
            response.put("success", true);
            response.put("message", "Estado actualizado exitosamente");
            response.put("data", produccion);
            
            return ResponseEntity.ok(response);
        } catch (RuntimeException e) {
            Map<String, Object> error = new HashMap<>();
            error.put("success", false);
            error.put("message", e.getMessage());
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(error);
        }
    }
    
    /**
     * DELETE /api/produccion/{id} - Eliminar producción
     */
    @DeleteMapping("/{id}")
    public ResponseEntity<?> eliminarProduccion(@PathVariable Long id) {
        try {
            produccionService.eliminarProduccion(id);
            
            Map<String, Object> response = new HashMap<>();
            response.put("success", true);
            response.put("message", "Producción eliminada exitosamente");
            
            return ResponseEntity.ok(response);
        } catch (RuntimeException e) {
            Map<String, Object> error = new HashMap<>();
            error.put("success", false);
            error.put("message", e.getMessage());
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(error);
        }
    }
}
package com.alcoyana.fabrica.models;

import jakarta.persistence.*;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;
import java.time.LocalDateTime;

/**
 * Entidad que representa una orden de producción
 */
@Entity
@Table(name = "producciones")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Produccion {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "codigo_lote", nullable = false, unique = true, length = 50)
    private String codigoLote;
    
    @Column(name = "producto_id", nullable = false)
    private Long productoId;
    
    @Column(name = "maquina_id")
    private Long maquinaId;
    
    @Column(name = "cantidad_planificada", nullable = false)
    private Double cantidadPlanificada;
    
    @Column(name = "cantidad_producida")
    private Double cantidadProducida = 0.0;
    
    @Column(name = "unidad_medida", length = 20)
    private String unidadMedida = "metros";
    
    @Column(name = "estado", length = 30)
    private String estado = "Planificada";
    
    @Column(name = "turno_id")
    private Long turnoId;
    
    @Column(name = "usuario_id", nullable = false)
    private Long usuarioId;
    
    @Column(name = "sala_id")
    private Long salaId;
    
    @Column(name = "fecha_inicio")
    private LocalDateTime fechaInicio;
    
    @Column(name = "fecha_fin")
    private LocalDateTime fechaFin;
    
    @Column(name = "observaciones", columnDefinition = "TEXT")
    private String observaciones;
    
    @Column(name = "created_at", updatable = false)
    private LocalDateTime createdAt;
    
    @Column(name = "updated_at")
    private LocalDateTime updatedAt;
    
    @PrePersist
    protected void onCreate() {
        createdAt = LocalDateTime.now();
        updatedAt = LocalDateTime.now();
        if (fechaInicio == null) {
            fechaInicio = LocalDateTime.now();
        }
        if (cantidadProducida == null) {
            cantidadProducida = 0.0;
        }
    }
    
    @PreUpdate
    protected void onUpdate() {
        updatedAt = LocalDateTime.now();
    }
    
    /**
     * Calcula el porcentaje de eficiencia de la producción
     */
    public Double calcularPorcentajeEficiencia() {
        if (cantidadPlanificada == null || cantidadPlanificada == 0) {
            return 0.0;
        }
        return (cantidadProducida / cantidadPlanificada) * 100;
    }
}
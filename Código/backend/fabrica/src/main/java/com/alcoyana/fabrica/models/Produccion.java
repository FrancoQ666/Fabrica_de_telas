package com.alcoyana.fabrica.models;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "produccion", uniqueConstraints = {
    @UniqueConstraint(columnNames = {"codigo_lote"})
})
public class Produccion {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "codigo_lote", length = 100, nullable = false)
    private String codigoLote;

    @Column(name = "producto_id")
    private Long productoId;

    @Column(name = "maquina_id")
    private Long maquinaId;

    @Column(name = "cantidad_planificada")
    private Double cantidadPlanificada;

    @Column(name = "cantidad_producida")
    private Double cantidadProducida;

    @Column(name = "unidad_medida", length = 20)
    private String unidadMedida;

    @Column(length = 50)
    private String estado;

    @Column(name = "turno_id")
    private Long turnoId;

    @Column(name = "usuario_id")
    private Long usuarioId;

    @Column(name = "sala_id")
    private Long salaId;

    @Column(columnDefinition = "TEXT")
    private String observaciones;

    @Column(name = "fecha_inicio")
    private LocalDateTime fechaInicio;

    @Column(name = "fecha_fin")
    private LocalDateTime fechaFin;

    @Column(name = "created_at", updatable = false)
    private LocalDateTime createdAt;

    @Column(name = "updated_at")
    private LocalDateTime updatedAt;

    public Produccion() {}

    @PrePersist
    protected void onCreate() {
        this.createdAt = LocalDateTime.now();
        this.updatedAt = this.createdAt;
    }

    @PreUpdate
    protected void onUpdate() {
        this.updatedAt = LocalDateTime.now();
    }

    // Getters y setters (omito por brevedad en este listado; añádelos todos)
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getCodigoLote() { return codigoLote; }
    public void setCodigoLote(String codigoLote) { this.codigoLote = codigoLote; }

    public Long getProductoId() { return productoId; }
    public void setProductoId(Long productoId) { this.productoId = productoId; }

    public Long getMaquinaId() { return maquinaId; }
    public void setMaquinaId(Long maquinaId) { this.maquinaId = maquinaId; }

    public Double getCantidadPlanificada() { return cantidadPlanificada; }
    public void setCantidadPlanificada(Double cantidadPlanificada) { this.cantidadPlanificada = cantidadPlanificada; }

    public Double getCantidadProducida() { return cantidadProducida; }
    public void setCantidadProducida(Double cantidadProducida) { this.cantidadProducida = cantidadProducida; }

    public String getUnidadMedida() { return unidadMedida; }
    public void setUnidadMedida(String unidadMedida) { this.unidadMedida = unidadMedida; }

    public String getEstado() { return estado; }
    public void setEstado(String estado) { this.estado = estado; }

    public Long getTurnoId() { return turnoId; }
    public void setTurnoId(Long turnoId) { this.turnoId = turnoId; }

    public Long getUsuarioId() { return usuarioId; }
    public void setUsuarioId(Long usuarioId) { this.usuarioId = usuarioId; }

    public Long getSalaId() { return salaId; }
    public void setSalaId(Long salaId) { this.salaId = salaId; }

    public String getObservaciones() { return observaciones; }
    public void setObservaciones(String observaciones) { this.observaciones = observaciones; }

    public LocalDateTime getFechaInicio() { return fechaInicio; }
    public void setFechaInicio(LocalDateTime fechaInicio) { this.fechaInicio = fechaInicio; }

    public LocalDateTime getFechaFin() { return fechaFin; }
    public void setFechaFin(LocalDateTime fechaFin) { this.fechaFin = fechaFin; }

    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }

    public LocalDateTime getUpdatedAt() { return updatedAt; }
    public void setUpdatedAt(LocalDateTime updatedAt) { this.updatedAt = updatedAt; }
}
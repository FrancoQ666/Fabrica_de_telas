package com.alcoyana.fabrica.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

public class ProduccionRequestDTO {

    @NotBlank
    private String codigoLote;

    @NotNull
    private Long productoId;

    @NotNull
    private Long maquinaId;

    @NotNull
    private Double cantidadPlanificada;

    private String unidadMedida;

    private Long turnoId;
    private Long usuarioId;
    private Long salaId;
    private String observaciones;

    public ProduccionRequestDTO() {}

    // Getters y setters
    public String getCodigoLote() { return codigoLote; }
    public void setCodigoLote(String codigoLote) { this.codigoLote = codigoLote; }

    public Long getProductoId() { return productoId; }
    public void setProductoId(Long productoId) { this.productoId = productoId; }

    public Long getMaquinaId() { return maquinaId; }
    public void setMaquinaId(Long maquinaId) { this.maquinaId = maquinaId; }

    public Double getCantidadPlanificada() { return cantidadPlanificada; }
    public void setCantidadPlanificada(Double cantidadPlanificada) { this.cantidadPlanificada = cantidadPlanificada; }

    public String getUnidadMedida() { return unidadMedida; }
    public void setUnidadMedida(String unidadMedida) { this.unidadMedida = unidadMedida; }

    public Long getTurnoId() { return turnoId; }
    public void setTurnoId(Long turnoId) { this.turnoId = turnoId; }

    public Long getUsuarioId() { return usuarioId; }
    public void setUsuarioId(Long usuarioId) { this.usuarioId = usuarioId; }

    public Long getSalaId() { return salaId; }
    public void setSalaId(Long salaId) { this.salaId = salaId; }

    public String getObservaciones() { return observaciones; }
    public void setObservaciones(String observaciones) { this.observaciones = observaciones; }
}
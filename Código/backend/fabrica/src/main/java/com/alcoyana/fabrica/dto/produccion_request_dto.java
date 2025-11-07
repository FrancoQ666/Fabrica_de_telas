package com.alcoyana.fabrica.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Positive;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

/**
 * DTO para crear una nueva producción
 */
@Data
@NoArgsConstructor
@AllArgsConstructor
public class ProduccionRequestDTO {
    
    @NotBlank(message = "El código de lote es obligatorio")
    private String codigoLote;
    
    @NotNull(message = "El ID del producto es obligatorio")
    private Long productoId;
    
    @NotNull(message = "El ID de la máquina es obligatorio")
    private Long maquinaId;
    
    @NotNull(message = "La cantidad planificada es obligatoria")
    @Positive(message = "La cantidad planificada debe ser mayor a 0")
    private Double cantidadPlanificada;
    
    private String unidadMedida = "metros";
    
    @NotNull(message = "El ID del turno es obligatorio")
    private Long turnoId;
    
    @NotNull(message = "El ID del usuario es obligatorio")
    private Long usuarioId;
    
    private Long salaId;
    
    private String observaciones;
}
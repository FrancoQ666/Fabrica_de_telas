package com.alcoyana.fabrica.repositories;

import com.alcoyana.fabrica.models.Produccion;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

/**
 * Repository para la entidad Produccion
 * Proporciona métodos CRUD y consultas personalizadas
 */
@Repository
public interface ProduccionRepository extends JpaRepository<Produccion, Long> {
    
    /**
     * Buscar producción por código de lote
     */
    Optional<Produccion> findByCodigoLote(String codigoLote);
    
    /**
     * Buscar todas las producciones por estado
     */
    List<Produccion> findByEstado(String estado);
    
    /**
     * Buscar producciones de un usuario específico
     */
    List<Produccion> findByUsuarioId(Long usuarioId);
    
    /**
     * Buscar producciones por máquina
     */
    List<Produccion> findByMaquinaId(Long maquinaId);
    
    /**
     * Buscar producciones por sala
     */
    List<Produccion> findBySalaId(Long salaId);
    
    /**
     * Buscar producciones por turno
     */
    List<Produccion> findByTurnoId(Long turnoId);
    
    /**
     * Buscar producciones en un rango de fechas
     */
    @Query("SELECT p FROM Produccion p WHERE p.fechaInicio BETWEEN :fechaInicio AND :fechaFin")
    List<Produccion> findByFechaRange(
        @Param("fechaInicio") LocalDateTime fechaInicio, 
        @Param("fechaFin") LocalDateTime fechaFin
    );
    
    /**
     * Buscar producciones activas del día actual
     */
    @Query("SELECT p FROM Produccion p WHERE DATE(p.fechaInicio) = CURRENT_DATE AND p.estado IN ('En Proceso', 'Planificada')")
    List<Produccion> findProduccionesActivasHoy();
    
    /**
     * Contar producciones por estado
     */
    Long countByEstado(String estado);
    
    /**
     * Buscar últimas N producciones
     */
    List<Produccion> findTop10ByOrderByCreatedAtDesc();
}
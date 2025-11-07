package com.alcoyana.fabrica.repositories;

import com.alcoyana.fabrica.models.Produccion;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

public interface ProduccionRepository extends JpaRepository<Produccion, Long> {

    Optional<Produccion> findByCodigoLote(String codigoLote);

    List<Produccion> findByEstado(String estado);

    // Encuentra producciones activas en el rango start..end (útil para "hoy")
    @Query("SELECT p FROM Produccion p WHERE p.estado NOT IN ('Completada','Cancelada') AND p.fechaInicio >= :start AND p.fechaInicio < :end")
    List<Produccion> findProduccionesActivasHoy(@Param("start") LocalDateTime start, @Param("end") LocalDateTime end);

    List<Produccion> findTop10ByOrderByCreatedAtDesc();
}   
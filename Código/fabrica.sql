-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-11-2025 a las 00:59:52
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `fabrica`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `controles_calidad`
--

CREATE TABLE `controles_calidad` (
  `id` int(11) NOT NULL,
  `produccion_id` int(11) NOT NULL,
  `resultado` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `observaciones` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `inspector` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fecha_control` timestamp NOT NULL DEFAULT current_timestamp(),
  `calificacion` decimal(5,2) DEFAULT NULL,
  `usuario_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_produccion`
--

CREATE TABLE `detalle_produccion` (
  `id` int(11) NOT NULL,
  `produccion_id` int(11) NOT NULL,
  `materia_prima_id` int(11) NOT NULL,
  `cantidad_usada` decimal(10,2) NOT NULL,
  `cantidad_requerida` decimal(10,2) NOT NULL,
  `porcentaje_usado` decimal(5,2) GENERATED ALWAYS AS (`cantidad_usada` / nullif(`cantidad_requerida`,0) * 100) STORED,
  `fecha_registro` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `logs_transacciones`
--

CREATE TABLE `logs_transacciones` (
  `id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `fecha` datetime NOT NULL DEFAULT current_timestamp(),
  `tabla_afectada` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `accion` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `detalle` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `ip_usuario` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `nivel_log` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `inicio_operacion` timestamp NULL DEFAULT NULL,
  `fin_operacion` timestamp NULL DEFAULT NULL,
  `duracion` decimal(10,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mantenimiento`
--

CREATE TABLE `mantenimiento` (
  `id` int(11) NOT NULL,
  `maquinaria_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `descripcion` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `tipo_mantenimiento` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `resultado` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `costo` decimal(10,2) DEFAULT NULL,
  `horas_trabajo` decimal(6,2) DEFAULT NULL,
  `fecha_inicio` timestamp NULL DEFAULT NULL,
  `fecha_fin` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Disparadores `mantenimiento`
--
DELIMITER $$
CREATE TRIGGER `tr_mantenimiento_after_insert` AFTER INSERT ON `mantenimiento` FOR EACH ROW BEGIN
    DECLARE duracion DECIMAL(10,3);
    IF NEW.fecha_inicio IS NOT NULL AND NEW.fecha_fin IS NOT NULL THEN
        SET duracion = TIMESTAMPDIFF(SECOND, NEW.fecha_inicio, NEW.fecha_fin);
    ELSE
        SET duracion = NULL;
    END IF;

    INSERT INTO logs_transacciones (
        usuario_id, fecha, tabla_afectada, accion, detalle,
        ip_usuario, nivel_log, inicio_operacion, fin_operacion, duracion
    ) VALUES (
        NEW.usuario_id,
        NOW(),
        'mantenimiento',
        'insert',
        CONCAT(
            'Mantenimiento registrado: ID=', NEW.id,
            ', Maquinaria=', NEW.maquinaria_id,
            ', Tipo=', NEW.tipo_mantenimiento,
            ', Estado=', NEW.resultado
        ),
        SUBSTRING_INDEX(USER(), '@', -1),
        'INFO',
        NEW.fecha_inicio,
        NEW.fecha_fin,
        duracion
    );
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `maquinaria`
--

CREATE TABLE `maquinaria` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tipo` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `estado` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fecha_adquisicion` date NOT NULL,
  `ubicacion` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ultima_revision` timestamp NULL DEFAULT NULL,
  `proxima_revision` timestamp NULL DEFAULT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp(),
  `fecha_modificacion` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materias_primas`
--

CREATE TABLE `materias_primas` (
  `id` int(11) NOT NULL,
  `codigo` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `unidad_medida` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `stock_minimo` int(11) NOT NULL,
  `stock_actual` int(11) NOT NULL DEFAULT 0,
  `fecha_ultima_actualizacion` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `usuario_ultima_actualizacion` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Disparadores `materias_primas`
--
DELIMITER $$
CREATE TRIGGER `tr_materias_primas_before_update` BEFORE UPDATE ON `materias_primas` FOR EACH ROW BEGIN
    IF NEW.stock_actual < NEW.stock_minimo THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El stock actual no puede ser menor que el stock minimo';
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producciones`
--

CREATE TABLE `producciones` (
  `id` int(11) NOT NULL,
  `codigo_lote` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `producto_id` int(11) DEFAULT NULL,
  `cantidad_planificada` decimal(10,2) NOT NULL,
  `cantidad_producida` decimal(10,2) NOT NULL DEFAULT 0.00,
  `estado` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `fecha_inicio` timestamp NOT NULL DEFAULT current_timestamp(),
  `fecha_fin` timestamp NULL DEFAULT NULL,
  `observaciones` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Disparadores `producciones`
--
DELIMITER $$
CREATE TRIGGER `tr_produccion_after_insert` AFTER INSERT ON `producciones` FOR EACH ROW BEGIN
    DECLARE duracion DECIMAL(10,3);
    IF NEW.fecha_inicio IS NOT NULL AND NEW.fecha_fin IS NOT NULL THEN
        SET duracion = TIMESTAMPDIFF(SECOND, NEW.fecha_inicio, NEW.fecha_fin);
    ELSE
        SET duracion = NULL;
    END IF;

    INSERT INTO logs_transacciones (
        usuario_id, fecha, tabla_afectada, accion, detalle,
        ip_usuario, nivel_log, inicio_operacion, fin_operacion, duracion
    ) VALUES (
        NEW.usuario_id,
        NOW(),
        'producciones',
        'insert',
        CONCAT(
            'Producci?n creada: ID=', NEW.id,
            ', Codigo Lote=', NEW.codigo_lote,
            ', Estado=', NEW.estado,
            ', Cantidad Planificada=', NEW.cantidad_planificada
        ),
        SUBSTRING_INDEX(USER(), '@', -1),
        'INFO',
        NEW.fecha_inicio,
        NEW.fecha_fin,
        duracion
    );
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp(),
  `fecha_modificacion` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `activo` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password_hash` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `rol_id` int(11) DEFAULT NULL,
  `ultimo_acceso` timestamp NULL DEFAULT NULL,
  `ip_ultima_sesion` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `intentos_fallidos` int(11) DEFAULT 0,
  `bloqueado` tinyint(1) DEFAULT 0,
  `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp(),
  `fecha_modificacion` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `controles_calidad`
--
ALTER TABLE `controles_calidad`
  ADD PRIMARY KEY (`id`),
  ADD KEY `controles_calidad_fk_prod` (`produccion_id`),
  ADD KEY `controles_calidad_fk_user` (`usuario_id`),
  ADD KEY `idx_controles_fecha` (`fecha_control`);

--
-- Indices de la tabla `detalle_produccion`
--
ALTER TABLE `detalle_produccion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `detalle_prod_fk_prod` (`produccion_id`),
  ADD KEY `detalle_prod_fk_materia` (`materia_prima_id`);

--
-- Indices de la tabla `logs_transacciones`
--
ALTER TABLE `logs_transacciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `logs_fk_user` (`usuario_id`);

--
-- Indices de la tabla `mantenimiento`
--
ALTER TABLE `mantenimiento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `mantenimiento_fk_maquina` (`maquinaria_id`),
  ADD KEY `mantenimiento_fk_user` (`usuario_id`),
  ADD KEY `idx_mantenimiento_fecha` (`fecha`);

--
-- Indices de la tabla `maquinaria`
--
ALTER TABLE `maquinaria`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `materias_primas`
--
ALTER TABLE `materias_primas`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`),
  ADD KEY `materias_primas_fk_usuario` (`usuario_ultima_actualizacion`),
  ADD KEY `idx_materias_stock` (`stock_actual`,`stock_minimo`);

--
-- Indices de la tabla `producciones`
--
ALTER TABLE `producciones`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo_lote` (`codigo_lote`),
  ADD KEY `producciones_fk_usuario` (`usuario_id`),
  ADD KEY `idx_producciones_estado` (`estado`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `usuarios_fk_rol` (`rol_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `controles_calidad`
--
ALTER TABLE `controles_calidad`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `detalle_produccion`
--
ALTER TABLE `detalle_produccion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `logs_transacciones`
--
ALTER TABLE `logs_transacciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `mantenimiento`
--
ALTER TABLE `mantenimiento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `maquinaria`
--
ALTER TABLE `maquinaria`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `materias_primas`
--
ALTER TABLE `materias_primas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `producciones`
--
ALTER TABLE `producciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `controles_calidad`
--
ALTER TABLE `controles_calidad`
  ADD CONSTRAINT `controles_calidad_fk_prod` FOREIGN KEY (`produccion_id`) REFERENCES `producciones` (`id`),
  ADD CONSTRAINT `controles_calidad_fk_user` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `detalle_produccion`
--
ALTER TABLE `detalle_produccion`
  ADD CONSTRAINT `detalle_prod_fk_materia` FOREIGN KEY (`materia_prima_id`) REFERENCES `materias_primas` (`id`),
  ADD CONSTRAINT `detalle_prod_fk_prod` FOREIGN KEY (`produccion_id`) REFERENCES `producciones` (`id`);

--
-- Filtros para la tabla `logs_transacciones`
--
ALTER TABLE `logs_transacciones`
  ADD CONSTRAINT `logs_fk_user` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `mantenimiento`
--
ALTER TABLE `mantenimiento`
  ADD CONSTRAINT `mantenimiento_fk_maquina` FOREIGN KEY (`maquinaria_id`) REFERENCES `maquinaria` (`id`),
  ADD CONSTRAINT `mantenimiento_fk_user` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `materias_primas`
--
ALTER TABLE `materias_primas`
  ADD CONSTRAINT `materias_primas_fk_usuario` FOREIGN KEY (`usuario_ultima_actualizacion`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `producciones`
--
ALTER TABLE `producciones`
  ADD CONSTRAINT `producciones_fk_usuario` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_fk_rol` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

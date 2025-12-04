create database fabrica;
use fabrica;

create table roles (
    id int auto_increment primary key,
    nombre varchar(50),
    descripcion varchar(100)
);

create table usuarios (
    id int auto_increment primary key,
    nombre varchar(50),
    email varchar(100),
    password_hash varchar(255),
    rol_id int,
    foreign key (rol_id) references roles(id)
);

create table materias_primas (
    id int auto_increment primary key,
    codigo varchar(50),
    nombre varchar(100),
    unidad_medida varchar(20),
    stock_minimo int
);

create table producciones (
    id int auto_increment primary key,
    codigo_lote varchar(50),
    producto_id int,
    cantidad_planificada int,
    cantidad_producida int,
    estado varchar(30),
    usuario_id int,
    foreign key (usuario_id) references usuarios(id)
);

create table controles_calidad (
    id int auto_increment primary key,
    produccion_id int,
    resultado varchar(50),
    observaciones text,
    inspector varchar(100),
    foreign key (produccion_id) references producciones(id)
);

create table detalle_produccion (
    id int auto_increment primary key,
    produccion_id int,
    materia_prima_id int,
    cantidad_usada int,
    foreign key (produccion_id) references producciones(id),
    foreign key (materia_prima_id) references materias_primas(id)
);

create table maquinaria (
    id int auto_increment primary key,
    nombre varchar(100),
    tipo varchar(50),
    estado varchar(50),
    fecha_adquisicion date,
    ubicacion varchar(100)
);

create table mantenimiento (
    id int auto_increment primary key,
    maquinaria_id int,
    usuario_id int,
    fecha date,
    descripcion text,
    tipo_mantenimiento varchar(30),
    resultado varchar(50),
    foreign key (maquinaria_id) references maquinaria(id),
    foreign key (usuario_id) references usuarios(id)
);

create table logs_transacciones (
    id int auto_increment primary key,
    usuario_id int,
    fecha datetime,
    tabla_afectada varchar(50),
    accion varchar(20),
    detalle text,
    foreign key (usuario_id) references usuarios(id)
);

delimiter $$

create trigger tr_produccion_insert
after insert on producciones
for each row
begin
    insert into logs_transacciones (usuario_id, fecha, tabla_afectada, accion, detalle)
    values (new.usuario_id, now(), 'producciones', 'insert', concat('se agregó la producción con id ', new.id));
end$$

create trigger tr_produccion_update
after update on producciones
for each row
begin
    insert into logs_transacciones (usuario_id, fecha, tabla_afectada, accion, detalle)
    values (new.usuario_id, now(), 'producciones', 'update', concat('se actualizó la producción id ', new.id));
end$$

create trigger tr_produccion_delete
after delete on producciones
for each row
begin
    insert into logs_transacciones (usuario_id, fecha, tabla_afectada, accion, detalle)
    values (old.usuario_id, now(), 'producciones', 'delete', concat('se eliminó la producción id ', old.id));
end$$

create trigger tr_mantenimiento_insert
after insert on mantenimiento
for each row
begin
    insert into logs_transacciones (usuario_id, fecha, tabla_afectada, accion, detalle)
    values (new.usuario_id, now(), 'mantenimiento', 'insert', concat('mantenimiento registrado id ', new.id));
end$$

create trigger tr_mantenimiento_update
after update on mantenimiento
for each row
begin
    insert into logs_transacciones (usuario_id, fecha, tabla_afectada, accion, detalle)
    values (new.usuario_id, now(), 'mantenimiento', 'update', concat('mantenimiento actualizado id ', new.id));
end$$

create trigger tr_mantenimiento_delete
after delete on mantenimiento
for each row
begin
    insert into logs_transacciones (usuario_id, fecha, tabla_afectada, accion, detalle)
    values (old.usuario_id, now(), 'mantenimiento', 'delete', concat('mantenimiento eliminado id ', old.id));
end$$

create trigger tr_materias_insert
after insert on materias_primas
for each row
begin
    insert into logs_transacciones (usuario_id, fecha, tabla_afectada, accion, detalle)
    values (1, now(), 'materias_primas', 'insert', concat('materia prima agregada id ', new.id));
end$$

create trigger tr_materias_update
after update on materias_primas
for each row
begin
    insert into logs_transacciones (usuario_id, fecha, tabla_afectada, accion, detalle)
    values (1, now(), 'materias_primas', 'update', concat('materia prima actualizada id ', new.id));
end$$

create trigger tr_materias_delete
after delete on materias_primas
for each row
begin
    insert into logs_transacciones (usuario_id, fecha, tabla_afectada, accion, detalle)
    values (1, now(), 'materias_primas', 'delete', concat('materia prima eliminada id ', old.id));
end$$

delimiter ;
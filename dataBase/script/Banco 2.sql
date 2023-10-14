CREATE database `bancoBoyaca`;
USE `bancoBoyaca`;

-- -----------------------------------------------------
-- Table `usuario`
-- -----------------------------------------------------
CREATE TABLE `usuario` (
  `cedula` BIGINT(25) NOT NULL,
  `nombres` VARCHAR(45),
  `apellidos` VARCHAR(45),
  `direccion` VARCHAR(45),
  `telefono` BIGINT(25),
  `correo` VARCHAR(45),
  `contrasena` VARCHAR(45),
  `rol` VARCHAR(45),
  PRIMARY KEY (`cedula`));

-- -----------------------------------------------------
-- Table `departamento`
-- -----------------------------------------------------
CREATE TABLE `departamento` (
  `id_departamento` INT NOT NULL,
  `nombre_departamento` VARCHAR(45) NULL,
PRIMARY KEY (`id_departamento`));


-- -----------------------------------------------------
-- Table `municipio`
-- -----------------------------------------------------
CREATE TABLE `municipio` (
	`id_municipio` INT NOT NULL,
	`nombre_municipio` VARCHAR(45),
	`id_departamento_municipio` INT,
	PRIMARY KEY (`id_municipio`),
	FOREIGN KEY (`id_departamento_municipio`) REFERENCES `departamento` (`id_departamento`)
);


-- -----------------------------------------------------
-- Table `sucursal`
-- -----------------------------------------------------
CREATE TABLE `sucursal` (
	`id_sucursal` INT NOT NULL,
	`nombre_sucursal` VARCHAR(45),
	`direccion` VARCHAR(45),
	`telefono` VARCHAR(45),
	`id_municipio_sucursal` INT NOT NULL,
	PRIMARY KEY (`id_sucursal`),
	FOREIGN KEY (`id_municipio_sucursal`) REFERENCES `municipio` (`id_municipio`)
);


-- -----------------------------------------------------
-- Table `cuenta`
-- -----------------------------------------------------
CREATE TABLE `cuenta` (
	`numero_cuenta` BIGINT NOT NULL,
	`id_sucursal_cuenta` INT NULL,
	`saldo` BIGINT,
	`fecha_apertura` DATE,
	`tasa_interes` INT,
	`ultimo_movimiento` VARCHAR(45),
	PRIMARY KEY (`numero_cuenta`),
    FOREIGN KEY (`id_sucursal_cuenta`) REFERENCES `sucursal` (`id_sucursal`)
);

-- -----------------------------------------------------
-- Table `historial_cuenta`
-- -----------------------------------------------------
CREATE TABLE `historial_cuenta` (
	`id_historial` INT NOT NULL,
	`id_numero_cuenta` BIGINT,
	`saldo` BIGINT,
	`movimiento` VARCHAR(45),
	`fecha_movimiento` DATE,
	`descripcion` VARCHAR(45),
	PRIMARY KEY (`id_historial`),
    FOREIGN KEY (`id_numero_cuenta`) REFERENCES `cuenta` (`numero_cuenta`)
);


-- -----------------------------------------------------
-- Table `cuenta_corriente`
-- -----------------------------------------------------
CREATE TABLE `cuenta_corriente` (
	`numero_cuenta` BIGINT NOT NULL,
	PRIMARY KEY (`numero_cuenta`),
    FOREIGN KEY (`numero_cuenta`) REFERENCES `cuenta` (`numero_cuenta`)
);


-- -----------------------------------------------------
-- Table `creditos`
-- -----------------------------------------------------
CREATE TABLE `creditos` (
	`numero_cuenta` BIGINT NOT NULL,
	PRIMARY KEY (`numero_cuenta`),
    FOREIGN KEY (`numero_cuenta`) REFERENCES `cuenta` (`numero_cuenta`)
);


-- -----------------------------------------------------
-- Table `cdt`
-- -----------------------------------------------------
CREATE TABLE `cdt` (
	`numero_cuenta` BIGINT NOT NULL,
	`clausula` VARCHAR(45) NOT NULL,
	`retencion` VARCHAR(45),
	`fecha_finalizacion` DATE,
	`aprox_interes` INT,
	PRIMARY KEY (`numero_cuenta`),
    FOREIGN KEY (`numero_cuenta`) REFERENCES `bancoBoyaca`.`cuenta` (`numero_cuenta`)
);

-- -----------------------------------------------------
-- Modificar Tabla "usuario"
-- -----------------------------------------------------
ALTER TABLE `usuario`
	ADD column `id_municipio_usuario` INT,
	ADD FOREIGN KEY (`id_municipio_usuario`) REFERENCES `municipio`(`id_municipio`);


ALTER TABLE `usuario`
	ADD COLUMN `fecha_nacimiento` DATE,
    ADD COLUMN `fehca_expedicion` DATE;
    
ALTER TABLE `usuario`
	ADD COLUMN `estado` varchar(15);
-- -----------------------------------------------------
-- Modificar Tabla "cuenta"
-- -----------------------------------------------------
ALTER TABLE `cuenta`
	ADD column `id_usuario_cuenta` bigint(25),
    ADD FOREIGN KEY (`id_usuario_cuenta`) REFERENCES `usuario`(`cedula`);
    
-- -----------------------------------------------------
-- Modificar Tabla "municipio"
-- -----------------------------------------------------
ALTER TABLE `MUNICIPIO`
	DROP constraint `municipio_ibfk_1`,
	DROP column `id_departamento_municipio`,
    ADD COLUMN `nombre_departamento` varchar (45);

-- -----------------------------------------------------
-- ELIMINAR Tabla "departamento"
-- -----------------------------------------------------

DROP Table `departamento`;

ALTER TABLE `sucursal`
	ADD COLUMN `estado` varchar(15);
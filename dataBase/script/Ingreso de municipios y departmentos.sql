USE `bancoBoyaca`;

-- ----------------------------
-- Cargar Texto plano
-- ----------------------------
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/departamentos y municipios subir.txt'
INTO TABLE municipio
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
(id_municipio, nombre_municipio, nombre_departamento);


select * from municipio;
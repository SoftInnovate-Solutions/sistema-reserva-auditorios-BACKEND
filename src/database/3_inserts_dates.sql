/*Piso*/
INSERT INTO PISO (NOMBRE_PIS)
VALUES 
    ('Sótano'),
    ('Planta Baja'),
    ('Primer Piso'),
    ('Segundo Piso'),
    ('Tercer Piso'),
    ('Cuarto Piso'),
    ('Quinto Piso'),
    ('Sexto Piso'),
    ('Séptimo Piso'),
    ('Octavo Piso'),
    ('Noveno Piso'),
    ('Décimo Piso');


/*Edificio*/
INSERT INTO EDIFICACION (NOMBRE_EDI)
VALUES 
    ('Bloque Central'),
    ('Sala Docentes'),
    ('Departamento de Fisica'),
    ('Centro de Aguas y Saneamiento Ambiental CASA'),
    ('Centro de alimentos y Productos Ambiental CAPN'),
    ('Departamaneto de Quimica'),
    ('Centros CTA'),
    ('CEB'),
    ('CEF'),
    ('CEIC'),
    ('Gabinete Fisica CE.Fis'),
    ('CEQA'),
    ('Depatamento de Biologia'),
    ('Elektro'),
    ('Simulacion Metodos y Seguridad'),
    ('CEMAT'),
    ('Palacio de la Ciencia y Cultura'),
    ('Area Abierta de Estudio 1'),
    ('Area Abierta de Estudio 2'),
    ('Planta de tratamiento de Agua'),
    ('Planta de alimentos'),
    ('Planta Agroquimico'),
    ('Planta de Biogas'),
    ('Laboratorio de Materiales'),
    ('CAD-CAM'),
    ('Automatizacion y Control Planta de Bioprocesos'),
    ('Parqueo Facultativo'),
    ('Dep. Industrial, CEB'),
    ('CEInf.'),
    ('Planta de Amoniaco'),
    ('CESA'),
    ('Academico 2'),
    ('Sala de Estudios de Ing. Civil'),
    ('Planta de Procesos Industriales'),
    ('Memi'),
    ('Posgrado FCyT'),
    ('Dep. Informatica y Sistema'),
    ('Sub. Estacion de Potencia'),
    ('Dep. Mantenimiento'),
    ('Dep. Infraestructura');
    


/*Facultad*/
INSERT INTO FACULTAD (NOMBRE_FAC)
VALUES 
    ('Facultad de Ciencias Económicas'),
    ('Facultad de Ciencias y Tecnología'),
    ('Facultad de Humanidades y Ciencias de la Educación'),
    ('Facultad de Ciencias Jurídicas y Políticas'),
    ('Facultad de Arquitectura y Ciencias del Hábitat'),
    ('Facultad de Ciencias Agrícolas y Pecuarias'),
    ('Facultad de Medicina'),
    ('Facultad de Odontología'),
    ('Facultad de Ciencias Bioquímicas y Farmacéuticas'),
    ('Facultad Politécnica del Valle Alto'),
    ('Facultad de Ciencias Sociales'),
    ('Facultad de Desarrollo Rural y Territorial'),
    ('Escuela Forestal'),
    ('Facultad de Enfermería'),
    ('Unidad Desconcentrada del Valle de Sacta'),
    ('Facultad de Ciencias Veterinarias');

/*Tipo ambiente*/
INSERT INTO TIPO_AMBIENTE (NOMBRE_TA)
VALUES 
    ('Laboratorio'),
    ('Aula'),
    ('Oficina'),
    ('Sala de Conferencias');

/*Estado ambiente*/
INSERT INTO ESTADO_AMBIENTE (NOMBRE_EA)
VALUES 
    ('Disponible'),
    ('No Disponible');

/*Tipo_Final*/
INSERT INTO TIPO_FINAL (NOMBRE_TF) VALUES
    ('Docente'),
    ('Auxiliar'),
    ('Estudiante');

INSERT INTO DIA (NOMBRE_DIA) VALUES
    ('Lunes'),
    ('Martes'),
    ('Miercoles'),
    ('Jueves'),
    ('Viernes'),
    ('Sabado'),
    ('Domingo');

INSERT INTO bloque (nombre_blo, hora_inicio_blo, hora_fin_blo)
VALUES 
('A', '06:45:00', '08:15:00'),
('B', '08:15:00', '09:45:00'),
('C', '09:45:00', '11:15:00'),
('D', '11:15:00', '12:45:00'),
('E', '12:45:00', '14:15:00'),
('F', '14:15:00', '15:45:00'),
('G', '15:45:00', '17:15:00'),
('H', '17:15:00', '18:45:00'),
('I', '18:45:00', '20:15:00'),
('J', '20:15:00', '21:45:00');


INSERT INTO usuario (nombre_usu, contrasenia_usu)
VALUES
  ('Anna', 'dd6833732ae7f9d7b201c42032173bdb157fd8737ae92b30bb549eae591ee108bf1f275327bb418cf0c6cfdece3067e6a3dc26737d99096fba9d8e3a6c428730'),
  ('Peter', 'd638891b37b933d03c88b0d08e73da5680606aed62fc2a91dadcf795340ff38cb73c4414eee767d92196b4721038988461ea097a028e51580c3a7b8fd0b5a14f'),
  ('Robert', 'b6f459289560694ba16f07ee610ff33e5b6002f39b3107d092b2ce95b030f456781ef4a7ec6dfe59fc73d7e62502b31cc0f49e6509c48e731740a541582067ee'),
  ('Manuel', 'd1707fcbab1f82f115c71e5c7bbdfc56eadace624a1c12db0685c4aba9dab0e65d01939d38293f758db7c5b55d1bd4d058fead0e3499e5c50381f46c0b747c57'),
  ('Paul', '27ad20032f5bf485ed3bd4011caca1ea998ea2c54a58a2e44aff4dfea1a6d71ac5cdfeaf15402097690ce02459ba50a20894dafd53886c09975e75c13b5565d6'),
  ('Jorge', '63e9a5363975b35dd779952afbb355612542af0f0e36629c725874f66711421a0de217dcf774de2f247327cbffb445e801e921cb41314c6e57acd8b62295621d'),
  ('Antonio', '08211e23d85690762b52cd2cbf77285d80760899b6d2097a7f9b5594b31d01cf6a764f26059676cf3c4b309e650e8ae3a3bd9fd3e9235f93b81cef9adde1a4b9'),
  ('Miguel', 'fbbfb18f24eaa6f1d41a1822bcbeee9949ad27c38d34023dcf9f1b0b4e9b84f03d62d5731c39a3215bf60e70095fd6265241b3b88ba824bb1609109cea72585f'),
  ('Fatima', 'f5c45a46b2e46a80249b58e54310f85ead9f4431411ab9060a197faeeb56503964f55f9e8f0baef8a54c40030dcaf739964995dd1ae8aad10c25879344512cdf'),
  ('Andres', 'c764222c35858ba115193bedc9f5bcf0146b453554e0471dd461eff30ed6b930f1be31b3908c1567d781e93b6e0465e7f0ee21bb675831cb45a2b420b4c48c5b'),
  ('Patricia', 'f38501894f151c88b4db35a7a6964d410527ebe0f8786e94c36d32b955bc02aa5253da22541fb6316244668b80b48c0191b18ab4a5dbc3677535f674b4ef9310'),
  ('Juan', '8ec42b2db20d1fe1904a249fb5085324e17f106633a51d17a3135e35a5cfeced14cb8460daf9b1b9fd10764d80403e95e1e1e7cb52a8bbf3d9f4e40110b25b49'),
  ('Maicol', 'fd595db0539d1cdb165d8f2fdd2deebfeca950d8c7e9df8f1c3af19420ab03e81ae446e4dfb949fd5820f8963e6ae1dc1e83eb959cf7c54aa885095b25073514'),
  ('Pandora', 'daf03b2815acd65102626866fc1e2f61b89c7d7c989e39ceb6fb16a41d3659d8d9a124d219b819cabdc43790eef64c82651291eb1951eda1d316b7bc734d403b'),
  ('Francisco', '1f69dbb9594deee270ea069dcbd57ff8a74fe9006107c918a65613138669a98828fe5f7a24f10a61cfc8b4d94d3904d385da7c4b2bc3bb3d6f42dbda07a19716'),
  ('Ramiro', '987742c44da91cbd8e1e52411d59dd88087f659b6cd28fcfff2ac6ca5a55c2519dfd2f73d50bb0da5165468af27ebfafdd008c2f96e764570e353f9ebd36d4c3'),
  ('Jemima', '2f36c163e07c26e9db645dab605cb253caf60ba8083ffa23d7cc3548343eba2a3da1037894cc8dc0a195faa9d40a777deeb6c8da348414feb02a653242357267'),
  ('Daniel', '6be7ed227073b4b8d47ffa3919cf910f44ed6aac05136ccedce466cb7a8b9e870bc74d0940e4fbd2f7c1974825a31bbc39c054b49bbbe0a1fff98069b8a58855'),
  ('Franz', 'ff99f79a9c7e66650a300517112fcc53c25c7f9f4552f38ce65ab8bb9438092159981e1ccf81925b41a5f21bf9a690950cf6987a681f3ef74c85787eda43d680'),
  ('Cecilia', 'f144de19ef83f6d205d200f960998f35ed21dc3ab64fe42716b3a47dbf1261739ed0438fa0ddc64cd5783dfec4b5c8609a793356deeb551f48cc485d9fd34ad5'),
  ('Elena', 'af1c0a20080b5c788e8436f877a97afddb509a72272cc9e122bfb411900756e62b188a9372a26f799c91e74024611e850f471519d402f8a825aa12e73f1b0106');


INSERT INTO administrador (cod_usuario,alias_adm)
VALUES (1, 'Anita');


INSERT INTO final (cod_usuario,cod_tipo_final,codigo_sis_fin)
VALUES
  (2,1, '2019045'),
  (3,1, '2018056'),
  (4,2, '2000082'),
  (5,2, '2001155'),
  (6,1, '2019589'),
  (7,2, '2011236'),
  (8,2, '2520365'),
  (9,2, '2000254'),
  (10,2, '1219045'),
  (11,2, '2569325'),
  (12,2, '2019581'),
  (13,1, '2532956'),
  (14,1, '2045296'),
  (15,2, '2259635'),
  (16,2, '2896572'),
  (17,1, '2569863'),
  (18,1, '2052369'),
  (19,1, '2069863'),
  (20,1, '2569835'),
  (21,1, '2589735');

INSERT INTO grupo (nombre_gru)
VALUES 
('G1'),
('G2'),
('G3'),
('G4'),
('G5'),
('G6'),
('G7'),
('G8'),
('G9'),
('G10');

INSERT INTO materia (nombre_mat)
VALUES
('INTRO A LA PROGRAMACION'),
('ELEMENTOS'),
('BASE DE DATOS'),
('TALLER DE INGENIERIA DE SOFTWARE'),
('INTELIGENCIA ARTIFICIAL'),
('CALCULO 2'),
('REDES'),
('ALGEBRA 1'),
('FISICA GENERAL');
  
INSERT INTO imparticion (cod_usuario, cod_materia, cod_grupo, cantidad_estudiantes_imp)
VALUES
(2,1,1,120),
(2,2,1,100),
(6,1,2,120),
(3,3,1,60),
(13,5,1,40),
(15,1,1,120),
(16,2,1,100);
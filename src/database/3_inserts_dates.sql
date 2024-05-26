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
    ('Edificio A'),
    ('Edificio B'),
    ('Edificio C'),
    ('Edificio D');


/*Facultad*/
INSERT INTO FACULTAD (NOMBRE_FAC)
VALUES 
    ('Facultad de Ciencias'),
    ('Facultad de Ingeniería'),
    ('Facultad de Artes'),
    ('Facultad de Derecho');

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
  ('Anna', '5ac8ca9b2504992a1ce21a39feb8a54c1b9964ec455751b163fece0235ba07ea87eb0204ef7922a1a6987876d40609681f1ddf11f5b7f8952954c22101e2c66c'),
  ('Peter', '1508ffa48c6e28bfaa97ba7435b6614a348716274edbf3bfa494f4f0b41d263ba5f98ec6d8d08b7d5323ec0c53a76c828b71983f6d6e9644f428eff274cafc04'),
  ('Robert', '35d3a6018875b4266c58c75b5ef51290674dbfbb43c5ba069d620421aceac187356a76a620fa9664aa28eca798cc7f0c6b1c16dbc4767cb15219d6368cec469d'),
  ('Manuel', 'cce0646867a245fcb61c8fa03cd581ac481c89bb3d3f3fd30a454e2e472ba1c0027657394542575d2f35f7304b7d76dee1fb6c61116850cb6fcea30a4bf38750'),
  ('Paul', 'b17a21f5882afecd2b5ca2615e3847420607e5edc1a72c7720fe5bfbb80e6c5274116b73b53ef24d9916726070a85ca55518ec2c55b8cd24c56360ac708972a0'),
  ('Jorge', '33fd33850bb42c0eda854babd9eb6fbbf913ed942270cc81c5b29b315f9423ebafe9ce2fbaf49dc74fa3a3f27a9aaeaf6333ff35ce3801742bb7ecbb245449a7'),
  ('Antonio', 'b9215ffe444384a2b91a1dbb6c69dc969e7f29e13b916cda6d3d6d059d7198ed85c3754011725fc8c5bc8d7fb4a02d30d2bc00dffe4cb35e5cbbd80888a94f17'),
  ('Miguel', 'ac901fd5503c15aea60e6887d47ae98c5015b5000d979f730c9ad6970204e7a21e2682961daf5f7dfee8aa4bcce859a54b2fdb37267bcde2864ecc99d1e80de5'),
  ('Fatima', '9bce1f7fb48e51a41992be11b847466b9d928fa392520929016af1b1468591a925b71869166efe0eaf77324b3d073508462710a469dbe8cd2251ee37446277c9'),
  ('Andres', '1fe9f8fd116b1bf9e9c400a6731f125558dc915310e522ba6b421f9d40b9659f16f8be3e6a15ba88db2e223b5cc93e2d02da635ff3380eefd1d4be988ae82407'),
  ('Patricia', '6760e9039559a7aaf5f9c3deddd6f7b7bb5aaa38eac7b80a96fd3386cf23038e856fb1daaa66112f39aca30ed2ce9a16ea46e35f51f6e2df81ca37f0c29ef08e'),
  ('Juan', 'fc4febc5dac1f5c6b4dde5857011aedd02ce96f15dcd064d65cef4973dad53827ee69def4a2ad5949b5aca5e69c77850c2ba3b17e1e6263d384ad878dbfba846'),
  ('Miguel', '06d3394397b41e05dbbf1c4b675fcc5771c1c5f207bff782304fa3754a50cc3ab6983ef0e8cef89ba4a34febc1a7b83a06ea812d8c2dee8c43b4b752ef176d5b'),
  ('Pandora', '4d63c58ed92175462fb957b5596ec736bd238385949e558cd4f291ee840cae185a96d18a3161d53201e408d684987c52533119d4e9299bb866d53e99129647ae'),
  ('Francisco', '6cbf24ba8042a7e6185e1dc64b3c02ee4b89df7de09d3d00a942e4f72321ec1350dff9b5bfd9c9bb2e4fe8eb2eb61c5806a67bf3cd42adf57231ece3d499c99c'),
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
/*==============================================================*/
/* DBMS name:      PostgreSQL 8                                 */
/* Created on:     28/05/2024 18:14:26                          */
/*==============================================================*/


drop index ADMINISTRADOR_PK;

drop table ADMINISTRADOR;

drop index TIENE1_FK;

drop index ESTA2_FK;

drop index HUBICA1_FK;

drop index AJUSTE_AMBIENTE_PK;

drop table AJUSTE_AMBIENTE;

drop index ENCUENTRA1_FK;

drop index PERTENECE1_FK;

drop index PERTENECE2_FK;

drop index ES1_FK;

drop index ESTA1_FK;

drop index AMBIENTE_PK;

drop table AMBIENTE;

drop index BLOQUE_PK;

drop table BLOQUE;

drop index TIENE3_FK;

drop index COMUNICADO_PK;

drop table COMUNICADO;

drop index DIA_PK;

drop table DIA;

drop index EDIFICACION_PK;

drop table EDIFICACION;

drop index ESTADO_AMBIENTE_PK;

drop table ESTADO_AMBIENTE;

drop index FACULTAD_PK;

drop table FACULTAD;

drop index ES_FK;

drop index FINAL_PK;

drop table FINAL;

drop index GRUPO_PK;

drop table GRUPO;

drop index IMPARTE_FK;

drop index EN2_FK;

drop index EN1_FK;

drop index IMPARTICION_PK;

drop table IMPARTICION;

drop index MATERIA_PK;

drop table MATERIA;

drop index RECIBE_FK;

drop index ENVIA_FK;

drop index MENSAJE_PK;

drop table MENSAJE;

drop index TIENE5_FK;

drop index RECIBE1_FK;

drop index ENVIA1_FK;

drop index NOTIFICACION_RESERVA_PK;

drop table NOTIFICACION_RESERVA;

drop index PERIODO_RESERVA_PK;

drop table PERIODO_RESERVA;

drop index PISO_PK;

drop table PISO;

drop index EL2_FK;

drop index EL1_FK;

drop index TIENE2_FK;

drop index ESTA3_FK;

drop index HUBICA2_FK;

drop index REALIZA_FK;

drop index RESERVA_PK;

drop table RESERVA;

drop index TIPO_AMBIENTE_PK;

drop table TIPO_AMBIENTE;

drop index TIPO_FINAL_PK;

drop table TIPO_FINAL;

drop index ES5_FK;

drop index ES3_FK;

drop index USUARIO_PK;

drop table USUARIO;

/*==============================================================*/
/* Table: ADMINISTRADOR                                         */
/*==============================================================*/
create table ADMINISTRADOR (
   COD_USUARIO          INT4                 not null,
   ALIAS_ADM            CHAR(25)             not null,
   constraint PK_ADMINISTRADOR primary key (COD_USUARIO)
);

/*==============================================================*/
/* Index: ADMINISTRADOR_PK                                      */
/*==============================================================*/
create unique index ADMINISTRADOR_PK on ADMINISTRADOR (
COD_USUARIO
);

/*==============================================================*/
/* Table: AJUSTE_AMBIENTE                                       */
/*==============================================================*/
create table AJUSTE_AMBIENTE (
   COD_DIA              INT4                 not null,
   COD_BLOQUE           INT4                 not null,
   COD_AMBIENTE         INT4                 not null,
   COD_AJUSTE_AMBIENTE  SERIAL               not null,
   FECHA_AA             DATE                 not null,
   constraint PK_AJUSTE_AMBIENTE primary key (COD_DIA, COD_BLOQUE, COD_AMBIENTE, COD_AJUSTE_AMBIENTE)
);

/*==============================================================*/
/* Index: AJUSTE_AMBIENTE_PK                                    */
/*==============================================================*/
create unique index AJUSTE_AMBIENTE_PK on AJUSTE_AMBIENTE (
COD_DIA,
COD_BLOQUE,
COD_AMBIENTE,
COD_AJUSTE_AMBIENTE
);

/*==============================================================*/
/* Index: HUBICA1_FK                                            */
/*==============================================================*/
create  index HUBICA1_FK on AJUSTE_AMBIENTE (
COD_DIA
);

/*==============================================================*/
/* Index: ESTA2_FK                                              */
/*==============================================================*/
create  index ESTA2_FK on AJUSTE_AMBIENTE (
COD_BLOQUE
);

/*==============================================================*/
/* Index: TIENE1_FK                                             */
/*==============================================================*/
create  index TIENE1_FK on AJUSTE_AMBIENTE (
COD_AMBIENTE
);

/*==============================================================*/
/* Table: AMBIENTE                                              */
/*==============================================================*/
create table AMBIENTE (
   COD_AMBIENTE         SERIAL               not null,
   COD_FACULTAD         INT4                 not null,
   COD_ESTADO_AMBIENTE  INT4                 not null,
   COD_PISO             INT4                 not null,
   COD_TIPO_AMBIENTE    INT4                 not null,
   COD_EDIFICACION      INT4                 not null,
   NOMBRE_AMB           CHAR(60)             not null,
   CAPACIDAD_AMB        INT4                 not null,
   UBICACION_AMB        CHAR(100)            not null,
   DESCRIPCION_AMB      CHAR(255)            not null,
   ALBERGACION_MAX_AMB  INT4                 not null,
   ALBERGACION_MIN_AMB  INT4                 not null,
   constraint PK_AMBIENTE primary key (COD_AMBIENTE)
);

/*==============================================================*/
/* Index: AMBIENTE_PK                                           */
/*==============================================================*/
create unique index AMBIENTE_PK on AMBIENTE (
COD_AMBIENTE
);

/*==============================================================*/
/* Index: ESTA1_FK                                              */
/*==============================================================*/
create  index ESTA1_FK on AMBIENTE (
COD_ESTADO_AMBIENTE
);

/*==============================================================*/
/* Index: ES1_FK                                                */
/*==============================================================*/
create  index ES1_FK on AMBIENTE (
COD_TIPO_AMBIENTE
);

/*==============================================================*/
/* Index: PERTENECE2_FK                                         */
/*==============================================================*/
create  index PERTENECE2_FK on AMBIENTE (
COD_FACULTAD
);

/*==============================================================*/
/* Index: PERTENECE1_FK                                         */
/*==============================================================*/
create  index PERTENECE1_FK on AMBIENTE (
COD_EDIFICACION
);

/*==============================================================*/
/* Index: ENCUENTRA1_FK                                         */
/*==============================================================*/
create  index ENCUENTRA1_FK on AMBIENTE (
COD_PISO
);

/*==============================================================*/
/* Table: BLOQUE                                                */
/*==============================================================*/
create table BLOQUE (
   COD_BLOQUE           SERIAL               not null,
   NOMBRE_BLO           CHAR(1)              not null,
   HORA_INICIO_BLO      TIME                 not null,
   HORA_FIN_BLO         TIME                 not null,
   constraint PK_BLOQUE primary key (COD_BLOQUE)
);

/*==============================================================*/
/* Index: BLOQUE_PK                                             */
/*==============================================================*/
create unique index BLOQUE_PK on BLOQUE (
COD_BLOQUE
);

/*==============================================================*/
/* Table: COMUNICADO                                            */
/*==============================================================*/
create table COMUNICADO (
   COD_COMUNICADO       SERIAL               not null,
   COD_TIPO_FINAL       INT4                 not null,
   TITULO_COM           CHAR(40)             not null,
   ASUNTO_COM           CHAR(500)            not null,
   FECHA_EMISION_COM    DATE                 not null,
   constraint PK_COMUNICADO primary key (COD_COMUNICADO)
);

/*==============================================================*/
/* Index: COMUNICADO_PK                                         */
/*==============================================================*/
create unique index COMUNICADO_PK on COMUNICADO (
COD_COMUNICADO
);

/*==============================================================*/
/* Index: TIENE3_FK                                             */
/*==============================================================*/
create  index TIENE3_FK on COMUNICADO (
COD_TIPO_FINAL
);

/*==============================================================*/
/* Table: DIA                                                   */
/*==============================================================*/
create table DIA (
   COD_DIA              SERIAL               not null,
   NOMBRE_DIA           CHAR(10)             not null,
   constraint PK_DIA primary key (COD_DIA)
);

/*==============================================================*/
/* Index: DIA_PK                                                */
/*==============================================================*/
create unique index DIA_PK on DIA (
COD_DIA
);

/*==============================================================*/
/* Table: EDIFICACION                                           */
/*==============================================================*/
create table EDIFICACION (
   COD_EDIFICACION      SERIAL               not null,
   NOMBRE_EDI           CHAR(20)             not null,
   constraint PK_EDIFICACION primary key (COD_EDIFICACION)
);

/*==============================================================*/
/* Index: EDIFICACION_PK                                        */
/*==============================================================*/
create unique index EDIFICACION_PK on EDIFICACION (
COD_EDIFICACION
);

/*==============================================================*/
/* Table: ESTADO_AMBIENTE                                       */
/*==============================================================*/
create table ESTADO_AMBIENTE (
   COD_ESTADO_AMBIENTE  SERIAL               not null,
   NOMBRE_EA            CHAR(15)             not null,
   constraint PK_ESTADO_AMBIENTE primary key (COD_ESTADO_AMBIENTE)
);

/*==============================================================*/
/* Index: ESTADO_AMBIENTE_PK                                    */
/*==============================================================*/
create unique index ESTADO_AMBIENTE_PK on ESTADO_AMBIENTE (
COD_ESTADO_AMBIENTE
);

/*==============================================================*/
/* Table: FACULTAD                                              */
/*==============================================================*/
create table FACULTAD (
   COD_FACULTAD         SERIAL               not null,
   NOMBRE_FAC           CHAR(50)             not null,
   constraint PK_FACULTAD primary key (COD_FACULTAD)
);

/*==============================================================*/
/* Index: FACULTAD_PK                                           */
/*==============================================================*/
create unique index FACULTAD_PK on FACULTAD (
COD_FACULTAD
);

/*==============================================================*/
/* Table: FINAL                                                 */
/*==============================================================*/
create table FINAL (
   COD_USUARIO          INT4                 not null,
   COD_TIPO_FINAL       INT4                 not null,
   CODIGO_SIS_FIN       CHAR(50)             not null,
   constraint PK_FINAL primary key (COD_USUARIO)
);

/*==============================================================*/
/* Index: FINAL_PK                                              */
/*==============================================================*/
create unique index FINAL_PK on FINAL (
COD_USUARIO
);

/*==============================================================*/
/* Index: ES_FK                                                 */
/*==============================================================*/
create  index ES_FK on FINAL (
COD_TIPO_FINAL
);

/*==============================================================*/
/* Table: GRUPO                                                 */
/*==============================================================*/
create table GRUPO (
   COD_GRUPO            SERIAL               not null,
   NOMBRE_GRU           CHAR(30)             not null,
   constraint PK_GRUPO primary key (COD_GRUPO)
);

/*==============================================================*/
/* Index: GRUPO_PK                                              */
/*==============================================================*/
create unique index GRUPO_PK on GRUPO (
COD_GRUPO
);

/*==============================================================*/
/* Table: IMPARTICION                                           */
/*==============================================================*/
create table IMPARTICION (
   COD_USUARIO          INT4                 not null,
   COD_MATERIA          INT4                 not null,
   COD_GRUPO            INT4                 not null,
   COD_IMPARTICION      SERIAL               not null,
   CANTIDAD_ESTUDIANTES_IMP INT4                 not null,
   constraint PK_IMPARTICION primary key (COD_USUARIO, COD_MATERIA, COD_GRUPO, COD_IMPARTICION)
);

/*==============================================================*/
/* Index: IMPARTICION_PK                                        */
/*==============================================================*/
create unique index IMPARTICION_PK on IMPARTICION (
COD_USUARIO,
COD_MATERIA,
COD_GRUPO,
COD_IMPARTICION
);

/*==============================================================*/
/* Index: EN1_FK                                                */
/*==============================================================*/
create  index EN1_FK on IMPARTICION (
COD_MATERIA
);

/*==============================================================*/
/* Index: EN2_FK                                                */
/*==============================================================*/
create  index EN2_FK on IMPARTICION (
COD_GRUPO
);

/*==============================================================*/
/* Index: IMPARTE_FK                                            */
/*==============================================================*/
create  index IMPARTE_FK on IMPARTICION (
COD_USUARIO
);

/*==============================================================*/
/* Table: MATERIA                                               */
/*==============================================================*/
create table MATERIA (
   COD_MATERIA          SERIAL               not null,
   NOMBRE_MAT           CHAR(90)             not null,
   constraint PK_MATERIA primary key (COD_MATERIA)
);

/*==============================================================*/
/* Index: MATERIA_PK                                            */
/*==============================================================*/
create unique index MATERIA_PK on MATERIA (
COD_MATERIA
);

/*==============================================================*/
/* Table: MENSAJE                                               */
/*==============================================================*/
create table MENSAJE (
   COD_USUARIO          INT4                 not null,
   USU_COD_USUARIO      INT4                 not null,
   COD_MENSAJE          SERIAL               not null,
   CONTENIDO_MEN        CHAR(150)            not null,
   FECHA_EMISION_MEN    DATE                 not null,
   constraint PK_MENSAJE primary key (COD_USUARIO, USU_COD_USUARIO, COD_MENSAJE)
);

/*==============================================================*/
/* Index: MENSAJE_PK                                            */
/*==============================================================*/
create unique index MENSAJE_PK on MENSAJE (
COD_USUARIO,
USU_COD_USUARIO,
COD_MENSAJE
);

/*==============================================================*/
/* Index: ENVIA_FK                                              */
/*==============================================================*/
create  index ENVIA_FK on MENSAJE (
COD_USUARIO
);

/*==============================================================*/
/* Index: RECIBE_FK                                             */
/*==============================================================*/
create  index RECIBE_FK on MENSAJE (
USU_COD_USUARIO
);

/*==============================================================*/
/* Table: NOTIFICACION_RESERVA                                  */
/*==============================================================*/
create table NOTIFICACION_RESERVA (
   USU_COD_USUARIO      INT4                 not null,
   COD_USUARIO          INT4                 not null,
   COD_AMBIENTE         INT4                 not null,
   COD_NOTIFICACION_RESERVA SERIAL               not null,
   FECHA_NR             DATE                 not null,
   HORA_NR              TIME                 not null,
   constraint PK_NOTIFICACION_RESERVA primary key (USU_COD_USUARIO, COD_USUARIO, COD_AMBIENTE, COD_NOTIFICACION_RESERVA)
);

/*==============================================================*/
/* Index: NOTIFICACION_RESERVA_PK                               */
/*==============================================================*/
create unique index NOTIFICACION_RESERVA_PK on NOTIFICACION_RESERVA (
USU_COD_USUARIO,
COD_USUARIO,
COD_AMBIENTE,
COD_NOTIFICACION_RESERVA
);

/*==============================================================*/
/* Index: ENVIA1_FK                                             */
/*==============================================================*/
create  index ENVIA1_FK on NOTIFICACION_RESERVA (
USU_COD_USUARIO
);

/*==============================================================*/
/* Index: RECIBE1_FK                                            */
/*==============================================================*/
create  index RECIBE1_FK on NOTIFICACION_RESERVA (
COD_USUARIO
);

/*==============================================================*/
/* Index: TIENE5_FK                                             */
/*==============================================================*/
create  index TIENE5_FK on NOTIFICACION_RESERVA (
COD_AMBIENTE
);

/*==============================================================*/
/* Table: PERIODO_RESERVA                                       */
/*==============================================================*/
create table PERIODO_RESERVA (
   COD_PERIODO_RESERVA  SERIAL               not null,
   FECHA_INICIO_GENERAL_PER DATE                 not null,
   FECHA_FIN_GENERAL_PER DATE                 not null,
   FECHA_INICIO_DOCENTE_PER DATE                 not null,
   FECHA_FIN_DOCENTE_PER DATE                 not null,
   FECHA_INICIO_AUXILIAR_PER DATE                 not null,
   FECHA_FIN_AUXILIAR_PER DATE                 not null,
   NOTIFICACION_PER     DATE                 not null,
   ESTADO_VISUALIZACION_PER BOOL                 not null,
   constraint PK_PERIODO_RESERVA primary key (COD_PERIODO_RESERVA)
);

/*==============================================================*/
/* Index: PERIODO_RESERVA_PK                                    */
/*==============================================================*/
create unique index PERIODO_RESERVA_PK on PERIODO_RESERVA (
COD_PERIODO_RESERVA
);

/*==============================================================*/
/* Table: PISO                                                  */
/*==============================================================*/
create table PISO (
   COD_PISO             SERIAL               not null,
   NOMBRE_PIS           CHAR(20)             not null,
   constraint PK_PISO primary key (COD_PISO)
);

/*==============================================================*/
/* Index: PISO_PK                                               */
/*==============================================================*/
create unique index PISO_PK on PISO (
COD_PISO
);

/*==============================================================*/
/* Table: RESERVA                                               */
/*==============================================================*/
create table RESERVA (
   COD_USUARIO          INT4                 not null,
   COD_DIA              INT4                 not null,
   COD_BLOQUE           INT4                 not null,
   COD_AMBIENTE         INT4                 not null,
   COD_GRUPO            INT4                 not null,
   COD_MATERIA          INT4                 not null,
   COD_RESERVA          SERIAL               not null,
   FECHA_RES            DATE                 not null,
   CANTIDAD_ESTUDIANTES_RES INT4                 not null,
   CANTIDAD_ESTUDIANTES_TOTAL_RES INT4                 not null,
   constraint PK_RESERVA primary key (COD_USUARIO, COD_DIA, COD_BLOQUE, COD_AMBIENTE, COD_GRUPO, COD_MATERIA, COD_RESERVA)
);

/*==============================================================*/
/* Index: RESERVA_PK                                            */
/*==============================================================*/
create unique index RESERVA_PK on RESERVA (
COD_USUARIO,
COD_DIA,
COD_BLOQUE,
COD_AMBIENTE,
COD_GRUPO,
COD_MATERIA,
COD_RESERVA
);

/*==============================================================*/
/* Index: REALIZA_FK                                            */
/*==============================================================*/
create  index REALIZA_FK on RESERVA (
COD_USUARIO
);

/*==============================================================*/
/* Index: HUBICA2_FK                                            */
/*==============================================================*/
create  index HUBICA2_FK on RESERVA (
COD_DIA
);

/*==============================================================*/
/* Index: ESTA3_FK                                              */
/*==============================================================*/
create  index ESTA3_FK on RESERVA (
COD_BLOQUE
);

/*==============================================================*/
/* Index: TIENE2_FK                                             */
/*==============================================================*/
create  index TIENE2_FK on RESERVA (
COD_AMBIENTE
);

/*==============================================================*/
/* Index: EL1_FK                                                */
/*==============================================================*/
create  index EL1_FK on RESERVA (
COD_GRUPO
);

/*==============================================================*/
/* Index: EL2_FK                                                */
/*==============================================================*/
create  index EL2_FK on RESERVA (
COD_MATERIA
);

/*==============================================================*/
/* Table: TIPO_AMBIENTE                                         */
/*==============================================================*/
create table TIPO_AMBIENTE (
   COD_TIPO_AMBIENTE    SERIAL               not null,
   NOMBRE_TA            CHAR(25)             not null,
   constraint PK_TIPO_AMBIENTE primary key (COD_TIPO_AMBIENTE)
);

/*==============================================================*/
/* Index: TIPO_AMBIENTE_PK                                      */
/*==============================================================*/
create unique index TIPO_AMBIENTE_PK on TIPO_AMBIENTE (
COD_TIPO_AMBIENTE
);

/*==============================================================*/
/* Table: TIPO_FINAL                                            */
/*==============================================================*/
create table TIPO_FINAL (
   COD_TIPO_FINAL       SERIAL               not null,
   NOMBRE_TF            CHAR(15)             not null,
   constraint PK_TIPO_FINAL primary key (COD_TIPO_FINAL)
);

/*==============================================================*/
/* Index: TIPO_FINAL_PK                                         */
/*==============================================================*/
create unique index TIPO_FINAL_PK on TIPO_FINAL (
COD_TIPO_FINAL
);

/*==============================================================*/
/* Table: USUARIO                                               */
/*==============================================================*/
create table USUARIO (
   COD_USUARIO          SERIAL               not null,
   ADM_COD_USUARIO      INT4                 null,
   FIN_COD_USUARIO      INT4                 null,
   NOMBRE_USU           CHAR(50)             not null,
   CONTRASENIA_USU      CHAR(150)            not null,
   constraint PK_USUARIO primary key (COD_USUARIO)
);

/*==============================================================*/
/* Index: USUARIO_PK                                            */
/*==============================================================*/
create unique index USUARIO_PK on USUARIO (
COD_USUARIO
);

/*==============================================================*/
/* Index: ES3_FK                                                */
/*==============================================================*/
create  index ES3_FK on USUARIO (
FIN_COD_USUARIO
);

/*==============================================================*/
/* Index: ES5_FK                                                */
/*==============================================================*/
create  index ES5_FK on USUARIO (
ADM_COD_USUARIO
);

alter table ADMINISTRADOR
   add constraint FK_ADMINIST_ES6_USUARIO foreign key (COD_USUARIO)
      references USUARIO (COD_USUARIO)
      on delete restrict on update restrict;

alter table AJUSTE_AMBIENTE
   add constraint FK_AJUSTE_A_ESTA2_BLOQUE foreign key (COD_BLOQUE)
      references BLOQUE (COD_BLOQUE)
      on delete restrict on update restrict;

alter table AJUSTE_AMBIENTE
   add constraint FK_AJUSTE_A_HUBICA1_DIA foreign key (COD_DIA)
      references DIA (COD_DIA)
      on delete restrict on update restrict;

alter table AJUSTE_AMBIENTE
   add constraint FK_AJUSTE_A_TIENE1_AMBIENTE foreign key (COD_AMBIENTE)
      references AMBIENTE (COD_AMBIENTE)
      on delete restrict on update restrict;

alter table AMBIENTE
   add constraint FK_AMBIENTE_ENCUENTRA_PISO foreign key (COD_PISO)
      references PISO (COD_PISO)
      on delete restrict on update restrict;

alter table AMBIENTE
   add constraint FK_AMBIENTE_ES1_TIPO_AMB foreign key (COD_TIPO_AMBIENTE)
      references TIPO_AMBIENTE (COD_TIPO_AMBIENTE)
      on delete restrict on update restrict;

alter table AMBIENTE
   add constraint FK_AMBIENTE_ESTA1_ESTADO_A foreign key (COD_ESTADO_AMBIENTE)
      references ESTADO_AMBIENTE (COD_ESTADO_AMBIENTE)
      on delete restrict on update restrict;

alter table AMBIENTE
   add constraint FK_AMBIENTE_PERTENECE_EDIFICAC foreign key (COD_EDIFICACION)
      references EDIFICACION (COD_EDIFICACION)
      on delete restrict on update restrict;

alter table AMBIENTE
   add constraint FK_AMBIENTE_PERTENECE_FACULTAD foreign key (COD_FACULTAD)
      references FACULTAD (COD_FACULTAD)
      on delete restrict on update restrict;

alter table COMUNICADO
   add constraint FK_COMUNICA_TIENE3_TIPO_FIN foreign key (COD_TIPO_FINAL)
      references TIPO_FINAL (COD_TIPO_FINAL)
      on delete restrict on update restrict;

alter table FINAL
   add constraint FK_FINAL_ES_TIPO_FIN foreign key (COD_TIPO_FINAL)
      references TIPO_FINAL (COD_TIPO_FINAL)
      on delete restrict on update restrict;

alter table FINAL
   add constraint FK_FINAL_ES4_USUARIO foreign key (COD_USUARIO)
      references USUARIO (COD_USUARIO)
      on delete restrict on update restrict;

alter table IMPARTICION
   add constraint FK_IMPARTIC_EN1_MATERIA foreign key (COD_MATERIA)
      references MATERIA (COD_MATERIA)
      on delete restrict on update restrict;

alter table IMPARTICION
   add constraint FK_IMPARTIC_EN2_GRUPO foreign key (COD_GRUPO)
      references GRUPO (COD_GRUPO)
      on delete restrict on update restrict;

alter table IMPARTICION
   add constraint FK_IMPARTIC_IMPARTE_FINAL foreign key (COD_USUARIO)
      references FINAL (COD_USUARIO)
      on delete restrict on update restrict;

alter table MENSAJE
   add constraint FK_MENSAJE_ENVIA_USUARIO foreign key (COD_USUARIO)
      references USUARIO (COD_USUARIO)
      on delete restrict on update restrict;

alter table MENSAJE
   add constraint FK_MENSAJE_RECIBE_USUARIO foreign key (USU_COD_USUARIO)
      references USUARIO (COD_USUARIO)
      on delete restrict on update restrict;

alter table NOTIFICACION_RESERVA
   add constraint FK_NOTIFICA_ENVIA1_USUARIO foreign key (USU_COD_USUARIO)
      references USUARIO (COD_USUARIO)
      on delete restrict on update restrict;

alter table NOTIFICACION_RESERVA
   add constraint FK_NOTIFICA_RECIBE1_USUARIO foreign key (COD_USUARIO)
      references USUARIO (COD_USUARIO)
      on delete restrict on update restrict;

alter table NOTIFICACION_RESERVA
   add constraint FK_NOTIFICA_TIENE5_AMBIENTE foreign key (COD_AMBIENTE)
      references AMBIENTE (COD_AMBIENTE)
      on delete restrict on update restrict;

alter table RESERVA
   add constraint FK_RESERVA_EL1_GRUPO foreign key (COD_GRUPO)
      references GRUPO (COD_GRUPO)
      on delete restrict on update restrict;

alter table RESERVA
   add constraint FK_RESERVA_EL2_MATERIA foreign key (COD_MATERIA)
      references MATERIA (COD_MATERIA)
      on delete restrict on update restrict;

alter table RESERVA
   add constraint FK_RESERVA_ESTA3_BLOQUE foreign key (COD_BLOQUE)
      references BLOQUE (COD_BLOQUE)
      on delete restrict on update restrict;

alter table RESERVA
   add constraint FK_RESERVA_HUBICA2_DIA foreign key (COD_DIA)
      references DIA (COD_DIA)
      on delete restrict on update restrict;

alter table RESERVA
   add constraint FK_RESERVA_REALIZA_FINAL foreign key (COD_USUARIO)
      references FINAL (COD_USUARIO)
      on delete restrict on update restrict;

alter table RESERVA
   add constraint FK_RESERVA_TIENE2_AMBIENTE foreign key (COD_AMBIENTE)
      references AMBIENTE (COD_AMBIENTE)
      on delete restrict on update restrict;

alter table USUARIO
   add constraint FK_USUARIO_ES3_FINAL foreign key (FIN_COD_USUARIO)
      references FINAL (COD_USUARIO)
      on delete restrict on update restrict;

alter table USUARIO
   add constraint FK_USUARIO_ES5_ADMINIST foreign key (ADM_COD_USUARIO)
      references ADMINISTRADOR (COD_USUARIO)
      on delete restrict on update restrict;


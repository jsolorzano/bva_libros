--
-- PostgreSQL database dump
--

-- Dumped from database version 9.4.9
-- Dumped by pg_dump version 9.4.9
-- Started on 2017-02-08 15:40:48 VET

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 1 (class 3079 OID 11861)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2283 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 173 (class 1259 OID 111579)
-- Name: auth_group; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


--
-- TOC entry 174 (class 1259 OID 111582)
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2284 (class 0 OID 0)
-- Dependencies: 174
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- TOC entry 175 (class 1259 OID 111584)
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- TOC entry 176 (class 1259 OID 111587)
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2285 (class 0 OID 0)
-- Dependencies: 176
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- TOC entry 177 (class 1259 OID 111589)
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


--
-- TOC entry 178 (class 1259 OID 111592)
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2286 (class 0 OID 0)
-- Dependencies: 178
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- TOC entry 179 (class 1259 OID 111594)
-- Name: auth_user; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


--
-- TOC entry 180 (class 1259 OID 111597)
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


--
-- TOC entry 181 (class 1259 OID 111600)
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2287 (class 0 OID 0)
-- Dependencies: 181
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- TOC entry 182 (class 1259 OID 111602)
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2288 (class 0 OID 0)
-- Dependencies: 182
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- TOC entry 183 (class 1259 OID 111604)
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


--
-- TOC entry 184 (class 1259 OID 111607)
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2289 (class 0 OID 0)
-- Dependencies: 184
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- TOC entry 205 (class 1259 OID 111903)
-- Name: autores_autor; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE autores_autor (
    id integer NOT NULL,
    cod_autor character varying(15) NOT NULL,
    autor character varying(200) NOT NULL,
    fecha_create timestamp with time zone,
    fecha_update timestamp with time zone,
    user_create_id integer,
    user_update_id integer
);


--
-- TOC entry 204 (class 1259 OID 111901)
-- Name: autores_autor_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE autores_autor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2290 (class 0 OID 0)
-- Dependencies: 204
-- Name: autores_autor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE autores_autor_id_seq OWNED BY autores_autor.id;


--
-- TOC entry 185 (class 1259 OID 111609)
-- Name: bitacora_bitacora; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE bitacora_bitacora (
    id integer NOT NULL,
    accion character varying(200) NOT NULL,
    usuario character varying(50) NOT NULL,
    fecha timestamp with time zone
);


--
-- TOC entry 186 (class 1259 OID 111612)
-- Name: bitacora_bitacora_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE bitacora_bitacora_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2291 (class 0 OID 0)
-- Dependencies: 186
-- Name: bitacora_bitacora_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE bitacora_bitacora_id_seq OWNED BY bitacora_bitacora.id;


--
-- TOC entry 187 (class 1259 OID 111614)
-- Name: categorias_categoria; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE categorias_categoria (
    id integer NOT NULL,
    cod_categoria character varying(15) NOT NULL,
    categoria character varying(200) NOT NULL,
    fecha_create timestamp with time zone,
    fecha_update timestamp with time zone,
    user_create_id integer,
    user_update_id integer
);


--
-- TOC entry 188 (class 1259 OID 111617)
-- Name: categorias_categoria_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE categorias_categoria_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2292 (class 0 OID 0)
-- Dependencies: 188
-- Name: categorias_categoria_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE categorias_categoria_id_seq OWNED BY categorias_categoria.id;


--
-- TOC entry 189 (class 1259 OID 111619)
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


--
-- TOC entry 190 (class 1259 OID 111626)
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2293 (class 0 OID 0)
-- Dependencies: 190
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- TOC entry 191 (class 1259 OID 111628)
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


--
-- TOC entry 192 (class 1259 OID 111631)
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2294 (class 0 OID 0)
-- Dependencies: 192
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- TOC entry 193 (class 1259 OID 111633)
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


--
-- TOC entry 194 (class 1259 OID 111639)
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2295 (class 0 OID 0)
-- Dependencies: 194
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- TOC entry 195 (class 1259 OID 111641)
-- Name: django_session; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


--
-- TOC entry 207 (class 1259 OID 112356)
-- Name: editoriales_editorial; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE editoriales_editorial (
    id integer NOT NULL,
    cod_editorial character varying(15) NOT NULL,
    editorial character varying(200) NOT NULL,
    fecha_create timestamp with time zone,
    fecha_update timestamp with time zone,
    user_create_id integer,
    user_update_id integer
);


--
-- TOC entry 206 (class 1259 OID 112354)
-- Name: editoriales_editorial_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE editoriales_editorial_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2296 (class 0 OID 0)
-- Dependencies: 206
-- Name: editoriales_editorial_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE editoriales_editorial_id_seq OWNED BY editoriales_editorial.id;


--
-- TOC entry 196 (class 1259 OID 111647)
-- Name: ejes_eje; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE ejes_eje (
    id integer NOT NULL,
    cod_eje character varying(15) NOT NULL,
    eje character varying(200) NOT NULL,
    fecha_create timestamp with time zone,
    fecha_update timestamp with time zone,
    user_create_id integer,
    user_update_id integer
);


--
-- TOC entry 197 (class 1259 OID 111650)
-- Name: ejes_eje_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE ejes_eje_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2297 (class 0 OID 0)
-- Dependencies: 197
-- Name: ejes_eje_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE ejes_eje_id_seq OWNED BY ejes_eje.id;


--
-- TOC entry 198 (class 1259 OID 111652)
-- Name: libros_libros; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE libros_libros (
    id integer NOT NULL,
    cod_libro character varying(15),
    titulo character varying(200),
    autor character varying(200),
    fecha_pub date,
    editorial character varying(200),
    fecha_create timestamp with time zone,
    fecha_update timestamp with time zone,
    categoria_id character varying(15),
    sede_id character varying(15),
    user_create_id integer,
    user_update_id integer
);


--
-- TOC entry 199 (class 1259 OID 111658)
-- Name: libros_libros_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE libros_libros_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2298 (class 0 OID 0)
-- Dependencies: 199
-- Name: libros_libros_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE libros_libros_id_seq OWNED BY libros_libros.id;


--
-- TOC entry 200 (class 1259 OID 111660)
-- Name: login_perfilesusuario; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE login_perfilesusuario (
    id integer NOT NULL,
    tlf character varying(15) NOT NULL,
    user_accion character varying(15),
    user_id integer NOT NULL
);


--
-- TOC entry 201 (class 1259 OID 111663)
-- Name: login_perfilesusuario_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE login_perfilesusuario_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2299 (class 0 OID 0)
-- Dependencies: 201
-- Name: login_perfilesusuario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE login_perfilesusuario_id_seq OWNED BY login_perfilesusuario.id;


--
-- TOC entry 202 (class 1259 OID 111665)
-- Name: sedes_sede; Type: TABLE; Schema: public; Owner: -; Tablespace: 
--

CREATE TABLE sedes_sede (
    id integer NOT NULL,
    cod_sede character varying(15) NOT NULL,
    sede character varying(200) NOT NULL,
    descripcion character varying(200) NOT NULL,
    fecha_create timestamp with time zone,
    fecha_update timestamp with time zone,
    eje_id character varying(15),
    user_create_id integer,
    user_update_id integer
);


--
-- TOC entry 203 (class 1259 OID 111668)
-- Name: sedes_sede_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE sedes_sede_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 2300 (class 0 OID 0)
-- Dependencies: 203
-- Name: sedes_sede_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE sedes_sede_id_seq OWNED BY sedes_sede.id;


--
-- TOC entry 1989 (class 2604 OID 111670)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- TOC entry 1990 (class 2604 OID 111671)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- TOC entry 1991 (class 2604 OID 111672)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- TOC entry 1992 (class 2604 OID 111673)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- TOC entry 1993 (class 2604 OID 111674)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- TOC entry 1994 (class 2604 OID 111675)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- TOC entry 2005 (class 2604 OID 111906)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY autores_autor ALTER COLUMN id SET DEFAULT nextval('autores_autor_id_seq'::regclass);


--
-- TOC entry 1995 (class 2604 OID 111676)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY bitacora_bitacora ALTER COLUMN id SET DEFAULT nextval('bitacora_bitacora_id_seq'::regclass);


--
-- TOC entry 1996 (class 2604 OID 111677)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY categorias_categoria ALTER COLUMN id SET DEFAULT nextval('categorias_categoria_id_seq'::regclass);


--
-- TOC entry 1997 (class 2604 OID 111678)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- TOC entry 1999 (class 2604 OID 111679)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- TOC entry 2000 (class 2604 OID 111680)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- TOC entry 2006 (class 2604 OID 112359)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY editoriales_editorial ALTER COLUMN id SET DEFAULT nextval('editoriales_editorial_id_seq'::regclass);


--
-- TOC entry 2001 (class 2604 OID 111681)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY ejes_eje ALTER COLUMN id SET DEFAULT nextval('ejes_eje_id_seq'::regclass);


--
-- TOC entry 2002 (class 2604 OID 111682)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY libros_libros ALTER COLUMN id SET DEFAULT nextval('libros_libros_id_seq'::regclass);


--
-- TOC entry 2003 (class 2604 OID 111683)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY login_perfilesusuario ALTER COLUMN id SET DEFAULT nextval('login_perfilesusuario_id_seq'::regclass);


--
-- TOC entry 2004 (class 2604 OID 111684)
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY sedes_sede ALTER COLUMN id SET DEFAULT nextval('sedes_sede_id_seq'::regclass);


--
-- TOC entry 2242 (class 0 OID 111579)
-- Dependencies: 173
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO auth_group (id, name) VALUES (1, 'administrador');
INSERT INTO auth_group (id, name) VALUES (2, 'sala');


--
-- TOC entry 2301 (class 0 OID 0)
-- Dependencies: 174
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('auth_group_id_seq', 2, true);


--
-- TOC entry 2244 (class 0 OID 111584)
-- Dependencies: 175
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2302 (class 0 OID 0)
-- Dependencies: 176
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- TOC entry 2246 (class 0 OID 111589)
-- Dependencies: 177
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (4, 'Can add permission', 2, 'add_permission');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (5, 'Can change permission', 2, 'change_permission');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (6, 'Can delete permission', 2, 'delete_permission');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (7, 'Can add group', 3, 'add_group');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (8, 'Can change group', 3, 'change_group');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (9, 'Can delete group', 3, 'delete_group');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (10, 'Can add user', 4, 'add_user');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (11, 'Can change user', 4, 'change_user');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (12, 'Can delete user', 4, 'delete_user');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (13, 'Can add content type', 5, 'add_contenttype');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (14, 'Can change content type', 5, 'change_contenttype');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (15, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (16, 'Can add session', 6, 'add_session');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (17, 'Can change session', 6, 'change_session');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (18, 'Can delete session', 6, 'delete_session');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (19, 'Can add perfiles usuario', 7, 'add_perfilesusuario');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (20, 'Can change perfiles usuario', 7, 'change_perfilesusuario');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (21, 'Can delete perfiles usuario', 7, 'delete_perfilesusuario');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (22, 'Can add eje', 8, 'add_eje');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (23, 'Can change eje', 8, 'change_eje');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (24, 'Can delete eje', 8, 'delete_eje');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (25, 'Can add sede', 9, 'add_sede');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (26, 'Can change sede', 9, 'change_sede');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (27, 'Can delete sede', 9, 'delete_sede');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (28, 'Can add categoria', 10, 'add_categoria');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (29, 'Can change categoria', 10, 'change_categoria');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (30, 'Can delete categoria', 10, 'delete_categoria');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (31, 'Can add bitacora', 11, 'add_bitacora');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (32, 'Can change bitacora', 11, 'change_bitacora');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (33, 'Can delete bitacora', 11, 'delete_bitacora');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (34, 'Can add libros', 12, 'add_libros');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (35, 'Can change libros', 12, 'change_libros');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (36, 'Can delete libros', 12, 'delete_libros');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (37, 'Can add autor', 13, 'add_autor');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (38, 'Can change autor', 13, 'change_autor');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (39, 'Can delete autor', 13, 'delete_autor');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (40, 'Can add editorial', 14, 'add_editorial');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (41, 'Can change editorial', 14, 'change_editorial');
INSERT INTO auth_permission (id, name, content_type_id, codename) VALUES (42, 'Can delete editorial', 14, 'delete_editorial');


--
-- TOC entry 2303 (class 0 OID 0)
-- Dependencies: 178
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('auth_permission_id_seq', 42, true);


--
-- TOC entry 2248 (class 0 OID 111594)
-- Dependencies: 179
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (2, 'pbkdf2_sha256$15000$fDmywJiT1jiE$kZS7DhOBsZ9/Kx8Bh/BewzYXMG+Kgjw1vNNeP/D4dRc=', '2015-09-16 13:46:37.392076-04:30', true, 'jmrodriguez', 'JOSE MIGUEL', 'RODRIGUEZ RODRIGUEZ', '22290917', true, true, '2015-05-22 12:54:43.001975-04:30');
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (3, 'pbkdf2_sha256$20000$6bwFBXJjyvpG$0PndlcEGGqKcJcmd7cjC98tfJ9cgHvX0j0pRE6lgWyU=', '2015-05-22 12:54:43.001975-04:30', true, 'jose', 'JOSE MIGUEL', 'RODRIGUEZ RODRIGUEZ', '22290917', true, true, '2015-05-22 12:54:43.001975-04:30');
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (4, 'pbkdf2_sha256$20000$YBcLUT2wdkC6$OA5NKcsKi7rYjHMSSiDDej/6bApprMSlS9ECPkf14b0=', '2015-05-22 12:54:43.001975-04:30', true, 'jm', 'JOSE MIGUEL', 'RODRIGUEZ RODRIGUEZ', '22290917', true, true, '2015-05-22 12:54:43.001975-04:30');
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (5, 'pbkdf2_sha256$15000$eesXIji9p9eH$VPM5ys+C6HC9hj+BkRitDH6wIL0OVw8Gc0sExznx27Q=', '2015-10-08 10:00:12.786741-04:30', true, 'mackfe', 'CRISTIAN MOISES', 'MAZA SANCHEZ', '22290916', true, true, '2015-05-22 12:54:43.001975-04:30');
INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (1, 'pbkdf2_sha256$20000$VYl8ojW53nHq$5yF6126ByhZZV62ZVp3XYxSORTa2wc+LKjBqj6mxEfM=', '2017-02-08 08:05:25.508834-04', true, 'admin', '', '', '', true, true, '2015-09-14 14:51:49-04:30');


--
-- TOC entry 2249 (class 0 OID 111597)
-- Dependencies: 180
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO auth_user_groups (id, user_id, group_id) VALUES (1, 1, 1);
INSERT INTO auth_user_groups (id, user_id, group_id) VALUES (2, 2, 2);
INSERT INTO auth_user_groups (id, user_id, group_id) VALUES (5, 5, 2);


--
-- TOC entry 2304 (class 0 OID 0)
-- Dependencies: 181
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 5, true);


--
-- TOC entry 2305 (class 0 OID 0)
-- Dependencies: 182
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('auth_user_id_seq', 5, true);


--
-- TOC entry 2252 (class 0 OID 111604)
-- Dependencies: 183
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2306 (class 0 OID 0)
-- Dependencies: 184
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- TOC entry 2274 (class 0 OID 111903)
-- Dependencies: 205
-- Data for Name: autores_autor; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO autores_autor (id, cod_autor, autor, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (1, 'A0001', 'Simón Rodríguez', '2017-02-08 11:14:57.169647-04', '2017-02-08 11:14:57.169672-04', 1, NULL);
INSERT INTO autores_autor (id, cod_autor, autor, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (2, 'A0002', 'Rómulo Betancourt', '2017-02-08 11:14:57.329971-04', '2017-02-08 11:14:57.329993-04', 1, NULL);
INSERT INTO autores_autor (id, cod_autor, autor, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (3, 'A0003', 'Juan Antonio Pérez Bonalde', '2017-02-08 11:14:57.347168-04', '2017-02-08 11:14:57.347199-04', 1, NULL);
INSERT INTO autores_autor (id, cod_autor, autor, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (4, 'A0004', 'Miguel Otero Silva', '2017-02-08 11:14:57.363948-04', '2017-02-08 11:14:57.363979-04', 1, NULL);
INSERT INTO autores_autor (id, cod_autor, autor, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (5, 'A0005', 'Teresa de la Parra', '2017-02-08 11:14:57.380824-04', '2017-02-08 11:14:57.380855-04', 1, NULL);
INSERT INTO autores_autor (id, cod_autor, autor, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (6, 'A0006', 'Julio Garmendia', '2017-02-08 11:14:57.39743-04', '2017-02-08 11:14:57.397461-04', 1, NULL);
INSERT INTO autores_autor (id, cod_autor, autor, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (7, 'A0007', 'Andrés Bello', '2017-02-08 11:14:57.413758-04', '2017-02-08 11:14:57.4138-04', 1, NULL);
INSERT INTO autores_autor (id, cod_autor, autor, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (8, 'A0008', 'Rómulo Gallegos', '2017-02-08 11:14:57.430616-04', '2017-02-08 11:14:57.430644-04', 1, NULL);
INSERT INTO autores_autor (id, cod_autor, autor, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (9, 'A0009', 'Arturo Uslar Pietri', '2017-02-08 11:14:57.446843-04', '2017-02-08 11:14:57.44687-04', 1, NULL);
INSERT INTO autores_autor (id, cod_autor, autor, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (10, 'A0010', 'Antonia Palacios', '2017-02-08 11:14:57.479001-04', '2017-02-08 11:14:57.47903-04', 1, NULL);
INSERT INTO autores_autor (id, cod_autor, autor, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (11, 'A0011', 'nuevos', '2017-02-08 12:43:35.471457-04', '2017-02-08 12:43:50.507599-04', 1, 1);


--
-- TOC entry 2307 (class 0 OID 0)
-- Dependencies: 204
-- Name: autores_autor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('autores_autor_id_seq', 11, true);


--
-- TOC entry 2254 (class 0 OID 111609)
-- Dependencies: 185
-- Data for Name: bitacora_bitacora; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (1, 'Registro de nueva categoría desde csv (CT0001)...', 'admin', '2015-09-14 15:10:34.741776-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (2, 'Registro de nueva categoría desde csv (CT0002)...', 'admin', '2015-09-14 15:10:34.765607-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (3, 'Registro de nueva categoría desde csv (CT0003)...', 'admin', '2015-09-14 15:10:34.777564-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (4, 'Registro de nueva categoría desde csv (CT0004)...', 'admin', '2015-09-14 15:10:34.789513-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (5, 'Registro de nueva categoría desde csv (CT0005)...', 'admin', '2015-09-14 15:10:34.801496-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (6, 'Registro de nueva categoría desde csv (CT0006)...', 'admin', '2015-09-14 15:10:34.819728-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (7, 'Registro de nueva categoría desde csv (CT0007)...', 'admin', '2015-09-14 15:10:34.837419-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (8, 'Registro de nueva categoría desde csv (CT0008)...', 'admin', '2015-09-14 15:10:34.855438-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (9, 'Registro de nueva categoría desde csv (CT0009)...', 'admin', '2015-09-14 15:10:34.873685-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (10, 'Registro de nueva categoría desde csv (CT0010)...', 'admin', '2015-09-14 15:10:34.885303-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (11, 'Registro de nueva categoría desde csv (CT0011)...', 'admin', '2015-09-14 15:10:34.897257-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (12, 'Registro de nueva categoría desde csv (CT0012)...', 'admin', '2015-09-14 15:10:34.90921-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (13, 'Registro de nueva categoría desde csv (CT0013)...', 'admin', '2015-09-14 15:10:34.921167-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (14, 'Registro de nueva categoría desde csv (CT0014)...', 'admin', '2015-09-14 15:10:34.939103-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (15, 'Registro de nueva categoría desde csv (CT0015)...', 'admin', '2015-09-14 15:10:34.951057-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (16, 'Registro de nueva categoría desde csv (CT0016)...', 'admin', '2015-09-14 15:10:34.968994-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (17, 'Registro de nueva categoría desde csv (CT0017)...', 'admin', '2015-09-14 15:10:34.980938-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (18, 'Registro de nuevo eje desde csv (E0001)...', 'admin', '2015-09-14 15:11:29.367508-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (19, 'Registro de nuevo eje desde csv (E0002)...', 'admin', '2015-09-14 15:11:29.385367-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (20, 'Registro de nuevo eje desde csv (E0003)...', 'admin', '2015-09-14 15:11:29.397312-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (21, 'Registro de nuevo eje desde csv (E0004)...', 'admin', '2015-09-14 15:11:29.409285-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (22, 'Registro de nuevo eje desde csv (E0005)...', 'admin', '2015-09-14 15:11:29.421221-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (23, 'Registro de nueva sede desde csv (S0001)...', 'admin', '2015-09-14 15:11:37.705733-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (24, 'Registro de nueva sede desde csv (S0002)...', 'admin', '2015-09-14 15:11:37.723573-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (25, 'Registro de nueva sede desde csv (S0003)...', 'admin', '2015-09-14 15:11:37.741509-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (26, 'Registro de nueva sede desde csv (S0004)...', 'admin', '2015-09-14 15:11:37.75956-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (27, 'Registro de nueva sede desde csv (S0005)...', 'admin', '2015-09-14 15:11:37.777491-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (28, 'Registro de nueva sede desde csv (S0006)...', 'admin', '2015-09-14 15:11:37.795417-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (29, 'Registro de nueva sede desde csv (S0007)...', 'admin', '2015-09-14 15:11:37.813346-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (30, 'Registro de nueva sede desde csv (S0008)...', 'admin', '2015-09-14 15:11:37.831289-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (31, 'Registro de nueva sede desde csv (S0009)...', 'admin', '2015-09-14 15:11:37.849213-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (32, 'Registro de nueva sede desde csv (S0010)...', 'admin', '2015-09-14 15:11:37.867147-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (33, 'Registro de nueva sede desde csv (S0011)...', 'admin', '2015-09-14 15:11:37.885218-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (34, 'Registro de nueva sede desde csv (S0012)...', 'admin', '2015-09-14 15:11:37.90314-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (35, 'Registro de nueva sede desde csv (S0013)...', 'admin', '2015-09-14 15:11:37.921087-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (36, 'Registro de nueva sede desde csv (S0014)...', 'admin', '2015-09-14 15:11:37.939034-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (37, 'Registro de nueva sede desde csv (S0015)...', 'admin', '2015-09-14 15:11:37.95694-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (38, 'Registro de nueva sede desde csv (S0016)...', 'admin', '2015-09-14 15:11:37.974872-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (39, 'Registro de nueva sede desde csv (S0017)...', 'admin', '2015-09-14 15:11:37.992801-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (40, 'Registro de nueva sede desde csv (S0018)...', 'admin', '2015-09-14 15:11:38.010867-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (41, 'Registro de nueva sede desde csv (S0019)...', 'admin', '2015-09-14 15:11:38.028796-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (42, 'Registro de nueva sede desde csv (S0020)...', 'admin', '2015-09-14 15:11:38.046735-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (43, 'Registro de nueva sede desde csv (S0021)...', 'admin', '2015-09-14 15:11:38.064659-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (44, 'Registro de nueva sede desde csv (S0022)...', 'admin', '2015-09-14 15:11:38.082575-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (45, 'Registro de nueva sede desde csv (S0023)...', 'admin', '2015-09-14 15:11:38.100518-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (46, 'Registro de nueva sede desde csv (S0024)...', 'admin', '2015-09-14 15:11:38.118464-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (47, 'Registro de nueva sede desde csv (S0025)...', 'admin', '2015-09-14 15:11:38.136383-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (48, 'Registro de nueva sede desde csv (S0026)...', 'admin', '2015-09-14 15:11:38.154464-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (49, 'Registro de nueva sede desde csv (S0027)...', 'admin', '2015-09-14 15:11:38.172378-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (50, 'Registro de nueva sede desde csv (S0028)...', 'admin', '2015-09-14 15:11:38.190325-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (51, 'Registro de nueva sede desde csv (S0029)...', 'admin', '2015-09-14 15:11:38.208238-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (52, 'Registro de nueva sede desde csv (S0030)...', 'admin', '2015-09-14 15:11:38.226184-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (53, 'Registro de nueva sede desde csv (S0031)...', 'admin', '2015-09-14 15:11:38.244118-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (54, 'Registro de nueva sede desde csv (S0032)...', 'admin', '2015-09-14 15:11:38.262035-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (55, 'Registro de nuevo libro (L0001)...', 'jmrodriguez', '2015-09-16 13:47:09.960515-04:30');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (56, 'Registro de nuevo libro (L0002)...', 'admin', '2017-01-30 16:02:25.557847-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (57, 'Registro de nuevo autor desde csv (A0001)...', 'admin', '2017-02-08 11:14:57.213866-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (58, 'Registro de nuevo autor desde csv (A0002)...', 'admin', '2017-02-08 11:14:57.337025-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (59, 'Registro de nuevo autor desde csv (A0003)...', 'admin', '2017-02-08 11:14:57.353787-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (60, 'Registro de nuevo autor desde csv (A0004)...', 'admin', '2017-02-08 11:14:57.370413-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (61, 'Registro de nuevo autor desde csv (A0005)...', 'admin', '2017-02-08 11:14:57.387133-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (62, 'Registro de nuevo autor desde csv (A0006)...', 'admin', '2017-02-08 11:14:57.403771-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (63, 'Registro de nuevo autor desde csv (A0007)...', 'admin', '2017-02-08 11:14:57.420428-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (64, 'Registro de nuevo autor desde csv (A0008)...', 'admin', '2017-02-08 11:14:57.437045-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (65, 'Registro de nuevo autor desde csv (A0009)...', 'admin', '2017-02-08 11:14:57.453748-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (66, 'Registro de nuevo autor desde csv (A0010)...', 'admin', '2017-02-08 11:14:57.49548-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (67, 'Registro de nueva categoria (CT0018)...', 'admin', '2017-02-08 11:39:48.941841-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (68, 'Registro de nuevo autor (A0011)...', 'admin', '2017-02-08 12:43:35.493937-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (69, 'Actualización del autor ''A0011''...', 'admin', '2017-02-08 12:43:50.543761-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (70, 'Registro de nueva editorial desde csv (ED0001)...', 'admin', '2017-02-08 15:30:57.591556-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (71, 'Registro de nueva editorial desde csv (ED0002)...', 'admin', '2017-02-08 15:30:57.683158-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (72, 'Registro de nueva editorial desde csv (ED0003)...', 'admin', '2017-02-08 15:30:57.699798-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (73, 'Registro de nueva editorial desde csv (ED0004)...', 'admin', '2017-02-08 15:30:57.716428-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (74, 'Registro de nueva editorial desde csv (ED0005)...', 'admin', '2017-02-08 15:30:57.733026-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (75, 'Registro de nueva editorial (CT0006)...', 'admin', '2017-02-08 15:31:35.907471-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (76, 'Actualización de la categoría ''CT0006''...', 'admin', '2017-02-08 15:31:48.490557-04');
INSERT INTO bitacora_bitacora (id, accion, usuario, fecha) VALUES (77, 'Eliminación de la editorial ''CT0006''...', 'admin', '2017-02-08 15:31:55.657381-04');


--
-- TOC entry 2308 (class 0 OID 0)
-- Dependencies: 186
-- Name: bitacora_bitacora_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('bitacora_bitacora_id_seq', 77, true);


--
-- TOC entry 2256 (class 0 OID 111614)
-- Dependencies: 187
-- Data for Name: categorias_categoria; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO categorias_categoria (id, cod_categoria, categoria, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (1, 'CT0001', 'Biografías-Memorias', '2015-09-14 15:10:34.729615-04:30', '2015-09-14 15:10:34.729708-04:30', 1, NULL);
INSERT INTO categorias_categoria (id, cod_categoria, categoria, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (2, 'CT0002', 'Clásicos de la literatura', '2015-09-14 15:10:34.756952-04:30', '2015-09-14 15:10:34.757044-04:30', 1, NULL);
INSERT INTO categorias_categoria (id, cod_categoria, categoria, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (3, 'CT0003', 'Cómics Novela Gráfica', '2015-09-14 15:10:34.774531-04:30', '2015-09-14 15:10:34.774622-04:30', 1, NULL);
INSERT INTO categorias_categoria (id, cod_categoria, categoria, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (4, 'CT0004', 'Ensayo', '2015-09-14 15:10:34.786533-04:30', '2015-09-14 15:10:34.786624-04:30', 1, NULL);
INSERT INTO categorias_categoria (id, cod_categoria, categoria, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (5, 'CT0005', 'Fantástica-ciencia ficción', '2015-09-14 15:10:34.798423-04:30', '2015-09-14 15:10:34.798512-04:30', 1, NULL);
INSERT INTO categorias_categoria (id, cod_categoria, categoria, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (6, 'CT0006', 'Ficción literaria', '2015-09-14 15:10:34.810376-04:30', '2015-09-14 15:10:34.810467-04:30', 1, NULL);
INSERT INTO categorias_categoria (id, cod_categoria, categoria, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (7, 'CT0007', 'Histórica y aventuras', '2015-09-14 15:10:34.82908-04:30', '2015-09-14 15:10:34.829189-04:30', 1, NULL);
INSERT INTO categorias_categoria (id, cod_categoria, categoria, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (8, 'CT0008', 'Humor', '2015-09-14 15:10:34.847063-04:30', '2015-09-14 15:10:34.847172-04:30', 1, NULL);
INSERT INTO categorias_categoria (id, cod_categoria, categoria, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (9, 'CT0009', 'Infantil y juvenil', '2015-09-14 15:10:34.86599-04:30', '2015-09-14 15:10:34.866121-04:30', 1, NULL);
INSERT INTO categorias_categoria (id, cod_categoria, categoria, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (10, 'CT0010', 'Lecturas complementarias', '2015-09-14 15:10:34.882326-04:30', '2015-09-14 15:10:34.882418-04:30', 1, NULL);
INSERT INTO categorias_categoria (id, cod_categoria, categoria, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (11, 'CT0011', 'Literatura contemporánea', '2015-09-14 15:10:34.894241-04:30', '2015-09-14 15:10:34.894332-04:30', 1, NULL);
INSERT INTO categorias_categoria (id, cod_categoria, categoria, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (12, 'CT0012', 'Narrativa', '2015-09-14 15:10:34.90614-04:30', '2015-09-14 15:10:34.906252-04:30', 1, NULL);
INSERT INTO categorias_categoria (id, cod_categoria, categoria, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (13, 'CT0013', 'No ficción', '2015-09-14 15:10:34.918096-04:30', '2015-09-14 15:10:34.918207-04:30', 1, NULL);
INSERT INTO categorias_categoria (id, cod_categoria, categoria, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (14, 'CT0014', 'Novela negra-intriga-terror', '2015-09-14 15:10:34.930281-04:30', '2015-09-14 15:10:34.930372-04:30', 1, NULL);
INSERT INTO categorias_categoria (id, cod_categoria, categoria, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (15, 'CT0015', 'Poesía-teatro', '2015-09-14 15:10:34.948012-04:30', '2015-09-14 15:10:34.948103-04:30', 1, NULL);
INSERT INTO categorias_categoria (id, cod_categoria, categoria, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (16, 'CT0016', 'Romántica', '2015-09-14 15:10:34.960112-04:30', '2015-09-14 15:10:34.960202-04:30', 1, NULL);
INSERT INTO categorias_categoria (id, cod_categoria, categoria, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (17, 'CT0017', 'Varios', '2015-09-14 15:10:34.977875-04:30', '2015-09-14 15:10:34.977966-04:30', 1, NULL);
INSERT INTO categorias_categoria (id, cod_categoria, categoria, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (18, 'CT0018', 'nuevo', '2017-02-08 11:39:48.750821-04', '2017-02-08 11:39:48.750843-04', 1, NULL);


--
-- TOC entry 2309 (class 0 OID 0)
-- Dependencies: 188
-- Name: categorias_categoria_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('categorias_categoria_id_seq', 18, true);


--
-- TOC entry 2258 (class 0 OID 111619)
-- Dependencies: 189
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (1, '2015-09-14 15:09:27.501073-04:30', '1', 'administrador', 1, '', 3, 1);
INSERT INTO django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (2, '2015-09-14 15:09:34.612628-04:30', '2', 'sala', 1, '', 3, 1);
INSERT INTO django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) VALUES (3, '2015-09-14 15:10:17.820268-04:30', '1', 'admin', 2, 'Modifica groups.', 4, 1);


--
-- TOC entry 2310 (class 0 OID 0)
-- Dependencies: 190
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 3, true);


--
-- TOC entry 2260 (class 0 OID 111628)
-- Dependencies: 191
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO django_content_type (id, app_label, model) VALUES (1, 'admin', 'logentry');
INSERT INTO django_content_type (id, app_label, model) VALUES (2, 'auth', 'permission');
INSERT INTO django_content_type (id, app_label, model) VALUES (3, 'auth', 'group');
INSERT INTO django_content_type (id, app_label, model) VALUES (4, 'auth', 'user');
INSERT INTO django_content_type (id, app_label, model) VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO django_content_type (id, app_label, model) VALUES (6, 'sessions', 'session');
INSERT INTO django_content_type (id, app_label, model) VALUES (7, 'login', 'perfilesusuario');
INSERT INTO django_content_type (id, app_label, model) VALUES (8, 'ejes', 'eje');
INSERT INTO django_content_type (id, app_label, model) VALUES (9, 'sedes', 'sede');
INSERT INTO django_content_type (id, app_label, model) VALUES (10, 'categorias', 'categoria');
INSERT INTO django_content_type (id, app_label, model) VALUES (11, 'bitacora', 'bitacora');
INSERT INTO django_content_type (id, app_label, model) VALUES (12, 'libros', 'libros');
INSERT INTO django_content_type (id, app_label, model) VALUES (13, 'autores', 'autor');
INSERT INTO django_content_type (id, app_label, model) VALUES (14, 'editoriales', 'editorial');


--
-- TOC entry 2311 (class 0 OID 0)
-- Dependencies: 192
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('django_content_type_id_seq', 14, true);


--
-- TOC entry 2262 (class 0 OID 111633)
-- Dependencies: 193
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO django_migrations (id, app, name, applied) VALUES (1, 'contenttypes', '0001_initial', '2015-09-14 14:51:11.230424-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (2, 'auth', '0001_initial', '2015-09-14 14:51:12.062683-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (3, 'admin', '0001_initial', '2015-09-14 14:51:12.364108-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (4, 'sessions', '0001_initial', '2015-09-14 14:51:12.489743-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (5, 'bitacora', '0001_initial', '2015-09-14 14:52:04.097289-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (6, 'categorias', '0001_initial', '2015-09-14 14:52:04.360947-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (7, 'ejes', '0001_initial', '2015-09-14 14:52:04.59368-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (8, 'sedes', '0001_initial', '2015-09-14 14:52:04.929267-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (9, 'libros', '0001_initial', '2015-09-14 14:52:05.363245-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (10, 'login', '0001_initial', '2015-09-14 14:52:05.507018-04:30');
INSERT INTO django_migrations (id, app, name, applied) VALUES (11, 'contenttypes', '0002_remove_content_type_name', '2017-02-07 10:35:21.956769-04');
INSERT INTO django_migrations (id, app, name, applied) VALUES (12, 'auth', '0002_alter_permission_name_max_length', '2017-02-07 10:35:21.98068-04');
INSERT INTO django_migrations (id, app, name, applied) VALUES (13, 'auth', '0003_alter_user_email_max_length', '2017-02-07 10:35:22.005876-04');
INSERT INTO django_migrations (id, app, name, applied) VALUES (14, 'auth', '0004_alter_user_username_opts', '2017-02-07 10:35:22.024959-04');
INSERT INTO django_migrations (id, app, name, applied) VALUES (15, 'auth', '0005_alter_user_last_login_null', '2017-02-07 10:35:22.047524-04');
INSERT INTO django_migrations (id, app, name, applied) VALUES (16, 'auth', '0006_require_contenttypes_0002', '2017-02-07 10:35:22.056512-04');
INSERT INTO django_migrations (id, app, name, applied) VALUES (17, 'autores', '0001_initial', '2017-02-08 10:52:32.471503-04');
INSERT INTO django_migrations (id, app, name, applied) VALUES (18, 'autores', '0002_auto_20170208_1052', '2017-02-08 10:52:33.079559-04');
INSERT INTO django_migrations (id, app, name, applied) VALUES (19, 'editoriales', '0001_initial', '2017-02-08 14:36:42.864828-04');
INSERT INTO django_migrations (id, app, name, applied) VALUES (20, 'editoriales', '0002_auto_20170208_1436', '2017-02-08 14:36:43.272664-04');


--
-- TOC entry 2312 (class 0 OID 0)
-- Dependencies: 194
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('django_migrations_id_seq', 20, true);


--
-- TOC entry 2264 (class 0 OID 111641)
-- Dependencies: 195
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO django_session (session_key, session_data, expire_date) VALUES ('wh5cnocqmoybs0ko1k5p0yjn491u3tth', 'NjJjYjA5ZWJlNDAxYjc4YmZhOTRmNmRlNzY0OWI5NGJhNDM3ZTQxOTp7Il9hdXRoX3VzZXJfaGFzaCI6IjBhNjgzZDVhMDQ2YWZkYzM2MTAyN2UyNzk1NjdhM2RiZmJiZmE0ZjAiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9', '2015-09-28 16:08:44.005428-04:30');
INSERT INTO django_session (session_key, session_data, expire_date) VALUES ('q2bnsjg152lpogv116mskixthttizt3q', 'MjVlZDA0YzQxNzkxZGZjMDQ5NzBlYTEwYWM0NDAyMDg3OTAzZGY0ZDp7fQ==', '2015-09-28 16:24:07.895246-04:30');
INSERT INTO django_session (session_key, session_data, expire_date) VALUES ('wolu3ptthi04nqbrrjgifez7mu2mi7i8', 'MjVlZDA0YzQxNzkxZGZjMDQ5NzBlYTEwYWM0NDAyMDg3OTAzZGY0ZDp7fQ==', '2015-09-29 13:39:18.125968-04:30');
INSERT INTO django_session (session_key, session_data, expire_date) VALUES ('717j3f2e65dmxdcv98njyree4eoi3o72', 'MjVlZDA0YzQxNzkxZGZjMDQ5NzBlYTEwYWM0NDAyMDg3OTAzZGY0ZDp7fQ==', '2015-09-30 13:47:22.49526-04:30');
INSERT INTO django_session (session_key, session_data, expire_date) VALUES ('vgztc6mf9y791ju2gksrkjuqbj72blsl', 'OWQ1NDc0N2M4Y2QxMTFhZTU0NTY2NmZlNmM0MzA2NzY5YTlmMmJlMjp7Il9hdXRoX3VzZXJfaGFzaCI6IjQxMTUwMjM4MzA3ZjBiOTFjNzliMjQxYjhmMzU5MGY3OGIwYmY3YmMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjV9', '2015-10-22 10:00:12.810694-04:30');
INSERT INTO django_session (session_key, session_data, expire_date) VALUES ('s3jd5dhkuc1qas1e8wu5x7yk50grvofe', 'MjVlZDA0YzQxNzkxZGZjMDQ5NzBlYTEwYWM0NDAyMDg3OTAzZGY0ZDp7fQ==', '2015-11-05 13:27:49.28286-04:30');
INSERT INTO django_session (session_key, session_data, expire_date) VALUES ('en9fwi692gcjt0ughp0qke24qryd0rn8', 'MjVlZDA0YzQxNzkxZGZjMDQ5NzBlYTEwYWM0NDAyMDg3OTAzZGY0ZDp7fQ==', '2017-02-13 08:36:51.029838-04');
INSERT INTO django_session (session_key, session_data, expire_date) VALUES ('fdoudl8upxf6xoznggyvh4hkrurhhmwe', 'MjVlZDA0YzQxNzkxZGZjMDQ5NzBlYTEwYWM0NDAyMDg3OTAzZGY0ZDp7fQ==', '2017-02-13 16:05:02.760203-04');
INSERT INTO django_session (session_key, session_data, expire_date) VALUES ('sfblgamnjj39sak3aosrn3qtysqz4es5', 'MjVlZDA0YzQxNzkxZGZjMDQ5NzBlYTEwYWM0NDAyMDg3OTAzZGY0ZDp7fQ==', '2017-02-14 09:31:18.038026-04');
INSERT INTO django_session (session_key, session_data, expire_date) VALUES ('p80wvxi8clm7frv3qerum4vlz44eor0h', 'MjVlZDA0YzQxNzkxZGZjMDQ5NzBlYTEwYWM0NDAyMDg3OTAzZGY0ZDp7fQ==', '2017-02-14 12:10:30.989075-04');
INSERT INTO django_session (session_key, session_data, expire_date) VALUES ('uruoitzbwx58kzzoo4sjkckvtsm7guch', 'MjVlZDA0YzQxNzkxZGZjMDQ5NzBlYTEwYWM0NDAyMDg3OTAzZGY0ZDp7fQ==', '2017-02-16 11:21:39.577986-04');
INSERT INTO django_session (session_key, session_data, expire_date) VALUES ('hhawi2o0zzpfwh70qxb4w0upynfhiu1g', 'NmQ4MzBhZmExMDNkNDNhNDk1OTdjYTEyNWNhNjYzMjk5ODcxZGJlNTp7Il9hdXRoX3VzZXJfaGFzaCI6ImI4MjA3M2ZkM2E1NGEyMzE0MjM2YmFjOGQ4Yjk0Yzg2Nzg0ZmI1ZTciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2017-02-22 08:05:25.55087-04');


--
-- TOC entry 2276 (class 0 OID 112356)
-- Dependencies: 207
-- Data for Name: editoriales_editorial; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO editoriales_editorial (id, cod_editorial, editorial, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (1, 'ED0001', 'Planeta', '2017-02-08 15:30:57.548211-04', '2017-02-08 15:30:57.54823-04', 1, NULL);
INSERT INTO editoriales_editorial (id, cod_editorial, editorial, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (2, 'ED0002', 'Salesiana', '2017-02-08 15:30:57.676573-04', '2017-02-08 15:30:57.676606-04', 1, NULL);
INSERT INTO editoriales_editorial (id, cod_editorial, editorial, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (3, 'ED0003', 'Aptitud', '2017-02-08 15:30:57.693172-04', '2017-02-08 15:30:57.693196-04', 1, NULL);
INSERT INTO editoriales_editorial (id, cod_editorial, editorial, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (4, 'ED0004', 'Librartes', '2017-02-08 15:30:57.709284-04', '2017-02-08 15:30:57.709304-04', 1, NULL);
INSERT INTO editoriales_editorial (id, cod_editorial, editorial, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (5, 'ED0005', 'Larousse', '2017-02-08 15:30:57.726404-04', '2017-02-08 15:30:57.726432-04', 1, NULL);


--
-- TOC entry 2313 (class 0 OID 0)
-- Dependencies: 206
-- Name: editoriales_editorial_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('editoriales_editorial_id_seq', 6, true);


--
-- TOC entry 2265 (class 0 OID 111647)
-- Dependencies: 196
-- Data for Name: ejes_eje; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO ejes_eje (id, cod_eje, eje, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (1, 'E0001', 'CENTRO', '2015-09-14 15:11:29.356936-04:30', '2015-09-14 15:11:29.357029-04:30', 1, NULL);
INSERT INTO ejes_eje (id, cod_eje, eje, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (2, 'E0002', 'COSTA', '2015-09-14 15:11:29.376651-04:30', '2015-09-14 15:11:29.376742-04:30', 1, NULL);
INSERT INTO ejes_eje (id, cod_eje, eje, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (3, 'E0003', 'ESTE', '2015-09-14 15:11:29.394263-04:30', '2015-09-14 15:11:29.394354-04:30', 1, NULL);
INSERT INTO ejes_eje (id, cod_eje, eje, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (4, 'E0004', 'METRO', '2015-09-14 15:11:29.406202-04:30', '2015-09-14 15:11:29.406292-04:30', 1, NULL);
INSERT INTO ejes_eje (id, cod_eje, eje, fecha_create, fecha_update, user_create_id, user_update_id) VALUES (5, 'E0005', 'SUR', '2015-09-14 15:11:29.418143-04:30', '2015-09-14 15:11:29.418257-04:30', 1, NULL);


--
-- TOC entry 2314 (class 0 OID 0)
-- Dependencies: 197
-- Name: ejes_eje_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('ejes_eje_id_seq', 5, true);


--
-- TOC entry 2267 (class 0 OID 111652)
-- Dependencies: 198
-- Data for Name: libros_libros; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO libros_libros (id, cod_libro, titulo, autor, fecha_pub, editorial, fecha_create, fecha_update, categoria_id, sede_id, user_create_id, user_update_id) VALUES (1, 'L0001', 'Libro', 'Jose', '2014-02-06', 'JM', '2015-09-16 13:47:09.911502-04:30', '2015-09-16 13:47:09.911588-04:30', 'CT0001', 'S0001', NULL, NULL);
INSERT INTO libros_libros (id, cod_libro, titulo, autor, fecha_pub, editorial, fecha_create, fecha_update, categoria_id, sede_id, user_create_id, user_update_id) VALUES (2, 'L0002', 'Proyectos Productivos', 'FIDES', '2004-12-02', 'Oficina de Participación Comunitaria', '2017-01-30 16:02:25.426375-04', '2017-01-30 16:02:25.426457-04', 'CT0010', 'S0009', NULL, NULL);


--
-- TOC entry 2315 (class 0 OID 0)
-- Dependencies: 199
-- Name: libros_libros_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('libros_libros_id_seq', 2, true);


--
-- TOC entry 2269 (class 0 OID 111660)
-- Dependencies: 200
-- Data for Name: login_perfilesusuario; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 2316 (class 0 OID 0)
-- Dependencies: 201
-- Name: login_perfilesusuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('login_perfilesusuario_id_seq', 1, false);


--
-- TOC entry 2271 (class 0 OID 111665)
-- Dependencies: 202
-- Data for Name: sedes_sede; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (1, 'S0001', 'BV San Mateo', 'Biblioteca Virtual San Mateo', '2015-09-14 15:11:37.691461-04:30', '2015-09-14 15:11:37.691552-04:30', 'E0003', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (2, 'S0002', 'BV Camatagua', 'Biblioteca Virtual Camatagua', '2015-09-14 15:11:37.715075-04:30', '2015-09-14 15:11:37.715168-04:30', 'E0002', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (3, 'S0003', 'BV Francisco de Miranda', 'Biblioteca Virtual Francisco de Miranda', '2015-09-14 15:11:37.732593-04:30', '2015-09-14 15:11:37.732682-04:30', 'E0001', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (4, 'S0004', 'BV Morean Soto', 'Biblioteca Virtual Morean Soto', '2015-09-14 15:11:37.750561-04:30', '2015-09-14 15:11:37.75065-04:30', 'E0001', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (5, 'S0005', 'BV Barrio El Carmen', 'Biblioteca Virtual Barrio El Carmen', '2015-09-14 15:11:37.768593-04:30', '2015-09-14 15:11:37.768682-04:30', 'E0004', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (6, 'S0006', 'BV Brisas del Lago', 'Biblioteca Virtual Brisas del Lago', '2015-09-14 15:11:37.786531-04:30', '2015-09-14 15:11:37.78662-04:30', 'E0004', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (7, 'S0007', 'BV Contraloría', 'Biblioteca Virtual Contraloria', '2015-09-14 15:11:37.804478-04:30', '2015-09-14 15:11:37.804567-04:30', 'E0004', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (8, 'S0008', 'BV Hospital Militar', 'Biblioteca Virtual Hospital Militar', '2015-09-14 15:11:37.822394-04:30', '2015-09-14 15:11:37.822482-04:30', 'E0001', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (9, 'S0009', 'BV Maracay', 'Biblioteca Virtual Maracay', '2015-09-14 15:11:37.840305-04:30', '2015-09-14 15:11:37.840396-04:30', 'E0004', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (10, 'S0010', 'BV San Vicente', 'Biblioteca Virtual San Vicente', '2015-09-14 15:11:37.858247-04:30', '2015-09-14 15:11:37.858336-04:30', 'E0004', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (11, 'S0011', 'BV Tiempo Meteorológico', 'Biblioteca Virtual Tiempo Meteorológico', '2015-09-14 15:11:37.876163-04:30', '2015-09-14 15:11:37.876252-04:30', 'E0004', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (12, 'S0012', 'BV UCV Maracay', 'Biblioteca Virtual UCV', '2015-09-14 15:11:37.894277-04:30', '2015-09-14 15:11:37.894369-04:30', 'E0004', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (13, 'S0013', 'BV UPEL Maracay', 'Biblioteca Virtual Upel Maracay', '2015-09-14 15:11:37.912182-04:30', '2015-09-14 15:11:37.912271-04:30', 'E0001', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (14, 'S0014', 'BV La Victoria', 'Biblioteca Virtual La Victoria', '2015-09-14 15:11:37.93011-04:30', '2015-09-14 15:11:37.930221-04:30', 'E0003', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (15, 'S0015', 'BV Palo Negro', 'Biblioteca Virtual Palo Negro', '2015-09-14 15:11:37.948076-04:30', '2015-09-14 15:11:37.948166-04:30', 'E0003', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (16, 'S0016', 'BV Ocumare de la Costa', 'Biblioteca Virtual Ocumare de la Costa', '2015-09-14 15:11:37.965937-04:30', '2015-09-14 15:11:37.966026-04:30', 'E0002', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (17, 'S0017', 'BV San Casimiro', 'Biblioteca Virtual San Casimiro', '2015-09-14 15:11:37.983889-04:30', '2015-09-14 15:11:37.983979-04:30', 'E0005', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (18, 'S0018', 'BV Vallecito', 'Biblioteca Virtual Vallecito', '2015-09-14 15:11:38.001803-04:30', '2015-09-14 15:11:38.001892-04:30', 'E0005', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (19, 'S0019', 'BV San Sebastián de los Reyes', 'Biblioteca Virtual San Sebastián de los Reyes', '2015-09-14 15:11:38.019896-04:30', '2015-09-14 15:11:38.019986-04:30', 'E0005', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (20, 'S0020', 'BV Quebrada Honda', 'Biblioteca Virtual Quebrada Honda', '2015-09-14 15:11:38.037782-04:30', '2015-09-14 15:11:38.037871-04:30', 'E0005', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (21, 'S0021', 'BV Cepe', 'Biblioteca Virtual Cepe', '2015-09-14 15:11:38.055749-04:30', '2015-09-14 15:11:38.055839-04:30', 'E0002', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (22, 'S0022', 'BV Chuao', 'Biblioteca Virtual Chuao', '2015-09-14 15:11:38.07366-04:30', '2015-09-14 15:11:38.073749-04:30', 'E0002', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (23, 'S0023', 'BV Turmero', 'Biblioteca Virtual Turmero', '2015-09-14 15:11:38.091615-04:30', '2015-09-14 15:11:38.091704-04:30', 'E0001', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (24, 'S0024', 'BV UPEL Mácaro', 'Biblioteca Virtual Upel Macaro', '2015-09-14 15:11:38.109507-04:30', '2015-09-14 15:11:38.109595-04:30', 'E0001', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (25, 'S0025', 'BV Cagua', 'Biblioteca Virtual Cagua', '2015-09-14 15:11:38.127479-04:30', '2015-09-14 15:11:38.127569-04:30', 'E0003', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (26, 'S0026', 'BV Colonia Tovar', 'Biblioteca Virtual Colonia Tovar', '2015-09-14 15:11:38.145402-04:30', '2015-09-14 15:11:38.14549-04:30', 'E0003', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (27, 'S0027', 'BV Barbacoas', 'Biblioteca Virtual Barbacoas', '2015-09-14 15:11:38.163477-04:30', '2015-09-14 15:11:38.163568-04:30', 'E0005', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (28, 'S0028', 'BV San Francisco de Cara', 'Biblioteca Virtual San Francisco de Cara', '2015-09-14 15:11:38.181679-04:30', '2015-09-14 15:11:38.181768-04:30', 'E0005', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (29, 'S0029', 'BV Villa de Cura', 'Biblioteca Virtual Villa de Cura', '2015-09-14 15:11:38.199338-04:30', '2015-09-14 15:11:38.199429-04:30', 'E0001', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (30, 'S0030', 'BV Piñonal', 'Biblioteca Virtual Piñonal', '2015-09-14 15:11:38.21725-04:30', '2015-09-14 15:11:38.217338-04:30', 'E0001', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (31, 'S0031', 'BV Santa Cruz', 'Biblioteca Virtual Santa Cruz', '2015-09-14 15:11:38.235191-04:30', '2015-09-14 15:11:38.235282-04:30', 'E0003', 1, NULL);
INSERT INTO sedes_sede (id, cod_sede, sede, descripcion, fecha_create, fecha_update, eje_id, user_create_id, user_update_id) VALUES (32, 'S0032', 'Proyecto Alcatraz', 'Proyecto Alcatraz', '2015-09-14 15:11:38.253142-04:30', '2015-09-14 15:11:38.253231-04:30', 'E0001', 1, NULL);


--
-- TOC entry 2317 (class 0 OID 0)
-- Dependencies: 203
-- Name: sedes_sede_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('sedes_sede_id_seq', 32, true);


--
-- TOC entry 2009 (class 2606 OID 111686)
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- TOC entry 2015 (class 2606 OID 111688)
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- TOC entry 2017 (class 2606 OID 111690)
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 2011 (class 2606 OID 111692)
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- TOC entry 2020 (class 2606 OID 111694)
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- TOC entry 2022 (class 2606 OID 111696)
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- TOC entry 2031 (class 2606 OID 111698)
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- TOC entry 2033 (class 2606 OID 111700)
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- TOC entry 2024 (class 2606 OID 111702)
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- TOC entry 2037 (class 2606 OID 111704)
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 2039 (class 2606 OID 111706)
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- TOC entry 2027 (class 2606 OID 111708)
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- TOC entry 2098 (class 2606 OID 111910)
-- Name: autores_autor_cod_autor_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY autores_autor
    ADD CONSTRAINT autores_autor_cod_autor_key UNIQUE (cod_autor);


--
-- TOC entry 2100 (class 2606 OID 111908)
-- Name: autores_autor_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY autores_autor
    ADD CONSTRAINT autores_autor_pkey PRIMARY KEY (id);


--
-- TOC entry 2041 (class 2606 OID 111710)
-- Name: bitacora_bitacora_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY bitacora_bitacora
    ADD CONSTRAINT bitacora_bitacora_pkey PRIMARY KEY (id);


--
-- TOC entry 2046 (class 2606 OID 111712)
-- Name: categorias_categoria_cod_categoria_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY categorias_categoria
    ADD CONSTRAINT categorias_categoria_cod_categoria_key UNIQUE (cod_categoria);


--
-- TOC entry 2048 (class 2606 OID 111714)
-- Name: categorias_categoria_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY categorias_categoria
    ADD CONSTRAINT categorias_categoria_pkey PRIMARY KEY (id);


--
-- TOC entry 2052 (class 2606 OID 111716)
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- TOC entry 2054 (class 2606 OID 111718)
-- Name: django_content_type_app_label_45f3b1d93ec8c61c_uniq; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_45f3b1d93ec8c61c_uniq UNIQUE (app_label, model);


--
-- TOC entry 2056 (class 2606 OID 111720)
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- TOC entry 2058 (class 2606 OID 111722)
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- TOC entry 2061 (class 2606 OID 111724)
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- TOC entry 2105 (class 2606 OID 112363)
-- Name: editoriales_editorial_cod_editorial_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY editoriales_editorial
    ADD CONSTRAINT editoriales_editorial_cod_editorial_key UNIQUE (cod_editorial);


--
-- TOC entry 2107 (class 2606 OID 112361)
-- Name: editoriales_editorial_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY editoriales_editorial
    ADD CONSTRAINT editoriales_editorial_pkey PRIMARY KEY (id);


--
-- TOC entry 2067 (class 2606 OID 111726)
-- Name: ejes_eje_cod_eje_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY ejes_eje
    ADD CONSTRAINT ejes_eje_cod_eje_key UNIQUE (cod_eje);


--
-- TOC entry 2069 (class 2606 OID 111728)
-- Name: ejes_eje_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY ejes_eje
    ADD CONSTRAINT ejes_eje_pkey PRIMARY KEY (id);


--
-- TOC entry 2076 (class 2606 OID 111730)
-- Name: libros_libros_cod_libro_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY libros_libros
    ADD CONSTRAINT libros_libros_cod_libro_key UNIQUE (cod_libro);


--
-- TOC entry 2079 (class 2606 OID 111732)
-- Name: libros_libros_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY libros_libros
    ADD CONSTRAINT libros_libros_pkey PRIMARY KEY (id);


--
-- TOC entry 2082 (class 2606 OID 111734)
-- Name: login_perfilesusuario_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY login_perfilesusuario
    ADD CONSTRAINT login_perfilesusuario_pkey PRIMARY KEY (id);


--
-- TOC entry 2084 (class 2606 OID 111736)
-- Name: login_perfilesusuario_user_id_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY login_perfilesusuario
    ADD CONSTRAINT login_perfilesusuario_user_id_key UNIQUE (user_id);


--
-- TOC entry 2090 (class 2606 OID 111738)
-- Name: sedes_sede_cod_sede_key; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY sedes_sede
    ADD CONSTRAINT sedes_sede_cod_sede_key UNIQUE (cod_sede);


--
-- TOC entry 2093 (class 2606 OID 111740)
-- Name: sedes_sede_pkey; Type: CONSTRAINT; Schema: public; Owner: -; Tablespace: 
--

ALTER TABLE ONLY sedes_sede
    ADD CONSTRAINT sedes_sede_pkey PRIMARY KEY (id);


--
-- TOC entry 2007 (class 1259 OID 111741)
-- Name: auth_group_name_253ae2a6331666e8_like; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX auth_group_name_253ae2a6331666e8_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- TOC entry 2012 (class 1259 OID 111742)
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);


--
-- TOC entry 2013 (class 1259 OID 111743)
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);


--
-- TOC entry 2018 (class 1259 OID 111744)
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);


--
-- TOC entry 2028 (class 1259 OID 111745)
-- Name: auth_user_groups_0e939a4f; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX auth_user_groups_0e939a4f ON auth_user_groups USING btree (group_id);


--
-- TOC entry 2029 (class 1259 OID 111746)
-- Name: auth_user_groups_e8701ad4; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX auth_user_groups_e8701ad4 ON auth_user_groups USING btree (user_id);


--
-- TOC entry 2034 (class 1259 OID 111747)
-- Name: auth_user_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_8373b171 ON auth_user_user_permissions USING btree (permission_id);


--
-- TOC entry 2035 (class 1259 OID 111748)
-- Name: auth_user_user_permissions_e8701ad4; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_e8701ad4 ON auth_user_user_permissions USING btree (user_id);


--
-- TOC entry 2025 (class 1259 OID 111750)
-- Name: auth_user_username_51b3b110094b8aae_like; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX auth_user_username_51b3b110094b8aae_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- TOC entry 2094 (class 1259 OID 111921)
-- Name: autores_autor_21f9472f; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX autores_autor_21f9472f ON autores_autor USING btree (user_create_id);


--
-- TOC entry 2095 (class 1259 OID 111922)
-- Name: autores_autor_8c874724; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX autores_autor_8c874724 ON autores_autor USING btree (user_update_id);


--
-- TOC entry 2096 (class 1259 OID 111923)
-- Name: autores_autor_cod_autor_49c13095ba49b88a_like; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX autores_autor_cod_autor_49c13095ba49b88a_like ON autores_autor USING btree (cod_autor varchar_pattern_ops);


--
-- TOC entry 2042 (class 1259 OID 111751)
-- Name: categorias_categoria_21f9472f; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX categorias_categoria_21f9472f ON categorias_categoria USING btree (user_create_id);


--
-- TOC entry 2043 (class 1259 OID 111752)
-- Name: categorias_categoria_8c874724; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX categorias_categoria_8c874724 ON categorias_categoria USING btree (user_update_id);


--
-- TOC entry 2044 (class 1259 OID 111753)
-- Name: categorias_categoria_cod_categoria_39b503704c426cf2_like; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX categorias_categoria_cod_categoria_39b503704c426cf2_like ON categorias_categoria USING btree (cod_categoria varchar_pattern_ops);


--
-- TOC entry 2049 (class 1259 OID 111754)
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);


--
-- TOC entry 2050 (class 1259 OID 111755)
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);


--
-- TOC entry 2059 (class 1259 OID 111756)
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);


--
-- TOC entry 2062 (class 1259 OID 111757)
-- Name: django_session_session_key_461cfeaa630ca218_like; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX django_session_session_key_461cfeaa630ca218_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- TOC entry 2101 (class 1259 OID 112374)
-- Name: editoriales_editorial_21f9472f; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX editoriales_editorial_21f9472f ON editoriales_editorial USING btree (user_create_id);


--
-- TOC entry 2102 (class 1259 OID 112375)
-- Name: editoriales_editorial_8c874724; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX editoriales_editorial_8c874724 ON editoriales_editorial USING btree (user_update_id);


--
-- TOC entry 2103 (class 1259 OID 112376)
-- Name: editoriales_editorial_cod_editorial_6666c7607dfdb7bc_like; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX editoriales_editorial_cod_editorial_6666c7607dfdb7bc_like ON editoriales_editorial USING btree (cod_editorial varchar_pattern_ops);


--
-- TOC entry 2063 (class 1259 OID 111758)
-- Name: ejes_eje_21f9472f; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX ejes_eje_21f9472f ON ejes_eje USING btree (user_create_id);


--
-- TOC entry 2064 (class 1259 OID 111759)
-- Name: ejes_eje_8c874724; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX ejes_eje_8c874724 ON ejes_eje USING btree (user_update_id);


--
-- TOC entry 2065 (class 1259 OID 111760)
-- Name: ejes_eje_cod_eje_7a3843d50f33afa5_like; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX ejes_eje_cod_eje_7a3843d50f33afa5_like ON ejes_eje USING btree (cod_eje varchar_pattern_ops);


--
-- TOC entry 2070 (class 1259 OID 111761)
-- Name: libros_libros_0687f864; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX libros_libros_0687f864 ON libros_libros USING btree (sede_id);


--
-- TOC entry 2071 (class 1259 OID 111762)
-- Name: libros_libros_21f9472f; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX libros_libros_21f9472f ON libros_libros USING btree (user_create_id);


--
-- TOC entry 2072 (class 1259 OID 111763)
-- Name: libros_libros_8c874724; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX libros_libros_8c874724 ON libros_libros USING btree (user_update_id);


--
-- TOC entry 2073 (class 1259 OID 111764)
-- Name: libros_libros_categoria_id_7246453c4755ea92_like; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX libros_libros_categoria_id_7246453c4755ea92_like ON libros_libros USING btree (categoria_id varchar_pattern_ops);


--
-- TOC entry 2074 (class 1259 OID 111765)
-- Name: libros_libros_cod_libro_670b7980efe1eb37_like; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX libros_libros_cod_libro_670b7980efe1eb37_like ON libros_libros USING btree (cod_libro varchar_pattern_ops);


--
-- TOC entry 2077 (class 1259 OID 111766)
-- Name: libros_libros_daf3833b; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX libros_libros_daf3833b ON libros_libros USING btree (categoria_id);


--
-- TOC entry 2080 (class 1259 OID 111767)
-- Name: libros_libros_sede_id_179bd09e03baf207_like; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX libros_libros_sede_id_179bd09e03baf207_like ON libros_libros USING btree (sede_id varchar_pattern_ops);


--
-- TOC entry 2085 (class 1259 OID 111768)
-- Name: sedes_sede_21f9472f; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX sedes_sede_21f9472f ON sedes_sede USING btree (user_create_id);


--
-- TOC entry 2086 (class 1259 OID 111769)
-- Name: sedes_sede_8c874724; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX sedes_sede_8c874724 ON sedes_sede USING btree (user_update_id);


--
-- TOC entry 2087 (class 1259 OID 111770)
-- Name: sedes_sede_9f752dfe; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX sedes_sede_9f752dfe ON sedes_sede USING btree (eje_id);


--
-- TOC entry 2088 (class 1259 OID 111771)
-- Name: sedes_sede_cod_sede_7321d55d703c3fe5_like; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX sedes_sede_cod_sede_7321d55d703c3fe5_like ON sedes_sede USING btree (cod_sede varchar_pattern_ops);


--
-- TOC entry 2091 (class 1259 OID 111772)
-- Name: sedes_sede_eje_id_51d5615b97ffd8b7_like; Type: INDEX; Schema: public; Owner: -; Tablespace: 
--

CREATE INDEX sedes_sede_eje_id_51d5615b97ffd8b7_like ON sedes_sede USING btree (eje_id varchar_pattern_ops);


--
-- TOC entry 2121 (class 2606 OID 111773)
-- Name: D9142ee944241a855f2d2687194b41f6; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY libros_libros
    ADD CONSTRAINT "D9142ee944241a855f2d2687194b41f6" FOREIGN KEY (categoria_id) REFERENCES categorias_categoria(cod_categoria) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2110 (class 2606 OID 111778)
-- Name: auth_content_type_id_508cf46651277a81_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_content_type_id_508cf46651277a81_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2108 (class 2606 OID 111783)
-- Name: auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2109 (class 2606 OID 111788)
-- Name: auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2113 (class 2606 OID 111793)
-- Name: auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2111 (class 2606 OID 111798)
-- Name: auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2112 (class 2606 OID 111803)
-- Name: auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2114 (class 2606 OID 111808)
-- Name: auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2129 (class 2606 OID 111911)
-- Name: autores_autor_user_create_id_33fca06d1a87d21_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY autores_autor
    ADD CONSTRAINT autores_autor_user_create_id_33fca06d1a87d21_fk_auth_user_id FOREIGN KEY (user_create_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2130 (class 2606 OID 111916)
-- Name: autores_autor_user_update_id_40a66a82f6fa7b7a_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY autores_autor
    ADD CONSTRAINT autores_autor_user_update_id_40a66a82f6fa7b7a_fk_auth_user_id FOREIGN KEY (user_update_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2115 (class 2606 OID 111813)
-- Name: categorias_cate_user_create_id_1cbb44a658b584db_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY categorias_categoria
    ADD CONSTRAINT categorias_cate_user_create_id_1cbb44a658b584db_fk_auth_user_id FOREIGN KEY (user_create_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2116 (class 2606 OID 111818)
-- Name: categorias_cate_user_update_id_5db003ec8d97cc5a_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY categorias_categoria
    ADD CONSTRAINT categorias_cate_user_update_id_5db003ec8d97cc5a_fk_auth_user_id FOREIGN KEY (user_update_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2117 (class 2606 OID 111823)
-- Name: djan_content_type_id_697914295151027a_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT djan_content_type_id_697914295151027a_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2118 (class 2606 OID 111828)
-- Name: django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2131 (class 2606 OID 112364)
-- Name: editoriales_edi_user_create_id_614fe19c4e7b1f83_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY editoriales_editorial
    ADD CONSTRAINT editoriales_edi_user_create_id_614fe19c4e7b1f83_fk_auth_user_id FOREIGN KEY (user_create_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2132 (class 2606 OID 112369)
-- Name: editoriales_edi_user_update_id_21a9404bd8227b82_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY editoriales_editorial
    ADD CONSTRAINT editoriales_edi_user_update_id_21a9404bd8227b82_fk_auth_user_id FOREIGN KEY (user_update_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2119 (class 2606 OID 111833)
-- Name: ejes_eje_user_create_id_43e32a371da935b5_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY ejes_eje
    ADD CONSTRAINT ejes_eje_user_create_id_43e32a371da935b5_fk_auth_user_id FOREIGN KEY (user_create_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2120 (class 2606 OID 111838)
-- Name: ejes_eje_user_update_id_674a28ea9e926480_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY ejes_eje
    ADD CONSTRAINT ejes_eje_user_update_id_674a28ea9e926480_fk_auth_user_id FOREIGN KEY (user_update_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2122 (class 2606 OID 111843)
-- Name: libros_libros_sede_id_179bd09e03baf207_fk_sedes_sede_cod_sede; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY libros_libros
    ADD CONSTRAINT libros_libros_sede_id_179bd09e03baf207_fk_sedes_sede_cod_sede FOREIGN KEY (sede_id) REFERENCES sedes_sede(cod_sede) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2123 (class 2606 OID 111848)
-- Name: libros_libros_user_create_id_2ff0ee6244c8164b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY libros_libros
    ADD CONSTRAINT libros_libros_user_create_id_2ff0ee6244c8164b_fk_auth_user_id FOREIGN KEY (user_create_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2124 (class 2606 OID 111853)
-- Name: libros_libros_user_update_id_12ce7cc53b474e8a_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY libros_libros
    ADD CONSTRAINT libros_libros_user_update_id_12ce7cc53b474e8a_fk_auth_user_id FOREIGN KEY (user_update_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2125 (class 2606 OID 111858)
-- Name: login_perfilesusuario_user_id_68b0ace2f71d1bee_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY login_perfilesusuario
    ADD CONSTRAINT login_perfilesusuario_user_id_68b0ace2f71d1bee_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2126 (class 2606 OID 111863)
-- Name: sedes_sede_eje_id_51d5615b97ffd8b7_fk_ejes_eje_cod_eje; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY sedes_sede
    ADD CONSTRAINT sedes_sede_eje_id_51d5615b97ffd8b7_fk_ejes_eje_cod_eje FOREIGN KEY (eje_id) REFERENCES ejes_eje(cod_eje) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2127 (class 2606 OID 111868)
-- Name: sedes_sede_user_create_id_3b438b33e88e9cb9_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY sedes_sede
    ADD CONSTRAINT sedes_sede_user_create_id_3b438b33e88e9cb9_fk_auth_user_id FOREIGN KEY (user_create_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- TOC entry 2128 (class 2606 OID 111873)
-- Name: sedes_sede_user_update_id_484f283e79bdf512_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY sedes_sede
    ADD CONSTRAINT sedes_sede_user_update_id_484f283e79bdf512_fk_auth_user_id FOREIGN KEY (user_update_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


-- Completed on 2017-02-08 15:40:49 VET

--
-- PostgreSQL database dump complete
--


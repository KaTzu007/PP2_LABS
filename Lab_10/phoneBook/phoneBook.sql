PGDMP                      }         	   phoneBook    17.4    17.4                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false                        0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            !           1262    16414 	   phoneBook    DATABASE     q   CREATE DATABASE "phoneBook" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'ru-RU';
    DROP DATABASE "phoneBook";
                     postgres    false            �            1259    16416 	   phonebook    TABLE     l   CREATE TABLE public.phonebook (
    id integer NOT NULL,
    name text NOT NULL,
    phone text NOT NULL
);
    DROP TABLE public.phonebook;
       public         heap r       postgres    false            �            1259    16415    phonebook_id_seq    SEQUENCE     �   CREATE SEQUENCE public.phonebook_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.phonebook_id_seq;
       public               postgres    false    218            "           0    0    phonebook_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.phonebook_id_seq OWNED BY public.phonebook.id;
          public               postgres    false    217            �           2604    16419    phonebook id    DEFAULT     l   ALTER TABLE ONLY public.phonebook ALTER COLUMN id SET DEFAULT nextval('public.phonebook_id_seq'::regclass);
 ;   ALTER TABLE public.phonebook ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    218    217    218                      0    16416 	   phonebook 
   TABLE DATA           4   COPY public.phonebook (id, name, phone) FROM stdin;
    public               postgres    false    218   �
       #           0    0    phonebook_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.phonebook_id_seq', 1, false);
          public               postgres    false    217            �           2606    16423    phonebook phonebook_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.phonebook
    ADD CONSTRAINT phonebook_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.phonebook DROP CONSTRAINT phonebook_pkey;
       public                 postgres    false    218                  x������ � �     
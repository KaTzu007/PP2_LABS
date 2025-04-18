PGDMP  *    (                }            phonebook11    17.4    17.4     '           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            (           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            )           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            *           1262    16433    phonebook11    DATABASE     q   CREATE DATABASE phonebook11 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'ru-RU';
    DROP DATABASE phonebook11;
                     postgres    false            X           1247    16473 	   userinput    TYPE     a   CREATE TYPE public.userinput AS (
	inname text,
	insurname text,
	innumber text,
	len integer
);
    DROP TYPE public.userinput;
       public               postgres    false            �            1255    16455    deletefromtable(text, text) 	   PROCEDURE     0  CREATE PROCEDURE public.deletefromtable(IN targetname text DEFAULT NULL::text, IN targetnumber text DEFAULT NULL::text)
    LANGUAGE plpgsql
    AS $$
BEGIN
DELETE FROM phonebook p
WHERE (targetname IS NOT NULL AND p.name = targetname)
OR (targetnumber IS NOT NULL AND p.number = targetnumber);
END;
$$;
 Q   DROP PROCEDURE public.deletefromtable(IN targetname text, IN targetnumber text);
       public               postgres    false            �            1255    16470     insertorupdate(text, text, text) 	   PROCEDURE     �  CREATE PROCEDURE public.insertorupdate(IN inname text, IN insurname text, IN innumber text)
    LANGUAGE plpgsql
    AS $$
DECLARE
usercount INT;
BEGIN
SELECT COUNT(*) INTO usercount FROM phonebook
WHERE name = inname AND surname = insurname;
IF usercount = 0 THEN
INSERT INTO phonebook (name, surname, number)
VALUES (inname, insurname, innumber);
ELSE
UPDATE phonebook
SET number = innumber
WHERE name = inname AND surname = insurname;
END IF;
END;
$$;
 [   DROP PROCEDURE public.insertorupdate(IN inname text, IN insurname text, IN innumber text);
       public               postgres    false            �            1255    16475    manyusers(public.userinput[]) 	   PROCEDURE     �  CREATE PROCEDURE public.manyusers(IN users public.userinput[])
    LANGUAGE plpgsql
    AS $$
DECLARE
u userinput
;
invalidusers userinput[] := '{}';
BEGIN
FOREACH u IN ARRAY users
LOOP
IF u.len = 15 THEN
CALL insertorupdate(u.inname, u.insurname, u.innumber);
ELSE
invalidusers := array_append(invalidusers, u);
END IF;
END LOOP;
RAISE NOTICE 'Invalid users: %', invalidusers;
END;
$$;
 >   DROP PROCEDURE public.manyusers(IN users public.userinput[]);
       public               postgres    false    856            �            1255    16454    pagination(integer, integer)    FUNCTION     )  CREATE FUNCTION public.pagination(limitint integer, offsetint integer) RETURNS TABLE(id integer, name text, surname text, number text)
    LANGUAGE plpgsql
    AS $$
BEGIN
RETURN QUERY
SELECT p.id, p.name, p.surname, p.number FROM phonebook p
ORDER BY id
LIMIT limitint OFFSET offsetint;
END;
$$;
 F   DROP FUNCTION public.pagination(limitint integer, offsetint integer);
       public               postgres    false            �            1255    16453 !   searchbypattern(text, text, text)    FUNCTION     .  CREATE FUNCTION public.searchbypattern(namepattern text DEFAULT NULL::text, surnamepattern text DEFAULT NULL::text, numberpattern text DEFAULT NULL::text) RETURNS TABLE(id integer, name text, surname text, number text)
    LANGUAGE plpgsql
    AS $$
BEGIN
RETURN QUERY
SELECT p.id, p.name, p.surname, p.number FROM phonebook p
WHERE (namePattern IS NULL OR p.name ILIKE '%' || namePattern || '%')
AND (surnamePattern IS NULL OR p.surname ILIKE '%' || surnamePattern || '%')
AND (numberPattern IS NULL OR p.number ILIKE '%' || numberPattern || '%');
END;
$$;
 a   DROP FUNCTION public.searchbypattern(namepattern text, surnamepattern text, numberpattern text);
       public               postgres    false            �            1259    16457 	   phonebook    TABLE     m   CREATE TABLE public.phonebook (
    id integer NOT NULL,
    name text,
    surname text,
    number text
);
    DROP TABLE public.phonebook;
       public         heap r       postgres    false            �            1259    16456    phonebook_id_seq    SEQUENCE     �   CREATE SEQUENCE public.phonebook_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.phonebook_id_seq;
       public               postgres    false    218            +           0    0    phonebook_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.phonebook_id_seq OWNED BY public.phonebook.id;
          public               postgres    false    217            �           2604    16460    phonebook id    DEFAULT     l   ALTER TABLE ONLY public.phonebook ALTER COLUMN id SET DEFAULT nextval('public.phonebook_id_seq'::regclass);
 ;   ALTER TABLE public.phonebook ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    217    218    218            $          0    16457 	   phonebook 
   TABLE DATA           >   COPY public.phonebook (id, name, surname, number) FROM stdin;
    public               postgres    false    218   K       ,           0    0    phonebook_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.phonebook_id_seq', 9, true);
          public               postgres    false    217            �           2606    16464    phonebook phonebook_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.phonebook
    ADD CONSTRAINT phonebook_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.phonebook DROP CONSTRAINT phonebook_pkey;
       public                 postgres    false    218            $   �   x�5�=�0D�����p
M2vD|���QCU��1�J�?�Yp���
��b���58������>>p��H$��P'�,j'|h[�B{t���*"���0�����5�gEgX�������&     
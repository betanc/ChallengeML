CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_name TEXT,
    fec_alta TIMESTAMP,
    codigo_zip TEXT,
    cuenta_numero TEXT,  --  tc clien
    direccion TEXT,
    geo_latitud NUMERIC,
    geo_longitud NUMERIC,
    color_favorito TEXT,
    foto_dni TEXT,
    ip TEXT,
    auto TEXT,
    auto_modelo TEXT,
    auto_tipo TEXT,
    auto_color TEXT,
    cantidad_compras_realizadas INTEGER,
    avatar TEXT,
    fec_birthday TIMESTAMP
);

CREATE TABLE credit_cards (
    id SERIAL PRIMARY KEY,
    cuenta_numero TEXT,  -- tc clien
    user_id INTEGER,
    credit_card_num TEXT,
    credit_card_ccv TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

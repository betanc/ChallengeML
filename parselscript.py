import json

# Parsel de los datos compartidos
def generate_sql(json_data, file):
    for item in json_data:
        user_insert = f"""
        INSERT INTO users(id, user_name, fec_alta, codigo_zip, cuenta_numero, direccion, geo_latitud, geo_longitud, color_favorito, foto_dni, ip, auto, auto_modelo, auto_tipo, auto_color, cantidad_compras_realizadas, avatar, fec_birthday) 
        VALUES ('{item.get('id', 'NULL')}', '{item.get('user_name', 'NULL')}', '{item.get('fec_alta', 'NULL')}', '{item.get('codigo_zip', 'NULL')}', '{item.get('cuenta_numero', 'NULL')}', '{item.get('direccion', 'NULL')}', '{item.get('geo_latitud', 'NULL')}', '{item.get('geo_longitud', 'NULL')}', '{item.get('color_favorito', 'NULL')}', '{item.get('foto_dni', 'NULL')}', '{item.get('ip', 'NULL')}', '{item.get('auto', 'NULL')}', '{item.get('auto_modelo', 'NULL')}', '{item.get('auto_tipo', 'NULL')}', '{item.get('auto_color', 'NULL')}', '{item.get('cantidad_compras_realizadas', 'NULL')}', '{item.get('avatar', 'NULL')}', '{item.get('fec_birthday', 'NULL')}');
        """
        file.write(user_insert)

        cc_insert = f"""
        INSERT INTO credit_cards(user_id, cuenta_numero, credit_card_num, credit_card_ccv) 
        VALUES ('{item.get('id', 'NULL')}', '{item.get('cuenta_numero', 'NULL')}', '{item.get('credit_card_num', 'NULL')}', '{item.get('credit_card_ccv', 'NULL')}');
        """
        file.write(cc_insert)

# Load the JSON data
with open('datos.json') as f:
    data = json.load(f)

# escribir en data.sql
with open('data.sql', 'w') as f:
    generate_sql(data, f)
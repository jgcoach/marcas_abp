import sqlite3
conn = sqlite3.connect('data-riv.db',check_same_thread=False)
c = conn.cursor()


def create_table_riv():
	c.execute('CREATE TABLE IF NOT EXISTS tablariv(rival TEXT,alineacionriv TEXT,amenaza1 INTEGER,amenaza2 INTEGER)')


def add_data_riv(rival,alineacionriv,amenaza1,amenaza2):
	c.execute('INSERT INTO tablariv(rival,alineacionriv,amenaza1,amenaza2) VALUES (?,?,?,?)',(rival,alineacionriv,amenaza1,amenaza2))
	conn.commit()


def view_all_data_riv():
	c.execute('SELECT * FROM tablariv')
	data = c.fetchall()
	return data

def view_all_nombres_riv():
	c.execute('SELECT DISTINCT rival FROM tablariv')
	data = c.fetchall()
	return data

def view_titulares_riv():
	c.execute('SELECT DISTINCT rival FROM tablariv WHERE alineacionriv="Titular"')
	data = c.fetchall()
	return data

def view_suplentes_riv():
	c.execute('SELECT DISTINCT rival FROM tablariv WHERE alineacionriv="Suplente"')
	data = c.fetchall()
	return data

def view_estado_tit_riv():
	c.execute('SELECT DISTINCT alineacionriv FROM tablariv WHERE alineacionriv="Titular"')
	data = c.fetchall()
	return data

def view_estado_sup_riv():
	c.execute('SELECT DISTINCT alineacionriv FROM tablariv WHERE alineacionriv="Suplente"')
	data = c.fetchall()
	return data

def get_rival(rival):
	c.execute('SELECT * FROM tablariv WHERE rival="{}"'.format(rival))
	data = c.fetchall()
	return data

def get_amenaza1(amenaza1):
	c.execute('SELECT * FROM tablariv WHERE amenaza1="{}"'.format(amenaza1))
	data = c.fetchall()

def edit_rival_tit_to_sup(selected_titular_riv,selected_suplente_riv):
	c.execute('UPDATE tablariv SET alineacionriv="Suplente" WHERE rival="{}" and alineacionriv="Titular"'.format(selected_titular_riv))
	c.execute('UPDATE tablariv SET alineacionriv="Titular" WHERE rival="{}" and alineacionriv="Suplente"'.format(selected_suplente_riv))
	conn.commit()
	data = c.fetchall()
	return data

def edit_rival(new_rival,new_alineacionriv,new_amenaza1,new_amenaza2,rival,alineacionriv,amenaza1,amenaza2):
	c.execute("UPDATE tablariv SET rival=?,alineacionriv=?,amenaza1=?,amenaza2=? WHERE rival=? and alineacionriv=? and amenaza1=? and amenaza2=? ",(new_rival,new_alineacionriv,new_amenaza1,new_amenaza2,rival,alineacionriv,amenaza1,amenaza2))
	conn.commit()
	data = c.fetchall()
	return data

def sustitucion_rival(new_alineacionriv,alineacionriv):
	c.execute("UPDATE tablariv SET alineacionriv=? WHERE alineacionriv=? ",(new_alineacionriv,alineacionriv))
	conn.commit()
	data = c.fetchall()
	return data

def delete_rival(rival):
	c.execute('DELETE FROM tablariv WHERE rival="{}"'.format(rival))
	conn.commit()
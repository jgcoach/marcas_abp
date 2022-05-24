import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()


def create_table_atm():
	c.execute('CREATE TABLE IF NOT EXISTS tablaatm(jugadora TEXT,alineacion TEXT,prioridad1 INTEGER,prioridad2 INTEGER,prioridad3 INTEGER)')


def add_data(jugadora,alineacion,prioridad1,prioridad2,prioridad3):
	c.execute('INSERT INTO tablaatm(jugadora,alineacion,prioridad1,prioridad2,prioridad3) VALUES (?,?,?,?,?)',(jugadora,alineacion,prioridad1,prioridad2,prioridad3))
	conn.commit()


def view_all_data():
	c.execute('SELECT * FROM tablaatm')
	data = c.fetchall()
	return data

def view_all_nombres_jugadoras():
	c.execute('SELECT DISTINCT jugadora FROM tablaatm')
	data = c.fetchall()
	return data

def get_jugadora(jugadora):
	c.execute('SELECT * FROM tablaatm WHERE jugadora="{}"'.format(jugadora))
	data = c.fetchall()
	return data

def get_prioridad1(prioridad1):
	c.execute('SELECT * FROM tablaatm WHERE prioridad1="{}"'.format(prioridad1))
	data = c.fetchall()


def edit_jugadora(new_jugadora,new_alineacion,new_prioridad1,new_prioridad2,new_prioridad3,jugadora,alineacion,prioridad1,prioridad2,prioridad3):
	c.execute("UPDATE tablaatm SET jugadora=?,alineacion=?,prioridad1=?,prioridad2=?,prioridad3=? WHERE jugadora=? and alineacion=? and prioridad1=? and prioridad2=? and prioridad3=? ",(new_jugadora,new_alineacion,new_prioridad1,new_prioridad2,new_prioridad3,jugadora,alineacion,prioridad1,prioridad2,prioridad3))
	conn.commit()
	data = c.fetchall()
	return data

def view_titulares():
	c.execute('SELECT DISTINCT jugadora FROM tablaatm WHERE alineacion="Titular"')
	data = c.fetchall()
	return data

def view_suplentes():
	c.execute('SELECT DISTINCT jugadora FROM tablaatm WHERE alineacion="Suplente"')
	data = c.fetchall()
	return data

def edit_tit_to_sup(selected_titular,selected_suplente):
	c.execute('UPDATE tablaatm SET alineacion="Suplente" WHERE jugadora="{}" and alineacion="Titular"'.format(selected_titular))
	c.execute('UPDATE tablaatm SET alineacion="Titular" WHERE jugadora="{}" and alineacion="Suplente"'.format(selected_suplente))
	conn.commit()
	data = c.fetchall()
	return data

def delete_jugadora(jugadora_result_del):
	c.execute('DELETE FROM tablaatm WHERE jugadora="{}"'.format(jugadora_result_del))
	conn.commit()

def delete_equipo(jugadora,alineacion,prioridad1,prioridad2,prioridad3):
	c.execute('DELETE FROM tablaatm')
	conn.commit()
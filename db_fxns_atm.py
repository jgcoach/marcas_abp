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

def sustitucion(new_alineacion,alineacion):
	c.execute("UPDATE tablaatm SET alineacion=? WHERE alineacion=? ",(new_alineacion,alineacion))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(jugadora):
	c.execute('DELETE FROM tablaatm WHERE jugadora="{}"'.format(jugadora))
	conn.commit()
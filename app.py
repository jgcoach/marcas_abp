import streamlit as st
import pandas as pd
import numpy as np
from db_fxns_atm import * 
from db_fxns_riv import * 

def main():
	st.title("App Marcas en Córners")
	menu = ["Equipo ATM","Equipo Rival","Marcas","Sustituciones"]
	choice = st.sidebar.selectbox("Menu",menu)
	create_table_atm()
	create_table_riv()

	if choice == "Equipo ATM":
		st.subheader("Añadir Jugadoras ATM")

		jugadora = st.text_input("Jugadora ATM")
		alineacion = st.selectbox("Alineación",["Titular","Suplente"])
		prioridad1 = st.selectbox("Prioridad 1", ["Individual","Zona","Frontal"])
		prioridad2 = st.selectbox("Prioridad 2", ["Individual","Zona","Frontal"])
		prioridad3 = st.selectbox("Prioridad 3", ["Individual","Zona","Frontal"])

		if st.button("Añadir Jugadora"):
			add_data(jugadora,alineacion,prioridad1,prioridad2,prioridad3)
			st.success("{} añadida con éxito a la lista de Jugadoras ATM".format(jugadora))

		result = view_all_data()
		clean_df = pd.DataFrame(result,columns=["Jugadora ATM","Alineación","Prioridad 1","Prioridad 2","Prioridad 3"])
		st.dataframe(clean_df)

		with st.expander("Editar Jugadora ATM"):

			lista_jugadoras = [i[0] for i in view_all_nombres_jugadoras()]
			selected_jugadora = st.selectbox("Jugadora",lista_jugadoras)
			jugadora_result = get_jugadora(selected_jugadora)
			#st.write(jugadora_result)

			if jugadora_result:

				jugadora = jugadora_result[0][0]
				alineacion = jugadora_result[0][1]
				prioridad1 = jugadora_result[0][2]
				prioridad2 = jugadora_result[0][3]
				prioridad3 = jugadora_result[0][4]
				
				new_jugadora = st.text_input("Modificar Nombre",jugadora)	
				new_alineacion = st.selectbox("Nueva Alineación",["Titular","Suplente"])
				new_prioridad1 = st.selectbox("Nueva Prioridad 1", ["Individual","Zona","Frontal"])
				new_prioridad2 = st.selectbox("Nueva Prioridad 2", ["Individual","Zona","Frontal"])
				new_prioridad3 = st.selectbox("Nueva Prioridad 3", ["Individual","Zona","Frontal"])

				if st.button("Actualizar Jugadora ATM"):
					edit_jugadora(new_jugadora,new_alineacion,new_prioridad1,new_prioridad2,new_prioridad3,jugadora,alineacion,prioridad1,prioridad2,prioridad3)
					st.success("{} Jugadora Actualizada {}".format(jugadora,new_jugadora))
				
		with st.expander("Ver Lista Actualizada"):
			result2 = view_all_data()
			# st.write(result)
			clean_df2 = pd.DataFrame(result2,columns=["Jugadora","Alineación","Prioridad 1","Prioridad 2","Prioridad 3"])
			st.dataframe(clean_df2)
			
	if choice == "Equipo Rival":
		st.subheader("Añadir Jugadoras Rivales")

		rival = st.text_input("Jugadora Rival")
		alineacionriv = st.selectbox("Alineación",["Titular","Suplente"])
		amenaza1 = st.selectbox("Amenaza 1", ["1","2","3"])
		amenaza2 = st.selectbox("Amenaza 2", ["1","2","3"])

		if st.button("Añadir Jugadora Rival"):
			add_data_riv(rival,alineacionriv,amenaza1,amenaza2)
			st.success("{} añadida con éxito a la lista de Jugadoras Rivales".format(rival))

		result_riv = view_all_data_riv()
		clean_df_riv = pd.DataFrame(result_riv,columns=["Jugadora Rival","Alineación","Amenaza 1","Amenaza 2"])
		st.dataframe(clean_df_riv)

		with st.expander("Editar Jugadora Rival"):

			lista_jugadoras_riv = [i[0] for i in view_all_nombres_riv()]
			selected_jugadora_riv = st.selectbox("Jugadora",lista_jugadoras_riv)
			jugadora_riv_result = get_rival(selected_jugadora_riv)
			#st.write(jugadora_result)

			if jugadora_riv_result:

				rival = jugadora_riv_result[0][0]
				alineacionriv = jugadora_riv_result[0][1]
				amenaza1 = jugadora_riv_result[0][2]
				amenaza2 = jugadora_riv_result[0][3]
				
				new_rival = st.text_input("Modificar Nombre",rival)	
				new_alineacionriv = st.selectbox("Nueva Alineación",["Titular","Suplente"])
				new_amenaza1 = st.selectbox("Nueva Amenaza 1", ["1","2","3"])
				new_amenaza2 = st.selectbox("Nueva Amenaza 2", ["1","2","3"])

				if st.button("Actualizar Jugadora Rival"):
					edit_rival(new_rival,new_alineacionriv,new_amenaza1,new_amenaza2,rival,alineacionriv,amenaza1,amenaza2)
					st.success("{} Jugadora Actualizada {}".format(rival,new_rival))
				
		with st.expander("Ver Lista Actualizada"):
			result3 = view_all_data_riv()
			# st.write(result)
			clean_df3 = pd.DataFrame(result3,columns=["Jugadora Rival","Alineación","Amenaza 1","Amenaza 2"])
			st.dataframe(clean_df3)		

	if choice == "Marcas":
		st.subheader("Asignación de marcas ABP")

		col1,col2 = st.columns(2)

		result3 = view_all_data()
		df = pd.DataFrame(result3,columns=["Jugadora ATM","Alineación","Prioridad 1", "Prioridad 2", "Prioridad 3"])

		df.loc[ ( (df['Prioridad 1']) == 'Individual'), 'P1' ] = 'A'
		df.loc[ ( (df['Prioridad 1']) == 'Zona'), 'P1' ] = 'B'
		df.loc[ ( (df['Prioridad 1']) == 'Frontal'), 'P1' ] = 'C'
		df.loc[ ( (df['Prioridad 2']) == 'Individual'), 'P2' ] = 'A'
		df.loc[ ( (df['Prioridad 2']) == 'Zona'), 'P2' ] = 'B'
		df.loc[ ( (df['Prioridad 2']) == 'Frontal'), 'P2' ] = 'C'
		df.loc[ ( (df['Prioridad 3']) == 'Individual'), 'P3' ] = 'A'
		df.loc[ ( (df['Prioridad 3']) == 'Zona'), 'P3' ] = 'B'
		df.loc[ ( (df['Prioridad 3']) == 'Frontal'), 'P3' ] = 'C'

		df['Tipo'] = df['P1']+df['P2']+df['P3']

		# Prioridad individual

		df.loc[ ( (df['Tipo']) == 'AAB'), 'Prioridad Ind' ] = '1'
		df.loc[ ( (df['Tipo']) == 'AAC'), 'Prioridad Ind' ] = '2'
		df.loc[ ( (df['Tipo']) == 'ABA'), 'Prioridad Ind' ] = '3'
		df.loc[ ( (df['Tipo']) == 'ABC'), 'Prioridad Ind' ] = '4'
		df.loc[ ( (df['Tipo']) == 'ACB'), 'Prioridad Ind' ] = '5'
		df.loc[ ( (df['Tipo']) == 'ACC'), 'Prioridad Ind' ] = '6'
		df.loc[ ( (df['Tipo']) == 'BBA'), 'Prioridad Ind' ] = '7'
		df.loc[ ( (df['Tipo']) == 'BBC'), 'Prioridad Ind' ] = '8'
		df.loc[ ( (df['Tipo']) == 'BAB'), 'Prioridad Ind' ] = '9'
		df.loc[ ( (df['Tipo']) == 'BAC'), 'Prioridad Ind' ] = '10'
		df.loc[ ( (df['Tipo']) == 'ABB'), 'Prioridad Ind' ] = '11'
		df.loc[ ( (df['Tipo']) == 'CCA'), 'Prioridad Ind' ] = '12'
		df.loc[ ( (df['Tipo']) == 'CCB'), 'Prioridad Ind' ] = '13'
		df.loc[ ( (df['Tipo']) == 'CAC'), 'Prioridad Ind' ] = '14'
		df.loc[ ( (df['Tipo']) == 'CBC'), 'Prioridad Ind' ] = '15'
		df.loc[ ( (df['Tipo']) == 'CAB'), 'Prioridad Ind' ] = '16'

		df['Prioridad Ind'] = df['Prioridad Ind'].astype(int)

		tit_df = df[df.Alineación.eq('Titular')]

		tit_df['PRI'] = pd.cut(tit_df['Prioridad Ind'], bins=[0,6,12,17], labels=[3, 1, 2]).to_numpy()

		#(2)
		ordered_priority_df = tit_df.sort_values(by=['PRI'])

		#(3)
		out = np.split(ordered_priority_df, [3,5])

		result4 = view_all_data_riv()
		dfr = pd.DataFrame(result4,columns=["Jugadora Rival","Alineación","Amenaza 1", "Amenaza 2"])
		dfr['Nivel de Amenaza'] = dfr['Amenaza 1']+dfr['Amenaza 2']-1
		tit_dfr = dfr[dfr.Alineación.eq('Titular')].sort_values(by=['Nivel de Amenaza']).head(5)

		with col1:
			st.subheader("Marcas individuales")
			st.dataframe(out[2].sort_values(by=['Prioridad Ind']).head(5))
			st.subheader("Marcas en Zona")
			st.dataframe(out[0].sort_values(by=['Prioridad Ind'], ascending=False))
			st.subheader("Fuera del área")
			st.dataframe(out[1].sort_values(by=['Prioridad Ind']))

		with col2:
			st.subheader("Amenazas Rivales")
			st.dataframe(tit_dfr)

	if choice == "Sustituciones":
		st.subheader("Cambios en el rival")
		result5 = view_all_data_riv()

		lista_titulares_riv = [i[0] for i in view_titulares_riv()]
		selected_titular_riv = st.selectbox("Jugadora Titular",lista_titulares_riv)

		lista_suplentes_riv = [i[0] for i in view_suplentes_riv()]
		selected_suplente_riv = st.selectbox("Jugadora Suplente",lista_suplentes_riv)

		if st.button("Confirmar Cambio"):
			edit_rival_tit_to_sup(selected_titular_riv,selected_suplente_riv)
			st.success("{} sustituida con éxito por {}".format(selected_titular_riv,selected_suplente_riv))


if __name__ == '__main__':
	main()
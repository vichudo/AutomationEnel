import pandas as pd
import numpy as np
import streamlit as st
import base64
import io

st.title("Automated GDA")

df = pd.DataFrame()
uploaded_file = st.file_uploader(
    'Sube un archivo del tipo "GD_Comercial_Detalle_de_registros_XXXXXX.xls"', type='xls')


if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    df_ = df[df['Estado'] ==
             '7 - Requiere que devuelvan el llamado (marco 5)']
    st.text(df_)
    #st.download_button("Descargar", df_.to_excel("Final.xls"))

    # df_.to_excel(
    #   'update2.xlsx', index=False, header=True, encoding='utf-8')

    towrite = io.BytesIO()
    downloaded_file = df_.to_excel(
        towrite, encoding='utf-8', index=False, header=True)  # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    linko = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="GDA Konecta ready.xlsx">Descargar Excel</a>'
    st.markdown(linko, unsafe_allow_html=True)

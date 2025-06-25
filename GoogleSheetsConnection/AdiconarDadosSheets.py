'''
----Instalação:----
pip install gspread pandas streamlit
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2
-------------------
'''
import streamlit as st
import gspread #interagir com o google sheets
import pandas as pd #manipulação de dados
from google.oauth2.service_account import Credentials 
    #serviço de credencial - autenticação do google


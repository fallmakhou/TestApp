import streamlit as st

# Titre de l'application
st.title("Qui est la plus belle ?")

# Champ d'entrée pour l'utilisateur
reponse = st.text_input("C'est qui la plus belle ?")

# Vérification de la réponse
if reponse:
    if reponse == "Nafissatou Diagne Diallo":
        st.success("Correct! T'es un connaisseur toi")
    else:
        st.error("Faux! La plus belle est Nafissatou Diagne Diallo.")

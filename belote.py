import streamlit as st

# Initialiser les scores et l'état du gagnant si cela n'a pas encore été fait
if "score_joueur1" not in st.session_state:
    st.session_state.score_joueur1 = 0
if "score_joueur2" not in st.session_state:
    st.session_state.score_joueur2 = 0
if "gagnant" not in st.session_state:
    st.session_state.gagnant = False

def saisir_bilan():
    # Saisie des noms des joueurs
    joueur1 = st.text_input("Entrez le nom du joueur 1 : ", key="joueur1_name")
    joueur2 = st.text_input("Entrez le nom du joueur 2 : ", key="joueur2_name")

    # Afficher les inputs de score seulement si les noms des joueurs sont fournis
    if joueur1 and joueur2 and not st.session_state.gagnant:
        # Entrée des points pour chaque tour avec des clés uniques
        points_joueur1 = st.number_input(f"Entrez les points de {joueur1.upper()} pour ce tour : ", min_value=0, step=1, key="points_joueur1")
        points_joueur2 = st.number_input(f"Entrez les points de {joueur2.upper()} pour ce tour : ", min_value=0, step=1, key="points_joueur2")

        # Mettre à jour les scores lorsque le bouton est cliqué
        if st.button("Mettre à jour les scores"):
            st.session_state.score_joueur1 += points_joueur1
            st.session_state.score_joueur2 += points_joueur2
            st.write(f"Score actuel - {joueur1} : {st.session_state.score_joueur1}, {joueur2} : {st.session_state.score_joueur2}")


        # Vérifier si l'un des joueurs a gagné
        if st.session_state.score_joueur1 >= 70:
            st.success(f"{joueur1.upper()} a gagné ! Félicitations !")
            st.error(f"{joueur2}, t'es nul !")
            st.session_state.gagnant = True
        elif st.session_state.score_joueur2 >= 70:
            st.success(f"{joueur2.upper()} a gagné ! Félicitations !")
            st.error(f"{joueur1.upper()}, t'es nul !")
            st.session_state.gagnant = True

    # Bouton pour réinitialiser le jeu
    if st.button("Réinitialiser le jeu"):
        st.session_state.score_joueur1 = 0
        st.session_state.score_joueur2 = 0
        st.session_state.gagnant = False
        st.success("Le jeu a été réinitialisé.")
       

# Appeler la fonction pour démarrer la partie
saisir_bilan()





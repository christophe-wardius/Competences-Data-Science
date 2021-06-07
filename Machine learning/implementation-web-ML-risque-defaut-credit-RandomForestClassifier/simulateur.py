%%writefile simulateur.py
 
import pickle
import streamlit as st
 
# chargement du modèle entraîné via pickle
pickle_in = open('classifier-pickle.pkl', 'rb') 
classifier-pickle = pickle.load(pickle_in)
 
@st.cache()
  
# Fonction qui réalisera la prédiction en utilisant les données entrées par l'utilisateur
def prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History):   
 
    # Pre-processing des entrées de l'utilisateur    
    if Gender == "Masculin":
        Gender = 0
    else:
        Gender = 1
 
    if Married == "Non marié":
        Married = 0
    else:
        Married = 1
 
    if Credit_History == "Non, pas d'autre crédit en cours":
        Credit_History = 0
    else:
        Credit_History = 1  
 
    LoanAmount = LoanAmount / 1000
 
    # Réalisation de la prediction personnalisée 
    prediction = classifier-pickle.predict( 
        [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
     
    if prediction == 0:
        pred = 'rejeté'
    else:
        pred = 'approuvé'
    return pred
      

#Fonction de création de la page web Streamlit
def main():       
    # Elements front end 
    html_temp = """ 
    <div style="background-color:#76D7C4; padding:13px"> 
    <h1 style="color:black; text-align:center">Simulateur de crédit via une prédiction de Machine Learning</h1>
    <p>Afin de voir le résultat en bas de page, choisissez vos caractéristiques&#160;:</p>
    </div> 
    """
      
    # Afficher le front end
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # Champs personnalisés par l'utilisateur. Ils sont obligatoires pour faire une prédiction
    Gender = st.selectbox('Genre&#160;:',("Masculin","Féminin"))
    Married = st.selectbox('Statut marital&#160;:',("Non marié","Marié")) 
    ApplicantIncome = st.number_input("Revenu mensuel du demandeur&#160;:") 
    LoanAmount = st.number_input("Montant total du prêt demandé&#160;:")
    Credit_History = st.selectbox('Avez-vous un crédit actuellement en cours&#160;?',("Oui, autre crédit en cours","Non, pas d'autre crédit en cours"))
    result =""
      
    # Quand le bouton 'Prédire' est cliqué, réaliser la prédiction et afficher le résultat 
    if st.button("Prédire"): 
        result = prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History) 
        st.success('Votre crédit est {}'.format(result))
        print(LoanAmount)
     
if __name__=='__main__': 
    main()
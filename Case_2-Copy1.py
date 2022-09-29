#!/usr/bin/env python
# coding: utf-8

# PACKAGES.

# In[1]:


#Streamlit & dash installeren. 
#pip install streamlit


# In[2]:


#importeren van packages.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px 
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st


# DATA.

# In[3]:


#Dataset inlezen. 
student = pd.read_csv("student_data.csv")


# In[4]:


#Dataframe aanmaken. 
students = pd.DataFrame(student)
students2 = pd.DataFrame(student)
#print(students2)


# In[5]:


#Aanmaken van het students.describe met gelijknamige variabel om weer te geven op het dashboard. 
students_describe = students.describe()


# In[6]:


#Variabele passmark aanmaken die de cijfers van de studenten indeelt op Onvoldoende en Voldoende. 
passmark = 10
students2['Eindcijfer'] = np.where(students['G3']< passmark, 'Onvoldoende', 'Voldoende')
students2.Eindcijfer.value_counts()


# In[7]:


students3 = pd.DataFrame(student)
cgem = (students3.G1 + students3.G2 + students3.G3) / 3
students3['Cijfer Gem'] = cgem
#print(students3)
#students3.head(4)


# TITEL/OPMAAK APP.

# In[8]:


st.set_page_config(page_title="Dashboard Groep 22", page_icon="👩‍🎓", layout = "wide", initial_sidebar_state="expanded")


# In[9]:


#Title voor de app, weergegeven boven elke pagina.  
st.title('Data Explorer Student Performance')


# In[10]:


#Opmaak van sidebar in de app. 
st.sidebar.title('Navigatie')


# PLOTS.

# In[11]:


#Histogram die het aantal vrouwelijke/mannelijke leerlingen per school weergeeft. 

#Custom legend name voor het aanpassen van 'F' naar 'Vrouw' in de legenda.  
def custom_legend_name(new_names):
    for i, new_name in enumerate(new_names):
     fig1.data[i].name = new_name
        
fig1 = go.Figure(px.histogram(students, x='school' ,color='sex', title='Studenten per School', barmode='group', text_auto=True, width = 800,
                   labels = {'school': 'School', 'count': 'Aantal Studenten', 'sex': 'Geslacht', 'GP': 'Gabriel Pereira', 'MS': 'Mousinho da Silveira'}))
fig1.update_layout(yaxis_title="Aantal")
custom_legend_name(['Vrouw','Man'])
#fig1.show()
#st.plotly_chart(fig1, use_container_width=True)


# In[12]:


#Histogram die het aantal vrouwelijke/mannelijke leerlingen en de leeftijden weergeeft. 

#Custom legend name voor het aanpassen van 'F' naar 'Vrouw' in de legenda.  
def custom_legend_name(new_names):
    for i, new_name in enumerate(new_names):
     fig2.data[i].name = new_name
    
fig2 = go.Figure(px.histogram(students, x='age', color='sex', title='Leeftijd Studenten', barmode='group', text_auto=True, 
                              width = 800,
                   labels = {'age': 'Leeftijd', 'sex': 'Geslacht'}))
fig2.update_layout(yaxis_title="Aantal")
custom_legend_name(['Vrouw','Man'])
#fig2.show()
#st.plotly_chart(fig2, use_container_width=True)


# In[13]:


#histogram die voldoendes/onvoldoendes per geslacht laat zien. 

#Custom legend name voor het aanpassen van 'F' naar 'Vrouw' in de legenda.  
def custom_legend_name(new_names):
    for i, new_name in enumerate(new_names):
     fig7.data[i].name = new_name
    
fig7 = go.Figure(px.histogram(students2, x='Eindcijfer', color='sex', title='Voldoende of Onvoldoende Eindcijfer (G3)', barmode='group', text_auto=True, 
                              width = 800,
                   labels = {'age': 'Leeftijd', 'sex': 'Geslacht'}))
fig7.update_layout(yaxis_title="Aantal")
custom_legend_name(['Vrouw','Man'])
#fig7.show()


# In[14]:


#Histogram die het gemiddelde eindcijfer per geslacht laat zien.

#Custom legend name voor het aanpassen van 'F' naar 'Vrouw' in de legenda.  
def custom_legend_name(new_names):
    for i, new_name in enumerate(new_names):
     fig3.data[i].name = new_name
    
colors = 'blue'
fig3 = go.Figure(px.histogram(students3, x='sex', y='Cijfer Gem', title= 'Gemiddeld Eindcijfer per Geslacht',
                            barmode='group', text_auto=True, histfunc='avg', color = 'sex', width = 800,
                             labels = {'sex': 'Geslacht', 'F': 'Vrouw', 'M': 'Man'}))
fig3.update_layout(yaxis_title="Gemiddeld Eindcijfer")
custom_legend_name(['Vrouw','Man'])
#fig3.show()


# In[15]:


#Histogram met dropdown menu waar gekozen kan worden tussen G1/G2/G3. 
dropdown_buttons = [{'label':'G1, G2, G3', 'method': 'update', 
                     'args':[{'visible': [True, True, True]},
                            {'title': 'G1, G2, G3'}]},
                    {'label':'G1', 'method': 'update', 
                     'args':[{'visible': [True, False, False]},
                            {'title': 'G1'}]},
                   {'label':'G2', 'method': 'update', 
                     'args':[{'visible': [False, True, False]},
                            {'title': 'G2'}]},
                   {'label':'G3', 'method': 'update', 
                     'args':[{'visible': [False, False, True]},
                            {'title': 'G3'}]},
                   ]

fig4 = px.histogram(students, x=['G1', 'G2', 'G3'], barmode='group', nbins=40, width = 800,  
                   )
fig4.update_layout({'updatemenus':[{'type': "dropdown",
                                  'x': 1.3,
                                  'y': 0.5,
                                  'showactive': True,
                                  'active': 0,
                                  'buttons': dropdown_buttons}]})

fig4.update_layout(
    title_text = 'Cijfers per periode',
    xaxis_title_text = 'Behaalde cijfers',
    yaxis_title_text = 'Aantal',
    legend_title_text = 'Periodes',
    bargap=0.2,
    bargroupgap=0.1)

#fig4.show()


# In[16]:


#Cijfers per periode Vrouwen.
dropdown_buttons = [{'label':'G1, G2, G3', 'method': 'update', 
                     'args':[{'visible': [True, True, True]},
                            {'title': 'G1, G2, G3'}]},
                    {'label':'G1', 'method': 'update', 
                     'args':[{'visible': [True, False, False]},
                            {'title': 'G1'}]},
                   {'label':'G2', 'method': 'update', 
                     'args':[{'visible': [False, True, False]},
                            {'title': 'G2'}]},
                   {'label':'G3', 'method': 'update', 
                     'args':[{'visible': [False, False, True]},
                            {'title': 'G3'}]},
                   ]
students_vrouw = students[students['sex'] == 'F']


fig5 = px.histogram(students_vrouw, x=['G1', 'G2', 'G3'], barmode='group', nbins=30, width = 800,
                   )
fig5.update_layout({'updatemenus':[{'type': "dropdown",
                                  'x': 1.3,
                                  'y': 0.5,
                                  'showactive': True,
                                  'active': 0,
                                  'buttons': dropdown_buttons}]})

fig5.update_layout(
    title_text = 'Cijfers per periode van de vrouwen',
    xaxis_title_text = 'Behaalde cijfers',
    yaxis_title_text = 'Aantal',
    legend_title_text = 'Periodes',
    bargap=0.2,
    bargroupgap=0.1)

#fig5.show()


# In[17]:


#Cijfers per periode Mannen.

dropdown_buttons = [{'label':'G1, G2, G3', 'method': 'update', 
                     'args':[{'visible': [True, True, True]},
                            {'title': 'G1, G2, G3'}]},
                    {'label':'G1', 'method': 'update', 
                     'args':[{'visible': [True, False, False]},
                            {'title': 'G1'}]},
                   {'label':'G2', 'method': 'update', 
                     'args':[{'visible': [False, True, False]},
                            {'title': 'G2'}]},
                   {'label':'G3', 'method': 'update', 
                     'args':[{'visible': [False, False, True]},
                            {'title': 'G3'}]},
                   ]
students_man = students[students['sex'] == 'M']


fig6 = px.histogram(students_man, x=['G1', 'G2', 'G3'], barmode='group', nbins=40, width = 800,
                   )
fig6.update_layout({'updatemenus':[{'type': "dropdown",
                                  'x': 1.3,
                                  'y': 0.5,
                                  'showactive': True,
                                  'active': 0,
                                  'buttons': dropdown_buttons}]})

fig6.update_layout(
    title_text = 'Cijfers per periode van de mannen',
    xaxis_title_text = 'Behaalde cijfers',
    yaxis_title_text = 'Aantal',
    legend_title_text = 'Periodes',
    bargap=0.2,
    bargroupgap=0.1)

#fig6.show()


# In[18]:


#Boxplot die het behaalde eindcijfer (G3) laat zien tegenover het opleidingsniveau van de Moeder. 

def custom_legend_name(new_names):
    for i, new_name in enumerate(new_names):
     fig8.data[i].name = new_name

fig8 = go.Figure(px.box(students, x='Medu', y='G3', color = 'sex', width = 1000,
                        title = 'Eindcijfer (G3) ten opzichte van Opleidingsniveau Moeder',
                       labels = {'age': 'Leeftijd', 'G3': 'Eindcijfer', 'sex': 'Geslacht', 'Medu':'Opleiding Moeder'}))
fig8.add_annotation(text='0: Geen <br>1: Basisonderwijs (4 jaar) <br>2: Basisonderwijs (5-9 jaar) <br>3: Voortgezet Onderwijs <br>4: Hoger Onderwijs', 
                    align='left',
                    showarrow=False,
                    xref='paper',
                    yref='paper',
                    x=1.15,
                    y=0.5,
                    bordercolor='black',
                    borderwidth=1)
custom_legend_name(['Vrouw','Man'])
#fig8.show()


# In[19]:


#Boxplot die het behaalde eindcijfer (G3) laat zien tegenover het opleidingsniveau van de Vader. 

def custom_legend_name(new_names):
    for i, new_name in enumerate(new_names):
     fig14.data[i].name = new_name

fig14 = go.Figure(px.box(students, x='Fedu', y='G3', color = 'sex', width = 1000,
                        title = 'Eindcijfer (G3) ten opzichte van Opleidingsniveau Vader',
                       labels = {'age': 'Leeftijd', 'G3': 'Eindcijfer', 'sex': 'Geslacht', 'Medu':'Opleiding Moeder'}))
fig14.add_annotation(text='0: Geen <br>1: Basisonderwijs (4 jaar) <br>2: Basisonderwijs (5-9 jaar) <br>3: Voortgezet Onderwijs <br>4: Hoger Onderwijs', 
                    align='left',
                    showarrow=False,
                    xref='paper',
                    yref='paper',
                    x=1.15,
                    y=0.5,
                    bordercolor='black',
                    borderwidth=1)
custom_legend_name(['Vrouw','Man'])
#fig14.show()


# In[20]:


#Histogram met studeertijd per geslacht. 

def custom_legend_name(new_names):
    for i, new_name in enumerate(new_names):
     fig9.data[i].name = new_name

fig9 = px.histogram(students, x='studytime', histnorm='percent', color='sex', width = 1000, barmode='group', text_auto=True,
                    title = "Studeertijd per Geslacht",
                    labels = {'studytime': 'Studeertijd', 'sex': 'Geslacht'})
fig9.update_layout(bargap=0.1)
custom_legend_name(['Vrouw','Man'])
fig9.update_layout(yaxis_title="Percentage") 
#fig9.show()


# In[21]:


#Boxplot die het behaalde eindcijfer (G3) laat zien tegenover de studeertijd.  

def custom_legend_name(new_names):
    for i, new_name in enumerate(new_names):
     fig10.data[i].name = new_name

fig10 = go.Figure(px.box(students, x='studytime', y='G3', color='sex', width = 1000,
                        title = 'Eindcijfer (G3) ten opzichte van Studeertijd',
                       labels = {'age': 'Leeftijd', 'G3': 'Eindcijfer', 'sex': 'Geslacht', 'studytime':'Studeertijd'}))
custom_legend_name(['Vrouw','Man']) 
fig10.add_annotation(text='1: < 2 uur/week <br>2: 2-5 uur/week <br>3: 5-10 uur/week <br>4: > 10 uur/week', 
                    align='left',
                    showarrow=False,
                    xref='paper',
                    yref='paper',
                    x=1.12,
                    y=0.5,
                    bordercolor='black',
                    borderwidth=1)
#fig10.show()


# In[22]:


#Eindcijfer (G3) ten opzichte van Studeertijd, met leeftijd als animatie. 

students = students.sort_values('age', ascending=True)

def custom_legend_name(new_names):
    for i, new_name in enumerate(new_names):
     fig11.data[i].name = new_name
    
fig11 = go.Figure(px.box(students, x='studytime', y='G3', color='sex', animation_frame='age', height=600 ,width = 1000,
                        title = 'Eindcijfer (G3) ten opzichte van Studeertijd met Leeftijd als animatie',
                       labels = {'age': 'Leeftijd', 'G3': 'Eindcijfer', 'sex': 'Geslacht', 'studytime':'Studeertijd'}))
custom_legend_name(['Vrouw','Man'])
fig11.add_annotation(text='1: < 2 uur/week <br>2: 2-5 uur/week <br>3: 5-10 uur/week <br>4: > 10 uur/week', 
                    align='left',
                    showarrow=False,
                    xref='paper',
                    yref='paper',
                    x=1.12,
                    y=0.5,
                    bordercolor='black',
                    borderwidth=1)
#fig11.show()


# In[23]:


#Boxplot die het behaalde eindcijfer (G3) laat zien tegenover de absentie.  

def custom_legend_name(new_names):
    for i, new_name in enumerate(new_names):
     fig12.data[i].name = new_name

fig12 = px.histogram(students, x='absences', y='G3', color='sex', barmode='group', histfunc='avg', text_auto=True, nbins=25,
                      title = "Eindcijfer (G3) ten opzichte van Absentie", width = 1000,
                    labels = {'age': 'Leeftijd', 'G3': 'Eindcijfer', 'sex': 'Geslacht', 'studytime':'Studeertijd'})
fig12.update_layout(yaxis_title="Gemiddeld Eindcijfer (G3)", xaxis_title="Absenties")  
custom_legend_name(['Vrouw','Man'])

#fig12.show()


# In[24]:





# In[25]:


#Correlatie tabel maken.

corr = students3.corr()
figc, ax = plt.subplots(figsize=(15,15))
mask = np.triu(np.ones_like(corr, dtype=bool))
np.fill_diagonal(mask, False)
sns.heatmap(students3.corr(), ax=ax, vmin=-1, cmap="plasma_r", mask=mask ,annot=True)


# In[ ]:





# OPMAAK APP.

# In[26]:


#Kolommen verwijderen uit dataframes. 

del students['Eindcijfer']
del students['Cijfer Gem']
del students2['Cijfer Gem']


# In[27]:


#Opmaak Dashboard tussen 'knoppen' bij bijbehorende pagina. 

#Radioknoppen in de sidebar die navigatie over de pagina mogelijk maken. 
pages = st.sidebar.radio('paginas', options=['Home','Dataset', 'Visualisaties', 'Einde'], label_visibility='hidden')

if pages == 'Home':
    st.markdown("Welkom op het dashboard van groep 22. Gebruik de knoppen in de sidebar om tussen de verschillende paginas te navigeren. ")
    st.image("hva.png", width=None ,output_format='auto')
elif pages == 'Dataset':
    st.subheader('Dataset Student Performance')
    st.markdown("Hieronder wordt de door ons gekozen dataset in z'n geheel weergegeven.")
    st.dataframe(data=students, use_container_width=False)
    st.subheader('Beschrijving van de gegevens in het dataframe door middel van de describe functie.')
    st.markdown("Hierin is te zien dat er geen data ontbreekt. De nulwaardes horen in het dataframe.")
    st.dataframe(data=students_describe, use_container_width=False)
    st.subheader('Vergelijking tussen de cijferschalen van Portugal en Nederland.')
    st.image("Cijfers.png", output_format='auto')
    st.subheader('Dataframe na aanpassen voor voldoende en onvoldoende resultaten.')
    st.dataframe(data=students2, use_container_width=False)
    st.subheader("Correlatietabel van de dataset 'Student Performance'.")
    st.markdown("Correlatie geeft de mate van samenhang tussen twee variabelen weer, ofwel in hoeverre twee variabelen elkaar beïnvloeden. De correlatie wordt uitgedrukt in de correlatiecoëfficiënt. De waarde van de correlatiecoëfficiënt ligt tussen -1 en +1. Een positieve correlatiecoëfficiënt geeft aan dat dat de variabelen beiden in dezelfde richting veranderen. Een negatieve correlatiecoëfficiënt geeft aan dat de variabelen precies het tegenovergestelde van elkaar doen. Een correlatiecoëfficiënt van 0 geeft aan dat er geen verband is tussen de variabelen.")
    st.write(figc)
    st.markdown("P. Cortez and A. Silva. Using Data Mining to Predict Secondary School Student Performance. In A. Brito and J. Teixeira Eds., Proceedings of 5th FUture BUsiness TEChnology Conference (FUBUTEC 2008) pp. 5-12, Porto, Portugal, April, 2008, EUROSIS, ISBN 978-9077381-39-7.")
    st.markdown("Bron Dataset: https://www.kaggle.com/datasets/devansodariya/student-performance-data")
elif pages == 'Visualisaties':
    st.subheader("Hier worden de visualisaties weergegeven die wij hebben opgesteld."), st.markdown("De verdeling van de studenten in de Dataset. GP staat voor Gabriel Pereira en MS voor Mousinho da Silveira, dit zijn de schoolnamen. "), st.plotly_chart(fig1), st.markdown("In de onderstaande grafiek is de verdeling van de leeftijden op de scholen weergegeven."), st.plotly_chart(fig2), st.markdown("In de onderstaande grafiek is te zien dat de vrouwelijke studenten meer voldoendes hebben gehaald, echter zijn er wel meer vrouwelijke studenten in de dataset opgenomen."), st.plotly_chart(fig7), st.markdown("In de onderstaande grafiek is te zien dat het gemiddelde eindcijfer bij de mannelijke studenten hoger is."), st.plotly_chart(fig3), st.markdown("In de onderstaande grafiek zijn de behaalde cijfers per periode te zien. De twee grafieken hierna laten hetzelfde zien, maar dan per geslacht."), st.plotly_chart(fig4), st.plotly_chart(fig5), st.plotly_chart(fig6), st.markdown("De volgende twee grafieken geven aan dat het opleidingsniveau van de ouder wel degelijk invloed heeft op het behaalde resultaat van het kind."), st.plotly_chart(fig8), st.plotly_chart(fig14), st.markdown("De Onderstaande grafiek laat zien dat vrouwelijke leerlingen meer tijd besteden aan het studeren."),st.plotly_chart(fig9), st.markdown("In de onderstaande grafiek is het verschil tussen de behaalde resultaten te zien. De mannelijke studenten scoren beter bij het zelfde aantal studieuren."), st.plotly_chart(fig10), st.plotly_chart(fig11), st.markdown("De onderstaande grafiek toont aan dat absentie invloedt heeft op het behaalde cijfer, vooral voor mannen. De vrouwelijke studenten presenteren beter als ze een aantal keer absent zijn geweest dan mannen die lessen gemist hebben."), st.plotly_chart(fig12), st.plotly_chart(fig13)
elif pages == 'Einde':
    st.markdown('Bedankt voor het bezoeken.')
    st.markdown('Groep 22: Bente van Hameren, Lukas Čović, Noah Wijnheimer, Ayat Bagdady.')


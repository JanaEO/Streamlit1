import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Netflix Subscription Fees Across Different Countries")
data=pd.read_csv('/Users/janaaloud/Desktop/Netflix subscription fee Dec-2021.csv')
data.head()

st.image('https://logowik.com/content/uploads/images/750_netflix.jpg')


#Netflix Dataset
st.subheader('Raw data')
if st.checkbox("Show Raw Data"):
    st.subheader('Netfix Subscription Fees for December 2021')
    st.write(data)

#Sidebar
st.write("Please refer to the sidebar for a small quiz!")
st.sidebar.subheader("Welcome!")
add_selectbox=st.sidebar.selectbox("Which Country do you think has the highest basic Netflix Subscription Fees? ",("United Kingdom","Switzerland","Mexico"))
st.sidebar.write('You selected:',add_selectbox )

#Fluctuation of Total Library Size in Different Countries histogram
st.subheader('Fluctuation of Total Library Size in Different Countries ')
st.set_option('deprecation.showPyplotGlobalUse', False)
dataframe=pd.DataFrame(data[:64],columns=["TotalLibrarySize"])
dataframe.hist()
st.pyplot()

bar_chart=px.bar(data,x='Country',y='TotalLibrarySize',template='plotly_white')
st.plotly_chart(bar_chart)

st.write("These barcharts show how different countries have different library sizes with the lowest library size  having less than 2000 and the highest having more than 7000 tv shows and movies.")

#Fluctuation of Different Subscription Fees in Different Countries
st.subheader('Fluctuation of Different Subscription Fees in Different Countries ')
st.text("There are three different subscription options to choose from in each country.")
st.text("The charts below visualize how these fees flucuate based on location.")
st.set_option('deprecation.showPyplotGlobalUse', False)
#Histograms
dataframe1=pd.DataFrame(data[:64],columns=["CostPerMonth-Basic($)","CostPerMonth-Standard($)","CostPerMonth-Premium($)"])
dataframe1.hist()
st.pyplot()
st.write("It is evident that the basic suscription fees in some countries are equal to the premium in others!")

#line chart
st.line_chart(dataframe1)

#Scatterplot
st.subheader('Scatterplot analysis')

selected_x_var = st.selectbox('What do you want the x variable to be?', data.columns)
selected_y_var = st.selectbox('What about the y?', data.columns)
fig = px.scatter(data, x = data[selected_x_var], y = data[selected_y_var], color="Country")
st.plotly_chart(fig)
st.write("Refer to the above scatter plot for different visualizations of the fees and library size!")



if(st.button("Click me for sidebar solution!")):
    st.text("The correct answer is Switzerland!")
    st.text(" Basic subscription is $12.88!")
    st.text(" This is almost the premium subscription in other countries such as Thailand ($12.52)!")
    st.balloons()

#importing libraries
import pickle
import pandas as pd
import streamlit as st
import numpy as np

model = pickle.load(open('rf.pkl','rb'))



st.title('SELLING CAR PRICE PREDICTION')
n=np.zeros([1,34],dtype=int)


#taking input and storing data

year = st.slider("Select Year",1992,2022)
n[0,0]=year

km = st.slider("Select total kilometer driven",0,1000000,)
n[0,1]=km



#for fuel
fuel = st.selectbox("Fuel type: ",
                     ['Petrol','Diesel','CNG','LPG','Electric'])

if fuel=='CNG':
  n[0,2]=1
elif fuel=='Diesel':
  n[0,3]=1
elif fuel=='Electric':
  n[0,4]=1
elif fuel=='LPG':
  n[0,5]=1
else:
  n[0,6]=1
  
  
#for seller type
s_t = st.radio("Select Seller Type: ",
                     ('Individual','Dealer','Trustmark Dealer'))
if s_t=='Dealer':
  n[0,7]=1
elif s_t=='Individual':
  n[0,8]=1
else:
  n[0,9]=1
  

#for owner
owner = st.selectbox("Owner: ",
                     ['First Owner','Second Owner','Third Owner','Fourth & Above Owner','Test Drive Car'])

if owner=='First Owner':
  n[0,10]=1
elif owner=='Fourth & Above Owner':
  n[0,11]=1
elif owner=='Second Owner':
  n[0,12]=1
elif owner=='Test Drive Car':
  n[0,13]=1
else:
  n[0,14]=1
  
  
# for transmission
tran = st.radio("Select Transmission: ", ('Manual','Automatic'))


if tran=='Automatic':
  n[0,15]=1
else:
  n[0,16]=1
  
  
#for manufacturer
man = st.selectbox("Select car Manufacturer: ",['Maruti','Hyundai','Mahindra','Tata','Ford','Honda','Toyota','Chevrolet','Renault',
                      'Volkswagen','Nissan','Skoda','Fiat','Audi','Datsun','BMW','Mercedes-Benz'])

if man=='Audi':
  n[0,17]=1
elif man=='BMW':
  n[0,18]=1
elif man=='Chevrolet':
  n[0,19]=1
elif man=='Datsun':
  n[0,20]=1
elif man=='Fiat':
  n[0,21]=1
elif man=='Ford':
  n[0,22]=1
elif man=='Honda':
  n[0,23]=1
elif man=='Hyundai':
  n[0,24]=1
elif man=='Mahindra':
  n[0,25]=1
elif man=='Maruti':
  n[0,26]=1
elif man=='Mercedes-Benz':
  n[0,27]=1
elif man=='Nissan':
  n[0,28]=1
elif man=='Renault':
  n[0,29]=1
elif man=='Skoda':
  n[0,30]=1
elif man=='Tata':
  n[0,31]=1
elif man=='Toyota':
  n[0,32]=1
else:
  n[0,33]=1

#making a Dataframe using array n
data=pd.DataFrame(n)
  
  

if(st.button('Submit')):
  result = model.predict(data)
  st.text("estimate selling price is :")
  st.success(np.round(result[0]))

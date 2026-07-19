import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

movie={"avengers":{"price":200,"genre":"action","Day":"friday"},
       "spiderman":{"price":150,"genre":"action","Day":"saturday"},
       "titanic":{"price":100,"genre":"romance","Day":"sunday"},
        "inception":{"price":250,"genre":"action","Day":"monday"},
        "the notebook":{"price":120,"genre":"romance","Day":"tuesday"},
        "the godfather":{"price":300,"genre":"drama","Day":"wednesday"},
        "the dark knight":{"price":220,"genre":"action","Day":"thursday"},
        "forrest gump":{"price":180,"genre":"drama","Day":"friday"},
        "the shawshank redemption":{"price":280,"genre":"drama","Day":"saturday"},
        "the lion king":{"price":160,"genre":"animation","Day":"sunday"},
        "frozen":{"price":140,"genre":"animation","Day":"monday"},
        "toy story":{"price":130,"genre":"animation","Day":"tuesday"},
        "the matrix":{"price":240,"genre":"action","Day":"thursday"},
}
df=pd.DataFrame(movie).T
le=LabelEncoder()
l1=LabelEncoder()
df["genre"]=le.fit_transform(df["genre"])
df["Day"]=l1.fit_transform(df['Day'])
x=df[["genre","Day"]]
y=df["price"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)

import streamlit as st
choice=st.text_input("Enter your choice of movie: ").lower().strip()
if choice in movie:
    st.write("you have selected",choice)
    st.success(f"price is {movie[choice]['price']}")
    st.write("genre is",movie[choice]["genre"])
    st.write("day is",movie[choice]["Day"])  
else:
    ques=st.text_input("Enter the genre: ").lower().strip()
    ques1=st.selectbox(" select day: ", [ "monday", "tuesday", "wednesday", "thursday","friday", "saturday", "sunday",])

    if st.button("predict price"):
        genre=le.transform([ques])[0]
        Day =l1.transform([ques1])[0]
        new_data =pd.DataFrame({"genre":[genre],"Day":[Day]})
        prediction=model.predict(new_data)
        st.success(f"price is {round(prediction[0])}")
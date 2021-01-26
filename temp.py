import pickle
import streamlit as st
import streamlit.components.v1 as components
pickle_in=open('deploy1.pkl', 'rb')
model = pickle.load(pickle_in)

def predict_popu(acousticness,danceability,energy,loudness,tempo,instrumentalness):
    
    prediction = model.predict([[acousticness,danceability,energy,loudness,tempo,instrumentalness]])
    print(prediction)
    return prediction

def main():
    st.title("Spotify songs")
    html_temp2 = """
                 <div style='background-color:royalblue;padding:10px;border-radius:10px'>
                 <h2 style='color:white;text-align:center;'>Spotify songsr</h2>
                 <h1 style='color:white;text-align:center;'>Popularity prediction</h1>
                 </div>
    """
    components.html(html_temp2)
    acousticness = st.text_input("acousticness","Type Here")
    danceability = st.text_input("danceability","Type Here")
    energy = st.text_input("energy","Type Here")
    loudness = st.text_input("loudness","Type Here")
    tempo = st.text_input("tempo","Type Here")
    instrumentalness = st.text_input("instrumentalness","Type Here")
    result =''
    
    if st.button('Predict'):
        result = predict_popu(acousticness,danceability,energy,loudness,tempo,instrumentalness)
    st.success("Popularity of the song is {}".format(result))
    if st.button('About'):
        st.text("Lets learn")
        st.text("Built with streamlit")
        
if __name__=='__main__':
    main()











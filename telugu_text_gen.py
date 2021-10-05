from googletrans import Translator
from PIL import Image
import streamlit as st
import requests

st.set_option('deprecation.showfileUploaderEncoding', False)

img = Image.open("telugu-talli.png")
st.sidebar.image(img)
st.sidebar.subheader("దేశ భాషలందు తెలుగు లెస్స \n పంచదార కన్న \n పనస తొనల కన్న \n కమ్మని తేనె కన్న \n తెలుగు మిన్న\n")

st.sidebar.write("You can find some telugu\ntext here (for custom input):\n https://te.wikipedia.org/wiki/")

st.title("Telugu Language Text Generator")
st.subheader("This is a simple AI text generator. It takes a seed text as input and generates telugu text based on seed/prompt as output.")

option = st.selectbox('Input custom prompt or use one of our examples:',('Custom Prompt', 'ప్రపంచంలో ఒకప్పుడు', 'ఆరోగ్యంగా ఉండటానికి', 'ప్రపంచంలోని ఉత్తమ సంగీత స్వరకర్త', 'పర్యావరణ కాలుష్యం', 'నా పేరు'))

if option=="Custom Prompt":
	telugu_query = st.text_input(label="Enter seed(prompt) text in telugu")
else:
	telugu_query = option

with st.form(key='my_form'):

	amount_of_text = st.slider(label="Selcect the amount of text to generate", min_value = 1, max_value=10, step = 1)
	submit_button = st.form_submit_button(label='Submit')

if submit_button:
	if not telugu_query:
		st.info("You haven't given any seed text in telugu (తెలుగు) language")
	else:
		translator = Translator()
		try:
		    temp1 = translator.translate(telugu_query, src='te', dest='en')
		    english_query = temp1.text
		    english_text = ''
		    for i in range(amount_of_text):
		        r = requests.post('https://api.deepai.org/api/text-generator',
		                          data={'text': english_query},
		                          headers={'api-key': '15a3b63b-c64b-413a-b313-f36a383f3fe1'
		                          })
		        english_text += r.json()['output']
		
		    temp2 = translator.translate(english_text, src='en', dest='te')
		    telugu_text = temp2.text
		    st.write(telugu_text)
		    st.info("Successfully generated telugu text")
		    # st.balloons()
		except:
		    pass

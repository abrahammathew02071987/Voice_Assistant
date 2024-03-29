import streamlit as st
import youtube_dl
import requests
import pprint
from configure import auth_key
from time import sleep

st.title("""
VOICE ASSISTANT - JARVIS

""")
st.markdown("""**Artificial Intelligence when used with machines, it shows us the capability of
thinking like humans. In this, a computer system is designed in such a way that typically
requires interaction from human. As we know Python is an emerging language so it
becomes easy to write a script for Voice Assistant in Python. The instructions for the
assistant can be handled as per the requirement of user. Speech recognition is the Alexa,
Siri, etc. In Python there is an API called Speech Recognition which allows us to
convert speech into text. It was an interesting task to make my own assistant. It became
easier to send emails without typing any word, Searching on Google without opening
the browser, and performing many other daily tasks like playing music, opening your
favorite IDE with the help of a single voice command. In the current scenario,
advancement in technologies are such that they can perform any task with same
effectiveness or can say more effectively than us. By making this project, I realized that
the concept of AI in every field is decreasing human effort and saving time. Inspired by Marvel's Iron Man**.""")
st.markdown("**Functionalities of this project include:**")
st.markdown("""

1. **It can have some basic conversation.**
2. **It can give weather forecast.**
3. **It can tell you latest news updates.**
4. **It can open websites like Google, YouTube, etc., in a web browser.**
5. **It can read PDF.**
6. **It can send text on WhatsApp.**
7. **It can set up reminder, alarm **
8. **It can play music.**
9. **It can do Wikipedia searches for you.**
10. **It can provide movie review, recommendation based on rating.**
8. **It can authenticate user**
9. **It can download from GITHUB repository**
10. **It can create, stop and delete Azure VM machine **
11. **It can perform Windows operations**
                                                        **and many more….**
                                                        
                                                        """)
#video = open("https://drive.google.com/file/d/1j0EGiJFIfh_fKP3L7jBJ4DXMHPJM6J0t/view?usp=sharing" )
#video_bytes = video.read()
st.video('https://youtu.be/gzKQfyzTC_w')

st.markdown("**LIMITATIONS**")
st.markdown("""

1. **Security is somewhere an issue, there is no voice command encryption in this
project.**
2. **Background voice can interfere.**
3. **Misinterpretation because of accents and may cause inaccurate results.**
""")

st.markdown("**LIMITATIONS**")
st.markdown("""

1. **Make JARVIS to learn more on its own and develop a new skill in it.**
2. **JARVIS android app can also be developed.**
3. **Voice commands can be encrypted to maintain security.**
""")

#---------------------------------------------------YT Transcribe-----------------------------------------
if 'status' not in st.session_state:
    st.session_state['status'] = 'submitted'

ydl_opts = {
   'format': 'bestaudio/best',
   'postprocessors': [{
       'key': 'FFmpegExtractAudio',
       'preferredcodec': 'mp3',
       'preferredquality': '192',
   }],
   'ffmpeg-location': './',
   'outtmpl': "./%(id)s.%(ext)s",
}

transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
upload_endpoint = 'https://api.assemblyai.com/v2/upload'

headers_auth_only = {'authorization': auth_key}
headers = {
   "authorization": auth_key,
   "content-type": "application/json"
}
CHUNK_SIZE = 5242880
 
@st.cache
def transcribe_from_link(link, categories: bool):
	_id = link.strip()

	def get_vid(_id):
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			return ydl.extract_info(_id)

	# download the audio of the YouTube video locally
	meta = get_vid(_id)
	save_location = meta['id'] + ".mp3"

	print('Saved mp3 to', save_location)


	def read_file(filename):
		with open(filename, 'rb') as _file:
			while True:
				data = _file.read(CHUNK_SIZE)
				if not data:
					break
				yield data


	# upload audio file to AssemblyAI
	upload_response = requests.post(
		upload_endpoint,
		headers=headers_auth_only, data=read_file(save_location)
	)

	audio_url = upload_response.json()['upload_url']
	print('Uploaded to', audio_url)

	# start the transcription of the audio file
	transcript_request = {
		'audio_url': audio_url,
		'iab_categories': 'True' if categories else 'False',
	}

	transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)

	# this is the id of the file that is being transcribed in the AssemblyAI servers
	# we will use this id to access the completed transcription
	transcript_id = transcript_response.json()['id']
	polling_endpoint = transcript_endpoint + "/" + transcript_id

	print("Transcribing at", polling_endpoint)

	return polling_endpoint


def get_status(polling_endpoint):
	polling_response = requests.get(polling_endpoint, headers=headers)
	st.session_state['status'] = polling_response.json()['status']

def refresh_state():
	st.session_state['status'] = 'submitted'


st.title('Easily transcribe YouTube videos')

link = st.text_input('Enter your YouTube video link', 'https://www.youtube.com/watch?v=ASbgIVNuAV0', on_change=refresh_state)
st.video(link)

st.text("The transcription is " + st.session_state['status'])

polling_endpoint = transcribe_from_link(link, False)

st.button('check_status', on_click=get_status, args=(polling_endpoint,))

transcript=''
if st.session_state['status']=='completed':
	polling_response = requests.get(polling_endpoint, headers=headers)
	transcript = polling_response.json()['text']

st.markdown(transcript)

#------------------------------------------------------------Covid tracker --------------------------------------------------


import streamlit as st
st.title("""
# VOICE ASSISTANT - JARVIS

""")
st.write("""
As we know Python is an emerging language so it becomes easy to write a script for Voice
Assistant in Python. The instructions for the assistant can be handled as per the requirement
of user. Speech recognition is the process of converting speech into text. This is commonly
used in voice assistants like Alexa, Siri, etc. In Python there is an API called
SpeechRecognition which allows us to convert speech into text. It was an interesting task
to make my own assistant. It became easier to send emails without typing any word,
Searching on Google without opening the browser, and performing many other daily tasks
like playing music, opening your favorite IDE with the help of a single voice command. In
the current scenario, advancement in technologies are such that they can perform any task
with same effectiveness or can say more effectively than us. By making this project, I
realized that the concept of AI in every field is decreasing human effort and saving time. Inspired by Marvel's Iron Man.

Functionalities of this project include:
1. It can have some basic conversation.
2. It can give weather forecast.
3. It can tell you latest news updates.
4. It can open websites like Google, YouTube, etc., in a web browser.
5. It can read PDF.
6. It can send text on WhatsApp.
7. It can set up reminder, alarm 
8. It can play music.
9. It can do Wikipedia searches for you.
10. It can provide movie review, recommendation based on rating.
8. It can authenticate user
9. It can download from GITHUB repository
10. It can create, stop and delete Azure VM machine 
11. It can perform Windows operations
                                                        and many more….

""")
video = open("AI_Assistant.mp4","rb")
st.video(video)
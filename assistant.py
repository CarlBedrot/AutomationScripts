import speech_recognition as sr
import os
import datetime
import sys
import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Define mood-based playlists with Spotify URIs
mood_playlists = {
    "happy": "spotify:playlist:1XjEAOoLkFfZdj9Myam77q",
    "calm": "spotify:playlist:3zN1aaValMUW7dZgDCDnjl",
    "electronic": "spotify:playlist:610mGeRdifW4ZikhHJkgGm",
    "spanish": "spotify:playlist:33PAsTMFHNyC0NJgMt7Swc",  # Corrected here
}

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="6cf2114f2edb4694b434f6d0794b34be",
                                               client_secret="e13978f8cd494cbfb09a6abe38e48434",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope="user-read-playback-state,user-modify-playback-state,playlist-read-private"))

# Initialize the speech recognizer
listener = sr.Recognizer()

# Function to use macOS's built-in text-to-speech
def speak(text):
    os.system(f'say -v Karen "{text}"')

# Greeting from the assistant
def greet():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        speak("Good morning Carl, how can I assist you today?")
    elif 12 <= current_hour < 18:
        speak("Good afternoon Carl, how can I assist you today?")
    else:
        speak("Good evening Carl, how can I assist you today?")

# Function to ask if the user has more commands
def ask_for_more():
    speak("Is there anything else I can help with?")
    return listen_command()

# Function to listen for voice commands
def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        command = ""
        try:
            command = listener.recognize_google(voice)
            print(f"You said: {command}")
        except Exception as e:
            print(f"Error: {e}")
        return command.lower()

# Function to perform actions based on the command
def perform_action(command):
    if 'play' in command and 'music' in command:
        mood = command.replace('play', '').replace('music', '').strip()
        play_mood_music(mood)
    elif 'quit music' in command:
        sp.pause_playback()
       
    elif 'open' in command:
        if 'vs code' in command:
            os.system('open -a "Visual Studio Code"')
        elif 'chrome' in command:
            os.system('open -a "Google Chrome"')
        elif 'youtube' in command:
            # open the web browser to the YouTube homepage
            webbrowser.get('chrome').open('https://www.youtube.com') 
        elif 'the office' in command:
            webbrowser.get('chrome').open('https://www.netflix.com/watch/70108695?trackId=14170286')
        elif 'open spotify' in command:
            webbrowser.get('chrome').open('https://open.spotify.com/browse/featured')    
        # Add more 'open' commands as needed
        elif 'open swedish television' in command: 
            webbrowser.get('chrome').open('https://www.svtplay.se/')
        elif 'open god' in command:
            webbrowser.get('chrome').open('https://chat.openai.com/')
    elif 'what time is it' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        speak(f"Current time is {time}")
    elif 'search for' in command:
        search_query = command.replace('search for', '').strip()
        url = f"https://www.google.com/search?q={search_query}"
        webbrowser.get('chrome').open(url)
        speak(f"Here are the results for {search_query}")
    elif 'close chrome' in command:
        os.system("osascript -e 'quit app \"Google Chrome\"'")
        speak("Chrome closed.")
    elif 'lower the volume' in command:
        lower_volume()
    elif 'raise the volume' in command:
        raise_volume()
    elif 'quit script' in command:
        print("Terminating the script...")
        speak("Okay, that's all for now! Goodbye!")
        sys.exit(0)

# Function to lower the system volume slightly
def lower_volume():
    os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) - 20)'")
    speak("Volume lowered.")

# Function to raise the system volume slightly
def raise_volume():
    os.system("osascript -e 'set volume output volume ((output volume of (get volume settings)) + 10)'")
    speak("Volume raised.")

# Function to play mood-based music on Spotify
def play_mood_music(mood):
    if mood in mood_playlists:
        playlist_uri = mood_playlists[mood]
        sp.start_playback(context_uri=playlist_uri)
    else:
        speak("I'm not sure what music to play for that mood.")

# Main loop to continuously listen for commands
if __name__ == "__main__":
    greet()
    while True:
        try:
            command = listen_command()
            perform_action(command)
        except Exception as e:
            print("An error occurred: ", e)
            break

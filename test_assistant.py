import unittest
from unittest.mock import patch
import assistant

class TestAssistant(unittest.TestCase):

    def test_greet(self):
        with patch('assistant.speak') as mock_speak:
            assistant.greet()
            mock_speak.assert_called_with("Good morning Carl, how can I assist you today?")

    def test_lower_volume(self):
        with patch('os.system') as mock_os_system:
            assistant.lower_volume()
            mock_os_system.assert_called_with("osascript -e 'set volume output volume ((output volume of (get volume settings)) - 20)'")

    def test_raise_volume(self):
        with patch('os.system') as mock_os_system:
            assistant.raise_volume()
            mock_os_system.assert_called_with("osascript -e 'set volume output volume ((output volume of (get volume settings)) + 10)'")

    def test_play_mood_music(self):
        mood = "happy"
        playlist_uri = assistant.mood_playlists[mood]
        with patch('assistant.sp.start_playback') as mock_start_playback, \
             patch('assistant.speak') as mock_speak:
            assistant.play_mood_music(mood)
            mock_start_playback.assert_called_with(context_uri=playlist_uri)
            mock_speak.assert_called_with(f"Playing {mood} music on Spotify.")

    # Add more test cases as needed

if __name__ == "__main__":
    unittest.main()
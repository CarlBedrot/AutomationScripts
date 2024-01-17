import tkinter as tk
from tkinter import font as tkFont
from random import choice

# Vocabulary: Italian words with Swedish definitions
vocabulary = {
    'ciao': 'hej (används både för att säga hej och hejdå)',
    'libro': 'bok',
    'mela': 'äpple',
    'gatto': 'katt',
    'cane': 'hund',
    'grazie': 'tack',
    'per favore': 'snälla',
    'scusa': 'ursäkta',
    'si': 'ja',
    'no': 'nej',
    'acqua': 'vatten',
    'amico': 'vän',
    'amore': 'kärlek',
    'auto': 'bil',
    'bambino': 'barn',
    'casa': 'hus',
    'città': 'stad',
    'classe': 'klass',
    'donna': 'kvinna',
    'famiglia': 'familj',
    'fiore': 'blomma',
    'fratello': 'bror',
    'giorno': 'dag',
    'giovane': 'ung',
    'lavoro': 'arbete',
    'libertà': 'frihet',
    'luce': 'ljus',
    'mare': 'hav',
    'mese': 'månad',
    'mondo': 'värld',
    'notte': 'natt',
    'padre': 'far',
    'pane': 'bröd',
    'parola': 'ord',
    'piazza': 'torg',
    'ragazzo': 'pojke',
    'scuola': 'skola',
    'sole': 'sol',
    'strada': 'gata',
    'tempo': 'tid',
    'uomo': 'man',
    'vita': 'liv',
    'voce': 'röst',
    # Continue adding more words and definitions
}


# Styling constants
BG_COLOR = "#ffa500"
WORD_FONT = ("Helvetica", 24, "bold")
DEFINITION_FONT = ("Helvetica", 18)
BUTTON_FONT = ("Helvetica", 14, "bold")
BUTTON_COLOR = "#ff0000"
# make hover color red
HOVER_COLOR = "#ff0000"



# Function to update the popup window with a new random word and its definition
def update_word_label(word_label, definition_label, popup):
    word, meaning = choice(list(vocabulary.items()))
    word_label.config(text=word)
    definition_label.config(text=meaning)
    schedule_next_word(popup, word_label, definition_label)

# Function to schedule the update of the word label
def schedule_next_word(popup, word_label, definition_label, interval=5000):
    popup.after(interval, lambda: update_word_label(word_label, definition_label, popup))

# Main function to set up the popup window
def main():
    popup = tk.Tk()
    popup.title("Learn a New Word!")
    popup.configure(bg=BG_COLOR)

    # Using more engaging fonts
    customWordFont = tkFont.Font(family="Arial", size=28, weight="bold")
    customDefinitionFont = tkFont.Font(family="Arial", size=20)

    word_label = tk.Label(popup, font=customWordFont, bg=BG_COLOR)
    word_label.pack(pady=(20, 10))

    definition_label = tk.Label(popup, font=customDefinitionFont, bg=BG_COLOR)
    definition_label.pack(pady=(0, 20))

    # Styling the close button
    close_button = tk.Button(popup, text="Close", command=popup.destroy, font=BUTTON_FONT, bg=BUTTON_COLOR, relief=tk.FLAT)
    close_button.pack(pady=(10, 20))
    close_button.bind("<Enter>", lambda e: close_button.config(bg=HOVER_COLOR))
    close_button.bind("<Leave>", lambda e: close_button.config(bg=BUTTON_COLOR))

    popup.geometry("500x300")

    # Update the word label immediately and then at intervals
    update_word_label(word_label, definition_label ,popup)
    schedule_next_word(popup, word_label, definition_label)

    popup.mainloop()

# Main code
if __name__ == "__main__":
    main()


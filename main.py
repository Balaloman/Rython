from rss_parser import Parser
from requests import get
import PySimpleGUI as sg
import sys


def main():
    # begin error handling
    while True:
        try:
            sg.theme('DarkGrey')
            # user inputs an url
            user_url = sg.PopupGetText("Enter your URL: ", title='Rython RSS Reader')
            if user_url is None:
                sys.exit()
            # user inputs an integer for amount of entries, try except allows for cancel without error message
            try:
                user_limit = int(sg.PopupGetText("How many entries would you like to see? ", title='Rython RSS Reader'))
            except:
                sys.exit()
            # translating user entries for rss-parser
            xml = get(user_url)
            # rss-parser logic
            parser = Parser(xml=xml.content, limit=user_limit)
            feed = parser.parse()
        # small exception that handles both the url and the integer value
        except ValueError:
            sg.theme('DarkBrown4')
            sg.popup("Enter valid values!")
        else:
            break

    def main_window():
        # window for reader output
        sg.theme('DarkGrey')
        # layout for the window
        layout = [[sg.MLine(size=(80, 40), key='-Main-')],
                  [sg.B('View'), sg.B('Cancel')]]

        window = sg.Window('Rython RSS Reader', layout)
        # event loop for the main window
        while True:
            event, values = window.read()
            # cancel button logic
            if event in (None, 'Cancel'):
                break
            # view button logic
            if event == 'View':
                # fetch and print from parser
                for item in feed.feed:
                    window['-Main-'].print(item.title, " ", item.description, " ")
        window.close()

    main_window()

main()
from rss_parser import Parser
from requests import get
import PySimpleGUI as sg
import os
import sys


def main():
    # begin error handling
    try:
        sg.theme('DarkGrey')
        # user inputs an url
        user_url = sg.PopupGetText("Enter your URL: ")
        # user inputs an integer for amount of entries
        user_limit = int(sg.PopupGetText("How many entries would you like to see? "))

        # translating user entries for rss-parser
        rss_url = user_url
        xml = get(rss_url)
        # rss-parser logic
        parser = Parser(xml=xml.content, limit=user_limit)
        feed = parser.parse()
        # small exception that handles both the url and the integer value
    except ValueError:
        sg.theme('DarkBrown4')
        sg.popup("Enter valid values!")
    # continue if everything is fine
    else:
        # print out rss feed contents
        for item in feed.feed:
            sg.popup_scrolled(item.title, " ", item.description, " ")


# restart the script
if __name__ == '__main__':
    main()
    os.execv(sys.executable, ['python'] + [sys.argv[0]])

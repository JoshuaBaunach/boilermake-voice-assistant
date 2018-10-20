'''
This is the main program that integrates all of the components.
'''
from voice_interperet import collect_speech
from emailBot import get_response
import sys

def main(debug=False):
    print('Welcome! How can I help?')
    bot_response = ""
    while (bot_response != "Bye"):
        if (debug):
            user_response = sys.stdin.readline()
        else:
            user_response = collect_speech()
        print('Your input: ' + user_response)
        bot_response = get_response(user_response)
        print(bot_response)

if __name__ == '__main__':
    main(debug=False)
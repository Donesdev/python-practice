def main():
    me = ('hello world, How are you?')
    print(me)
    user = input()
    happy_phrases = ('I am fine', 'I am good' , 'I am okay', 'I am great', 'I am happy')
    sad_phrases = ('I am sad', 'I am down', 'I am not okay', 'I am not happy')

    if user in happy_phrases:
        print('I am happy to hear that!')
    elif user in sad_phrases:
        print(" What's wrong?")
    else:
        print ( " So What's New with you?")
main()
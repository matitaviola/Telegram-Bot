import re

def sample_response(input_msg):
    user_message = str(input_msg).lower()

    match user_message:
        case "who are you?":
            return "me"
        case "who am i?":
            return "you"
        case "what is my level?":
            return "not implemented yet"
        case _:
            if "[[" in user_message and "]]" in user_message:
                user_message = re.sub(r'\[\[(?:[^\]|]*\|)?([^\]|]*)\]\]', r'\1', user_message)
                card = re.sub(r'-+' ,'-', re.sub('[\s,]', '-', user_message))
                return "https://edhrec.com/cards/"+card
            else:
                return
    
    #"https://edhrec.com/cards/"+user_message
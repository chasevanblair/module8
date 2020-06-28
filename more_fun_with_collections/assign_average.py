def switch_average(user_dict, key):
    user_key = str(key).upper()
    if user_key in user_dict:
        if user_key == 'A':
            print("thats an a")
            return user_dict.get('A')
        elif user_key == 'B':
            print("thats a b")
            return user_dict.get('B')
        elif user_key == 'C':
            print("thats a c")
            return user_dict.get('C')
        elif user_key == 'D':
            print("thats a d")
            return user_dict.get('D')
        elif user_key == 'E':
            print("thats an e")
            return user_dict.get('E')
    else:
        print("thats nothing")
        return None

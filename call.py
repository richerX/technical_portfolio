dict1 = {'game_short_name': None, 'chat_instance': '105088715621095546', 'id': '1234167447543173780', 'from_user': {'id': 287352001, 'is_bot': False, 'first_name': 'Ilya', 'username': 'Richer_f', 'last_name': None, 'language_code': 'ru'}, 'message': {'content_type': 'text', 'message_id': 5625, 'from_user': '<telebot.types.User object at 0x057B58B0>', 'date': 1548272582, 'chat': '<telebot.types.Chat object at 0x057DC250>', 'forward_from_chat': None, 'forward_from': None, 'forward_date': None, 'reply_to_message': None, 'edit_date': None, 'media_group_id': None, 'author_signature': None, 'text': 'Choose your name', 'entities': ['<telebot.types.MessageEntity object at 0x057DCDF0>'], 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'json': {'message_id': 5625, 'from': {'id': 283237531, 'is_bot': True, 'first_name': 'TEST Town Wars TEST', 'username': 'RedVanguardBot'}, 'chat': {'id': 287352001, 'first_name': 'Ilya', 'username': 'Richer_f', 'type': 'private'}, 'date': 1548272582, 'text': 'Choose your name', 'entities': [{'offset': 0, 'length': 16, 'type': 'bold'}]}}, 'data': '/start', 'inline_message_id': None}

for key in dict1.keys():
    
    try:
        keys = list(dict1[key].keys())
        print("{:<30}".format(key), "{:<30}".format(keys[0]), dict1[key][keys[0]])
        for key2 in keys[1:]:
            
            try:
                keys2 = list(dict1[key][key2].keys())
                print(" " * 30, "{:<30}".format(key2), "{:<30}".format(keys2[0]), dict1[key][key2][keys2[0]])
                for key3 in keys2[1:]:
                    
                    try:
                        keys3 = list(dict1[key][key2][key3].keys())
                        print(" " * 61, "{:<30}".format(key3), "{:<30}".format(keys3[0]), dict1[key][key2][key3][keys3[0]])
                        for key4 in keys3[1:]:
                            print(" " * 93 + "{:<30}".format(key4), dict1[key][key2][key3][key4])
                    except:
                        
                        print(" " * 62 + "{:<30}".format(key3), dict1[key][key2][key3])
            except:
                
                print(" " * 31 + "{:<30}".format(key2), dict1[key][key2])          
    except:
        
        print("{:<30}".format(key), dict1[key])
        
    print("-" * 150)
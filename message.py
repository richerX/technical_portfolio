dict1 = {'content_type': 'text', 'message_id': 5589, 'from_user': {'id': 287352001, 'is_bot': False, 'first_name': 'Ilya', 'username': 'Richer_f', 'last_name': None, 'language_code': 'ru'}, 'date': 1548262363, 'chat': {'type': 'private', 'last_name': None, 'first_name': 'Ilya', 'username': 'Richer_f', 'id': 287352001, 'title': None, 'all_members_are_administrators': None, 'photo': None, 'description': None, 'invite_link': None, 'pinned_message': None, 'sticker_set_name': None, 'can_set_sticker_set': None}, 'forward_from_chat': None, 'forward_from': None, 'forward_date': None, 'reply_to_message': None, 'edit_date': None, 'media_group_id': None, 'author_signature': None, 'text': '/start', 'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'json': {'message_id': 5589, 'from': {'id': 287352001, 'is_bot': False, 'first_name': 'Ilya', 'username': 'Richer_f', 'language_code': 'ru'}, 'chat': {'id': 287352001, 'first_name': 'Ilya', 'username': 'Richer_f', 'type': 'private'}, 'date': 1548262363, 'text': '🏂Боец'}}

for key in dict1.keys():   
    try:
        keys = list(dict1[key].keys())
        print("{:<30}".format(key), "{:<30}".format(keys[0]), dict1[key][keys[0]])
        for key2 in keys[1:]:
            
            try:
                keys2 = list(dict1[key][key2].keys())
                print(" " * 30, "{:<30}".format(key2), "{:<30}".format(keys2[0]), dict1[key][key2][keys2[0]])
                for key3 in keys2[1:]:
                    print(" " * 62 + "{:<30}".format(key3), dict1[key][key2][key3])
            except:
                print(" " * 31 + "{:<30}".format(key2), dict1[key][key2])          
            
    except:
        print("{:<30}".format(key), dict1[key])
    print("-" * 102)

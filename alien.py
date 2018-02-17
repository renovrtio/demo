# alien_0 = {'color': 'green', 'points': 5}
# aliens = {'alien_0' : alien_0}
# aliens['alien_0']['X_position'] = 0
# aliens['alien_0']['y_position'] = 255
# for key, value in aliens.items():
#     print("\nKey:" + key)
#     for  value2 in value.values():
#         # print("Key2:" + key2)
#         print("Value2:" + str(value2))
# # print(aliens)


# def describe_pet(animal_type='hamster', pet_name='dog'):
#     """显示宠物的信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet('dog', 'hamster')

# def get_formatted_name(first_name, last_name, middle_name=''):
#     """返回全名"""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name
# full_name = get_formatted_name("jon", 'hooker')
# print(full_name)


def build_perfile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first'] = first
    profile['last'] = last
    print(type(user_info))
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_perfile('albert', 'einstein', location='princeton', fied='physics')
print(type(user_profile))
print(user_profile)

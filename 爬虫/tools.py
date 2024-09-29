import json
import re
class Role:

    def __init__(self, name='', level='', type='', attribute='', link='', shape='', statsoul1='', statsoul2='', statsoul3='', statsoul4='', statsoul5='', statsoul6='', statsoul1_info='', statsoul2_info='', statsoul3_info='', statsoul4_info='', statsoul5_info='', statsoul6_info='', attack='', attack_info='', secret_skill='', secret_skill_info='', ultimate_skill='', ultimate_skill_info='', war_skill='', war_skill_info='', talent='', talent_info='', additional_skill1='', additional_skill1_info='', additional_skill2='', additional_skill2_info='', additional_skill3='', additional_skill3_info='', slogan='', detail='', story1='', story2='', story3='', story4='',sex='',interactive_voice='',battle_voice=''):
        self.name = name
        self.level = level
        self.type = type
        self.attribute = attribute
        self.link = link
        self.shape = shape
        self.statsoul1 = statsoul1
        self.statsoul2 = statsoul2
        self.statsoul3 = statsoul3
        self.statsoul4 = statsoul4
        self.statsoul5 = statsoul5
        self.statsoul6 = statsoul6
        self.statsoul1_info = statsoul1_info
        self.statsoul2_info = statsoul2_info
        self.statsoul3_info = statsoul3_info
        self.statsoul4_info = statsoul4_info
        self.statsoul5_info = statsoul5_info
        self.statsoul6_info = statsoul6_info
        self.attack = attack
        self.attack_info = attack_info
        self.secret_skill = secret_skill
        self.secret_skill_info = secret_skill_info
        self.ultimate_skill = ultimate_skill
        self.ultimate_skill_info = ultimate_skill_info
        self.war_skill = war_skill
        self.war_skill_info = war_skill_info
        self.talent = talent
        self.talent_info = talent_info
        self.additional_skill1 = additional_skill1
        self.additional_skill1_info = additional_skill1_info
        self.additional_skill2 = additional_skill2
        self.additional_skill2_info = additional_skill2_info
        self.additional_skill3 = additional_skill3
        self.additional_skill3_info = additional_skill3_info
        self.slogan = slogan
        self.detail = detail
        self.story1 = story1
        self.story2 = story2
        self.story3 = story3
        self.story4 = story4
        self.sex = sex
        self.interactive_voice = interactive_voice
        self.battle_voice = battle_voice

    def __str__(self):
        return 'name:' + self.name + ' level:' + self.level + ' type:' + self.type + ' attribute:' + self.attribute + ' link:' + self.link + ' shape:' + self.shape + ' statsoul1:' + self.statsoul1 + ' statsoul2:' + self.statsoul2 + ' statsoul3:' + self.statsoul3 + ' statsoul4:' + self.statsoul4 + ' statsoul5:' + self.statsoul5 + ' statsoul6:' + self.statsoul6 + ' statsoul1_info:' + self.statsoul1_info + ' statsoul2_info:' + self.statsoul2_info + ' statsoul3_info:' + self.statsoul3_info + ' statsoul4_info:' + self.statsoul4_info + ' statsoul5_info:' + self.statsoul5_info + ' statsoul6_info:' + self.statsoul6_info + ' attack:' + self.attack + ' attack_info:' + self.attack_info + ' secret_skill:' + self.secret_skill + ' secret_skill_info:' + self.secret_skill_info + ' ultimate_skill:' + self.ultimate_skill + ' ultimate_skill_info:' + self.ultimate_skill_info + ' war_skill:' + self.war_skill + ' war_skill_info:' + self.war_skill_info + ' talent:' + self.talent + ' talent_info:' + self.talent_info + ' additional_skill1:' + self.additional_skill1 + ' additional_skill1_info:' + self.additional_skill1_info + ' additional_skill2:' + self.additional_skill2 + ' additional_skill2_info:' + self.additional_skill2_info + ' additional_skill3:' + self.additional_skill3 + ' additional_skill3_info:' + self.additional_skill3_info + ' slogan:' + self.slogan + ' detail:' + self.detail + ' story1:' + self.story1 + ' story2:' + self.story2 + ' story3:' + self.story3 + ' story4:'+ self.story4 + 'sex:' + self.sex

class Weapon:
    def __init__(self, name='', level='', type='', attribute='', link='', story=''):
        self.name = name
        self.level = level
        self.type = type
        self.attribute = attribute
        self.link = link
        self.story = story

class Enemy:
    def __init__(self, name='', belong='', type='',weakness = '',attack = '',  link='', story='', skills=''):
        self.name = name
        self.belong = belong
        self.link = link
        self.type = type
        self.weakness = weakness
        self.attack = attack
        self.story = story
        self.skills = skills

class Book:
    def __init__(self, name='', belong='', slogan='', link='', story=''):
        self.name = name
        self.belong = belong
        self.link = link
        self.slogan = slogan
        self.story = story

class Material:
    def __init__(self, name='', belong='', link='', story='', desc='', from_to='', level=''):
        self.name = name
        self.level = level
        self.belong = belong
        self.from_to = from_to
        self.link = link
        self.story = story
        self.desc = desc

class Consumables:
    def __init__(self, name='', belong='', link='', story='', desc='', from_to='', level='', type=''):
        self.name = name
        self.level = level
        self.belong = belong
        self.from_to = from_to
        self.type = type
        self.link = link
        self.story = story
        self.desc = desc

class Decoration:
    def __init__(self, name='', desc='', from_to='', level='', type=''):
        self.name = name
        self.level = level
        self.type = type
        self.from_to = from_to
        self.desc = desc

class Prop:
    def __init__(self, name='', link='', story='', from_to='', level='', type=''):
        self.name = name
        self.level = level
        self.type = type
        self.from_to = from_to
        self.link = link
        self.story = story

class DevelopTask:
    def __init__(self, name='', link='', desc='', sub_tasks=[]):
        self.name = name
        self.link = link
        self.desc = desc
        self.sub_tasks = sub_tasks
class SubTask:
    def __init__(self, name='', link='', desc='', flow_path='',detail=''):
        self.name = name
        self.link = link
        self.desc = desc
        self.flow_path = flow_path
        self.detail = detail

def remove_newlines(obj):
    if isinstance(obj, dict):
        return {key: remove_newlines(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [remove_newlines(item) for item in obj]
    elif isinstance(obj, str):
        return obj.replace('\n', '')
    else:
        return obj

def remove_all_n_with_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    cleaned_data = remove_newlines(data)
    with open('achievements.json', 'w', encoding='utf-8') as output_file:
        json.dump(cleaned_data, output_file, indent=4, ensure_ascii=False)
    print("处理完成！")

def merge_role_and_voice():
    with open('roles.json', 'r', encoding='utf-8') as file:
        roles = json.load(file)
    with open('voices.json', 'r', encoding='utf-8') as file:
        voices = json.load(file)
    for voive in voices:
        for role in roles:
            if voive['name'] == role['name']:
                role['interactive_voice'] = voive['interactive_voice']
                role['battle_voice'] = voive['battle_voice']
# 开拓者•同谐 开拓者•毁灭 开拓者•存护
    destruction = []  # '毁灭'
    protection = []  # '存护'
    harmony = []  # '同谐'
    others = []  # 其他
    kaituo_voice = voices[0]
    for battle in kaituo_voice['battle_voice']:
        if '毁灭' in battle['title']:
            destruction.append(battle)
        elif '存护' in battle['title']:
            protection.append(battle)
        elif '同谐' in battle['title']:
            harmony.append(battle)
        else:
            others.append(battle)
    destruction = destruction + others
    protection = protection + others
    harmony = harmony + others
    for role in roles:
        if '毁灭' in role['name']:
            role['interactive_voice'] = kaituo_voice['interactive_voice']
            role['battle_voice'] = destruction
        elif '存护' in role['name']:
            role['interactive_voice'] = kaituo_voice['interactive_voice']
            role['battle_voice'] = protection
        elif '同谐' in role['name']:
            role['interactive_voice'] = kaituo_voice['interactive_voice']
            role['battle_voice'] = harmony

    with open('roles.json', 'w', encoding='utf-8') as output_file:
        json.dump(roles, output_file, indent=4, ensure_ascii=False)

def merge_books():
    with open('bookss.json', 'r', encoding='utf-8') as file:
        books1 = json.load(file)
    with open('booksss.json', 'r', encoding='utf-8') as file:
        books2 = json.load(file)
    books = books1 + books2
    with open('books.json', 'w', encoding='utf-8') as output_file:
        json.dump(books, output_file, indent=4, ensure_ascii=False)
    pass

def split_consumables_from():
    with open('consumables.json', 'r', encoding='utf-8') as file:
        consumables = json.load(file)
    for consumable in consumables:
        if 'from_to' in consumable:
            str = consumable['from_to']
            str = str.replace('万能合成机', '万能合成机、')
            str = str.replace('梦境贩售店', '梦境贩售店、')
            str = str.replace('）', '）、')
            if "坐在爆米花餐车" not in str:
                str = str.replace('爆米花餐车', '爆米花餐车、')
            if "附近的钟表餐厅" not in str:
                str = str.replace('钟表餐厅', '钟表餐厅、')
            str = str.replace('尚滋味', '尚滋味、')
            str = str.replace('杜氏茶庄', '杜氏茶庄、')
            str = str.replace('安德森', '安德森、')
            str = str.replace('泠泠的药材摊', '泠泠的药材摊、')
            str = str.replace('寿考堂', '寿考堂、')
            if "获得该" not in str and "获得配方" not in str:
                str = str.replace('获得', '获得、')
            str = str.replace('掉落', '掉落、')
            if str[-1] == '、':
                str = str[:-1]
            consumable['from_to'] = str
            print(consumable['from_to'])
    with open('consumables.json', 'w', encoding='utf-8') as output_file:
        json.dump(consumables, output_file, indent=4, ensure_ascii=False)

def collapse_newlines(text):
    # 使用正则表达式替换多个连续的换行符为单个换行符
    return re.sub(r'\n+', '\n', text)

def multi_n_remove():
    with open('develop_taskss.json', 'r', encoding='utf-8') as file:
        develop_tasks = json.load(file)
    for develop_task in develop_tasks:
        tasks = develop_task['sub_tasks']
        for i in tasks:
            strs = i['detail']
            for j in strs:
                j['detail'] = collapse_newlines(j['detail'])
    with open('develop_tasks.json', 'w', encoding='utf-8') as output_file:
        json.dump(develop_tasks, output_file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    multi_n_remove()
    pass

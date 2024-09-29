from time import sleep

import requests
from lxml import html
from tools import *
import json

# https://wiki.biligame.com/sr/%E9%A6%96%E9%A1%B5   崩坏星穹铁道  wiki   非官方民间组织，为爱发电，欢迎各路能人异士加入。
# CC BY-NC-SA 4.0协议
def main():
    # 1.获取所有角色的链接地址
    # 2.获取每个角色的信息 # 2.1 语音
    # 3.获取所有光锥的链接地址
    # 4.获取每个光锥的信息
    # 5.获取所有敌人的链接地址
    # 6.获取所有敌人的简介
    # 7.按照etree获取所有成就节点，如果每个成就有center节点，添加该属性
    # 8.获取所有任务（有点多，单独写）
    # 8.1 开拓任务
    # 8.1.1 找到所有h2标签并添加之后直到下一个h2标签的链接为它的所有子故事
    # 8.1.2 进入链接，找到所有h2标签及后面的center标签链接
    # 8.1.3 提取任务流程和剧情内容下的所有内容，如果一个标签内只有“折叠”则排除，如果是plotBox类型，分别记录所有选项以及对应的输出
    # 8.2 开拓续闻
    # 8.2.1 获取所有链接地址
    # 8.2.2 进入链接，找到所有h2标签及后面的center标签链接
    # 8.2.3 提取任务流程和剧情内容下的所有内容，如果一个标签内只有“折叠”则排除，如果是plotBox类型，分别记录所有选项以及对应的输出
    # 8.3 同行任务 （同8.1）
    # 8.4 冒险任务
    # 8.4.1 提取所有li标签的地址
    # 8.4.2 提取任务流程和剧情内容下的所有内容，如果一个标签内只有“折叠”则排除，如果是plotBox类型，分别记录所有选项以及对应的输出
    # 8.5 日常任务（同8.4）
    # 8.6 活动任务（同8.1）
    # 9.获取所有阅读物链接
    # 10.获取所有阅读物的内容
    # 11.获取所有材料的链接地址
    # 12.获取每个材料的类型、描述和介绍
    # 13.获取所有消耗品的链接地址
    # 14.获取每个消耗品的类型和介绍
    # 15.获取所有道具的链接地址
    # 16.获取所有道具的类型和介绍
    # 17.获取所有装饰的信息
    pass

# 1.获取所有角色的链接地址
def get_all_roles_links():
    url = 'https://wiki.biligame.com/sr/%E8%A7%92%E8%89%B2%E5%9B%BE%E9%89%B4'
    response = requests.get(url)
    tree = html.fromstring(response.content)
    div_element = tree.xpath(r'//*[@id="CardSelectTr"]')[0]
    first_divs = div_element.xpath('./div')
    ans = []
    for div in first_divs:
        tmp = Role()
        tmp.level = div.get('data-param1')
        tmp.type = div.get('data-param2')
        tmp.attribute = div.get('data-param3')
        links = div.xpath('.//a')
        tmp.link = links[0].get('href')
        tmp.name = links[0].get('title')
        ans.append(tmp)
    return ans

# 2.获取每个角色的信息
def get_every_role_info(role,base_url):
    # 有两个模板，需要分开处理
    base_path0 = r'//*[@id="mw-content-text"]/div/div[3]'
    base_path1 = r'//*[@id="mw-content-text"]/div/div[4]'
    base_path2 = r'//*[@id="mw-content-text"]/div/div[5]'
    base_path3 = r'//*[@id="mw-content-text"]/div/div[6]'
    base_path_up = base_path0
    base_path_down = base_path2


    url = base_url + role.link
    response = requests.get(url)
    tree = html.fromstring(response.content)

    choose = tree.xpath(base_path_up + r'/div[1]/span[2]')
    if len(choose) == 0:
        base_path_up = base_path1
        base_path_down = base_path3

    role.slogan = tree.xpath(base_path_up + r'/div[1]/span[2]')[0].text_content().strip()
    role.shape = tree.xpath(base_path_up + r'/div[3]/div[2]/table[1]/tbody/tr[7]/td')[0].text_content().strip()
    role.sex = tree.xpath(base_path_up + r'/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[2]')[0].text_content().strip()
    role.statsoul1 = tree.xpath(base_path_up + r'/div[4]/div/div/div[1]/table/tbody/tr[2]/td[1]')[0].text_content().strip()
    role.statsoul2 = tree.xpath(base_path_up + r'/div[4]/div/div/div[1]/table/tbody/tr[3]/td[1]')[0].text_content().strip()
    role.statsoul3 = tree.xpath(base_path_up + r'/div[4]/div/div/div[1]/table/tbody/tr[4]/td[1]')[0].text_content().strip()
    role.statsoul4 = tree.xpath(base_path_up + r'/div[4]/div/div/div[1]/table/tbody/tr[5]/td[1]')[0].text_content().strip()
    role.statsoul5 = tree.xpath(base_path_up + r'/div[4]/div/div/div[1]/table/tbody/tr[6]/td[1]')[0].text_content().strip()
    role.statsoul6 = tree.xpath(base_path_up + r'/div[4]/div/div/div[1]/table/tbody/tr[7]/td[1]')[0].text_content().strip()
    role.statsoul1_info = tree.xpath(base_path_up + r'/div[4]/div/div/div[1]/table/tbody/tr[2]/td[2]')[0].text_content().strip()
    role.statsoul2_info = tree.xpath(base_path_up + r'/div[4]/div/div/div[1]/table/tbody/tr[3]/td[2]')[0].text_content().strip()
    role.statsoul3_info = tree.xpath(base_path_up + r'/div[4]/div/div/div[1]/table/tbody/tr[4]/td[2]')[0].text_content().strip()
    role.statsoul4_info = tree.xpath(base_path_up + r'/div[4]/div/div/div[1]/table/tbody/tr[5]/td[2]')[0].text_content().strip()
    role.statsoul5_info = tree.xpath(base_path_up + r'/div[4]/div/div/div[1]/table/tbody/tr[6]/td[2]')[0].text_content().strip()
    role.statsoul6_info = tree.xpath(base_path_up + r'/div[4]/div/div/div[1]/table/tbody/tr[7]/td[2]')[0].text_content().strip()

    # 普攻、战技、终结技都有可能有多个需要找到所有类型为skill-contain的div并提取，设定第一个div的名字为技能名，后面的为附属描述

    outer_attack_divs = tree.xpath(base_path_down +r'/div/div[2]/div[1]')[0]
    attack_divs = outer_attack_divs.xpath('./div')
    skill_attack_contain_divs = [div for div in attack_divs if div.get('class') == 'skill-contain']
    first_attack_divs = skill_attack_contain_divs[0].xpath('./div')
    role.attack = [div for div in first_attack_divs if div.get('class') == 'skill-name'][0].text_content().strip()
    first_attack_detail = [div for div in first_attack_divs if div.get('class') == 'skill-text'][0].text_content().strip()
    for i in range(1,len(skill_attack_contain_divs)):
        attack_div = skill_attack_contain_divs[i].xpath('./div')
        name = [div for div in attack_div if div.get('class') == 'skill-name'][0].text_content().strip()
        detail = [div for div in attack_div if div.get('class') == 'skill-text'][0].text_content().strip()
        first_attack_detail += name + ':' + detail
    role.attack_info = first_attack_detail

    role.secret_skill = tree.xpath(base_path_down +r'/div/div[2]/div[4]/div[2]/div[1]')[0].text_content().strip()
    role.secret_skill_info = tree.xpath(base_path_down +r'/div/div[2]/div[4]/div[2]/div[3]')[0].text_content().strip()

    outer_ultimate_divs = tree.xpath(base_path_down +r'/div/div[2]/div[3]')[0]
    ultimate_divs = outer_ultimate_divs.xpath('./div')
    skill_contain_divs = [div for div in ultimate_divs if div.get('class') == 'skill-contain']
    first_skill_divs = skill_contain_divs[0].xpath('./div')
    role.ultimate_skill = [div for div in first_skill_divs if div.get('class') == 'skill-name'][0].text_content().strip()
    first_skill_detail = [div for div in first_skill_divs if div.get('class') == 'skill-text'][0].text_content().strip()
    for i in range(1,len(skill_contain_divs)):
        skill_div = skill_contain_divs[i].xpath('./div')
        name = [div for div in skill_div if div.get('class') == 'skill-name'][0].text_content().strip()
        detail = [div for div in skill_div if div.get('class') == 'skill-text'][0].text_content().strip()
        first_skill_detail += name + ':' + detail
    role.ultimate_skill_info = first_skill_detail

    outer_war_divs = tree.xpath(base_path_down +r'/div/div[2]/div[2]')[0]
    war_divs = outer_war_divs.xpath('./div')
    skill_war_contain_divs = [div for div in war_divs if div.get('class') == 'skill-contain']
    first_war_divs = skill_war_contain_divs[0].xpath('./div')
    role.war_skill = [div for div in first_war_divs if div.get('class') == 'skill-name'][0].text_content().strip()
    first_war_detail = [div for div in first_war_divs if div.get('class') == 'skill-text'][0].text_content().strip()
    for i in range(1,len(skill_war_contain_divs)):
        war_div = skill_war_contain_divs[i].xpath('./div')
        name = [div for div in war_div if div.get('class') == 'skill-name'][0].text_content().strip()
        detail = [div for div in war_div if div.get('class') == 'skill-text'][0].text_content().strip()
        first_war_detail += name + ':' + detail
    role.war_skill_info = first_war_detail

    # 天赋也需要按照类型匹配
    outer_talent_divs = tree.xpath(base_path_down +r'/div/div[2]/div[5]')[0]
    talent_divs = outer_talent_divs.xpath('./div')
    talent_contain_div = [div for div in talent_divs if div.get('class') == 'skill-contain'][0]
    talent_divs = talent_contain_div.xpath('./div')
    role.talent = [div for div in talent_divs if div.get('class') == 'skill-name'][0].text_content().strip()
    role.talent_info = [div for div in talent_divs if div.get('class') == 'skill-text'][0].text_content().strip()
    role.additional_skill1 = tree.xpath(base_path_down +r'/div/div[2]/div[6]/div[2]')[0].text_content().strip()
    role.additional_skill1_info = tree.xpath(base_path_down +r'/div/div[2]/div[6]/div[3]')[0].text_content().strip()
    role.additional_skill2 = tree.xpath(base_path_down +r'/div/div[2]/div[7]/div[2]')[0].text_content().strip()
    role.additional_skill2_info = tree.xpath(base_path_down +r'/div/div[2]/div[7]/div[3]')[0].text_content().strip()
    role.additional_skill3 = tree.xpath(base_path_down +r'/div/div[2]/div[8]/div[2]')[0].text_content().strip()
    role.additional_skill3_info = tree.xpath(base_path_down +r'/div/div[2]/div[8]/div[3]')[0].text_content().strip()
    # 有些人的角色详情需要单独处理
    #
    if role.name == '黄泉':
        role.detail = tree.xpath(r'//*[@id="mw-content-text"]/div/div[3]/div[3]/div[2]/div[1]/div/div/div[2]/table/tbody/tr[2]/td')[0].text_content().strip()
        role.story1 = tree.xpath(r'//*[@id="mw-customcollapsible-chara_story1g"]')[0].text_content().strip()
        role.story2 = tree.xpath(r'//*[@id="mw-customcollapsible-chara_story2g"]')[0].text_content().strip()
        role.story3 = tree.xpath(r'//*[@id="mw-customcollapsible-chara_story3g"]')[0].text_content().strip()
        role.story4 = tree.xpath(r'//*[@id="mw-customcollapsible-chara_story4g"]')[0].text_content().strip()
    else:
        role.detail = tree.xpath(base_path_up + r'/div[3]/div[2]/table[2]/tbody/tr[2]/td')[0].text_content().strip()
        role.story1 = tree.xpath(r'//*[@id="mw-customcollapsible-chara_story1"]')[0].text_content().strip()
        role.story2 = tree.xpath(r'//*[@id="mw-customcollapsible-chara_story2"]')[0].text_content().strip()
        role.story3 = tree.xpath(r'//*[@id="mw-customcollapsible-chara_story3"]')[0].text_content().strip()
        # 有些人没有4个故事
        if len(tree.xpath(r'//*[@id="mw-customcollapsible-chara_story4"]')) == 0:
            role.story4 = ''
        else:
            role.story4 = tree.xpath(r'//*[@id="mw-customcollapsible-chara_story4"]')[0].text_content().strip()
    print(role)

# 2.1 获取每个角色的语音（缺少三月七·巡猎;开拓者的语言都在一起，先收集起来再写分配）
def get_every_role_voice():
    base_url = 'https://wiki.biligame.com'
    url = 'https://wiki.biligame.com/sr/%E8%A7%92%E8%89%B2/%E8%AF%AD%E9%9F%B3'
    response = requests.get(url)
    tree = html.fromstring(response.content)
    outer_all_roles_divs = tree.xpath(r'//*[@id="mw-content-text"]/div')[0]
    all_roles_divss = outer_all_roles_divs.xpath('./div')
    all_roles_divs = [div for div in all_roles_divss if div.get('class') == 'ping0']
    result = []
    # 搞成name、voice1、voice2的形式
    for div in all_roles_divs:
        # 开拓者和别人的地址不一样
        name = div.xpath('.//b')[0].text_content().strip()
        print(name)
        # 取出a连接
        links = div.xpath('.//a')
        link = links[0].get('href')
        inner_url = base_url + link
        response = requests.get(inner_url)
        inner_tree = html.fromstring(response.content)
        # 互动语音
        xpath_first = r'//*[@id="mw-content-text"]/div/div[6]/div/div/div[1]'
        xpath_second = r'//*[@id="mw-content-text"]/div/div[6]/div/div/div[2]'
        if name == '开拓者':
            xpath_first = r'//*[@id="tabber-cc9a4c93113a46060305cf86cc6962ac"]/div[1]/div/div/div/div[1]'
            xpath_second = r'//*[@id="tabber-cc9a4c93113a46060305cf86cc6962ac"]/div[1]/div/div/div/div[2]'
        else:
            test_div = inner_tree.xpath(xpath_first)
            if len(test_div) == 0:
                xpath_first = r'//*[@id="mw-content-text"]/div/div[7]/div/div/div[1]'
                xpath_second = r'//*[@id="mw-content-text"]/div/div[7]/div/div/div[2]'
                testt_div = inner_tree.xpath(xpath_first)
                if len(testt_div) == 0:
                    continue

        outer_interactive_voice_div = inner_tree.xpath(xpath_first)[0]
        outer_interactive_voice_divs = outer_interactive_voice_div.xpath('./div')
        interactive_voice_divs = [div for div in outer_interactive_voice_divs if div.get('class') == 'visible-md visible-sm visible-lg']
        interactive_ans = []
        for inner_div in interactive_voice_divs:
            tmp = {}
            in_inner_div = inner_div.xpath('./div')[0]
            in_inner_divs = in_inner_div.xpath('./div')
            tmp['title'] = in_inner_divs[0].text_content().strip()
            # 只要中文
            languages_divs = in_inner_divs[-1].xpath('./div')
            tmp['voice_detail'] = languages_divs[0].text_content().strip()
            interactive_ans.append(tmp)
        # 战斗语言
        outer_battle_voice_div = inner_tree.xpath(xpath_second)[0]
        outer_battle_voice_divs = outer_battle_voice_div.xpath('./div')
        battle_voice_divs = [div for div in outer_battle_voice_divs if div.get('class') == 'visible-md visible-sm visible-lg']
        battle_ans = []
        for inner_div in battle_voice_divs:
            tmp = {}
            in_inner_div = inner_div.xpath('./div')[0]
            in_inner_divs = in_inner_div.xpath('./div')
            tmp['title'] = in_inner_divs[0].text_content().strip()
            # 只要中文
            languages_divs = in_inner_divs[-1].xpath('./div')
            tmp['voice_detail'] = languages_divs[0].text_content().strip()
            battle_ans.append(tmp)

        temp = {
            'name': name,
            'interactive_voice': interactive_ans,
            'battle_voice': battle_ans
        }
        result.append(temp)
        sleep(2)
    with open('voices.json','w',encoding='utf-8') as f:
        json.dump(result,f,ensure_ascii=False,indent=4)
    pass

# 3.获取所有光锥的链接地址
def get_all_weapon_links():
    url = 'https://wiki.biligame.com/sr/%E5%85%89%E9%94%A5%E5%9B%BE%E9%89%B4'
    response = requests.get(url)
    tree = html.fromstring(response.content)
    div_element = tree.xpath(r'//*[@id="CardSelectTr"]')[0]
    first_divs = div_element.xpath('./div')
    ans = []
    for div in first_divs:
        tmp = Weapon()
        tmp.level = div.get('data-param1')
        tmp.type = div.get('data-param2')
        tmp.attribute = div.get('data-param3')
        links = div.xpath('.//a')
        tmp.link = links[0].get('href')
        tmp.name = links[0].get('title')
        ans.append(tmp)
    return ans
    pass

# 4.获取每个光锥的故事
def get_every_weapon_story(weapon):
    base_url = 'https://wiki.biligame.com'
    url = base_url + weapon.link
    response = requests.get(url)
    tree = html.fromstring(response.content)
    weapon.story = tree.xpath(r'//*[@id="mw-content-text"]/div/div[2]/div[1]/table[3]/tbody/tr/td')[0].text_content().strip()
    print(weapon.name)

# 5.获取所有敌人的链接地址
def get_all_enemy_links():
    url = 'https://wiki.biligame.com/sr/%E6%95%8C%E4%BA%BA%E7%AD%9B%E9%80%89'
    response = requests.get(url)
    tree = html.fromstring(response.content)
    tbody_element = tree.xpath(r'//*[@id="CardSelectTr"]/tbody')[0]
    trs = tbody_element.xpath('.//tr')
    ans = []
    for tr in trs[1:]:
        tmp = Enemy()
        tmp.belong = tr.get('data-param1')
        tmp.type = tr.get('data-param2')
        tmp.weakness = tr.get('data-param3')
        tmp.attack = tr.get('data-param4')
        links = tr.xpath('./td/a')
        tmp.link = links[0].get('href')
        tmp.name = links[0].get('title')
        ans.append(tmp)
    return ans

# 6.获取每个敌人的简介和技能
def get_every_enemy_info(enemy):
    base_url = 'https://wiki.biligame.com'
    url = base_url + enemy.link
    response = requests.get(url)
    tree = html.fromstring(response.content)
    enemy.story = tree.xpath(r'//*[@id="mw-content-text"]/div/table[1]/tbody/tr[5]/td/div')[0].text_content().strip()
    outer_skills_div = tree.xpath(r'//div[@class="r-skill-bg"]')
    print(enemy.name)
    print(len(outer_skills_div))
    skill_ans = []
    if len(outer_skills_div) == 0:
        enemy.skills = skill_ans
        return
    else:
        for skill in outer_skills_div:
            tmp = {}
            tmp['name'] = skill.xpath('.//big')[0].text_content().strip()
            tmp['type'] = skill.xpath('.//span')[0].text_content().strip()
            # 有可能是9或者12
            choose = skill.xpath('.//div[@class="col-sm-9"]')
            if len(choose) == 0:
                choose = skill.xpath('.//div[@class="col-sm-12"]')
            skill_div = choose[0]
            skill_p = skill_div.xpath('.//p')[0].text_content().strip()
            skill_detail = skill_div.text_content().strip()
            tmp['detail'] = skill_detail.replace(skill_p,'').strip()
            skill_ans.append(tmp)
        enemy.skills = skill_ans

# 7.按照etree获取所有成就节点，如果每个成就有center节点，添加该属性
def get_all_achievements():
    baseurl = 'https://wiki.biligame.com'
    url = r'https://wiki.biligame.com/sr/%E6%88%90%E5%B0%B1'
    response = requests.get(url)
    tree = html.fromstring(response.content)
    divs = tree.xpath(r'//div[@class="acBox"]')
    ans = []
    for div in divs:
        tmp_ans = {}
        links = div.xpath('.//a')
        tmp_ans['name'] = links[0].get('title')
        # print('--------',tmp_ans['name'])
        inner_url = baseurl + links[0].get('href')
        inner_response = requests.get(inner_url)
        inner_tree = html.fromstring(inner_response.content)
        achievements_div = inner_tree.xpath(r'//div[@class="bwiki-collection"]')
        # print(len(achievements_div))
        innes_ans = []
        for inner_div in achievements_div:
            tmp = {}
            tmp['name'] = inner_div.get('data-collection')
            print(tmp['name'])
            explain = inner_div.xpath('.//center')
            if len(explain) == 0:
                tmp['explain'] = ''
            else:
                tmp['explain'] = explain[0].text_content().strip()
            tmp['detail'] = inner_div.xpath('.//td')[0].text_content().strip()
            innes_ans.append(tmp)
            tmp_ans['achievements'] = innes_ans
        ans.append(tmp_ans)
    return ans

# 8.获取所有任务（有点多，单独写）
# 9. 获取所有阅读物链接
def get_all_reading_links():
    url = 'https://wiki.biligame.com/sr/%E4%B9%A6%E6%9E%B6'
    response = requests.get(url)
    tree = html.fromstring(response.content)
    books = tree.xpath('//div[@class="divsort"]')
    print(len(books))
    ans = []
    for book in books:
        tmp = Book()
        links = book.xpath('.//a')
        tmp.link = links[0].get('href')
        tmp.name = links[0].get('title')
        ans.append(tmp)
    return ans

# 10.获取所有阅读物的内容
def get_every_book_content(book):
    base_url = 'https://wiki.biligame.com'
    url = base_url + book.link
    response = requests.get(url)
    tree = html.fromstring(response.content)
    print(book.name)
    if len(tree.xpath(r'//*[@id="mw-content-text"]/div/blockquote/div')) != 0:
        book.slogan = tree.xpath(r'//*[@id="mw-content-text"]/div/blockquote/div')[0].text_content().strip()
    else:
        book.slogan = ''
    # print(book.slogan)
    if len(tree.xpath(r'//*[@id="mw-content-text"]/div/table/tbody/tr[4]/td')) != 0:
        book.belong = tree.xpath(r'//*[@id="mw-content-text"]/div/table/tbody/tr[4]/td')[0].text_content().strip()
    else:
        book.belong = ''
    # print(book.belong)
    storys = tree.xpath(r'//div[@class="boxright-left"]')
    # print(len(storys))
    story_ans = []
    for story in storys:
        tmp = {}
        tmp["story_name"] = story.xpath('.//span[@class="mw-headline"]')[0].text_content().strip()
        # print(tmp["story_name"])
        tmp["story_detail"] = story.xpath('.//p')[0].text_content().strip()
        # print(tmp["story_detail"])
        story_ans.append(tmp)
    book.story = story_ans

# 11.获取所有材料的链接地址
def get_all_material_links():
    url = 'https://wiki.biligame.com/sr/%E6%9D%90%E6%96%99%E7%AD%9B%E9%80%89'
    response = requests.get(url)
    tree = html.fromstring(response.content)
    tbody_element = tree.xpath(r'//*[@id="CardSelectTr"]/tbody')[0]
    trs = tbody_element.xpath('.//tr')
    ans = []
    for tr in trs[1:]:
        tmp = Material()
        tmp.level = tr.get('data-param1')
        tmp.belong = tr.get('data-param2')
        tmp.from_to = tr.get('data-param3')
        links = tr.xpath('./td/a')
        tmp.link = links[0].get('href')
        tmp.name = links[0].get('title')
        ans.append(tmp)
    return ans

# 12.获取每个材料的简介和描述
def get_every_material_info(material):
    base_url = 'https://wiki.biligame.com'
    url = base_url + material.link
    response = requests.get(url)
    tree = html.fromstring(response.content)
    print(material.name)
    material.desc = tree.xpath(r'//*[@id="mw-content-text"]/div/table/tbody/tr[5]/td')[0].text_content().strip()
    material.story = tree.xpath(r'//*[@id="mw-content-text"]/div/table/tbody/tr[6]/td')[0].text_content().strip()
    # if len(tree.xpath(r'//*[@id="mw-content-text"]/div/table/tbody/tr[5]/td')) != 0:
    #     material.detail = tree.xpath(r'//*[@id="mw-content-text"]/div/table/tbody/tr[5]/td')[0].text_content().strip()
    # else:
    #     material.detail = ''
    # if len(tree.xpath(r'//*[@id="mw-content-text"]/div/table/tbody/tr[6]/td')) != 0:
    #     material.story = tree.xpath(r'//*[@id="mw-content-text"]/div/table/tbody/tr[6]/td')[0].text_content().strip()
    # else:
    #     material.story = ''

# 13.获取所有消耗品的链接地址
def get_all_consumable_links():
    url = 'https://wiki.biligame.com/sr/%E6%B6%88%E8%80%97%E5%93%81%E7%AD%9B%E9%80%89'
    response = requests.get(url)
    tree = html.fromstring(response.content)
    tbody_element = tree.xpath(r'//*[@id="CardSelectTr"]/tbody')[0]
    trs = tbody_element.xpath('.//tr')
    ans = []
    for tr in trs[1:]:
        tmp = Consumables()
        tmp.level = tr.get('data-param1')
        tmp.type = tr.get('data-param2')
        tmp.belong = tr.get('data-param4')
        tmp.from_to = tr.xpath(r'./td[6]')[0].text_content().strip()# 这里要根据换行处理一下(不会，所以单独处理)
        tmp.desc = tr.xpath(r'./td[7]')[0].text_content().strip()
        links = tr.xpath('./td/a')
        tmp.link = links[0].get('href')
        tmp.name = links[0].get('title')
        ans.append(tmp)
    return ans

# 14.获取每个消耗品的类型和介绍
def get_every_consumable_info(consumable):
    base_url = 'https://wiki.biligame.com'
    url = base_url + consumable.link
    response = requests.get(url)
    tree = html.fromstring(response.content)
    print(consumable.name)
    # //*[@id="mw-content-text"]/div/div[3]/div[1]/table/tbody/tr[8]/td
    if len(tree.xpath(r'//*[@id="mw-content-text"]/div/div[2]/div[1]/table/tbody/tr[8]/td')) != 0:
        consumable.story = tree.xpath(r'//*[@id="mw-content-text"]/div/div[2]/div[1]/table/tbody/tr[8]/td')[0].text_content().strip()
    else:
        consumable.story = tree.xpath(r'//*[@id="mw-content-text"]/div/div[3]/div[1]/table/tbody/tr[8]/td')[0].text_content().strip()

# 15.获取所有道具的链接地址
def get_all_prop_links():
    url = 'https://wiki.biligame.com/sr/%E9%81%93%E5%85%B7%E7%AD%9B%E9%80%89'
    response = requests.get(url)
    tree = html.fromstring(response.content)
    tbody_element = tree.xpath(r'//*[@id="CardSelectTr"]/tbody')[0]
    trs = tbody_element.xpath('.//tr')
    ans = []
    for tr in trs[1:]:
        tmp = Prop()
        tmp.level = tr.get('data-param1')
        tmp.type = tr.get('data-param2')
        tmp.from_to = tr.xpath(r'./td[5]')[0].text_content().strip()  # 这里要根据换行处理一下(不会，所以单独处理)
        links = tr.xpath('./td[2]/a')
        tmp.link = links[0].get('href')
        tmp.name = links[0].get('title')
        ans.append(tmp)
    return ans

# 16.获取每个道具的介绍
def get_every_prop_info(prop):
    base_url = 'https://wiki.biligame.com'
    url = base_url + prop.link
    response = requests.get(url)
    tree = html.fromstring(response.content)
    print(prop.name)
    # 有些道具的介绍在第五个，有些在第六个
    if len(tree.xpath(r'//*[@id="mw-content-text"]/div/table/tbody/tr[6]/td')) != 0:
        str = tree.xpath(r'//*[@id="mw-content-text"]/div/table/tbody/tr[6]/td')[0].text_content().strip()
        if str is None or str.strip() == "" :
            if len(tree.xpath(r'//*[@id="mw-content-text"]/div/table/tbody/tr[5]/td')) != 0:
                prop.story = tree.xpath(r'//*[@id="mw-content-text"]/div/table/tbody/tr[5]/td')[0].text_content().strip()
        else:
            prop.story = str

    print(prop.story)

# 17.获取所有装饰的信息
def get_all_decorations():
    url = 'https://wiki.biligame.com/sr/%E8%A3%85%E9%A5%B0%E4%B8%80%E8%A7%88'
    response = requests.get(url)
    tree = html.fromstring(response.content)
    tbody_element = tree.xpath(r'//*[@id="CardSelectTr"]/tbody')[0]
    trs = tbody_element.xpath('.//tr')
    ans = []
    for tr in trs[1:]:
        tmp = Decoration()
        tmp.level = tr.get('data-param1')
        tmp.type = tr.get('data-param2')
        tmp.from_to = tr.get('data-param3')
        links = tr.xpath('./td[2]/a')
        tmp.name = links[0].get('title')
        tmp.desc = tr.xpath('./td[7]')[0].text_content().strip()
        ans.append(tmp)
    return ans

# 8.1 开拓任务link
def get_develop_task_links():
    url = r'https://wiki.biligame.com/sr/%E5%BC%80%E6%8B%93%E4%BB%BB%E5%8A%A1'
    response = requests.get(url)
    tree = html.fromstring(response.content)
    # 先获取所有开拓任务的名字、描述和连接
    divs = tree.xpath(r'//div[@class="drop-down-wrap"]')
    res = []
    for div in divs:
        tmp = DevelopTask()
        links = div.xpath('.//a')
        tmp.link = links[0].get('href')
        tmp.name = links[0].get('title')
        tmp.desc = div.xpath('.//center')[0].text_content().strip()
        res.append(tmp)
    return res
# 8.2 获取每个开拓任务的详细信息
def get_every_develop_task_info(task):
    base_url = 'https://wiki.biligame.com'
    url = base_url + task.link
    response = requests.get(url)
    tree = html.fromstring(response.content)
    print(task.name)
    # 获取每个子任务的名字、描述、流程和连接
    root = tree.xpath(r'//*[@id="mw-content-text"]/div')[0]
    childrens = root.getchildren()
    res = []
    for index,children in enumerate(childrens):
        if children.tag == 'h2':
            if len(childrens[index+1].xpath('.//a')) == 0:
                continue
            temp = SubTask()
            temp.link = childrens[index+1].xpath('.//a')[0].get('href')
            temp.name = childrens[index+1].xpath('.//a')[0].get('title')
            print(temp.name)
            temp.desc = childrens[index+2].text_content().strip()
            flow_path_li = childrens[index+3].xpath('.//li')
            flow_path = ''
            for indexx,li in enumerate(flow_path_li):
                flow_path += str(indexx+1) + '.' + li.text_content().strip() + ';'
            temp.flow_path = flow_path
            inner_url = base_url + temp.link
            inner_response = requests.get(inner_url)
            inner_tree = html.fromstring(inner_response.content)
            inner_root = inner_tree.xpath(r'//*[@id="mw-content-text"]/div')[0]
            inner_childrens = inner_root.getchildren()
            stop_index = 0
            for indexx,inner_children in enumerate(inner_childrens):
                if inner_children.tag == 'h2':
                    stop_index = indexx
                    break
            print(stop_index)
            inner_res = []
            other_text = ''
            tmpp = {}
            tmpp['name'] = "剧情内容——start"
            for i in range(stop_index,len(inner_childrens)):
                if inner_childrens[i].tag not in ['ul','dl','div','h3','blockquote']:
                    continue
                inner_texttt = inner_childrens[i].text_content().strip()
                if "window" in inner_texttt:
                    continue
                inner_texttt = inner_texttt.replace('折叠','')
                other_text += inner_texttt + '\n'
                if inner_childrens[i].tag == 'h3':
                    tmpp['detail'] = other_text
                    inner_res.append(tmpp.copy())
                    tmpp['name'] = inner_childrens[i].text_content().strip()
                    other_text = ''
            tmpp['detail'] = other_text
            inner_res.append(tmpp.copy())
            temp.detail = inner_res
            res.append(temp)
    task.sub_tasks = res

# 8.3 开拓续闻link
def get_develop_task_follow_links():
    url = r'https://wiki.biligame.com/sr/%E5%BC%80%E6%8B%93%E7%BB%AD%E9%97%BB'
    response = requests.get(url)
    tree = html.fromstring(response.content)
    # 先获取所有开拓任务的名字、描述和连接
    divs = tree.xpath(r'//div[@class="drop-down-wrap"]')
    res = []
    for div in divs:
        tmp = DevelopTask()
        links = div.xpath('.//a')
        tmp.link = links[0].get('href')
        tmp.name = links[0].get('title')
        tmp.desc = div.xpath('.//center')[0].text_content().strip()
        res.append(tmp)
    return res
    pass

# 8.5 同行任务link,完全可以复用开拓任务的代码
def get_same_task_links(url):
    response = requests.get(url)
    tree = html.fromstring(response.content)
    # 先获取所有开拓任务的名字、描述和连接
    divs = tree.xpath(r'//div[@class="drop-down-wrap"]')
    res = []
    for div in divs:
        tmp = DevelopTask()
        links = div.xpath('.//a')
        tmp.link = links[0].get('href')
        tmp.name = links[0].get('title')
        tmp.desc = div.xpath('.//center')[0].text_content().strip()
        res.append(tmp)
    return res

# 8.6 冒险任务link ,有几个#开头的手动处理一下
def get_adventure_task_links(url):
    response = requests.get(url)
    tree = html.fromstring(response.content)
    # 先获取所有开拓任务的名字、描述和连接
    root = tree.xpath(r'//*[@id="mw-content-text"]/div')[0]
    lis = root.xpath('.//li')
    res = []
    for li in lis:
        tmp = SubTask()
        links = li.xpath('.//a')
        tmp.link = links[0].get('href')
        tmp.name = links[0].get('title')
        res.append(tmp)
    return res

# 8.7 获取每个冒险任务的详细信息
def get_every_adventure_task_info(task):
    base_url = 'https://wiki.biligame.com'
    url = base_url + task.link
    response = requests.get(url)
    tree = html.fromstring(response.content)
    print(task.name)
    # 复用时的处理
    if task.name == "海滩守护者" or task.name == "新茶上市":
        # //*[@id="mw-content-text"]/div/div[2]  任务流程
        flow_div = tree.xpath(r'//*[@id="mw-content-text"]/div/div[2]')[0]
        flow_div_childrens = flow_div.getchildren()
        stop_index = 0
        for indexx, inner_children in enumerate(flow_div_childrens):
            if inner_children.tag == 'h3' and inner_children.text_content().strip() == '任务流程':
                stop_index = indexx
                break
        flow_str = ''
        for i in range(stop_index, len(flow_div_childrens)):
            flow_str += flow_div_childrens[i].text_content().strip() + ';'
        task.flow_path = flow_str
        # //*[@id="mw-content-text"]/div/div[3]  任务详情
        detail_divv = tree.xpath(r'//*[@id="mw-content-text"]/div/div[3]')[0]
        detail_divs = detail_divv.xpath('.//div[@class="resp-tab-content"]')
        inner_res = []
        for detail_div in detail_divs:
            detail_div_childrens = detail_div.getchildren()
            tmpp = {}
            other_text = ''
            for i in range(len(detail_div_childrens)):
                if detail_div_childrens[i].tag not in ['ul', 'dl', 'div', 'h3', 'blockquote']:
                    continue
                inner_texttt = detail_div_childrens[i].text_content().strip()
                if "window" in inner_texttt:
                    continue
                inner_texttt = inner_texttt.replace('折叠', '')
                other_text += inner_texttt + '\n'
                if detail_div_childrens[i].tag == 'h3':
                    tmpp['detail'] = other_text
                    inner_res.append(tmpp.copy())
                    tmpp['name'] = detail_div_childrens[i].text_content().strip()
                    other_text = ''
            tmpp['detail'] = other_text
            inner_res.append(tmpp.copy())
        task.detail = inner_res
        pass
    else:
        root = tree.xpath(r'//*[@id="mw-content-text"]/div')[0]
        inner_childrens = root.getchildren()
        stop_index = 0
        for indexx, inner_children in enumerate(inner_childrens):
            if inner_children.tag == 'h2':
                stop_index = indexx
                break
        print(stop_index)
        inner_res = []
        other_text = ''
        tmpp = {}
        tmpp['name'] = "剧情内容——start"
        for i in range(stop_index, len(inner_childrens)):
            if inner_childrens[i].tag not in ['ul', 'dl', 'div', 'h3', 'blockquote']:
                continue
            inner_texttt = inner_childrens[i].text_content().strip()
            if "window" in inner_texttt:
                continue
            inner_texttt = inner_texttt.replace('折叠', '')
            other_text += inner_texttt + '\n'
            if inner_childrens[i].tag == 'h3':
                tmpp['detail'] = other_text
                inner_res.append(tmpp.copy())
                tmpp['name'] = inner_childrens[i].text_content().strip()
                other_text = ''
        tmpp['detail'] = other_text
        inner_res.append(tmpp.copy())
        task.detail = inner_res
        flow_div = inner_childrens[stop_index-1]
        flow_div_childrens = flow_div.getchildren()
        flow_path_li = flow_div_childrens[-1].xpath('.//li')
        print(len(flow_path_li))
        flow_path = ''
        for indexx, li in enumerate(flow_path_li):
            flow_path += str(indexx + 1) + '.' + li.text_content().strip() + ';'
        task.flow_path = flow_path

# 8.8 日常任务，复用冒险任务的代码


# 8.9 活动任务
def get_activity_task_links():
    url = r'https://wiki.biligame.com/sr/%E6%B4%BB%E5%8A%A8%E4%BB%BB%E5%8A%A1'
    response = requests.get(url)
    tree = html.fromstring(response.content)
    # 先获取所有开拓任务的名字、描述和连接
    divs = tree.xpath(r'//div[@class="drop-down-wrap"]')
    res = []
    for div in divs:
        tmp = DevelopTask()
        links = div.xpath('.//a')
        tmp.link = links[0].get('href')
        tmp.name = links[0].get('title')
        if len(div.xpath('.//center')) == 0:
            tmp.desc = ''
        else:
            tmp.desc = div.xpath('.//center')[0].text_content().strip()
        res.append(tmp)
    # 除了很详细的还有一些简单的
    root_div = tree.xpath(r'//*[@id="mw-content-text"]/div')[0]
    lis = root_div.xpath('.//li')
    for li in lis:
        links = li.xpath('.//a')
        if len(links) == 0:
            continue
        tmp = DevelopTask()
        tmp.link = links[0].get('href')
        tmp.name = links[0].get('title')
        res.append(tmp)
    return res

# 8.10 获取每个活动任务的详细信息
def get_every_activity_task_info(task):
    # 判断，如果有“剧情内容”的就复用冒险任务的代码否则复用开拓任务的代码
    base_url = 'https://wiki.biligame.com'
    url = base_url + task.link
    response = requests.get(url)
    tree = html.fromstring(response.content)
    print(task.name)
    test_div = tree.xpath(r'//*[@id="mw-content-text"]/div')[0]
    test_div_childrens = test_div.getchildren()
    flag = False
    for child in test_div_childrens:
        if child.tag == 'h2' and child.text_content().strip() == '剧情内容':
            flag = True
            break
    if not flag:
        get_every_develop_task_info(task)
    else:
        get_every_adventure_task_info(task)


def default_encoder(obj):
    if isinstance(obj, Role):
        return obj.__dict__
    if isinstance(obj, Weapon):
        return obj.__dict__
    if isinstance(obj, Enemy):
        return obj.__dict__
    if isinstance(obj, Book):
        return obj.__dict__
    if isinstance(obj, Material):
        return obj.__dict__
    if isinstance(obj, Consumables):
        return obj.__dict__
    if isinstance(obj, Prop):
        return obj.__dict__
    if isinstance(obj, Decoration):
        return obj.__dict__
    if isinstance(obj, DevelopTask):
        return obj.__dict__
    if isinstance(obj, SubTask):
        return obj.__dict__
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

if __name__ == '__main__':
    # 为了减少网站的访问次数，将获取到的数据保存到本地
    # 1.获取所有角色的链接地址
    # roles = get_all_roles_links()
    # with open('roles.json','w',encoding='utf-8') as f:
    #     json.dump(roles,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 2.获取每个角色的信息
    # with open('roles.json', 'r', encoding='utf-8') as f:
    #     roles_dicts = json.load(f)
    # roles = [Role(**i) for i in roles_dicts]
    # base_url = 'https://wiki.biligame.com'
    # # get_every_role_info(roles[15], base_url)
    # for role in roles:
    #     print(role.name)
    #     get_every_role_info(role,base_url)
    #     sleep(2)
    # with open('roles.json','w',encoding='utf-8') as f:
    #     json.dump(roles,f,default=default_encoder,ensure_ascii=False,indent=4)
    # remove_all_n_with_json('roles.json')
    # 2.1 获取每个角色的语音
    # with open('roles.json', 'r', encoding='utf-8') as f:
    #     roles_dicts = json.load(f)
    # roles = [Role(**i) for i in roles_dicts]
    # get_every_role_voice()
    # merge_role_and_voice()
    # 3.获取所有光锥的链接地址
    # weapons = get_all_weapon_links()
    # with open('weapons.json','w',encoding='utf-8') as f:
    #     json.dump(weapons,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 4.获取每个光锥的故事
    # with open('weapons.json', 'r', encoding='utf-8') as f:
    #     weapons_dicts = json.load(f)
    # weapons = [Weapon(**i) for i in weapons_dicts]
    # for weapon in weapons:
    #     get_every_weapon_story(weapon)
    #     sleep(2)
    # with open('weapons.json','w',encoding='utf-8') as f:
    #     json.dump(weapons,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 5.获取所有敌人的链接地址
    # enemies = get_all_enemy_links()
    # with open('enemies.json','w',encoding='utf-8') as f:
    #     json.dump(enemies,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 6.获取每个敌人的简介和技能
    # with open('enemies.json', 'r', encoding='utf-8') as f:
    #     enemies_dicts = json.load(f)
    # enemies = [Enemy(**i) for i in enemies_dicts]
    # for enemy in enemies:
    #     get_every_enemy_info(enemy)
    #     sleep(2)
    # with open('enemies.json','w',encoding='utf-8') as f:
    #     json.dump(enemies,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 7.按照etree获取所有成就节点，如果每个成就有center节点，添加该属性
    # achievements = get_all_achievements()
    # with open('achievements.json','w',encoding='utf-8') as f:
    #     json.dump(achievements,f,ensure_ascii=False,indent=4)
    # 9. 获取所有阅读物链接
    # books = get_all_reading_links()
    # with open('books.json','w',encoding='utf-8') as f:
    #     json.dump(books,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 10.获取所有阅读物的内容
    # with open('books.json', 'r', encoding='utf-8') as f:
    #     books_dicts = json.load(f)
    # books = [Book(**i) for i in books_dicts]
    # for book in books:
    #     get_every_book_content(book)
    #     sleep(2)
    #     with open('booksss.json','w',encoding='utf-8') as f:
    #         json.dump(books,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 11.获取所有材料的链接地址
    # materials = get_all_material_links()
    # with open('materials.json','w',encoding='utf-8') as f:
    #     json.dump(materials,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 12.获取每个材料的简介和描述
    # with open('materials.json', 'r', encoding='utf-8') as f:
    #     materials_dicts = json.load(f)
    # materials = [Material(**i) for i in materials_dicts]
    # for material in materials:
    #     get_every_material_info(material)
    #     sleep(2)
    #     with open('materials.json', 'w', encoding='utf-8') as f:
    #         json.dump(materials,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 13.获取所有消耗品的链接地址
    # consumables = get_all_consumable_links()
    # with open('consumables.json','w',encoding='utf-8') as f:
    #     json.dump(consumables,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 14.获取每个消耗品的介绍
    # with open('consumables.json', 'r', encoding='utf-8') as f:
    #     consumables_dicts = json.load(f)
    # consumables = [Consumables(**i) for i in consumables_dicts]
    # for consumable in consumables:
    #     get_every_consumable_info(consumable)
    #     sleep(1)
    # with open('consumables.json', 'w', encoding='utf-8') as f:
    #     json.dump(consumables,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 15.获取所有道具的链接地址
    # props = get_all_prop_links()
    # with open('props.json','w',encoding='utf-8') as f:
    #     json.dump(props,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 16.获取每个道具的介绍
    # with open('props.json', 'r', encoding='utf-8') as f:
    #     props_dicts = json.load(f)
    # props = [Prop(**i) for i in props_dicts]
    # for prop in props:
    #     get_every_prop_info(prop)
    #     sleep(1)
    #     with open('props.json', 'w', encoding='utf-8') as f:
    #         json.dump(props,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 17.获取所有装饰的信息
    # decorations = get_all_decorations()
    # with open('decorations.json','w',encoding='utf-8') as f:
    #     json.dump(decorations,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 8.1 开拓任务
    # develop_tasks = get_develop_task_links()
    # with open('develop_tasks.json','w',encoding='utf-8') as f:
    #     json.dump(develop_tasks,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 8.2 获取每个开拓任务的详细信息
    # with open('develop_tasks.json', 'r', encoding='utf-8') as f:
    #     develop_tasks_dicts = json.load(f)
    # develop_tasks = [DevelopTask(**i) for i in develop_tasks_dicts]
    # for task in develop_tasks:
    #     get_every_develop_task_info(task)
    #     sleep(2)
    #     with open('develop_taskss.json', 'w', encoding='utf-8') as f:
    #         json.dump(develop_tasks,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 8.3 开拓续闻
    # develop_follow_tasks = get_develop_task_follow_links()
    # with open('develop_follow_tasks.json','w',encoding='utf-8') as f:
    #     json.dump(develop_follow_tasks,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 8.4 获取每个开拓续闻的详细信息 可以直接公用开拓任务的方法
    # with open('develop_follow_tasks.json', 'r', encoding='utf-8') as f:
    #     develop_follow_tasks_dicts = json.load(f)
    # develop_follow_tasks = [DevelopTask(**i) for i in develop_follow_tasks_dicts]
    # for task in develop_follow_tasks:
    #     get_every_develop_task_info(task)
    #     sleep(2)
    #     with open('develop_follow_tasks.json', 'w', encoding='utf-8') as f:
    #         json.dump(develop_follow_tasks,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 8.5 同行任务
    # url = r'https://wiki.biligame.com/sr/%E5%90%8C%E8%A1%8C%E4%BB%BB%E5%8A%A1'
    # same_tasks = get_same_task_links(url)
    # with open('same_tasks.json','w',encoding='utf-8') as f:
    #     json.dump(same_tasks,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 8.5 获取每个同行任务的详细信息 可以直接公用开拓任务的方法
    # with open('same_tasks.json', 'r', encoding='utf-8') as f:
    #     same_tasks_dicts = json.load(f)
    # same_tasks = [DevelopTask(**i) for i in same_tasks_dicts]
    # for task in same_tasks:
    #     get_every_develop_task_info(task)
    #     sleep(2)
    #     with open('same_tasks.json', 'w', encoding='utf-8') as f:
    #         json.dump(same_tasks,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 8.6 冒险任务
    # url = r'https://wiki.biligame.com/sr/%E5%86%92%E9%99%A9%E4%BB%BB%E5%8A%A1'
    # adventure_tasks = get_adventure_task_links(url)
    # with open('adventure_tasks.json','w',encoding='utf-8') as f:
    #     json.dump(adventure_tasks,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 8.7 获取每个冒险任务的详细信息
    # with open('adventure_tasks.json', 'r', encoding='utf-8') as f:
    #     adventure_tasks_dicts = json.load(f)
    # adventure_tasks = [SubTask(**i) for i in adventure_tasks_dicts]
    # for task in adventure_tasks:
    #     get_every_adventure_task_info(task)
    #     sleep(2)
    #     with open('adventure_tasks.json', 'w', encoding='utf-8') as f:
    #         json.dump(adventure_tasks,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 8.8 日常任务
    # url = r'https://wiki.biligame.com/sr/%E6%97%A5%E5%B8%B8%E4%BB%BB%E5%8A%A1'
    # daily_tasks = get_adventure_task_links(url)
    # with open('daily_tasks.json','w',encoding='utf-8') as f:
    #     json.dump(daily_tasks,f,default=default_encoder,ensure_ascii=False,indent=4)

    # with open('daily_tasks.json', 'r', encoding='utf-8') as f:
    #     daily_tasks_dicts = json.load(f)
    # daily_tasks = [SubTask(**i) for i in daily_tasks_dicts]
    # for task in daily_tasks:
    #     get_every_adventure_task_info(task)
    #     sleep(2)
    #     with open('daily_tasks.json', 'w', encoding='utf-8') as f:
    #         json.dump(daily_tasks,f,default=default_encoder,ensure_ascii=False,indent=4)
    # 8.9 活动任务
    # activity_tasks = get_activity_task_links()
    # with open('activity_tasks.json','w',encoding='utf-8') as f:
    #     json.dump(activity_tasks,f,default=default_encoder,ensure_ascii=False,indent=4)
    with open('activity_tasks.json', 'r', encoding='utf-8') as f:
        activity_tasks_dicts = json.load(f)
    activity_tasks = [DevelopTask(**i) for i in activity_tasks_dicts]
    for task in activity_tasks:
        get_every_activity_task_info(task)
        sleep(2)
        with open('activity_taskss.json', 'w', encoding='utf-8') as f:
            json.dump(activity_tasks,f,default=default_encoder,ensure_ascii=False,indent=4)

    pass

from logger_lib import logger
import requests
from bs4 import BeautifulSoup
import random
from PIL import Image, ImageDraw, ImageFont
import pyinputplus as pyin
from prettytable import PrettyTable
from classes import NpcSingleton


def user_interface():
    from constants import sex_all, species_all, age_all, species_random
    from constants import class_by_species, careers_by_species, careers_by_class

    header = '\n\n\n' \
             '#############################################################\n' \
             '  NPC generator for Warhammer Fantasy Roleplay 4th edition\n' \
             '    git repository:\n' \
             '    https://github.com/pza007/wfrp_4_npc_generator.git\n' \
             '#############################################################\n'
    logger.debug(header)

    logger.debug('>>>>> Choose all random settings? (y/n):\n')
    f_all_rand = pyin.inputStr()
    logger.debug(f'user input: {f_all_rand}')
    #f_all_rand = pyin.inputStr(prompt='>>>>> Choose all random settings? (y/n):\n')
    if f_all_rand in ['y','Y']:
        # ALL RANDOM
        in_sex, in_species, in_age, in_class, in_career, in_xp = 'Any', 'Any', 'Any', 'Any', 'Any', 'Any'
        out_sex = random_pick(sex_all)
        out_species = random_pick(species_random)
        out_age = random_pick(age_all)
        list_classes = class_by_species[out_species]
        out_class = random_pick(list_classes)
        list_careers = list(set(careers_by_class[out_class]) & set(careers_by_species[out_species]))
        out_career = random_pick(list_careers)
        out_xp = random.randint(500, 20000) + 75
    else:
        # USER INPUTS
        # ---SEX
        logger.debug('>>>>> Please choose sex:\n')
        in_sex = pyin.inputMenu(choices=['Any'] + sex_all, numbered=True)
        logger.debug(f'user input: {in_sex}')
        #in_sex = pyin.inputMenu(prompt='>>>>> Please choose sex:\n', choices=['Any']+sex_all, numbered=True)
        if in_sex == 'Any':
            out_sex = random_pick(sex_all)
        else:
            out_sex = in_sex
        # ---SPECIES
        logger.debug('>>>>> Please choose species:\n')
        in_species = pyin.inputMenu(choices=['Any'] + sorted(species_all), numbered=True)
        logger.debug(f'user input: {in_species}')
        #in_species = pyin.inputMenu(prompt='>>>>> Please choose species:\n', choices=['Any']+sorted(species_all), numbered=True)
        if in_species == 'Any':
            out_species = random_pick(species_random)
        else:
            out_species = in_species
        # ---AGE
        logger.debug('>>>>> Please choose age:\n')
        in_age = pyin.inputMenu(choices=['Any'] + age_all, numbered=True)
        logger.debug(f'user input: {in_age}')
        #in_age = pyin.inputMenu(prompt='>>>>> Please choose age:\n', choices=['Any']+age_all, numbered=True)
        if in_age == 'Any':
            out_age = random_pick(age_all)
        else:
            out_age = in_age
        # ---CLASS
        list_classes = list(set(class_by_species[out_species]))
        logger.debug('>>>>> Please choose class:\n')
        in_class = pyin.inputMenu(choices=['Any'] + sorted(list_classes), numbered=True)
        logger.debug(f'user input: {in_class}')
        #in_class = pyin.inputMenu(prompt='>>>>> Please choose class:\n', choices=['Any']+sorted(list_classes), numbered=True)
        if in_class == 'Any':
            out_class = random_pick(list_classes)
        else:
            out_class = in_class
        # ---CAREER
        list_careers = list(set(careers_by_class[out_class]) & set(careers_by_species[out_species]))
        logger.debug('>>>>> Please choose career:\n')
        in_career = pyin.inputMenu(choices=['Any'] + sorted(list_careers), numbered=True)
        logger.debug(f'user input: {in_career}')
        #in_career = pyin.inputMenu(prompt='>>>>> Please choose career:\n', choices=['Any']+sorted(list_careers), numbered=True)
        if in_career == 'Any':
            out_career = random_pick(list_careers)
        else:
            out_career = in_career
        # ---XP
        logger.debug('>>>>> Please enter number of experience points (XP): ')
        in_xp = pyin.inputInt()
        logger.debug(f'user input: {in_xp}')
        #in_xp = pyin.inputInt(prompt='>>>>> Please enter number of experience points (XP): ')
        out_xp = in_xp
        # additional xp for randomization
        if in_species == 'Any':
            out_xp += 25
        if in_class == 'Any' and in_career == 'Any':
            out_xp += 50

    # SUMMARIES
    logger.debug('\nYour choices:')
    table = [['Sex', 'Species', 'Age', 'Class', 'Career', 'XP'],
             [in_sex, in_species, in_age, in_class, in_career, in_xp]]
    tab = PrettyTable(table[0])
    tab.add_rows(table[1:])
    logger.debug(tab)
    logger.debug('\nRoll values:')
    table = [['Sex', 'Species', 'Age', 'Class', 'Career', 'XP'],
             [out_sex, out_species, out_age, out_class, out_career, out_xp]]
    tab = PrettyTable(table[0])
    tab.add_rows(table[1:])
    logger.debug(tab)

    # GENERATE
    logger.debug('\nGenerating NPC, please wait...')

    npc = NpcSingleton()
    logger.debug('\t- Init values...')
    npc.get_init_values(**{'sex': out_sex,
                           'species': out_species,
                           'age': out_age,
                           'class': out_class,
                           'career': out_career,
                           'xp': out_xp})
    logger.debug('\t- Start values...')
    npc.roll_npc()
    logger.debug('\t- Check values...')
    npc.check_npc_1()
    logger.debug('\t- Advance in career levels (1-4)...')
    npc.advance_by_xp()

    if npc.career_level == 3:
        logger.debug('\t- Continue advancing at career level 4...')
        npc.advance_continue(npc.xp_left)

    logger.debug('\t- Final modifications...')
    npc.final_modifications()

    logger.debug('\t- Generate image...')
    file_name = put_text_to_image(npc)

    logger.debug(f'\nDone! File: {file_name} saved in local directory.')
    logger.debug(f'Experience points left = {npc.xp_left}')

############################################################################
# ROLLS
def roll1d10():
    return random.randint(1, 10)


def roll2d10():
    return roll1d10() + roll1d10()


def rollXd10(number):
    return sum([roll1d10() for i in range(number)])


def roll1d100():
    return random.randint(1, 100)


def random_pick(in_list):
    return in_list[random.randint(0, len(in_list)-1)]


############################################################################
# WEB
def get_text(in_request, in_npc):
    out_text = None

    if in_request == 'traits':
        headers = {
            'authority': 'www.rangen.co.uk',
            'accept': '*/*',
            'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'dnt': '1',
            'origin': 'https://www.rangen.co.uk',
            'referer': 'https://www.rangen.co.uk/chars/traitgen.php',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        data = {
            'contentVar': 'myDiv',
        }
        r = requests.post('https://www.rangen.co.uk/chars/traitScript.php', headers=headers, data=data)
        soup = BeautifulSoup(r.text, "lxml")
        out_text = soup.text

    elif in_request == 'appearance':
        headers = {
            'authority': 'www.rangen.co.uk',
            'accept': 'text/plain, */*; q=0.01',
            'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'dnt': '1',
            'origin': 'https://www.rangen.co.uk',
            'referer': 'https://www.rangen.co.uk/chars/appgen.php',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        data = {
            'event': 'Generate',
            'sex': in_npc.sex,
            'type': 'Realistic',
            'detail': 'Simple',
            'beard': 'RandomFhair',
            'HairL': 'RandomHair',
            'HLoss': 'RandomHLoss',
            'dye': 'RandomDye',
            'clothing': 'RandomClothes',
            'pierce': 'RandomPiercings',
            'scar': 'RandomScars',
            'tattoo': 'RandomTattoos',
            'makeup': 'RandomMakeup',
        }
        r = requests.post('https://www.rangen.co.uk/chars/appScript.php', headers=headers, data=data)
        soup = BeautifulSoup(r.text, "lxml")
        out_text = soup.text

    return out_text


def adjust_text(text_str, sex):
    if sex == 'Male':
        person = 'he'
    else:  # == 'Female'
        person = 'she'
    text_str = text_str.lower()
    text_str = text_str.replace('\n', '')
    text_str = text_str.replace('they', person)
    text_str = text_str.replace("'re", '')
    text_str = text_str.replace('have ', 'has ')
    text_str = text_str.replace('are ', 'is ')
    text_str = text_str.replace("weren't", "wasn't")
    text_str = text_str.replace("were", "was")
    text_str = text_str.replace("don't ", "doesn't ")
    text_str = text_str.replace("do ", "does ")
    if text_str.find('their'):
        if sex == 'Male': text_str = text_str.replace("their", "his")
        if sex == 'Female': text_str = text_str.replace("their", "her")
    if text_str.find('them'):
        if sex == 'Male': text_str = text_str.replace("their", "him")
        if sex == 'Female': text_str = text_str.replace("their", "her")
    # remove height information - e.g. ' A 5' 10" tall,'
    if text_str.find(' tall,') >= 0:
        text_str = text_str[text_str.find(' tall,') + 7:]
    return text_str, person


def get_traits(in_npc):
    """
    :param in_npc: [NpcSingleton]
    :return: out_general_look:  [str]
    :return: out_traits:        [list of str]
    :return: out_reactions:     [list of str]
    """
    # text
    in_text = get_text('traits', in_npc)
    # general look
    out_general_look = in_text[38: in_text.find('They:')]
    out_general_look, person = adjust_text(out_general_look, in_npc.sex)
    out_general_look = person + ' looks ' + out_general_look

    # traits
    tmp_text = in_text[in_text.find('They:'):]
    tmp_text = tmp_text.replace('They:', '')
    tmp_text = tmp_text.replace('(Behavioural traits and quirks)', '')
    tmp_text = tmp_text.replace('(Other traits and quirks)', '')
    tmp_text = tmp_text.replace('They also:', '')
    tmp_text = tmp_text.replace('↓ More details? MORE Details! ↓', '')
    tmp_text = tmp_text.replace('Are your characters in a SITUATION? Do they need to solve a PROBLEM?', '')
    tmp_text = tmp_text.replace('These trait suggestions show how this character performs when the need arises.', '')

    tmp_text, person = adjust_text(tmp_text, in_npc.sex)
    out_traits = []
    i_start, i_end = (None, None)
    for i in range(len(tmp_text)-1):
        if tmp_text[i].isdecimal() and tmp_text[i+1] == '.':
            i_start = i+2
        if i_start is not None and i > i_start and tmp_text[i] == '.':
            i_end = i
            out_traits.append(tmp_text[i_start:i_end])
            i_start, i_end = (None, None)
    out_traits = [person + text for text in out_traits]
    # reactions
    out_reactions = out_traits[-3:]
    out_traits = out_traits[:-3]

    return out_general_look, out_traits, out_reactions


def get_appearance(in_npc):
    """
    :param in_npc: [NpcSingleton]
    :return: out_appearance:  [str]
    """
    # text
    in_text = get_text('appearance', in_npc)
    # appearance
    tmp_text = in_text[4:in_text.find('2 -')]
    tmp_text, person = adjust_text(tmp_text, in_npc.sex)
    tmp_text = tmp_text.split('. ')
    out_appearance = [text for text in tmp_text if len(text) > 2]
    for i in range(len(out_appearance)):
        out_appearance[i] = out_appearance[i][0].upper() + out_appearance[i][1:]

    return out_appearance

# poor ENG-POL translation - not used
def translate(in_obj):
    """
    in_obj:  [str] or [list of str]
    out_obj: [str] or [list of str]
    """
    out_obj = None

    if type(in_obj) is str:
        in_text = in_obj
    elif type(in_obj) is list:
        in_text = '\n'.join(in_obj)
    else:
        return out_obj

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
        'Connection': 'keep-alive',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'DNT': '1',
        'Origin': 'https://www.reverso.net',
        'Referer': 'https://www.reverso.net/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'X-Reverso-Origin': 'translation.web',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-gpc': '1',
    }
    json_data = {
        'format': 'text',
        'from': 'eng',
        'to': 'pol',
        'input': in_text,
        'options': {
            'sentenceSplitter': True,
            'origin': 'translation.web',
            'contextResults': True,
            'languageDetection': True,
        },
    }
    r = requests.post('https://api.reverso.net/translate/v1/translation', headers=headers, json=json_data)
    translation = r.json()['translation']
    if len(translation) == 1:
        out_obj = translation[0]
    else:
        out_obj = translation

    return out_obj


############################################################################
# TEXT TO IMAGE
def put_text_to_image(npc):
    gray_color = (142, 144, 153, 255)       # (120, 123, 131, 255)
    img = Image.open('imgs/Character_Sheet.png')
    draw = ImageDraw.Draw(img)
    gl_v_lines = [66, 262, 730, 750, 990, 1251, 1316]
    gl_h_lines = [64, 420]

    def get_text_dimensions(text_string, font):
        ascent, descent = font.getmetrics()
        text_width = font.getmask(text_string).getbbox()[2]
        text_height = font.getmask(text_string).getbbox()[3] + descent
        return text_width, text_height

    def get_padx_center(in_text, in_font, x_left, x_right):
        w, h = get_text_dimensions(in_text, in_font)
        return (x_right - x_left - w) // 2

    def format_long_text(in_text, in_font, max_w=440):
        #max_w = 440

        w, h = get_text_dimensions(in_text, in_font)
        if w > max_w:
            words_splits = in_text.split(' ')
            out_splits = []
            tmp_text = words_splits[0]
            # merge words until limit, then add to: out_splits
            for i in range(1, len(words_splits)):
                if get_text_dimensions(tmp_text + ' ' + words_splits[i], in_font)[0] <= max_w:
                    tmp_text = tmp_text + ' ' + words_splits[i]
                else:
                    out_splits.append(tmp_text)
                    tmp_text = words_splits[i]
                # last one
                if i == len(words_splits) - 1 and len(tmp_text) > 0:
                    out_splits.append(tmp_text)

            return '\n'.join(out_splits)
        else:
            return in_text

    def draw_name_career_image(in_npc, in_draw, in_img):
        font = ImageFont.truetype('arial.ttf', 12)
        text_height = get_text_dimensions('Test', font)[1]
        fontb = ImageFont.truetype('arialbd.ttf', 14)
        textb_height = get_text_dimensions('Test', fontb)[1]
        pad_y = 3
        x_start = gl_v_lines[0]
        x_end = gl_v_lines[1]
        y_start = gl_h_lines[0]
        y_end = y_start + textb_height + pad_y

        # name
        text = in_npc.name
        in_draw.text((x_start + get_padx_center(text, fontb, x_start, x_end), y_start), text, fill=(0, 0, 0, 255), font=fontb, align="center")
        # career current
        y_start = y_end + 3
        y_end = y_start + text_height + pad_y
        text = f'Career (lvl {in_npc.career_level+1}): {in_npc.career_current.name}'
        in_draw.text((x_start + get_padx_center(text, font, x_start, x_end), y_start), text, fill=(0, 0, 0, 255), font=font, align="center")
        # career main
        y_start = y_end
        y_end = y_start + text_height + pad_y
        text = f'Career path: {in_npc.career_main_name}'
        in_draw.text((x_start + get_padx_center(text, font, x_start, x_end), y_start), text, fill=(0, 0, 0, 255), font=font, align="center")
        # class
        y_start = y_end
        y_end = y_start + text_height + pad_y
        text = f'Class: {in_npc.ch_class}'
        in_draw.text((x_start + get_padx_center(text, font, x_start, x_end), y_start), text, fill=(0, 0, 0, 255), font=font, align="center")
        # species, age
        y_start = y_end
        y_end = y_start + text_height + pad_y
        text = f'Species: {in_npc.species}, Age: {in_npc.age}'
        in_draw.text((x_start + get_padx_center(text, font, x_start, x_end), y_start), text, fill=(0, 0, 0, 255), font=font, align="center")
        # height, status
        y_start = y_end
        y_end = y_start + text_height + pad_y
        text = f'Height: {in_npc.height:.2f}m, Status: {in_npc.status}'
        in_draw.text((x_start + get_padx_center(text, font, x_start, x_end), y_start), text, fill=(0, 0, 0, 255), font=font, align="center")

        # image by sex and career
        ch_img_name = 'imgs\\'
        if in_npc.sex == 'Male':
            ch_img_name += 'm_'
        else:
            ch_img_name += 'f_'
        ch_img_name += npc.career_main_name + '.png'
        ch_img = Image.open(ch_img_name)
        y_start = y_end + 10
        y_end = y_start + ch_img.size[1]

        padding_x = (x_end - x_start - ch_img.size[0]) // 2
        #padding_y = (gl_h_lines[1] - y_start - ch_img.size[1]) // 2

        in_img.paste(ch_img, (x_start+padding_x, y_start), ch_img)

        return y_end

    def draw_descriptions(in_npc, in_draw):
        font = ImageFont.truetype('arial.ttf', 12)
        text_height = get_text_dimensions('Test', font)[1]
        pad_x = 3
        pad_y = 3

        # Appearance (npc.desc_gen_look not used)
        text = 'Appearance'
        #   rectangle
        x_start = gl_v_lines[1]
        x_end = gl_v_lines[2]
        y_start = gl_h_lines[0]
        y_end = y_start + (pad_y + text_height + pad_y)
        in_draw.rectangle([(x_start, y_start), (x_end, y_end)], fill=gray_color, outline="black")
        in_draw.text((x_start + pad_x, y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="center")
        #   sub-text
        for in_text in in_npc.desc_appearance:
            text = format_long_text(in_text, font)
            x_start = gl_v_lines[1] + 3*pad_x
            x_end = gl_v_lines[2]
            y_start = y_end
            y_end = y_start + (pad_y + text_height) * (1+text.count('\n'))
            in_draw.multiline_text((x_start, y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="left")
            # lines
            in_draw.line([(x_start, y_end), (x_end, y_end)], fill="black", width=1)
            in_draw.line([(x_end, y_start), (x_end, y_end)], fill="black", width=1)

        # Traits
        text = 'Traits'
        #   rectangle
        x_start = gl_v_lines[1]
        x_end = gl_v_lines[2]
        y_start = y_end + 10
        y_end = y_start + (pad_y + text_height + pad_y)
        in_draw.rectangle([(x_start, y_start), (x_end, y_end)], fill=gray_color, outline="black")
        in_draw.text((x_start + pad_x, y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="center")
        #   sub-text
        for in_text in in_npc.desc_traits[:3]:
            text = format_long_text(in_text, font)
            x_start = gl_v_lines[1] + 3*pad_x
            x_end = gl_v_lines[2]
            y_start = y_end
            y_end = y_start + (pad_y + text_height) * (1+text.count('\n'))
            in_draw.multiline_text((x_start, y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="left")
            # lines
            in_draw.line([(x_start, y_end), (x_end, y_end)], fill="black", width=1)
            in_draw.line([(x_end, y_start), (x_end, y_end)], fill="black", width=1)

        # Reactions
        text = 'Reactions'
        #   rectangle
        x_start = gl_v_lines[1]
        x_end = gl_v_lines[2]
        y_start = y_end + 10
        y_end = y_start + (pad_y + text_height + pad_y)
        in_draw.rectangle([(x_start, y_start), (x_end, y_end)], fill=gray_color, outline="black")
        in_draw.text((x_start + pad_x, y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="center")
        #   sub-text
        for in_text in in_npc.desc_reactions:
            text = format_long_text(in_text, font)
            x_start = gl_v_lines[1] + 3*pad_x
            x_end = gl_v_lines[2]
            y_start = y_end
            y_end = y_start + (pad_y + text_height) * (1+text.count('\n'))
            in_draw.multiline_text((x_start, y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="left")
            # lines
            in_draw.line([(x_start, y_end), (x_end, y_end)], fill="black", width=1)
            in_draw.line([(x_end, y_start), (x_end, y_end)], fill="black", width=1)

        # Trappings
        text = 'Trappings'
        #   rectangle
        x_start = gl_v_lines[1]
        x_end = gl_v_lines[2]
        y_start = y_end + 10
        y_end = y_start + (pad_y + text_height + pad_y)
        in_draw.rectangle([(x_start, y_start), (x_end, y_end)], fill=gray_color, outline="black")
        in_draw.text((x_start + pad_x, y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="center")
        #   sub-text
        text = format_long_text(in_npc.trapping, font)
        x_start = gl_v_lines[1] + 3*pad_x
        x_end = gl_v_lines[2]
        y_start = y_end
        y_end = y_start + (pad_y + text_height) * (1+text.count('\n'))
        in_draw.multiline_text((x_start, y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="left")
        # lines
        in_draw.line([(x_start, y_end), (x_end, y_end)], fill="black", width=1)
        in_draw.line([(x_end, y_start), (x_end, y_end)], fill="black", width=1)

        # Money
        text = 'Money'
        #   rectangle
        x_start = gl_v_lines[1]
        x_end = gl_v_lines[2]
        y_start = y_end + 10
        y_end = y_start + (pad_y + text_height + pad_y)
        in_draw.rectangle([(x_start, y_start), (x_end, y_end)], fill=gray_color, outline="black")
        in_draw.text((x_start + pad_x, y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="center")
        #   sub-text
        if in_npc.money is None:
            a = 1
        text = format_long_text(in_npc.money, font)
        x_start = gl_v_lines[1] + 3*pad_x
        x_end = gl_v_lines[2]
        y_start = y_end
        y_end = y_start + (pad_y + text_height) * (1+text.count('\n'))
        in_draw.multiline_text((x_start, y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="left")
        # lines
        in_draw.line([(x_start, y_end), (x_end, y_end)], fill="black", width=1)
        in_draw.line([(x_end, y_start), (x_end, y_end)], fill="black", width=1)

        # Dooming
        if len(in_npc.dooming) > 5:
            text = 'Dooming'
            #   rectangle
            x_start = gl_v_lines[1]
            x_end = gl_v_lines[2]
            y_start = y_end + 10
            y_end = y_start + (pad_y + text_height + pad_y)
            in_draw.rectangle([(x_start, y_start), (x_end, y_end)], fill=gray_color, outline="black")
            in_draw.text((x_start + pad_x, y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="center")
            #   sub-text
            text = format_long_text(in_npc.dooming, font)
            x_start = gl_v_lines[1] + 3*pad_x
            x_end = gl_v_lines[2]
            y_start = y_end
            y_end = y_start + (pad_y + text_height) * (1+text.count('\n'))
            in_draw.multiline_text((x_start, y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="left")
            # lines
            in_draw.line([(x_start, y_end), (x_end, y_end)], fill="black", width=1)
            in_draw.line([(x_end, y_start), (x_end, y_end)], fill="black", width=1)

        return y_end

    def draw_talents(in_npc, in_draw, in_y_start):
        def shorten_text(in_text, in_font, max_w=95):
            w, h = get_text_dimensions(in_text, in_font)
            mod = False
            while w > max_w:
                in_text = in_text[:-2]
                w, h = get_text_dimensions(in_text, in_font)
                mod = True
            if mod:
                return in_text + '.'
            else:
                return in_text

        v_line_middle = gl_v_lines[0] + 100    # line between gl_v_lines[0] and gl_v_lines[1]
        font = ImageFont.truetype('arial.ttf', 12)
        text_height = get_text_dimensions('Test', font)[1]
        pad_x = 3
        pad_y = 3

        # HEADER
        #   rectangle
        text = 'Talent'
        x_start = gl_v_lines[0]
        x_end = v_line_middle
        x0 = [x_start, x_end]
        y_start = in_y_start + 20
        y_end = y_start + (pad_y + text_height + pad_y)
        in_draw.rectangle([(x_start, y_start), (x_end, y_end)], fill=gray_color, outline="black")
        in_draw.text((x_start + get_padx_center(text, font, x_start, x_end), y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="left")
        #   rectangle
        text = 'L'  # level
        x_start = x_end
        x_end = x_start + 15
        x1 = [x_start, x_end]
        in_draw.rectangle([(x_start, y_start), (x_end, y_end)], fill=gray_color, outline="black")
        in_draw.text((x_start + get_padx_center(text, font, x_start, x_end), y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="center")
        #   rectangle
        text = 'Test'
        x_start = x_end
        x_end = x_start + 100
        x2 = [x_start, x_end]
        in_draw.rectangle([(x_start, y_start), (x_end, y_end)], fill=gray_color, outline="black")
        in_draw.text((x_start + get_padx_center(text, font, x_start, x_end), y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="left")
        #   rectangle
        text = 'Description'
        x_start = x_end
        x_end = gl_v_lines[2]
        x3 = [x_start, x_end]
        in_draw.rectangle([(x_start, y_start), (x_end, y_end)], fill=gray_color, outline="black")
        in_draw.text((x_start + get_padx_center(text, font, x_start, x_end), y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="left")

        # DESCRIPTIONS
        #   reshuffle talents (permanent at the end)
        _talents = []
        for talent_name, (talent_test, talent_advance, talent_description) in in_npc.talents.items():
            if talent_description.find('Permanent') < 0:
                _talents.append([talent_name, talent_test, talent_advance, talent_description])
        for talent_name, (talent_test, talent_advance, talent_description) in in_npc.talents.items():
            if talent_description.find('Permanent') >= 0:
                _talents.append([talent_name, talent_test, talent_advance, talent_description])
        # draw
        for talent_name, talent_test, talent_advance, talent_description in _talents:
            # Name
            #text = shorten_text(talent_name, font, max_w=95)
            x_start, x_end = x0
            y_start = y_end
            #in_draw.text((x_start + pad_x, y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="left")
            text = format_long_text(talent_name, font, max_w=95)
            y_end0 = y_start + (pad_y + text_height) * (1 + text.count('\n'))
            in_draw.multiline_text((x_start + pad_x, y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="left")

            # Advance
            text = str(talent_advance)
            x_start, x_end = x1
            y_end1 = y_start + (pad_y + text_height) * (1+text.count('\n'))
            in_draw.text((x_start + pad_x, y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="center")

            # Test
            if len(talent_test) <= 0:
                text = talent_test
            else:
                text = format_long_text(talent_test, font, max_w=95)
            x_start, x_end = x2
            y_end2 = y_start + (pad_y + text_height) * (1+text.count('\n'))
            in_draw.multiline_text((x_start + pad_x, y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="left")

            # Description
            text = format_long_text(talent_description, font, max_w=560-100-15)
            x_start, x_end = x3
            y_end3 = y_start + (pad_y + text_height) * (1+text.count('\n'))
            in_draw.multiline_text((x_start + pad_x, y_start + pad_y), text, fill=(0, 0, 0, 255), font=font, align="left")

            # lines
            #y_end = max([y_end1, y_end2])
            y_end = max([y_end0, y_end1, y_end2, y_end3])
            #   vertical: x0 x3
            in_draw.line([(x0[0], y_end), (x3[1], y_end)], fill="black", width=1)
            #   horizontal x0
            in_draw.line([(x0[0], y_start), (x0[0], y_end)], fill="black", width=1)
            #   horizontal x1
            in_draw.line([(x1[0], y_start), (x1[0], y_end)], fill="black", width=1)
            #   horizontal x2
            in_draw.line([(x2[0], y_start), (x2[0], y_end)], fill="black", width=1)
            #   horizontal x3
            in_draw.line([(x3[0], y_start), (x3[0], y_end)], fill="black", width=1)
            #   horizontal last one
            in_draw.line([(x3[1], y_start), (x3[1], y_end)], fill="black", width=1)

        return y_end

    def draw_stats(in_npc, in_draw):
        # "WS", "BS", "S", "T", "AG", "I", "DEX", "INT", "WP", "FEL"
        cell_width = 26
        fonts = ImageFont.truetype('arialbd.ttf', 11)
        font = ImageFont.truetype('arial.ttf', 12)
        fontb = ImageFont.truetype('arialbd.ttf', 13)
        texts_height = get_text_dimensions('Test', fonts)[1]
        text_height = get_text_dimensions('Test', font)[1]
        textb_height = get_text_dimensions('Test', fontb)[1]
        pad_x = 2
        pad_y = 3

        # HEADER
        x_start = gl_v_lines[3]
        x_end = x_start + cell_width*10
        y_start = gl_h_lines[0]
        y_end = y_start + (pad_y + texts_height + pad_y)
        in_draw.rectangle([(x_start, y_start), (x_end, y_end)], fill=gray_color, outline="black")
        for dx in range(cell_width, cell_width*10-1, cell_width):
            in_draw.line([(x_start+dx, y_start), (x_start+dx, y_end)], fill="black", width=1)
        stat_names = ["WS", "BS", "S", "T", "AG", "I", "DEX", "INT", "WP", "FEL"]
        for i, text in enumerate(stat_names):
            padding = get_padx_center(text, fonts, x_start + i*cell_width, x_start + (i+1)*cell_width)
            in_draw.text((x_start + padding + i*cell_width, y_start + pad_y), text, fill=(0, 0, 0, 255), font=fonts, align="left")

        # STAT VALUES
        # self.attributes  {stat_name: [basic, advance, total]}
        for i in range(3):
            if i in [0, 1]: in_font = font; in_text_height = text_height
            else: in_font = fontb; in_text_height = textb_height

            y_start = y_end
            y_end = y_start + (pad_y + in_text_height + pad_y)
            in_draw.rectangle([(x_start, y_start), (x_end, y_end)], outline="black")
            for dx in range(cell_width, cell_width*10-1, cell_width):
                in_draw.line([(x_start+dx, y_start), (x_start+dx, y_end)], fill="black", width=1)

            values = [str(in_npc.attributes[stat_name][i]) for stat_name in stat_names]
            for j, text in enumerate(values):
                padding = get_padx_center(text, in_font, x_start + j*cell_width, x_start + (j+1)*cell_width)
                in_draw.text((x_start + padding + j*cell_width, y_start + pad_y), text, fill=(0, 0, 0, 255), font=in_font, align="left")

        y_middle = 0
        # "Wounds", "MoveSpeed", "Fate", "Resilience"
        start = x_end + 20
        y_end = gl_h_lines[0]
        names = ["Wounds", "MoveSpeed", "Fate", "Resilience"]
        for i, name in enumerate(names):
            if i == 0: in_font1 = ImageFont.truetype('arialbd.ttf', 12); in_font2 = ImageFont.truetype('arialbd.ttf', 13); h= texts_height
            else: in_font1 = ImageFont.truetype('arial.ttf', 12); in_font2 = ImageFont.truetype('arial.ttf', 13); h = text_height
            # header
            x_start = start
            x_end = x_start + 75
            y_start = y_end
            y_end = y_start + (pad_y + h + pad_y)
            in_draw.rectangle([(x_start, y_start), (x_end, y_end)], fill=gray_color, outline="black")
            #padding = get_padx_center(name, fonts, x_start, x_end)
            in_draw.text((x_start + 3*pad_x, y_start + pad_y), name, fill=(0, 0, 0, 255), font=in_font1, align="left")
            # value
            x_start = x_end
            x_end = x_end + cell_width
            in_draw.rectangle([(x_start, y_start), (x_end, y_end)], outline="black")
            text = str(in_npc.attributes[name][2])  # total value
            padding = get_padx_center(text, fontb, x_start, x_end)
            in_draw.text((x_start + padding, y_start + pad_y), text, fill=(0, 0, 0, 255), font=in_font2, align="left")
            # line
            x_start = start
            x_end = x_start + 75 + cell_width
            in_draw.line([(x_start, y_end), (x_end, y_end)], fill="black", width=1)
            if i == 1: y_middle = y_end

        # "Fortune", "Resolve"
        start = x_end
        y_end = y_middle
        names = ["Fortune", "Resolve"]
        for i, name in enumerate(names):
            in_font1 = ImageFont.truetype('arial.ttf', 12); in_font2 = ImageFont.truetype('arial.ttf', 13); h = text_height
            # header
            x_start = start
            x_end = x_start + 75
            y_start = y_end
            y_end = y_start + (pad_y + h + pad_y)
            in_draw.rectangle([(x_start, y_start), (x_end, y_end)], fill=gray_color, outline="black")
            in_draw.text((x_start + 3 * pad_x, y_start + pad_y), name, fill=(0, 0, 0, 255), font=in_font1, align="left")
            # value
            x_start = x_end
            x_end = x_end + cell_width
            in_draw.rectangle([(x_start, y_start), (x_end, y_end)], outline="black")
            text = str(in_npc.attributes[name][2])  # total value
            padding = get_padx_center(text, fontb, x_start, x_end)
            in_draw.text((x_start + padding, y_start + pad_y), text, fill=(0, 0, 0, 255), font=in_font2, align="left")
            # line
            x_start = start
            x_end = x_start + 75 + cell_width
            in_draw.line([(x_start, y_end), (x_end, y_end)], fill="black", width=1)

        return y_end

    def draw_basic_skill_table(in_npc, in_draw, in_y_start):
        def shorten_text(in_text, in_font):
            w, h = get_text_dimensions(in_text, in_font)
            mod = False
            while w > 90:
                in_text = in_text[:-2]
                w, h = get_text_dimensions(in_text, in_font)
                mod = True
            if mod:
                return in_text + '.'
            else:
                return in_text
        # -----------------------------------------------------
        # ----------- BASIC
        # HEADER
        size = (gl_v_lines[3], in_y_start+20, 227, 20)   # x,y,with,height
        in_draw.rectangle([(size[0], size[1]), (size[0]+size[2], size[1]+size[3])], fill=gray_color, outline="black")
        #   v_lines
        v_lines_x = [size[0], size[0]+103, size[0]+134, size[0]+165, size[0]+196, size[0]+size[2]]
        in_draw.line([(v_lines_x[1], size[1]), (v_lines_x[1], size[1]+size[3])], fill="black", width=0)
        in_draw.line([(v_lines_x[3], size[1]), (v_lines_x[3], size[1]+size[3])], fill="black", width=0)
        in_draw.line([(v_lines_x[4], size[1]), (v_lines_x[4], size[1]+size[3])], fill="black", width=0)
        #   insert text
        padx, pady = 4, 3
        text_pos = [(v_lines_x[0]+padx, size[1]+pady),  # list of (x,y)
                    (v_lines_x[1]+padx, size[1]+pady),
                    (v_lines_x[3]+padx, size[1]+pady),
                    (v_lines_x[4]+padx, size[1]+pady)]
        for text, pos in zip(['BASIC Skill', '     Stat.', 'Adv.', 'Tot.'], text_pos):
            in_draw.text((pos[0], pos[1]), text, fill=(0, 0, 0, 255), font=ImageFont.truetype('arial.ttf', 12), align="center")
        # SKILLS
        font = ImageFont.truetype('arial.ttf', 12)
        fontb = ImageFont.truetype('arialbd.ttf', 13)
        padx, pady = 4, 3
        # top and bottom horizontal line's y-value
        h_lines_y = [size[1]+size[3], size[1]+size[3]+pady+get_text_dimensions('Test', font)[1]+pady]
        for skill_name, values_list in in_npc.skills_basic.items():
            # name
            skill_name = shorten_text(skill_name, font)
            # positions
            text_pos = [(v_lines_x[0]+padx, h_lines_y[0]+pady),     # name: x,y
                        (v_lines_x[1]+get_padx_center(str(values_list[0]), font, v_lines_x[1], v_lines_x[2]),  h_lines_y[0]+pady),  # stat: x,y
                        (v_lines_x[2]+get_padx_center(str(values_list[1]), font, v_lines_x[2], v_lines_x[3]),  h_lines_y[0]+pady),  # stat: x,y
                        (v_lines_x[3]+get_padx_center(str(values_list[2]), font, v_lines_x[3], v_lines_x[4]),  h_lines_y[0]+pady),  # stat: x,y
                        (v_lines_x[4]+get_padx_center(str(values_list[3]), fontb,v_lines_x[4], v_lines_x[5]),  h_lines_y[0]+pady-1)]  # stat: x,y
            # draw text
            in_draw.text(text_pos[0], skill_name, fill=(0, 0, 0, 255), font=font, align="center")
            in_draw.text(text_pos[1], str(values_list[0]), fill=(0, 0, 0, 255), font=font, align="center")
            in_draw.text(text_pos[2], str(values_list[1]), fill=(0, 0, 0, 255), font=font, align="center")
            in_draw.text(text_pos[3], str(values_list[2]), fill=(0, 0, 0, 255), font=font, align="center")
            in_draw.text(text_pos[4], str(values_list[3]), fill=(0, 0, 0, 255), font=fontb, align="center")
            # draw vertical lines
            in_draw.line([(v_lines_x[1], h_lines_y[0]), (v_lines_x[1], h_lines_y[1])], fill="black", width=0)
            in_draw.line([(v_lines_x[2], h_lines_y[0]), (v_lines_x[2], h_lines_y[1])], fill="black", width=0)
            in_draw.line([(v_lines_x[3], h_lines_y[0]), (v_lines_x[3], h_lines_y[1])], fill="black", width=0)
            in_draw.line([(v_lines_x[4], h_lines_y[0]), (v_lines_x[4], h_lines_y[1])], fill="black", width=0)
            in_draw.line([(v_lines_x[5], h_lines_y[0]), (v_lines_x[5], h_lines_y[1])], fill="black", width=0)
            # draw horizontal bottom line
            in_draw.line([(v_lines_x[0], h_lines_y[1]), (v_lines_x[-1], h_lines_y[1])], fill="black", width=0)
            h_lines_y = [h_lines_y[1], h_lines_y[1]+h_lines_y[1]-h_lines_y[0]]

        return gl_v_lines[3]+227, h_lines_y[1]

    def draw_advanced_skill_table(in_npc, in_draw, in_x_start, in_y_start):
        # -----------------------------------------------------
        # ----------- ADVANCED
        # HEADER
        size = (in_x_start+20, in_y_start+20, 227, 20)   # x,y,with,height
        in_draw.rectangle([(size[0], size[1]), (size[0]+size[2], size[1]+size[3])], fill=gray_color, outline="black")
        #   v_lines
        v_lines_x = [size[0], size[0]+103, size[0]+134, size[0]+165, size[0]+196, size[0]+size[2]]
        in_draw.line([(v_lines_x[1], size[1]), (v_lines_x[1], size[1]+size[3])], fill="black", width=0)
        in_draw.line([(v_lines_x[3], size[1]), (v_lines_x[3], size[1]+size[3])], fill="black", width=0)
        in_draw.line([(v_lines_x[4], size[1]), (v_lines_x[4], size[1]+size[3])], fill="black", width=0)
        #   insert text
        padx, pady = 4, 3
        text_pos = [(v_lines_x[0]+padx, size[1]+pady),  # list of (x,y)
                    (v_lines_x[1]+padx, size[1]+pady),
                    (v_lines_x[3]+padx, size[1]+pady),
                    (v_lines_x[4]+padx, size[1]+pady)]
        for text, pos in zip(['ADVANCED Skill', '     Stat.', 'Adv.', 'Tot.'], text_pos):
            in_draw.text((pos[0], pos[1]), text, fill=(0, 0, 0, 255), font=ImageFont.truetype('arial.ttf', 12), align="center")
        # SKILLS
        font = ImageFont.truetype('arial.ttf', 12)
        fontb = ImageFont.truetype('arialbd.ttf', 13)
        padx, pady = 4, 3
        # top, middle and bottom horizontal line's y-value
        h_lines_y = [size[1]+size[3], size[1]+size[3]+pady+get_text_dimensions('Test', font)[1]+pady]
        h_lines_y.append(h_lines_y[1] + h_lines_y[1]-h_lines_y[0])
        for skill_name, values_list in in_npc.skills_advanced.items():
            # positions
            text_pos = [(v_lines_x[0]+padx, h_lines_y[0]+pady),     # name: x,y
                        (v_lines_x[1]+get_padx_center(str(values_list[0]), font, v_lines_x[1], v_lines_x[2]),  h_lines_y[1]+pady),  # stat: x,y
                        (v_lines_x[2]+get_padx_center(str(values_list[1]), font, v_lines_x[2], v_lines_x[3]),  h_lines_y[1]+pady),  # stat: x,y
                        (v_lines_x[3]+get_padx_center(str(values_list[2]), font, v_lines_x[3], v_lines_x[4]),  h_lines_y[1]+pady),  # stat: x,y
                        (v_lines_x[4]+get_padx_center(str(values_list[3]), fontb,v_lines_x[4], v_lines_x[5]),  h_lines_y[1]+pady-1)]  # stat: x,y
            # draw text
            in_draw.text(text_pos[0], skill_name, fill=(0, 0, 0, 255), font=font, align="center")
            in_draw.text(text_pos[1], str(values_list[0]), fill=(0, 0, 0, 255), font=font, align="center")
            in_draw.text(text_pos[2], str(values_list[1]), fill=(0, 0, 0, 255), font=font, align="center")
            in_draw.text(text_pos[3], str(values_list[2]), fill=(0, 0, 0, 255), font=font, align="center")
            in_draw.text(text_pos[4], str(values_list[3]), fill=(0, 0, 0, 255), font=fontb, align="center")
            # draw vertical lines
            in_draw.line([(v_lines_x[1], h_lines_y[1]), (v_lines_x[1], h_lines_y[2])], fill="black", width=0)
            in_draw.line([(v_lines_x[2], h_lines_y[1]), (v_lines_x[2], h_lines_y[2])], fill="black", width=0)
            in_draw.line([(v_lines_x[3], h_lines_y[1]), (v_lines_x[3], h_lines_y[2])], fill="black", width=0)
            in_draw.line([(v_lines_x[4], h_lines_y[1]), (v_lines_x[4], h_lines_y[2])], fill="black", width=0)
            in_draw.line([(v_lines_x[5], h_lines_y[0]), (v_lines_x[5], h_lines_y[2])], fill="black", width=0)
            # draw horizontal lines
            in_draw.line([(v_lines_x[1], h_lines_y[1]), (v_lines_x[-1], h_lines_y[1])], fill="black", width=0)
            in_draw.line([(v_lines_x[0], h_lines_y[2]), (v_lines_x[-1], h_lines_y[2])], fill="black", width=0)
            h_lines_y = [
                h_lines_y[2],
                h_lines_y[2]+(h_lines_y[2]-h_lines_y[1]),
                h_lines_y[2]+2*(h_lines_y[2]-h_lines_y[1])]

        return h_lines_y[1]

    def finish(in_npc, in_img, in_y_start):
        # add image to end character sheet
        sheet_end = Image.open('imgs\\sheet_end.png')
        x_start = 0
        x_end = gl_v_lines[-1]
        y_start = in_y_start + 5
        y_end = y_start + sheet_end.size[1]
        in_img.paste(sheet_end, (x_start, y_start), sheet_end)

        # crop and save image
        left = 0
        top = 0
        right = x_end
        bottom = y_end
        out_img = in_img.crop((left, top, right, bottom))
        out_img.show()

        file_name = in_npc.career_main_name + "__" + in_npc.name + ".png"
        file_name = file_name.replace(' ', '_')
        out_img.save(file_name, quality=100)
        #out_img_pdf = out_img.convert('RGB')
        #out_img_pdf.save(r'test.pdf')
        return file_name

    y_end1 = draw_name_career_image(npc, draw, img)
    y_end2 = draw_descriptions(npc, draw)
    y_end3 = draw_talents(npc, draw, max([y_end1, y_end2]))

    y_end4 = draw_stats(npc, draw)
    x_end5, y_end5 = draw_basic_skill_table(npc, draw, y_end4)
    y_end6 = draw_advanced_skill_table(npc, draw, x_end5, y_end4)

    file_name = finish(npc, img, max([y_end1, y_end2, y_end3, y_end4, y_end5, y_end6]))
    return file_name


"""
HOW TO inspect page?
Network, Fetch/XHR, copy as cURL/bash
convert to python: https://curlconverter.com/
"""
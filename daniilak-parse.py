import os
import requests as req
import pandas as pd


def get_str(url: str) -> str:
    request = req.get(url)
    return(request.text)

def str_to_txt(string: str):
    f = open('bbbreaking.txt', 'w')
    f.write(string)
    f.close()
    f

def count_lines(path) -> int:
    with open(path, 'r') as f:
        for count, line in enumerate(f):
            pass
    f.close()
    return(count+1)

def remove_dublicates(name_list: list, act_list: list) -> dict:
    final_dict = { }

    num_of_acts = len(act_list)

    i = len(name_list) 
    while i != 0:
        i -= 1
        name_list[i] = name_list[i].strip(' \n')

    weighted_acts = { }
    for key in range(num_of_acts):
        for value in act_list:
            weighted_acts[key] = value
            act_list.remove(value)
            break
    weighted_acts.popitem()

    chosen_weights = [ ]
    for name in name_list:
        weights_by_name = [ ]
        for value in weighted_acts.values():
            if name in value:
                weights_by_name.append(list(weighted_acts.keys())[list(weighted_acts.values()).index(value)])
        if len(weights_by_name) > 1:
            chosen_weights.append(max(weights_by_name))
        elif len(weights_by_name) == 1:
            chosen_weights.append(weights_by_name[0])

    chosen_acts = []
    for key, value in weighted_acts.items():
        for num in chosen_weights:
            if key == num:
                chosen_acts.append(value)
            

    for key in name_list:
        for value in chosen_acts:
            final_dict[key] = value
            chosen_acts.remove(value)
            break
    
    return(final_dict)

# alpha_list = [dict() for x in range(26)] # 26 letters there are in english aplhabet
name_act_dict = { }
name_list = [ ]
act_list = [ ]

def parse_txt(path: str):
    # removes first 17 lines
    with open(path, 'r+') as f:
        lines = f.readlines()
        f.seek(0) # starts read from the first bite of the file
        f.truncate()
        f.writelines(lines[16:]) # deletes lines (rewrites to empty)
                                 # from the 1st to the 17th
    f.close()                         

    # removes all blank lines
    file_parsed = path[:-4] + '_p.txt'
    with open(path, 'r+') as f, open(file_parsed, 'w') as fp:
        for line in f:
            # if not line.isspace():
            if line.strip():
                fp.write(line)
    f.close()
    os.remove(path)
    os.rename(path[:-4] + '_p.txt', path)

    # parses txt
    with open(path, 'r+') as fp:
        prev_line = ''        
        for line in fp:
            for_prev_line = line
            if (line[:5] == '## **'):
                line = line[5:]
                if (line[-3:] == '** '):
                    line = line.replace('** ', '')
                    name_list.append(line)
                else:
                    line = line.replace('**', '')
                    name_list.append(line)

            elif (line[:4] == '# **'):
                line = line[4:]
                if (line[-3:] == '** '):
                    line = line.replace('** ', '')
                    name_list.append(line)
                else:
                    line = line.replace('**', '')
                    name_list.append(line)

            if (prev_line[:1] == '['):
                index = prev_line.index('] ')
                prev_line = prev_line[index+2:]

                act_list.append(prev_line)

            prev_line = for_prev_line

    f.close()

    act_list.append('Тайваньский производитель компьютерной техники' +
                        'Acer временно прекращает свою деятельность на ' +
                        'территории РФ из-за ситуации вокруг Украины — заявление')

    for item in name_list:
        item = item.strip(' \n')
        if '*' in item:
            item = item.replace('* ', '')
        else:
            item = item.replace(' ', '')

str_to_txt(get_str('https://raw.githubusercontent.com/daniilak/left-russia/main/README.md')) # arrange data from url to .txt file
parse_txt('bbbreaking.txt') # nests name_list and act_list

name_act_dict = remove_dublicates(name_list, act_list)

final_dict = {'Name': name_act_dict.keys(),
            'Action': name_act_dict.values()}

df = pd.DataFrame.from_dict(name_act_dict, orient='index')

df.to_csv('bbbreaking.csv')

from pprint import pprint
import re
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

header = contacts_list[0]
contacts_list_clean = [header]

for item in contacts_list[1:]:
    if item[0] != '' and item[1] != '' and item[2] != '':
        contacts_list_clean.append(item)
    else:
        full_name = ' '.join(item[0:3]).strip()
        other_item = item[3:]

        full_name_divided = re.split(r'\s+', full_name)

        if len(full_name_divided) == 3:
            pass
        else:
            full_name_divided.append('')

        full_raw = full_name_divided + other_item

        contacts_list_clean.append(full_raw)


for item in contacts_list_clean:
    phone_number = '(\+7|8)\s*\(?(\d{3})\)?\s*\-*(\d{3})-*(\d{2})-*(\d{2})\s*\(?(доб)?(\.)?\s*(\d*)\)?'
    find_number = re.findall(phone_number, item[5])
    text2 = re.sub(phone_number, r'+7(\2)\3-\4-\5 \6\7\8', item[5])
    item[5] = text2

contacts_list_clean_search = contacts_list_clean.copy()


contacts_list_clean_search[0].append('search_name_field')
pprint(contacts_list_clean_search)
i = 1
for item in contacts_list_clean_search[i:]:
    search_name = ' '.join(item[0:3]).strip()
    contacts_list_clean_search[i].append(search_name)
    i += 1


contacts_list_clean_no_dub = [header]

j = 0
for item in contacts_list_clean_search[1:]:
    j += 1
    k = 0
    for another_item in contacts_list_clean_no_dub:
        if contacts_list_clean_search[j][-1] not in contacts_list_clean_no_dub[k][-1]:
            k += 1
            if k == len(contacts_list_clean_no_dub):
                contacts_list_clean_no_dub.append(item)
                break
        else:
            for index, yet_another_item in enumerate(another_item[0:7]):
                if yet_another_item == '' and contacts_list_clean_search[j][index] != '':
                    another_item[index] = contacts_list_clean_search[j][index]
            break

for item in contacts_list_clean_no_dub:
    del item[7]

pprint(contacts_list_clean_no_dub)

with open('clean_contact_list.csv', 'w') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list_clean_no_dub)

import os, sys
from shutil import copyfile


def get_entry_count():
    curr = 0
    for filename in os.listdir('daily/templates/daily/'):
        if 'entry' in filename:
            temp = filename.split('_')[1].split('.')[0]
            if int(temp) > curr:
                curr = int(temp)
    return curr

def modify_urls_file(curr):
    new_content = ''
    new_line = f"path('entry_{curr+1}', views.entry_{curr+1}, name='entry_{curr+1}')"
    with open('daily/urls.py','r') as f:
        for line in f.readlines():
            if f'entry_{curr}' in line:
                line = line.rstrip('\n')
                line += f',\n\t{new_line}\n'
            new_content += line
    with open('daily/urls.py','w') as f:
        f.write(new_content)

def modify_views_file(curr):
    new_url = f'\'daily/entry_{curr+1}.html\''
    entry_temp = "{'entry':entry}"
    with open('daily/views.py','a') as f:
        f.write(f"\ndef entry_{curr+1}(request):\n")
        f.write(f"\tentry = Journal.objects.get(pk={curr+1})\n")
        f.write(f"\treturn render(request, {new_url}, {entry_temp})\n")

def add_entry():
    curr_num_entries = get_entry_count()
    modify_urls_file(curr_num_entries)
    modify_views_file(curr_num_entries)
    copyfile(f'daily/templates/daily/entry_{curr_num_entries}.html',f'daily/templates/daily/entry_{curr_num_entries+1}.html')
    print(f'added entry {curr_num_entries+1}')
    print(f'modify entry_{curr_num_entries+1}')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('missing argument.\ne.g. add')
        exit(1)

    if sys.argv[1] == 'add':
        add_entry()
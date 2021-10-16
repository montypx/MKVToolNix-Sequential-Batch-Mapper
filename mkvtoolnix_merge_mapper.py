# first python project in ages so might be a bit bad
import json
import os
from os.path import exists
import subprocess

mkv_merge_path = ""
# remember double backslashes i.e C:\\Users\\something\\...
options_filename = 'options.json'
ep_var_name = 'EPNUM'
out_folder = 'mkvmerge_out'

if not mkv_merge_path:
    print('read the readme lol')
    input('<press enter>')
    quit()

if not exists(mkv_merge_path):
    print('mkvmerge not there pal')
    input('<press enter>')
    quit()

if not exists(options_filename):
    print('no options file innit')
    input('<press enter>')
    quit()

print('Start Episode:')
start_episode = input()

print('End Episode:')
end_episode = input()

with open(options_filename) as json_file:
    options_data = json.load(json_file)

if not os.path.isdir(out_folder):
        os.mkdir(out_folder)

episode_num = int(start_episode)

while episode_num < int(end_episode)+1:
    options_data_temp = []
    options_data_temp += options_data

    if episode_num < 10:
        episode_string = '0' + str(episode_num)
    else:
        episode_string = str(episode_num)
    
    for i, v in enumerate(options_data_temp):
        if v.find(ep_var_name):
            options_data_temp[i] = options_data_temp[i].replace(ep_var_name, episode_string, 1)
        if v == '--output':
            full_path = options_data_temp[i + 1]
            pos = options_data_temp[i + 1].rindex("\\") + 1
            options_data_temp[i + 1] = full_path[:pos] + out_folder + "\\" + full_path[pos:]

    call_arguments = [mkv_merge_path] + options_data_temp 

    print('Starting Episode (' + str(episode_num) + '/' + str(end_episode) + ') ---------------')
    subprocess.call(call_arguments)
    print('Finished Processing ----------------')
    episode_num += 1

print('Done :)')
input('<press enter>')
quit()

import os
import yaml
import re
import  json
import re as regex
from collections import OrderedDict

def read_dir():
    pathDir = "D:\codes\yamls"
    obj = os.scandir(pathDir)
    # print("Files and Directories in '% s':" % pathDir)
    files = []
    for entry in obj:
        if entry.is_dir() or entry.is_file():
            #print(entry.name)
            files.append(entry.name)
    return files

def group_list(lst):
    res = [(el, lst.count(el)) for el in lst]
    return dict(OrderedDict(res).items())

def write_to_json(list_collection, filename):
    os.chdir("D:\\codes")
    with open(filename, "w") as outfile:
        json.dump(list_collection, outfile)

def parseYaml(currdir, filename):
    os.chdir(currdir)
    with open(filename) as fd:
        my_data = yaml.load(fd, Loader=yaml.FullLoader)
        #print(my_data.keys())
        allpaths = my_data["paths"]
        endpoints = []
        for k, v in allpaths.items():
            endpoints.append(k)
    return endpoints

def mergeDictionary(dict_1, dict_2):
   dict_3 = {**dict_1, **dict_2}
   for key, value in dict_3.items():
       if key in dict_1 and key in dict_2:
               dict_3[key] = [value , dict_1[key]]
   return dict_3

def process_resources(yaml_specs):

    for feature in yaml_specs:
        # json_dict[feature]= {}
        listendpoints = parseYaml("D:\\codes\\yamls", feature)
        #apiendpoints.extend(listendpoints)
        #print(apiendpoints)
        resources = []
        start = feature.index('-')
        end = feature.index('.', start + 1)
        dict_key = feature[start + 1:end]
        #print(dict_key)
        for res in listendpoints:
            #print("parsing endpoints...")
            #print(res)
            text = res.split('/')
            if len(text) > 5:
                # print(text[5])
                resources.append(text[5])
                if text[5] not in ep_dict:
                    ep_dict[text[5]] = list()
                    ep_dict[text[5]].append(res)
                else:
                    ep_dict[text[5]].append(res)
        json_dict[dict_key] = group_list(resources)
        #print(ep_dict)
    return(resources)

yamlFileList = read_dir()
#print(yamlFileList)
json_dict = {}
ep_dict = {}
#write_to_json(group_list(process_resources(yamlFileList)))
apiendpoints = []
process_resources(yamlFileList)
write_to_json(json_dict,"resources.json")
write_to_json(ep_dict,"endpoints.json")

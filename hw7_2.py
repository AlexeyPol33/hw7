
def merge_files(files_list):

    files_dict = []
    for file_name in files_list:
        with open(file_name,encoding= 'utf-8') as f:
            files_dict.append({file_name:f.readlines()})

    sorted_list = []
    while len(files_dict) > 0:
        low_rate = files_dict.pop(0)
        for i in range (len(files_dict)):
            if  (len(low_rate[str(*low_rate.keys())])) > len(files_dict[i][str(*files_dict[i].keys())]):
                files_dict.append(low_rate)
                low_rate = files_dict.pop(i)
        sorted_list.append(low_rate)

    files_dict = sorted_list
    with open('merged','w',encoding= 'utf-8') as f:
        for i in files_dict:
            f.write(*i.keys())
            f.write('\n')
            f.write(str(len(i[str(*i.keys())])))
            f.write('\n')
            for j in i[str(*i.keys())]:
                f.write(j)
            f.write('\n')

    return sorted_list

print (merge_files(['1.txt','2.txt','3.txt']))
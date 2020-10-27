# port/ip
# import matplotlib
#
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


import pandas as pd
import numpy as np
from collections import defaultdict
from collections import Counter
from collections import OrderedDict
import ipaddress


# Field -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport -e frame.len -e ip.proto -e tcp.flags.syn
# path = '/content/drive/My Drive/Out_going_Duong/outGo368_00000_20200925122100.csv'
def create_2D_array_data(path):
    numpy_data = (pd.read_csv(path)).to_numpy()
    transpose_data = np.transpose(numpy_data)

    ip_dst = list(transpose_data[1])
    len = list(transpose_data[6])
    test_array = np.transpose([ip_dst, len])
    list_arr = test_array.tolist()
    # test_array.astype(int)
    # print(list_arr)
    return list_arr


def create_dictionary_ip_port(list_arr):
    d = defaultdict(list)
    print(d)
    for year, month in list_arr:
        d[year].append(month)
    d.pop('nan')
    dic = defaultdict(list)
    for key, values in d.items():
        key = int(ipaddress.ip_address(key)) / pow(10, 32)
        dic[key].append(len(list(OrderedDict.fromkeys(values))) / 150)
    print(dic)
    return dic


def create_dictionary_ip_bytes(list_arr):
    d = defaultdict(list)
    print(d)
    for year, month in list_arr:
        d[year].append(int(month))
    d.pop('nan')
    dic = defaultdict(list)
    for key, values in d.items():
        key = int(ipaddress.ip_address(key)) / pow(10, 32)
        dic[key].append(sum(values) / 120)
    # print(dic)
    return dic


path = '/home/admin123/Documents/Hust_Data/file_355/csv_data/OutGoing355/outGo355_00000_20200924215500.csv'

list_data = create_2D_array_data(path)
dic_data = create_dictionary_ip_bytes(list_data)
print(sorted((dic_data.items()), key=lambda x: x[1], reverse=True))
print(dic_data.keys())
plt.scatter(dic_data.keys(), dic_data.values())  # Matplotlib
plt.xlabel("IP")
plt.ylabel("Bytes/s")
plt.title(path + " " + str(len(list_data)) + " IP")
print("Done1")
plt.show()
print("Done2")
plt.savefig('test_fig1.png')

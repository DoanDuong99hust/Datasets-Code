# port/ip
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import defaultdict
from collections import Counter
from collections import OrderedDict
import ipaddress

def create_2D_array_data(path):
  numpy_data = (pd.read_csv(path)).to_numpy()
  transpose_data = np.transpose(numpy_data)

  ip_src = list(transpose_data[0])
  upd_src_port = list(transpose_data[4])
  test_array = np.transpose([ip_src, upd_src_port])
  list_arr = test_array.tolist()
  # test_array.astype(int)
  print(list_arr)
  return list_arr

def create_dictionary(list_arr) :
  d = defaultdict(list)
  print(d)
  for year, month in list_arr:
      d[year].append(month)
  dic = defaultdict(list)
  for key,values in d.items():
    if (key == 'nan') :
      key = 0
      key = int(ipaddress.ip_address(key))/pow(10,32)
      dic[key].append(len(list(OrderedDict.fromkeys(values)))/120)
    else:
      key = int(ipaddress.ip_address(key))/pow(10,32)
      dic[key].append(len(list(OrderedDict.fromkeys(values)))/120)
  print(dic)
  return dic

path = '/home/doanduong/DoanDuong/csv_data/outGoingoutGo368_00000_20200925122100.csv'

list_data = create_2D_array_data(path)
dic_data = create_dictionary(list_data)
# print(tcp_srcport_total)
plt.scatter(dic_data.keys(),dic_data.values())  # Matplotlib
plt.xlabel("IP")
plt.ylabel("Ports/s")
plt.title(path + " " + str(len(list_data)) + " IP")
plt.show()
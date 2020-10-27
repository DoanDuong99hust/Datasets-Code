# port/ip
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import defaultdict
from collections import Counter
from collections import OrderedDict
import ipaddress

16909060
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
  print(list_arr)
  return list_arr

def create_dictionary_ip_port(list_arr) :
  d = defaultdict(list)
  print(d)
  for year, month in list_arr:
      d[year].append(month)
  d.pop('nan')
  dic = defaultdict(list)
  for key,values in d.items():
      key = int(ipaddress.ip_address(key))/pow(10,32)
      dic[key].append(len(list(OrderedDict.fromkeys(values)))/150)
  print(dic)
  return dic

def create_dictionary_ip_bytes(list_arr) :
  d = defaultdict(list)
  print(d)
  for year, month in list_arr:
      d[year].append(int(month))
  d.pop('nan')
  print(d)
  dic = defaultdict(list)
  for key, values in d.items():
      key = int(ipaddress.ip_address(key)) / pow(10, 32)
      dic[key].append(sum(values))
  # print(dic.keys())dic
  return dic

# path = '/content/drive/My Drive/Out_going_Duong/CsvData/outGo368_00001_20200925122310.csv'
path = '/home/doanduong/DoanDuong/csv_data/testfile.csv'
list_data = create_2D_array_data(path)
dic_data = create_dictionary_ip_bytes(list_data)
print(sorted((dic_data.items()),key=lambda x: x[1], reverse=True))
# plt.scatter(dic_data.keys(),dic_data.values())  # Matplotlib
# plt.xlabel("IP")
# plt.ylabel("Bytes/s")
# plt.title(path + " " + str(len(list_data)) + " IP")
# plt.show()


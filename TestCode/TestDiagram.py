# port/ip
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import defaultdict
from collections import Counter
from collections import OrderedDict
import ipaddress
import os, sys

# Field -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e udp.srcport -e udp.dstport -e frame.len -e ip.proto -e tcp.flags.syn
# path = '/content/drive/My Drive/Out_going_Duong/outGo368_00000_20200925122100.csv'
class CParserError(object):
    pass


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

def create_3D_array_data(path):
  numpy_data = (pd.read_csv(path)).to_numpy()
  transpose_data = np.transpose(numpy_data)

  ip_dst = list(transpose_data[1])
  len = list(transpose_data[6])
  time = list(transpose_data[0])

  test_array = np.transpose([ip_dst, len, time])
  # print(test_array)
  return test_array

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
  for key, values in list_arr:
      d[key].append(int(values))
  d.pop('nan')
  dic = defaultdict(list)
  for key,values in d.items():
      key = int(ipaddress.ip_address(key))/pow(10,32)
      dic[key].append(sum(values)/120)
  # print(dic)
  return dic

def _2D_plot(item1,item2,filename):
  plt.scatter(item1,item2)  # Matplotlib
  plt.xlabel("IP")
  plt.ylabel("Bytes/s")
  plt.title(path + " " + str(len(filename)) + " IP")
  plt.show()

def _3D_plot(item1,item2,item3) :
  fig = plt.figure()
  ax1 = fig.add_subplot(111, projection='3d')
  ax1.scatter(item1, item2, item3, zdir='z', s=10, c=None, depthshade=True)
  ax1.set_xlabel('Bytes/s')
  ax1.set_ylabel('Ports/s')
  ax1.set_zlabel('IP')
  plt.title()
  plt.show()

path = "/home/admin123/Documents/Hust_Data/file_356/csv_data/inComing356/"
# path='/content/drive/My Drive/Out_going_Duong/testfile.csv'
# path = '/content/drive/My Drive/Out_going_Duong/outGoingTest.csv'
lists = os.listdir(path)
for file in lists:
    list_data = create_2D_array_data(path+file)
    dic_data = create_dictionary_ip_bytes(list_data)
    _2D_plot(dic_data.keys(),dic_data.values(),path+file)

    sort_dict = sorted((dic_data.items()),key=lambda x: x[1], reverse=True)
    print(sort_dict[1])

    for i in range(5):
      print(ipaddress.IPv4Address(int(sort_dict[i][0]*pow(10,32))), sort_dict[i][1])
# list_data = create_2D_array_data(path)
# dic_data = create_dictionary_ip_bytes(list_data)
# print(len(dic_data.keys()))
# _2D_plot(dic_data.keys(),dic_data.values(),dic_data)
#
# sort_dict = sorted((dic_data.items()),key=lambda x: x[1], reverse=True)
# print(sort_dict[1])
#
# for i in range(5):
#   print(ipaddress.IPv4Address(int(sort_dict[i][0]*pow(10,32))), sort_dict[i][1])


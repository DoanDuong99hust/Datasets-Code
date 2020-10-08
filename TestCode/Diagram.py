# port/ip
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# path = '/content/drive/My Drive/Out_going_Duong/outGo368_00000_20200925122100.csv'
path = '/content/drive/My Drive/Out_going_Duong/testfile.csv'
numpy_data = (pd.read_csv(path)).to_numpy()
transpose_data = np.transpose(numpy_data)

ip_src = list(transpose_data[0])
upd_src_port = list(transpose_data[4])
test_array = np.transpose([ip_src, upd_src_port])
# test_array.astype(int)
print(type(upd_src_port))

dictation = dict(zip(ip_src,upd_src_prot))
print(type(dictation.keys()))
# ip_src_filter = np.unique(ip_src,axis=0)

# for i,j in dictation.items() :
#   print(i,j)
# print(ip_src_filter)
tcp_srcport = transpose_data[2]

tcp_srcport_total = np.ones(len(dictation))

for i in range(len(dictation)) :
  for j in test_array:
    if j[0] == dictation.keys():
      # tcp_srcport_total[i] = tcp_srcport_total[i]+1
      print(j[0], dictation.keys(), j[1], dictation.values())

# print(tcp_srcport_total)
# plt.scatter(ip_src_filter,tcp_srcport_total)  # Matplotlib
# plt.xlabel("IP")
# plt.ylabel("Ports/s")
# plt.title(path + " " + str(len(ip_src_filter)) + " IP")
# plt.show()
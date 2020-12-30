import pandas as pd
import matplotlib.pyplot as plt
import time as tm  # time counter
import datetime as dt
import numpy as np
import csv
import ipaddress
from collections import Counter
from collections import defaultdict
import collections
from mpl_toolkits.mplot3d import Axes3D  # 3d plotting
import itertools as iter_tool

'''Labeled data filtering '''


# l1: label
# l2: Source IP
# l3: Fw packets/s
# t4: Timestamp
def two_lists_to_np_array(x, y):
    new_array = np.array([x, y])
    new_array = np.transpose(a)
    return new_array


def Anormally_and_benign_filtering(l1, l2, l3, l4):
    global benign_list, abnormally_list
    for i, j, k, t in zip(l1, l2, l3, l4):
        if i == 'Syn':
            abnormally_list = np.vstack([abnormally_list, [j, k, t]])
        else:
            benign_list = np.vstack([benign_list, [j, k, t]])
    benign_list = np.delete(benign_list, 0, axis=0)  # axis = 0, performing with rows, axis=1, performing with columns
    abnormally_list = np.delete(abnormally_list, 0, axis=0)
    # benign_list = np.transpose(benign_list, axes=None)
    # abnormally_list = np.transpose(abnormally_list, axes=None)


'''3D plotting'''


def three_dimention_plot(a1, b1, c1, a2, b2, c2):
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    ax1.scatter(a1, b1, c1, zdir='z', s=10, c='blue', depthshade=True)
    ax1.scatter(a2, b2, c2, zdir='z', s=10, c='red', depthshade=True)
    ax1.set_xlabel('IP')
    ax1.set_ylabel('Pkts/s')
    ax1.set_zlabel('Timestamp')
    plt.title('Traffic Diagram')
    plt.show()


def Scatter_figure(a1, b1, a2, b2):
    # MatplotLib
    plt.scatter(a1, b1, color='blue', s=10)  # Matplotlib
    plt.scatter(a2, b2, color='red', s=10)  # Matplotlib
    plt.xlabel("IP")
    plt.ylabel("Packets/s")
    # plt.title(name)
    plt.show()


def Scatter_figure_2_lists(a1, b1):
    # MatplotLib
    plt.scatter(a1, b1, color='blue', s=10)  # Matplotlib
    # plt.scatter(a2, b2, color ='red',s=10)  # Matplotlib
    plt.xlabel("IP")
    plt.ylabel("Packets/s")
    plt.title('IP: ' + str(len(a1)))
    plt.savefig("/home/admin123/Documents/Hust_Data/file_355/csv_data/inComing355/mygraph1.png")
    plt.show()


'''Label check'''


def Label_checking():
    print((Counter(Label)))
    print(Counter((Counter(Label))).keys())


'''CSV Opening'''


def Open_csv_file(filename):
    with open(filename, mode='r') as f:
        loaded_file = np.loadtxt(f, unpack=True, skiprows=0)
    return loaded_file


'''CSV Generator'''


def Gen_csv_file(array1, xxx_File):
    # with open('/content/drive/Shared drives/Dataset_trash_storage/Lần sau up lên đây này anh Hiếu ạ =))/OutGo'+str(xxx_File)+'_pkts.csv','w') as f:
    with open(
            '/content/drive/Shared drives/Dataset_trash_storage/Lần sau up lên đây này anh Hiếu ạ =))/InCome' + str(
                    xxx_File) + '_pkts.csv', 'w') as f:
        np.savetxt(f, array1, delimiter=',', fmt='%d')


'''CSV Appanding'''


def Append_csv_file(array1, xxx_File):
    # with open('/content/drive/Shared drives/Dataset_trash_storage/Lần sau up lên đây này anh Hiếu ạ =))/OutGo'+str(xxx_File)+'_pkts.csv','a') as f:
    with open(
            '/content/drive/Shared drives/Dataset_trash_storage/Lần sau up lên đây này anh Hiếu ạ =))/InCome' + str(
                    xxx_File) + '_pkts.csv', 'a') as f:
        np.savetxt(f, array1, delimiter=',', fmt='%d')


'''IP address -> Decimal Converter '''


def Ip_address_converter(a):
    # l1=[]
    # l2=list(a)
    for index in range(len(list(a))):
        # l1[index]=int(ipaddress.ip_address(l2[index]))
        a[index] = int(ipaddress.ip_address(a[index]))
    return a


'''Time -> integer number Converter'''


def Time_to_int_number(time_stamp):
    s = pd.Series(time_stamp)
    new_time_stamp = pd.to_datetime(s).dt.round('H').dt.strftime('%m%d%H')
    new_time_stamp = new_time_stamp.to_numpy()
    new_time_stamp = new_time_stamp.astype(np.int)
    '''Optional section'''
    # new_time_stamp =new_time_stamp-np.amin(new_time_stamp)
    '''Upper part is optional'''
    return new_time_stamp


'''Create dictionary from 2 list --- Packet length '''


def Dict_from_2_list(a, b):
    temp = defaultdict(set)
    for delvt, pin in zip(a, b):
        temp[delvt].add(pin)
    # temp = collections.OrderedDict(sorted(temp.items()))        # SORT kEY FROM LOW TO HIGH
    return temp


'''Create dictionary from 2 list and cal total value --- Packet length'''


def dict_from_2_list_and_cal_total_in_value(a, b):
    temp = defaultdict(set)
    for delvt, pin in zip(a, b):
        temp[delvt].add(pin)
    temp = {k: sum(v) for k, v in temp.items()}  # Calculating the sum of all value in each key.
    temp = collections.OrderedDict(sorted(temp.items()))  # SORT kEY FROM LOW TO HIGH
    return temp


# fields=['Source IP', 'Source Port']
'''Packet Counter --- The number of packet '''


def pack_count(numpy_array):
    unique, counts = np.unique(numpy_array, return_counts=True)
    unique_counts = np.column_stack([unique, counts])
    return unique_counts


'''Pandas CSV Reading '''


def Reading_pandas(file_name):
    chunk_size = 1000
    data = pd.read_csv(file_name, chunksize=chunk_size, skipinitialspace=None, usecols=None, index_col=None)
    pd.set_option('display.expand_frame_repr',
                  False)  # expanding the full output screen mode in order to display all columns
    pd.options.display.max_columns = None
    data = pd.concat(data)
    print(data)
    return data


index_max = 4
Xxx_index_starting = 368
Index_file_starting = 0
file_xxx_max = 371
print("...Processing...")
file_name = '/home/admin123/DiepSon/inCom355_00000_20200924215500.csv'
'''Pandas read_csv'''
data = Reading_pandas(file_name)
'''Pandas read_csv done'''
# DestIP=data['ip.dst'].to_numpy()
SrcIP = data['ip.src'].to_numpy()
'''Eliminate NaN, Null values'''
# DestIP = DestIP[~pd.isnull(DestIP)]
SrcIP = SrcIP[~pd.isnull(SrcIP)]
print("Len SrcIP: ", len(SrcIP))
# print("Len DestIP: ",len(DestIP))
SrcIP_Dec = Ip_address_converter(SrcIP)
'''Packet counter'''
IP_Pkts = pack_count(SrcIP_Dec)
# IP_Pkts= pack_count(DestIP_deci)
'''Convert 2 np array to 1d numpy array: n rows, 2 columns'''
final_dict = dict(zip(IP_Pkts[:, 0], IP_Pkts[:, 1]))
final_dict = sorted(final_dict.items(), key=lambda x: x[1], reverse=True)  # Sort by value Decending
'''5 Highest traffic IP (Decending Order):'''
print(final_dict)
Scatter_figure_2_lists(IP_Pkts[:, 0], IP_Pkts[:, 1])
print("DONE")
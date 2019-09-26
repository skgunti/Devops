#!/usr/bin/python
import json
import os
import sys
import re
import pprint
##########################################################
def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError, e:
    return False
  return True
###########################################################
def my_function(asup,serial,file_path,w_file):
  #print asup,serial,file_path
  j_data =[]
  with open(file_path) as f:
    for line in f:
        try:
            j_data.append(json.loads(line))
        except ValueError:
            pass  # do nothing!
        #j_data.append(json.loads(line))
    for data in j_data:
        print_data(asup,serial,data,w_file)


####################################
def print_data(asup,serial,data,w_file):
    new_data = data['timestamps']
    new_dict = {'instance_name': 0, 'nfs_read_ops' : 0, 'nfs_write_ops' : 0,'nfs_other_ops' : 0,'cifs_read_ops' : 0,'cifs_write_ops' : 0,'cifs_other_ops' : 0
,'san_read_ops' : 0,'san_write_ops': 0,'san_other_ops' : 0,'iscsi_read_ops' : 0,'iscsi_write_ops' : 0,'iscsi_other_ops' : 0,'fcp_read_ops'  : 0,'fcp_write_op
s' : 0,'fcp_other_ops' : 0}
    for i in new_data:
      my_data = i['instances']
      for j in my_data:
        r_data = j['counters']
        #print(json.dumps(r_data, indent=4, sort_keys=True))
        for r in r_data:
          #print r
          #print(json.dumps(r, indent=4, sort_keys=True))
          if (r['counter_name'] in  'instance_name'):
                new_dict['instance_name'] = r['value']
          elif (r['counter_name'] in  'nfs_read_ops'):
                new_dict['nfs_read_ops'] = r['value']
          elif (r['counter_name'] in  'nfs_write_ops'):
                new_dict['nfs_write_ops'] = r['value']
          elif (r['counter_name'] in  'nfs_other_ops'):
                new_dict['nfs_other_ops'] = r['value']
          elif (r['counter_name'] in  'cifs_read_ops'):
                new_dict['cifs_read_ops'] = r['value']
          elif (r['counter_name'] in  'cifs_write_ops'):
                new_dict['cifs_write_ops'] = r['value']
          elif (r['counter_name'] in  'cifs_other_ops'):
                new_dict['cifs_other_ops'] = r['value']
          elif (r['counter_name'] in  'san_read_ops'):
                new_dict['san_read_ops'] = r['value']
          elif (r['counter_name'] in  'san_write_ops'):
                new_dict['san_write_ops'] = r['value']
          elif (r['counter_name'] in  'san_other_ops'):
                new_dict['san_other_ops'] = r['value']
          elif (r['counter_name'] in  'iscsi_read_ops'):
                new_dict['iscsi_read_ops'] = r['value']
          elif (r['counter_name'] in  'iscsi_write_ops'):
                new_dict['iscsi_write_ops'] = r['value']
          elif (r['counter_name'] in  'iscsi_other_ops'):
                new_dict['iscsi_other_ops'] = r['value']
          elif (r['counter_name'] in  'fcp_read_ops'):
                new_dict['fcp_read_ops'] = r['value']
          elif (r['counter_name'] in  'fcp_write_ops'):
                new_dict['fcp_write_ops'] = r['value']
          elif (r['counter_name'] in  'fcp_other_ops'):
                new_dict['fcp_other_ops'] = r['value']

        #print str(asup)+'~'+str(serial)+'~'+new_dict['instance_name']+'~'+str(new_dict['nfs_read_ops'])+'~'+str(new_dict['nfs_write_ops'])+'~'+str(new_dict[
'nfs_other_ops'])+'~'+str(new_dict['cifs_read_ops'])+'~'+str(new_dict['cifs_write_ops'])+'~'+str(new_dict['cifs_other_ops'])+'~'+str(new_dict['san_read_ops']
)+'~'+str(new_dict['san_write_ops'])+'~'+str(new_dict['san_other_ops'])+'~'+str(new_dict['iscsi_read_ops'])+'~'+str(new_dict['iscsi_write_ops'])+'~'+str(new_
dict['iscsi_other_ops'])+'~'+str(new_dict['fcp_read_ops'])+'~'+str(new_dict['fcp_write_ops'])+'~'+str(new_dict['fcp_other_ops'])
        if (new_dict['instance_name'] != 0) :
           #w_file.write(str(asup)+'~'+str(serial)+'~'+new_dict['instance_name']+'~'+str(new_dict['nfs_read_ops'])+'~'+str(new_dict['nfs_write_ops'])+'~'+str
(new_dict['nfs_other_ops'])+'~'+str(new_dict['cifs_read_ops'])+'~'+str(new_dict['cifs_write_ops'])+'~'+str(new_dict['cifs_other_ops'])+'~'+str(new_dict['san_
read_ops'])+'~'+str(new_dict['san_write_ops'])+'~'+str(new_dict['san_other_ops'])+'~'+str(new_dict['iscsi_read_ops'])+'~'+str(new_dict['iscsi_write_ops'])+'~
'+str(new_dict['iscsi_other_ops'])+'~'+str(new_dict['fcp_read_ops'])+'~'+str(new_dict['fcp_write_ops'])+'~'+str(new_dict['fcp_other_ops'])+'\n')
           w_file.write(str(asup)+'~'+str(serial)+'~'+new_dict['instance_name']+'~'+str(new_dict['nfs_read_ops'])+'~'+str(new_dict['nfs_write_ops'])+'~'+str(
new_dict['nfs_other_ops'])+'~'+str(new_dict['cifs_read_ops'])+'~'+str(new_dict['cifs_write_ops'])+'~'+str(new_dict['cifs_other_ops'])+'~'+str(new_dict['iscsi
_read_ops'])+'~'+str(new_dict['iscsi_write_ops'])+'~'+str(new_dict['iscsi_other_ops'])+'~'+str(new_dict['fcp_read_ops'])+'~'+str(new_dict['fcp_write_ops'])+'
~'+str(new_dict['fcp_other_ops'])+'~'+str(new_dict['san_read_ops'])+'~'+str(new_dict['san_write_ops'])+'~'+str(new_dict['san_other_ops'])+'\n')
        #pprint(new_dict)
        new_dict = {'instance_name': 0, 'nfs_read_ops' : 0, 'nfs_write_ops' : 0,'nfs_other_ops' : 0,'cifs_read_ops' : 0,'cifs_write_ops' : 0,'cifs_other_ops'
 : 0,'san_read_ops' : 0,'san_write_ops': 0,'san_other_ops' : 0,'iscsi_read_ops' : 0,'iscsi_write_ops' : 0,'iscsi_other_ops' : 0,'fcp_read_ops'  : 0,'fcp_writ
e_ops' : 0,'fcp_other_ops' : 0}

######################################################
#inputfile = ('vserver_'+(sys.argv[1]))
#inputfile = ('vserver_'+(sys.argv[1]))
#print inputfile
# Open the file with read only permit
#w_file = open("%s.txt" %inputfile, "w+")
w_file = open("/u/nbsvc/Data/PARSE/hive/temp/Vserver_Vol_Json_Out.txt", "w+")
head = 'asup_id~SERIAL~ENTITY_KEY~NFS_READ_OPS~NFS_WRITE_OPS~NFS_OTHER_OPS~CIFS_READ_OPS~CIFS_WRITE_OPS~CIFS_OTHER_OPS~ISCSI_READ_OPS~ISCSI_WRITE_OPS~ISCSI_O
THER_OPS~FCP_READ_OPS~FCP_WRITE_OPS~FCP_OTHER_OPS~SAN_READ_OPS~SAN_WRITE_OPS~SAN_OTHER_OPS\n'
w_file.write(head)
#w_file.write(asup_id+'~'+SERIAL+'~'+ENTITY_KEY+'~'+NFS_READ_OPS+'~'+NFS_WRITE_OPS+'~'+NFS_OTHER_OPS+'~'+CIFS_READ_OPS+'~'+CIFS_WRITE_OPS+'~'+CIFS_OTHER_OPS+
'~'+ISCSI_READ_OPS+'~'+ISCSI_WRITE_OPS+'~'+ISCSI_OTHER_OPS+'~'+FCP_READ_OPS+'~'+FCP_WRITE_OPS+'~'+FCP_OTHER_OPS+'~'+SAN_READ_OPS+'~'+SAN_WRITE_OPS+'~'+SAN_OT
HER_OPS)
#w_file = open('textfile.txt','w+')
#f = open(sys.argv[1], 'r')
f = open('/u/nbsvc/Data/Output/Controller/Controller_attr_All_ASUPS_daily.txt', 'r')
#f = open('/u/nbsvc/Data/Output/Controller/controller_chunk_20190502.TXT', 'r')
#f = open('sample')
# use readline() to read the first line
line = f.readline()
# use the read line to read further.
# If the file is not empty keep reading one line
# at a time, till the file is empty
path1 ='/willows/sac/asup/grissom/asupdw/AsupFilePath5/'
path2 ='CM-STATS-EVENT-DATA-CATALOGUE/volume.json'
while line:
    # in python 2+
    # print line
    # in python 3 print is a builtin function, so
    if "WEEKLY" in line:
       my_list = line.split('~|~')
       #print my_list[0],my_list[2],my_list[8],my_list[11],my_list[12],my_list[-1]
       my_list[-1] = my_list[-1].rstrip()
       #print path1+str(my_list[0][0:8])+/+str(my_list[0][8:12])/my_list[0]/CM-STATS-EVENT-DATA-CATALOGUE/volume.json
       myfiel_path = path1+str(my_list[0][0:8])+'/'+str(my_list[0][8:12])+'/'+str(my_list[0])+'/'+path2
       exists = os.path.isfile(myfiel_path)
       if re.match(r'^9',my_list[8]) and exists:
          #print  myfiel_path
          #print my_list[0],my_list[2],my_list[8],my_list[11],my_list[12],my_list[-1]
          my_function(my_list[0],my_list[2],myfiel_path,w_file)
    # use realine() to read next line
    line = f.readline()
f.close()
w_file.close()
os.popen('cp /u/nbsvc/Data/PARSE/hive/temp/Vserver_Vol_Json_Out.txt /u/nbsvc/Data/PARSE/hive/7M2CMODE/cm/Vol_82/')

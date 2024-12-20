stn = {}
lines = [line.rstrip() for line in open('clim_ncep.csv')]
for line in lines:
 line = line.split(' ')
 if line[0][:2] == 'IN':
  ln = [x for x in line if x != '']
  ln_ = ln[0].split(',')
  stn[ln_[0]] = ln_[1:5]
import glob
count = 0
files = glob.glob('/home/dc/Downloads/ghcnd_gsn/ghcnd_gsn/IN*.dly')
for file in files:
 lines = [line.rstrip() for line in open(file)]
 for line in lines:
  line = line.split(' ')
  if line[0][-4:] == 'PRCP':
   ln = [x for x in line if x != '']
   keylist = stn.keys()
   sorted(keylist)
   if ln[0][:-10] in keylist:
    idx = ln[0][:-10]
    print(ln[0][11:17])# == '202412':
     #count+=1
     #print(idx,stn[idx],ln)
print(count)

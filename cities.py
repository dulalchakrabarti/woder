import glob
import pandas as pd
fl = open('dec_fc.csv','w+')
stn = {}
lines = [line.rstrip() for line in open('dist.csv')]
for line in lines:
 line = line.split(',')
 lat = int(float(line[4]))
 lon = int(float(line[5]))
 lalo = str(lat)+'_'+str(lon)
 if lalo not in stn.keys():
  stn[lalo] = [line[3]]
 else:
  stn[lalo].append(line[3])
files = glob.glob('srf/*.csv')
for file in files:
 txt_ = file[4:-4]
 txt = txt_.split('_')
 lat = int(float(txt[0]))
 lon = int(float(txt[1]))
 lalo = str(lat)+'_'+str(lon)
 if lalo in stn.keys():
  towns = stn[lalo]
  for town in towns:
   df = pd.read_csv('srf/'+txt_+'.csv')
   df_date = df['valid_time'].tolist()
   df_fct = df['tp_diff'].tolist()
   for date, rf in zip(df_date, df_fct):
    print(town,date,rf)
    fl.write(town+','+date+','+str(rf)+'\n')


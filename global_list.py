fl = open('clim_ncep.csv','w+')
lines = [line.rstrip() for line in open('ghcnd-stations.txt')]
for line in lines:
 line = line.split(' ')
 if line[0][:2] == 'IN':
  ln = [x for x in line if x != '']
  txt = ','.join(x for x in ln)
  fl.write(txt+'\n')


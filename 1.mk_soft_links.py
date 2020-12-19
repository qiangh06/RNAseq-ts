#pwd: /datalus/heqiang/millet/ts/snd_30/data
import os
inf = opne('keys.txt','r')

for line in inf:
    _line = line.rstrip().split('\t')
    name = _line[0]
    cmd1 = 'ln -s %s %s_R1.fq.gz'%(_line[1],name)
    cmd2 = 'ln -s %s %s_R2.fq.gz'%(_line[1].replace('R1','R2'),name)
    os.system(cmd1)
    os.system(cmd2)
inf.close()

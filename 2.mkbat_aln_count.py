import glob,os

ref = '/datalus/liujun/genomes/SetariaItalica/Yugu1/Sitalica_312_v2'
gtf = '/datalus/liujun/genomes/SetariaItalica/Yugu1/Sitalica_312_v2.2.gene.gtf'

files = glob.glob('/datalus/heqiang/millet/ts/snd_30/data/*_R1.fq.gz')

for f in files:
    sample = os.path.basename(f).split('_R1')[0]
    out = open(sample+'.bat','w')
    cmd1 = 'hisat2 -p 16 -x %s -1 %s -2 %s -S %s.sam'%(ref,f,f.replace('_R1','_R2'),sample)
    cmd2 = 'samtools sort -@ 16 -o %s_sorted.bam %s.sam'%(sample,sample)
    cmd3 = 'samtools view -q 30 -b %s_sorted.bam > %s_sorted.q30.bam'%(sample,sample)
    cmd4 = 'htseq-count -f bam -q -r pos -s no %s %s'%(f,gtf)
    out.write(cmd1+'\n'+cmd2+'\n'+cmd3+'\n'+cmd4)
    out.close()

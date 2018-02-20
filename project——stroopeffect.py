import pandas as pd
import numpy as np
data=pd.read_csv("/Users/daolinghuang/Documents/datascience/UdacityNano/DataAnalysis/Project1_stroopEffect/stroopdata.csv")
a=np.mean(data['Congruent'])
a
b=np.mean(data['Incongruent'])
c=np.median(data['Congruent'])
d=np.median(data['Incongruent'])
e=np.mode(data['Congruent'])
f=np.mode(data['Incongruent'])

g=np.range(data['Congruent'])
h=np.range(data['Incongruent'])
i=np.var(data['Congruent'])
j=np.var(data['Incongruent'])
k=np.std(data['Congruent'])
l=np.std(data['Incongruent'])
q75,q25=np.percentile(data['Congruent'],[75,25])
q2_75,q2_25=np.percentile(data['Incongruent'],[75,25])
iqr1=q75-q25
iqr2=q2_75-q2_25

print 'a=', a,'b=', b,'c=', c,'d=', d,'e=', e,'f=', f,'g=', g,'h=', h,'i=', i,'j=', j,'k=', k,'l=', l,'iqr1=', iqr1,'iqr2=', iqr2'a=', a,
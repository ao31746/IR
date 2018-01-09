import os
import sys
import unicodedata
from collections import defaultdict
import json
import codecs
import math
import numpy as np
path = rootpath + 'data/'

IDF = dict()
for word in DF:
    IDF[word] = math.log10(countdoc / float(DF[word])) 
        
sorted_idf = sorted(IDF.items())

for filename in os.listdir(path):
	tmp = defaultdict(float)
	new_path = rootpath+'tfidf/'+filename
	new_days = open(new_path,'w')

	with codecs.open(path+filename,'rU', encoding="utf-8-sig") as f:
		data = []
		for line in f:
			data.append(json.loads(line))
			table = {c: '' for c in range(sys.maxunicode)	
					if unicodedata.category(chr(c)).startswith('P')}
			try:
				result = data[0]['content'].translate(table)
			except KeyError as name:
				continue
			seg_list = jieba.cut(result)
			# print("|".join(seg_list))
			words_filtered = [word for word in seg_list if word not in stopwords and not word.isdigit() and len(word)>1]

			for wd in words_filtered:
				tmp[wd] +=1
			sp = sorted(tmp.items())
			unorm=[]
			for i in range(len(sp)):
				unorm.append(sp[i][1] * IDF[sp[i][0]])
				
			for i in range(len(sp)):
				ide = [x+1 for x, y in enumerate(sorted_idf) if y[0] == sp[i][0]]
				new_days.write(str(ide[0]))
				
				new_days.write(' ' + str(sp[i][1] * IDF[sp[i][0]] / np.linalg.norm(unorm))+'\n')
			new_days.close()
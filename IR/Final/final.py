# -*-coding: utf8 -*-
import jieba
rootpath = 'C:/Users/lckung/Desktop/IR/IR/Final/'
jieba.set_dictionary(rootpath + 'dict.txt.big')
jieba.load_userdict(rootpath + 'pptdict.txt')
import os
import re
import sys
import unicodedata
from collections import defaultdict
import json
import codecs
import math
import numpy as np
jieba.dt.cache_file = 'jieba.final.new'
path = rootpath + 'data/'
with open(rootpath + 'stopword.txt','r', encoding="utf-8") as f:
    stopwords = f.readlines()
stopwords = [i.rstrip() for i in stopwords]
DF = defaultdict(int)
doccounter = 0

data = []
countdoc = 0
for filename in os.listdir(path):
	print(path+filename)
	
	countdoc+=1
	# if countdoc ==3:
		# break
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
			with open(rootpath + 'tf/'+ filename, 'w', encoding="utf-8") as file:
				file.write("title: %s\n" %(data[0]['article_title']))
				file.write("count: %d\n" %(data[0]['message_conut']['all']))
				file.write("|".join(seg_list))
				file.close()
			# print("|".join(seg_list))
			words_filtered = [word for word in seg_list if word not in stopwords and not word.isdigit() and len(word)>1]

			for wd in set(words_filtered):
				DF[wd] +=1

s = [(k, DF[k]) for k in sorted(DF, key=DF.get, reverse=True)]
with open(rootpath + 'dictir.txt', 'w', encoding="utf-8") as file:
	count = 0
	for k,v in s:	
		file.write("%d %s %d\n" %(count,k,v))
		count+=1
	file.close()
#=========================================================

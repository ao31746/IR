import numpy as np
rootpath = 'C:/Users/lckung/Desktop/IR/IR/Final/'
#print (up/(np.linalg.norm(a)*np.linalg.norm(b)))
def cosine(Docx, Docy):
	doc = [Docx, Docy]
	path = rootpath+'tfidf/'
	cos_vec = []
    
	for filename in doc:
        
		with open(path+filename) as f:
			content = f.readlines()
            # you may also want to remove whitespace characters like `\n` at the end of each line
			content = [x.strip() for x in content] 
		cos_vec.append([tuple([i.split()[0], float(i.split()[1])]) for i in content])
    
	vc_norm_x = [i[1] for i in cos_vec[0]]
	vc_norm_y = [i[1] for i in cos_vec[1]]

	up = 0
	for i in cos_vec[1]:
        #print ([y[0] for x, y in enumerate(cos_vec[0]) if y[0] == i[0]])
		for j in cos_vec[0]:
			if i[0]==j[0]:
				up+=i[1]*j[1]
                
	down = np.linalg.norm(vc_norm_x) * np.linalg.norm(vc_norm_y)
	if down == 0:
		return 0
	return up/down


count = 0
with open(rootpath + 'similar.txt', 'w', encoding="utf-8") as file:
	for j in range(0,106):
		ans = []
		for i in range(0,106):
			if i==j:
				continue
			#print(cosine('Gossiping'+str(ij)+'.json'), 'Gossiping'+str(i)+'.json'))
			ans.append(cosine('Gossiping'+str(j)+'.json', 'Gossiping'+str(i)+'.json'))

		file.write("%d %d\n" %(count, ans.index(max(ans))))
		count+=1
		file.flush()
		#print (ans.index(max(ans)))
		#print(ans.index(sorted(ans, reverse= True)[1]))
file.close()
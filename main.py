# -*- coding: utf-8 -*-
import nltk 
import codecs
import string
from make_word2vec_model import learnRepr 
import gensim 
import os

def potenCand(sen_id,word_id):
	sen_count,candidates =0,[]
	while 1:
		while word_id >0:
			if doc_tags[sen_id][word_id-1][1] in ['NN','NNS','NNP','NNPS']:
				candidates.append(doc_tags[sen_id][word_id-1][0])
			word_id  -= 1
		sen_count+=1
		sen_id -=1
		if sen_id <0 or sen_count>10:
			break
		else :
			word_id = len(doc_tags[sen_id]) 
	return candidates
		
def resolve(vector_repr):
	similarities = []
	for  sen_tags in doc_tags:
		for word_tag in sen_tags:
			if word_tag[1]=='PRP':
				candidates = potenCand(doc_tags.index(sen_tags),sen_tags.index(word_tag))
				for candidate in candidates:
					similarities.append(vector_repr.similarity(word_tag[0],candidate))
				list1, list2 = zip(*sorted(zip(candidates, similarities)))
#				zipped = zip(candidates,similarities)
#				zipped = sorted(zipped,key = lambda x: float(x[1]))
#				print zipped
#zipped = zipped.sort(key = lambda t: t[1])
#	list1,list2 = zip(*zipped.sort(key = lambda t:t[1]))
				print "pronoun resolved = ", word_tag[0]
				print list1
				print list2
				similarites = []
				

						
				
if __name__=="__main__":
	doc_tags = []
	tokenize=nltk.word_tokenize
	pos_tag =nltk.pos_tag
	rmv_punc =list(string.punctuation)
	fo = codecs.open("./train_data/input.txt","r",encoding='utf-8')
	for line in fo:
		line = line.strip("\n")
		text = tokenize(line)
		sen_tags=pos_tag(text)
		sen_tags = [word_tag for word_tag in sen_tags if word_tag[0] not in rmv_punc]
		if len(sen_tags)!=0:
			doc_tags.append(sen_tags)
	fo.close()
	learnRepr()
	vector_repr= gensim.models.word2vec.Word2Vec.load("./model")

	resolve(vector_repr)


	
		
	


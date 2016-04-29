def learnRepr():
	import gensim
	import os
#import logging
#	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	class MySentences(object):

    		def __init__(self, dirname):
    			self.dirname = dirname
    		def __iter__(self):
        		for fname in os.listdir(self.dirname):
            			for line in open(os.path.join(self.dirname, fname)):
                	 		yield line.split()
	sentences = MySentences('./train_data/')  #sentences is an  generator

	trained_model = gensim.models.word2vec.Word2Vec(sentences, size=300, window=5, min_count=0, workers=4)

	#print trained_model['apples']  		   #gives vector representation for the word apples 
	#print trained_model.similarity('apples','fruits')  #Gives cosine similarity between the two words 
	try:
		os.remove("./model")
	except:
		pass
	trained_model.save('./model')

import pickle
import numpy as np
from pyvi import ViTokenizer
import nltk
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from gensim.models import KeyedVectors 
w2v = KeyedVectors.load_word2vec_format("news/vi_txt/vi.vec")
vocab = w2v.wv.vocab
def TT(text):
	#Pre-processing
	text=(text.lower().strip())
	sentences = nltk.sent_tokenize(text)
	X = []
	for sentence in sentences:
	    sentence = ViTokenizer.tokenize(sentence)
	    words = sentence.split(" ")
	    sentence_vec = np.zeros((100))
	    for word in words:
	        if word in vocab:
	            sentence_vec+=w2v.wv[word]
	    X.append(sentence_vec)

	n_clusters = 5
	kmeans = KMeans(n_clusters=n_clusters)
	kmeans = kmeans.fit(X)
	avg = []
	for j in range(n_clusters):
	    idx = np.where(kmeans.labels_ == j)[0]
	    avg.append(np.mean(idx))
	closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, X)
	ordering = sorted(range(n_clusters), key=lambda k: avg[k])
	summary = ' '.join([sentences[closest[idx]] for idx in ordering])
	return (summary)
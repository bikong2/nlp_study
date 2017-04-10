#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
from gensim import *
from gensim.models import LdaModel
from gensim.corpora import Dictionary

train = []
stopwords = codecs.open('stopwords-list/stop_words_zh_UTF-8.txt','r',encoding='utf8').readlines()
stopwords = [ w.strip() for w in stopwords ]
fp = codecs.open('wiki.zh.text.seg','r',encoding='utf8')
i = 0
for line in fp:
    i += 1
    line = line.split()
    train.append([ w for w in line if w not in stopwords ])
    dictionary = corpora.Dictionary(train)
    corpus = [ dictionary.doc2bow(text) for text in train ]
    lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=100)
    if i%1000==0: print str(i)+" lines ok!"

lda.save('zhwiki_lda.model')
print "lda saved and load..."
lda = models.ldamodel.LdaModel.load('zhwiki_lda.model')

lda.print_topics(20)
lda.print_topic(20)

test_doc="中国队参加世界杯，中国队必胜，中国足球是世界足球的希望。中国政府对此表示高度关切，期待事态向好的方向发展。"
test_doc = list(jieba.cut(test_doc))
doc_bow = id2word.doc2bow(test_doc)
doc_lda = lda[doc_bow]
print doc_lda
for topic in doc_lda:
    print "%s\t%f\n"%(lda.print_topic(topic[0]), topic[1])

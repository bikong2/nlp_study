#python seg_wiki_data.py wiki.zh.text
#mv segfile wiki.zh.text.seg
#python train_word2vec_model.py wiki.zh.text.seg wiki.zh.text.model wiki.zh.text.vector
python lda_zhwiki.py

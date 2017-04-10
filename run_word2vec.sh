#python process_wiki_data.py /home/lixihua/datas/zhwiki-latest-pages-articles.xml.bz2 wiki.zh.text
python seg_wiki_data.py wiki.zh.text
#python train_word2vec_model.py wiki.zh.text.seg wiki.zh.text.model wiki.zh.text.vector
#python lda_zhwiki.py

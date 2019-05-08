from gensim import models
import os
import w2v
import gensim
save_model_name1='word2vec_779845.bin'
cut_file=''

def w2v_model():
    if not os.path.exists(save_model_name1):  # 判断文件是否存在
       w2v.model_train(cut_file, save_model_name1)
    else:
        print('此训练模型已经存在，不用再次训练')
def w2v_similary(word1,word2):
    # 加载已训练好的模型
    model_1 = models.KeyedVectors.load_word2vec_format(save_model_name1,binary=True)
    # 计算两个词的相似度/相关程度
    y1 = model_1.similarity(word1, word2)
    # print(word1+'和'+word2+'的相似度为:', y1)
    # print("-------------------------------\n")
    return y1

def w2v_topk(word):
    # 计算某个词的相关词列表,模拟用户的兴趣词，建立兴趣词表
    model_1 = models.KeyedVectors.load_word2vec_format(save_model_name1,binary=True)
    y2 = model_1.most_similar(word, topn=10)  # 10个最相关的
    if y2=={}:
        return
    print('和'+str(word)+'最相关的词有：\n')
    for item in y2:
        print(item[0], item[1])
    print("-------------------------------\n")
    return y2

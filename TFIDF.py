# -*- coding: utf-8 -*-
from jieba import analyse
import xlrd
import cut
def tfidf(text):
    # 引入TF-IDF关键词抽取接口
    tfidf = analyse.extract_tags

    #分词
    fenci=cut.cut_txt(text)
    str_out = ' '.join(fenci).replace('，', '').replace('。', '').replace('？', '').replace('！', '') \
        .replace('“', '').replace('”', '').replace('：', '').replace('…', '').replace('（', '').replace('）', '') \
        .replace('—', '').replace('《', '').replace('》', '').replace('、', '').replace('‘', '') \
        .replace('’', '')     # 去掉标点符号
    # 使用自定义停用词集合
    stopwords = [line.strip() for line in open('Stopwords.txt', encoding='UTF-8').readlines()]
    # 输出结果为outstr
    outstr = ''
    for word in str_out:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr+=''
    # print(outstr)
    # 基于TF-IDF算法进行关键词抽取
    keywords = tfidf(str(outstr), topK=5, withWeight=False, allowPOS=())
    # print ("keywords by tfidf:")
    # # 输出抽取出的关键词
    # for keyword in keywords:
    #     print (keyword + "/n")
    return keywords
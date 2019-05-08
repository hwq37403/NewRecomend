def cut_txt(text):
    import jieba
    try:
        new_text = jieba.cut(str(text), cut_all=False)  # 精确模式
    except BaseException as e:  # 因BaseException是所有错误的基类，用它可以获得所有错误类型
        print(Exception, ":", e)    # 追踪错误详细信息
    # str_out = ' '.join(new_text).replace('，', '').replace('。', '').replace('？', '').replace('！', '') \
    #     .replace('“', '').replace('”', '').replace('：', '').replace('…', '').replace('（', '').replace('）', '') \
    #     .replace('—', '').replace('《', '').replace('》', '').replace('、', '').replace('‘', '') \
    #     .replace('’', '')     # 去掉标点符号
    # fo = open(cut_file, 'w', encoding='utf-8')
    # fo.write(str_out)
    return new_text

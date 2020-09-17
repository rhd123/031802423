import jieba
import jieba.analyse
# jieba 分词
from sklearn.metrics.pairwise import cosine_similarity
# sklearn 中的cosine_similarity 可直接计算余弦相似度
import sys
# 用于读取命令行参数
'''
argv[1]为论文原文的文件的绝对路径
argv[2]为抄袭版论文的文件的绝对路径
argv[3]为输出的答案文件的绝对路径
'''


class CosineSimilarity(object):

    def __init__(self, text1, text2):
        self.s1 = text1
        self.s2 = text2

    @staticmethod
    # 提取关键词
    def Keyword(text):
        cut = [i for i in jieba.cut(text, cut_all=True) if i != '']
        keywords = jieba.analyse.extract_tags(",".join(cut), topK=topK, withWeight=False)
        # 提取关键词，按照权重返回前topK个关键词
        return keywords

    @staticmethod
    # oneHot编码
    def oneHot(dic, keywords):
        vector = [0] * len(dic)
        # 初始化全0向量
        for keyword in keywords:
            vector[dic[keyword]] += 1
        return vector

    @staticmethod
    # 计算余弦相似度
    def calculate(s1_code, s2_code):
        try:
            sample = [s1_code, s2_code]
            sim = cosine_similarity(sample)
            # sim[0][1]为 s1 与 s2 的相似度
            return sim[0][1]
        except Exception as e:
            print(e)
            return 0.0
            # 除0处理

    @staticmethod
    def constructHash(keywords):  # 构造哈希表
        dic = {}
        hash_value = 0
        for keyword in keywords:  # 哈希表赋值
            dic[keyword] = hash_value
            hash_value += 1  # 每个词对应的哈希值从数字0开始递增
        return dic

    def main(self):
        keywords1 = self.Keyword(self.s1)
        keywords2 = self.Keyword(self.s2)
        # 分别提取文本的关键词
        keywords = set(keywords1).union(set(keywords2))
        # set去重  关键词取并
        dic = self.constructHash(keywords)
        s1_code = self.oneHot(dic, keywords1)
        s2_code = self.oneHot(dic, keywords2)
        # oneHot编码
        sim_value = self.calculate(s1_code, s2_code)
        return sim_value
        # 返回相似度


if __name__ == '__main__':
    # 从Terminal输入绝对路径 读入原文本、抄袭文本 计算topK
    try:
        with open(sys.argv[1], "r", encoding='UTF-8') as fp:
            origin = fp.read()
            seg = [i for i in jieba.cut(origin, cut_all=True) if i != '']
        topK = int(len(seg) / 8)
    except:
        print("路径错误")
        topK = 0
    try:
        with open(sys.argv[2], "r", encoding='UTF-8') as fp:
            copy = fp.read()
    except:
        print("路径错误")

    similarity = CosineSimilarity(origin, copy)
    # 所计算的相似度按题目要求保留两位小数
    similarity = round(similarity.main(), 2)
    # 将相似度写入输出文本
    try:
        with open(sys.argv[3], "w+", encoding='UTF-8') as fp:
            fp.write(str(similarity))
    except:
        print("路径错误")

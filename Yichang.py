import jieba
import jieba.analyse
# jieba 分词
from sklearn.metrics.pairwise import cosine_similarity
# sklearn 中的cosine_similarity 可直接计算余弦相似度
import sys
import unittest


class CosineSimilarity(object):

    def __init__(self, text1, text2):
        self.s1 = text1
        self.s2 = text2

    @staticmethod
    # 提取关键词
    def Keyword(text):
        cut = [i for i in jieba.cut(text, cut_all=True) if i != '']
        keywords = jieba.analyse.extract_tags(",".join(cut), topK=200, withWeight=False)
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

    def test_empty(self):
        print("源文本和抄袭文本均为空的情况")
        with open("D:/python_work/pycharmWork/ChaChong/tt.txt", "r", encoding='UTF-8') as fp:
            origin = fp.read()
        with open("D:/python_work/pycharmWork/ChaChong/empty.txt", "r", encoding='UTF-8') as fp:
            copy = fp.read()
        similarity = CosineSimilarity(origin, copy)
        similarity = round(similarity.main(), 2)
        print(similarity)

    def test_same(self):
        print("源文本和抄袭文本内容完全相同的情况")
        with open("D:/python_work/pycharmWork/ChaChong/same1.txt", "r", encoding='UTF-8') as fp:
            origin = fp.read()
        with open("D:/python_work/pycharmWork/ChaChong/same2.txt", "r", encoding='UTF-8') as fp:
            copy = fp.read()
        similarity = CosineSimilarity(origin, copy)
        similarity = round(similarity.main(), 2)
        print(similarity)


if __name__ == '__main__':
    unittest.main()
import unittest
import jieba
import jieba.analyse
# 用于分词
from sklearn.metrics.pairwise import cosine_similarity
# sklearn中的 cosine_similarity 可直接计算余弦相似度
import sys
# 用于读取命令行参数


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

class MyTest(unittest.TestCase):

    def tearDown(self) -> None:
        print("test over!")

    def test_add(self):
        print("orig_0.8_add.txt 相似度")
        with open("D:/python_work/pycharmWork/ChaChong/sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            origin = fp.read()
        with open("D:/python_work/pycharmWork/ChaChong/sim_0.8/orig_0.8_add.txt", "r", encoding='UTF-8') as fp:
            copy = fp.read()
        similarity = CosineSimilarity(origin, copy)
        similarity = round(similarity.main(), 2)
        print(similarity)

    def test_del(self):
        print("orig_0.8_del.txt 相似度")
        with open("D:/python_work/pycharmWork/ChaChong/sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            origin = fp.read()
        with open("D:/python_work/pycharmWork/ChaChong/sim_0.8/orig_0.8_del.txt", "r", encoding='UTF-8') as fp:
            copy = fp.read()
        similarity = CosineSimilarity(origin, copy)
        similarity = round(similarity.main(), 2)
        print(similarity)

    def test_dis_1(self):
        print("orig_0.8_dis_1.txt 相似度")
        with open("D:/python_work/pycharmWork/ChaChong/sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            origin = fp.read()
        with open("D:/python_work/pycharmWork/ChaChong/sim_0.8/orig_0.8_dis_1.txt", "r", encoding='UTF-8') as fp:
            copy = fp.read()
        similarity = CosineSimilarity(origin, copy)
        similarity = round(similarity.main(), 2)
        print(similarity)

    def test_dis_3(self):
        print("orig_0.8_dis_3.txt 相似度")
        with open("D:/python_work/pycharmWork/ChaChong/sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            origin = fp.read()
        with open("D:/python_work/pycharmWork/ChaChong/sim_0.8/orig_0.8_dis_3.txt", "r", encoding='UTF-8') as fp:
            copy = fp.read()
        similarity = CosineSimilarity(origin, copy)
        similarity = round(similarity.main(), 2)
        print(similarity)

    def test_dis_7(self):
        print("orig_0.8_dis_7.txt 相似度")
        with open("D:/python_work/pycharmWork/ChaChong/sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            origin = fp.read()
        with open("D:/python_work/pycharmWork/ChaChong/sim_0.8/orig_0.8_dis_7.txt", "r", encoding='UTF-8') as fp:
            copy = fp.read()
        similarity = CosineSimilarity(origin, copy)
        similarity = round(similarity.main(), 2)
        print(similarity)

    def test_dis_10(self):
        print("orig_0.8_dis_10.txt 相似度")
        with open("D:/python_work/pycharmWork/ChaChong/sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            origin = fp.read()
        with open("D:/python_work/pycharmWork/ChaChong/sim_0.8/orig_0.8_dis_10.txt", "r", encoding='UTF-8') as fp:
            copy = fp.read()
        similarity = CosineSimilarity(origin, copy)
        similarity = round(similarity.main(), 2)
        print(similarity)

    def test_dis_15(self):
        print("orig_0.8_dis_15.txt 相似度")
        with open("D:/python_work/pycharmWork/ChaChong/sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            origin = fp.read()
        with open("D:/python_work/pycharmWork/ChaChong/sim_0.8/orig_0.8_dis_15.txt", "r", encoding='UTF-8') as fp:
            copy = fp.read()
        similarity = CosineSimilarity(origin, copy)
        similarity = round(similarity.main(), 2)
        print(similarity)

    def test_rep(self):
        print("orig_0.8_rep.txt 相似度")
        with open("D:/python_work/pycharmWork/ChaChong/sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            origin = fp.read()
        with open("D:/python_work/pycharmWork/ChaChong/sim_0.8/orig_0.8_rep.txt", "r", encoding='UTF-8') as fp:
            copy = fp.read()
        similarity = CosineSimilarity(origin, copy)
        similarity = round(similarity.main(), 2)
        print(similarity)

    def test_mix(self):
        print("orig_0.8_mix.txt 相似度")
        with open("D:/python_work/pycharmWork/ChaChong/sim_0.8/orig.txt", "r", encoding='UTF-8') as fp:
            origin = fp.read()
        with open("D:/python_work/pycharmWork/ChaChong/sim_0.8/orig_0.8_mix.txt", "r", encoding='UTF-8') as fp:
            copy = fp.read()
        similarity = CosineSimilarity(origin, copy)
        similarity = round(similarity.main(), 2)
        print(similarity)


if __name__ == '__main__':
    unittest.main()
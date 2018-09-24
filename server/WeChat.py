import itchat
from collections import Counter
from pyecharts import Map, WordCloud, Pie, Geo
import jieba

itchat.auto_login(hotReload=True)
friends = itchat.get_friends()

print(len(friends))  # 好友数量

nick_names, signatures, provinces, cities, sexes = zip(
    *[(p.NickName, p.Signature, p.Province, p.City, p.Sex) for p in friends])


# print(sex)

# for i in friends:
#     print(i.UserName, i.Province, i.City, u'男' if i.Sex == 1 else u'女')
#     print(u'网名：', i.NickName)
#     print(u'备注名：', i.RemarkName)
#     print(u'个性签名：', i.Signature)
#
# for k, v in dict(friends[-15]).items():
#     print(k, ': ', v)

# p = itchat.search_friends(userName='@b72656441320acff215a1534ed0c225b8224bdeef841ee3b5de7f79d943044b0')
# print type(p)
# print dir(p)
# print p
# itchat.send_msg(msg='hello world', toUserName=friends[-21].UserName)

def friends_map(provinces: list):
    counter = Counter(provinces)  # 地图插件不会显示不存在的地方，所以可以不做清洗

    map = Map('中国地区好友分布', width=1200, height=600)
    map.add(
        "",
        counter.keys(),
        counter.values(),
        maptype="china",
        is_visualmap=True,
        visual_text_color="#000",
        is_map_symbol_show=False
    )
    map.render()

    # geo = Geo(
    #     "全国主要城市空气质量",
    #     "data from pm2.5",
    #     title_color="#fff",
    #     title_pos="center",
    #     width=1200,
    #     height=600,
    #     background_color="#404a59",
    # )
    # geo.add(
    #     "",
    #     counter.keys(),
    #     counter.values(),
    #     visual_range=[0, 50],
    #     visual_text_color="#fff",
    #     symbol_size=15,
    #     is_visualmap=True,
    # )
    # geo.render()


def word_cloud(title, data: list):
    cut = jieba.cut(' '.join(data))
    counter = {k: v for k, v in Counter(cut).items() if len(k) >= 2 and v >= 2}
    print(counter)

    word_cloud = WordCloud(width=1300, height=620)
    word_cloud.add(title, counter.keys(), counter.values(), word_size_range=[20, 100])
    word_cloud.render()


def sex_rate(data: list):
    data = ['男' if s == 1 else ('女' if s == 2 else '未知') for s in data]
    counter = Counter(data)
    pie = Pie("好友性别分布比例", title_pos='center')
    pie.add(
        "",
        counter.keys(),
        counter.values(),
        radius=[40, 75],
        label_text_color=None,
        is_label_show=True,
        legend_orient="vertical",
        legend_pos="left",
    )
    pie.render()


friends_map(provinces)

# word_cloud('签名词云', signatures)

# sex_rate(sex)

# 群组信息
# 整理好友
# 知道哪些好友拉黑我

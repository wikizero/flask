import re
import time
import itchat
from itchat.content import *
from pathlib import Path
from pprint import pprint
from datetime import datetime
from .dbHelper import mongo

face_bug = None  # 针对表情包的内容
folder = 'files'


@itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO], isFriendChat=True,
                     isGroupChat=True, isMpChat=True)
def handle_receive_msg(msg):
    global face_bug
    # print(msg)
    user = ''
    sex = 0
    source = ''
    remark_name = ''

    user_info = msg.get('User')
    source_str = repr(type(msg.get('User')))
    msg_time = msg.get('CreateTime')  # 信息发送的时间
    msg_id = msg.get('MsgId')  # 每条信息的id
    msg_content = None  # 储存信息的内容
    msg_share_url = None  # 储存分享的链接，比如分享的文章和音乐
    source_name = user_info.get('NickName')  # 消息来源
    msg_type = msg.get('Type')  # 消息类型

    if 'MassivePlatform' in source_str:
        source = 'MassivePlatform'
        user = source_name
        sex = msg.get('RecommendInfo').get('Sex')

    elif 'Chatroom' in source_str:
        source = 'Chatroom'
        user = msg.get('ActualNickName')
        sex = msg.get('RecommendInfo').get('Sex')

    elif 'User' in source_str:
        source = 'User'

    search_user = itchat.search_friends(userName=msg.get('FromUserName'))
    if search_user:
        source_name = search_user.get('NickName')
        user = source_name
        sex = search_user.get('Sex')
        remark_name = search_user.get('RemarkName')

    sex = '男' if sex == 1 else '女'

    if msg_type == 'Text' or msg_type == 'Friends':  # 如果发送的消息是文本或者好友推荐
        msg_content = msg['Text']

    # 如果发送的消息是附件、视屏、图片、语音
    elif msg_type == "Attachment" or msg_type == "Video" \
            or msg_type == 'Picture' \
            or msg_type == 'Recording':
        msg_content = msg['FileName']  # 内容就是他们的文件名
        msg['Text'](Path(folder) / str(msg_content))  # 下载文件

    elif msg_type == 'Card':  # 如果消息是推荐的名片
        msg_content = msg['RecommendInfo']['NickName'] + '的名片'  # 内容就是推荐人的昵称和性别
        if msg['RecommendInfo']['Sex'] == 1:
            msg_content += '性别为男'
        else:
            msg_content += '性别为女'

    elif msg_type == 'Map':  # 如果消息为分享的位置信息
        x, y, location = re.search(
            "<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*", msg['OriContent']).group(1, 2, 3)
        if location is None:
            msg_content = r"纬度->" + x.__str__() + " 经度->" + y.__str__()  # 内容为详细的地址
        else:
            msg_content = r"" + location

    elif msg_type == 'Sharing':  # 如果消息为分享的音乐或者文章，详细的内容为文章的标题或者是分享的名字
        msg_content = msg['Text']
        msg_share_url = msg['Url']  # 记录分享的url

    face_bug = msg_content
    data = {
        '_id': msg_id,
        'msg': msg_content,
        'url': msg_share_url,
        'time': str(datetime.fromtimestamp(msg_time)),
        'type': msg_type,
        'source': source,
        'source_name': source_name,
        'user': user,
        'sex': sex,
        'remark_name': remark_name,
    }
    # save in db
    mongo.insert_one(data)


# 这个是用于监听是否有消息撤回
@itchat.msg_register(NOTE, isFriendChat=True, isGroupChat=True, isMpChat=True)
def information(msg):
    # 这里如果这里的msg['Content']中包含消息撤回和id，就执行下面的语句
    if '撤回了一条消息' in msg['Content']:
        old_msg_id = re.search("\<msgid\>(.*?)\<\/msgid\>", msg['Content']).group(1)  # 在返回的content查找撤回的消息的id
        old_msg = None
        while not old_msg:
            # 可能消息还没存到数据库，所以循环查
            time.sleep(1)
            old_msg = mongo.find_one({'_id': old_msg_id})

        ret = mongo.update_one({'_id': old_msg_id}, {'revoke': True})
        print(dict(ret))


itchat.auto_login(hotReload=True)
itchat.run()

# FIXME 讨论组自己发消息无法获取到 source_name
# msg_type  :Friends

import time
from datetime import datetime


print(datetime.fromtimestamp(1540648344))

'''
发给小兵
{'MsgId': '6475360283228650948', 'FromUserName': '@8b1c151db48848d3d9fe5d2348f63c1c4ba6538c9ff6446c1470aad712fa19e1',
 'ToUserName': '@d674a9df9992a77447dafc28a799f29b', 'MsgType': 1, 'Content': '。。', 'Status': 3, 'ImgStatus': 1, 
 'CreateTime': 1540657530, 'VoiceLength': 0, 'PlayLength': 0, 'FileName': '', 'FileSize': '', 'MediaId': '', 'Url': '', 
 'AppMsgType': 0, 'StatusNotifyCode': 0, 'StatusNotifyUserName': '', 'RecommendInfo': {'UserName': '', 'NickName': '', 'QQNum': 0, 
 'Province': '', 'City': '', 'Content': '', 'Signature': '', 'Alias': '', 'Scene': 0, 'VerifyFlag': 0, 'AttrStatus': 0, 'Sex': 0, 'Ticket': '', 'OpCode': 0}, 
 'ForwardFlag': 0, 'AppInfo': {'AppID': '', 'Type': 0}, 'HasProductId': 0, 'Ticket': '', 'ImgHeight': 0, 'ImgWidth': 0, 'SubMsgType': 0, 'NewMsgId': 6475360283228650948,
  'OriContent': '', 'EncryFileName': '', 'User': <MassivePlatform: {'MemberList': <ContactList: []>, 'Uin': 0, 'UserName': '@d674a9df9992a77447dafc28a799f29b', 
  'NickName': '小冰', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=647220570&username=@d674a9df9992a77447dafc28a799f29b&skey=@crypt_a0d2029_9e68876c978a40426ef4b0530a9667d2',
   'ContactFlag': 3, 'MemberCount': 0, 'RemarkName': '', 'HideInputBarFlag': 0, 'Sex': 0, 'Signature': '我是人工智能微软小冰~~', 'VerifyFlag': 24, 'OwnerUin': 0, 'PYInitial'
   : 'XB', 'PYQuanPin': 'xiaobing', 'RemarkPYInitial': '', 'RemarkPYQuanPin': '', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 0, 'Province': '北
   京', 'City': '海淀', 'Alias': '', 'SnsFlag': 0, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': 'gh_', 'EncryChatRoomId': '', 'IsOwner': 0}>, 'T
   ype': 'Text', 'Text': '。。'}


发给hello world群组
{'MsgId': '4530611372335508812', 'FromUserName': '@8b1c151db48848d3d9fe5d2348f63c1c4ba6538c9ff6446c1470aad712fa19e1',
 'ToUserName': '@@e5d7344c40c7d1b317abe7a0a57015efaeeba3a0072da6b255b8aeb1350b1669', 'MsgType': 1, 'Content': '😒', 'Status': 3, 
 'ImgStatus': 1, 'CreateTime': 1540657610, 'VoiceLength': 0, 'PlayLength': 0, 'FileName': '', 'FileSize': '', 'MediaId': '', 'Url': '',
  'AppMsgType': 0, 'StatusNotifyCode': 0, 'StatusNotifyUserName': '', 'RecommendInfo': {'UserName': '', 'NickName': '', 'QQNum': 0, 'Province': '',
   'City': '', 'Content': '', 'Signature': '', 'Alias': '', 'Scene': 0, 'VerifyFlag': 0, 'AttrStatus': 0, 'Sex': 0, 'Ticket': '', 'OpCode': 0}, 'ForwardFlag': 0, 
   'AppInfo': {'AppID': '', 'Type': 0}, 'HasProductId': 0, 'Ticket': '', 'ImgHeight': 0, 'ImgWidth': 0, 'SubMsgType': 0, 'NewMsgId': 4530611372335508812, 
   'OriContent': '', 'EncryFileName': '', 'ActualNickName': '', 'IsAt': False, 'ActualUserName': '@8b1c151db48848d3d9fe5d2348f63c1c4ba6538c9ff6446c1470aad712fa19e1', 
   'User': <Chatroom: {'UserName': '@@e5d7344c40c7d1b317abe7a0a57015efaeeba3a0072da6b255b8aeb1350b1669', 'MemberList': <ContactList: []>}>, 'Type': 'Text', 'Text': '😒'}


发给笑话
{'MsgId': '6049001063952249959', 'FromUserName': '@8b1c151db48848d3d9fe5d2348f63c1c4ba6538c9ff6446c1470aad712fa19e1', 
'ToUserName': '@64546a2b4ff89f99e699279479b3eed282d2c243d7f401e0c9e727279ac334f8', 'MsgType': 1, 'Content': '[皱眉]', 'Status': 3, 
'ImgStatus': 1, 'CreateTime': 1540657736, 'VoiceLength': 0, 'PlayLength': 0, 'FileName': '', 'FileSize': '', 'MediaId': '', 'Url': '', 
'AppMsgType': 0, 'StatusNotifyCode': 0, 'StatusNotifyUserName': '', 'RecommendInfo': {'UserName': '', 'NickName': '', 'QQNum': 0, 'Province': '', 
'City': '', 'Content': '', 'Signature': '', 'Alias': '', 'Scene': 0, 'VerifyFlag': 0, 'AttrStatus': 0, 'Sex': 0, 'Ticket': '', 'OpCode': 0}, 'ForwardFlag': 0, 
'AppInfo': {'AppID': '', 'Type': 0}, 'HasProductId': 0, 'Ticket': '', 'ImgHeight': 0, 'ImgWidth': 0, 'SubMsgType': 0, 'NewMsgId': 6049001063952249959, 'OriContent': '', 
'EncryFileName': '', 'User': <User: {'MemberList': <ContactList: []>, 'Uin': 0, 'UserName': '@64546a2b4ff89f99e699279479b3eed282d2c243d7f401e0c9e727279ac334f8', 
'NickName': 'summer_summer', 
'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=680565338&username=@64546a2b4ff89f99e699279479b3eed282d2c243d7f401e0c9e727279ac334f8&skey=@crypt_a0d2029_9e68876c978a40426ef4b0530a9667d2', 'ContactFlag': 3, 'MemberCount': 0, 'RemarkName': '林晓华', 'HideInputBarFlag': 0, 'Sex': 1, 'Signature': '好好学习，好好工作', 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': 'SUMMERSUMMER', 'PYQuanPin': 'summersummer', 'RemarkPYInitial': 'LXH', 'RemarkPYQuanPin': 'linxiaohua', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 104549, 'Province': '广东', 'City': '深圳', 'Alias': '', 'SnsFlag': 1, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': '', 'EncryChatRoomId': '', 'IsOwner': 0}>, 'Type': 'Text', 'Text': '[皱眉]'}


{'MsgId': '3934695105420938949', 'FromUserName': '@64546a2b4ff89f99e699279479b3eed282d2c243d7f401e0c9e727279ac334f8',
 'ToUserName': '@8b1c151db48848d3d9fe5d2348f63c1c4ba6538c9ff6446c1470aad712fa19e1', 'MsgType': 1, 'Content': '睡着都被你吵醒了', 
 'Status': 3, 'ImgStatus': 1, 'CreateTime': 1540657848, 'VoiceLength': 0, 'PlayLength': 0, 'FileName': '', 'FileSize': '', 'MediaId': '', 
 'Url': '', 'AppMsgType': 0, 'StatusNotifyCode': 0, 'StatusNotifyUserName': '', 'RecommendInfo': {'UserName': '', 'NickName': '', 'QQNum': 0,
  'Province': '', 'City': '', 'Content': '', 'Signature': '', 'Alias': '', 'Scene': 0, 'VerifyFlag': 0, 'AttrStatus': 0, 'Sex': 0, 'Ticket': '', 'OpCode': 0}, 
  'ForwardFlag': 0, 'AppInfo': {'AppID': '', 'Type': 0}, 'HasProductId': 0, 'Ticket': '', 'ImgHeight': 0, 'ImgWidth': 0, 'SubMsgType': 0, 'NewMsgId': 3934695105420938949, 
  'OriContent': '', 'EncryFileName': '', 'User': <User: {'MemberList': <ContactList: []>, 'Uin': 0, 'UserName': '@64546a2b4ff89f99e699279479b3eed282d2c243d7f401e0c9e727279ac334f8', 
  'NickName': 'summer_summer', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=680565338&username=@64546a2b4ff89f99e699279479b3eed282d2c243d7f401e0c9e727279ac334f8&skey=@crypt_a0d2029_9e68876c978a40426ef4b0530a9667d2', 'ContactFlag': 3, 'MemberCount': 0, 'RemarkName': '林晓华', 'HideInputBarFlag': 0, 'Sex': 1, 'Signature': '好好学习，好好工作', 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': 'SUMMERSUMMER', 'PYQuanPin': 'summersummer', 'RemarkPYInitial': 'LXH', 'RemarkPYQuanPin': 'linxiaohua', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 104549, 'Province': '广东', 'City': '深圳', 'Alias': '', 'SnsFlag': 1, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': '', 'EncryChatRoomId': '', 'IsOwner': 0}>, 'Type': 'Text', 'Text': '睡着都被你吵醒了'}


{'MsgId': '5029831029101078988', 'FromUserName': '@8b1c151db48848d3d9fe5d2348f63c1c4ba6538c9ff6446c1470aad712fa19e1', 
'ToUserName': '@@e5d7344c40c7d1b317abe7a0a57015efaeeba3a0072da6b255b8aeb1350b1669', 'MsgType': 1, 'Content': '😳', 'Status': 3, '
ImgStatus': 1, 'CreateTime': 1540658745, 'VoiceLength': 0, 'PlayLength': 0, 'FileName': '', 'FileSize': '', 'MediaId': '', 'Url': '', 'Ap
pMsgType': 0, 'StatusNotifyCode': 0, 'StatusNotifyUserName': '', 'RecommendInfo': {'UserName': '', 'NickName': '', 'QQNum': 0, 'Provin
ce': '', 'City': '', 'Content': '', 'Signature': '', 'Alias': '', 'Scene': 0, 'VerifyFlag': 0, 'AttrStatus': 0, 'Sex': 0, 'Ticket': '', 'OpCode'
: 0}, 'ForwardFlag': 0, 'AppInfo': {'AppID': '', 'Type': 0}, 'HasProductId': 0, 'Ticket': '', 'ImgHeight': 0, 'ImgWidth': 0, 'SubMsgType': 0, 'NewMsgId
': 5029831029101078988, 'OriContent': '', 'EncryFileName': '', 'ActualNickName': '', 'IsAt': False, 'ActualUserName': '@8b1c151db48848d3d9fe5d2348f63c1c4ba65
38c9ff6446c1470aad712fa19e1', 'User': <Chatroom: {'UserName': '@@e5d7344c40c7d1b317abe7a0a57015efaeeba3a0072da6b255b8aeb1350b1669', 'MemberList': <ContactList: []>
}>, 'Type': 'Text', 'Text': '😳'}


'''
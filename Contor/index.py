from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import EventMessage
from wechat_sdk.context.framework.django import DatabaseContextStore
from caicai.models import Users

# wechat_instance = WechatBasic(
#     token='spreadassistant.chltec.com',
#     appid='wxacbc8e8621b5140e',
#     appsecret='11d1e1723475771e958d1252f6ad045a'
# )
#
# @csrf_exempt
# def portal(request):
#     if request.method == 'GET':
#         # 检验合法性
#         # 从 request 中提取基本信息 (signature, timestamp, nonce, xml)
#         signature = request.GET.get('signature')
#         timestamp = request.GET.get('timestamp')
#         nonce = request.GET.get('nonce')
#
#         if not wechat_instance.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
#             return HttpResponseBadRequest('Verify Failed')
#
#         return HttpResponse(
#             request.GET.get('echostr', ''), content_type="text/plain")
#
#     # POST
#     # 解析本次请求的 XML 数据
#     try:
#         wechat_instance.parse_data(data=request.body)
#     except ParseError:
#         return HttpResponseBadRequest('Invalid XML Data')
#
#     # 获取解析好的微信请求信息
#     message = wechat_instance.get_message()
#     if isinstance(message, TextMessage):
#         print ('收到 文本消息')
#         elif isinstance(message, VoiceMessage):
#         print '收到 语音消息'
#     elif isinstance(message, ImageMessage):
#         print '收到 图片消息'
#     elif isinstance(message, VideoMessage):
#         print '收到 视频消息'
#     elif isinstance(message, LinkMessage):
#         print '收到 链接消息'
#     elif isinstance(message, LocationMessage):
#         print '收到 地理位置消息'
#     elif isinstance(message, EventMessage):
#         print '收到 事件消息'
#         #关注事件(包括普通关注事件和扫描二维码造成的关注事件)
#         #如果 key 和 ticket 均不为空，则是扫描二维码造成的关注事件
#
#         if message.type == 'subscribe':
#             print '这是 关注事件'
#         elif message.type == 'unsubscribe':
#             print '这是 取消关注事件'
#         elif message.type == 'scan':
#             print '这是 已关注用户扫描二维码！'
#         elif message.type == 'location':
#             print '这是 上报地理位置'
#         elif message.type == 'click':
#             print '这是 自定义菜单点击'
#         elif message.type == 'view':
#             print '这是 自定义菜单跳转链接'
#         elif message.type == 'templatesendjobfinish':
#             print '这是 模板消息'
#
#     reply_text = '已经响应了'
#     response = wechat_instance.response_text(content=reply_text)
#     return HttpResponse(response, content_type="application/xml")



def ddd(requst):
    User=Users.objects.all()
    print(User)
    for u in User:
        print(u.User_id)
        return {"s":u}
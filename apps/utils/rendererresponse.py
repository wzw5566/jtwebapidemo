# 导入控制返回的JSON格式的类
from rest_framework.renderers import JSONRenderer


class customrenderer(JSONRenderer):
    # 重构render方法
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context:
            # 获取需要返回的msg和code信息
            if isinstance(data, dict):
                msg = data.pop('msg', 'success')
                code = data.pop('code', 0)
            else:
                msg = 'success'
                code = 0
            # 重新构建返回的JSON字典
            ret = {
                'msg': msg,
                'code': code,
                'data': data,
            }
            # 返回JSON数据
            return super().render(ret, accepted_media_type, renderer_context)
        else:
            return super().render(data, accepted_media_type, renderer_context)
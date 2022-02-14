#待付款
from common.send_method import SendMethod
from interface.login_3interface import Login
from common.get_keyword import GetKeyword
class Pending:
    Login.login()
    # 单接口
    @staticmethod
    def pending(data):
        # 请求地址
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/order/list"
        # 请求参数
        response = SendMethod.send_method(url=url,data=data)
        return response

    @staticmethod
    def get_succeed(data):
        response = Pending.pending(data)
        return GetKeyword.get_value_by_keyword(response,"succeed")
if __name__ == '__main__':
    from interface.login_interface import Login
    session = Login.get_session()
    print(session)

    data = {"session":session,"type":"await_pay","pagination":{"count":10,"page":1}}
    print(Pending.pending(data))

'''

'''

from common.base import Base

class Cancel(Base):
    cancel_loc = ('link text','取消订单')
    def cancel(self):
        self.click(self.cancel_loc)

""""
claude
Don't make lab for this
But generate documentation and details to show how enum is bneing used
"""
from enum import Enum

from packaging.utils import InvalidName

"""
Different status
of an Order
"""
class OrderStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELLED = 5

class Order:
    def __init__(self, order_id, customer_name):
        self._order_id = order_id
        self._customer_name = customer_name
        self.order_status = OrderStatus.PENDING

    @property
    def order_id(self):
        return self._order_id

    @property
    def customer_name(self):
        return  self._customer_name

    @order_id.setter
    def set_order_id(self, order_id):
        self._order_id = order_id


    @customer_name.setter
    def set_order_id(self, customer_name):
        self._customer_name = customer_name

    def func_update_status(self, new_status):
        if isinstance(new_status, OrderStatus):
            self.order_status = new_status
        else:
            raise InvalidName("invalid status")

    def func_display_order(self):
        print(f'order id: {self.order_id}')
        print(f'customer name {self.customer_name}')
        print(f'order Status is : {self.order_status.name}')

order1 = Order(1001, "Adam")
order1.func_display_order()
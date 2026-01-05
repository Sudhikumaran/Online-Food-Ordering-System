from PaymentFactory import PaymentFactory

class OrderService:
    def process_order(self, order, payment_type):
        order.confirm_order()
        payment = PaymentFactory.get_payment_method(payment_type)
        payment.pay(order.get_final_amount())
        order.mark_paid()

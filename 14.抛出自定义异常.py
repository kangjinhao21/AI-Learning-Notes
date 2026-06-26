# 自定义异常：继承内置的 Exception 类，用于表达业务场景特有的错误类型
try:
    pay(50, 100)
except InsufficientBalanceError as e:
    print(f"错误提示：{e}")
    print(f"差额：{e.required_amount - e.current_balance} 元")
else:
    print("支付成功")
finally:
    print("支付流程结束")

'''
这个就先稍稍看下
'''
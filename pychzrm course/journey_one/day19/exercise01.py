# 增加验证权限功能，不改变两个功能基础


def verify_jurisdiction(func):
    def wrapper(*args, **kwargs):
        print("验证权限")

        return func(*args, **kwargs)

    return wrapper


@verify_jurisdiction
def enter_background():
    print("进入后台系统")


@verify_jurisdiction
def delete_order():
    print("删除订单")


result = enter_background()

# enter_background("九五之尊")
result1 = delete_order()

# -------------------------------------


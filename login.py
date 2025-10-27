def login(username, password):
    """用户登录功能"""
    # 这里实现登录逻辑
    if username == "admin" and password == "123456":
        return True
    return False


def logout():
    """用户登出功能"""
    print("用户已登出")
    return True

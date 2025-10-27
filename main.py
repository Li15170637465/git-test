from login import login, logout


def main():
    print("Hello, Git!")
    print("开始学习版本控制！")
    print("修复了显示问题")

    # 测试登录功能
    if login("admin", "123456"):
        print("登录成功！")
    else:
        print("登录失败！")


if __name__ == "__main__":
    main()

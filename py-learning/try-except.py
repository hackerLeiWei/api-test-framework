while True:
    try:
        text = input("请输入数字:")
        num = int(text)
        print(f"输入正确，数字:{num}")
        break
    except:
        print(f"输入有误，请输入数字")
while (1):
    val = input("请输入带温度表示符号的温度值(例如: 32C): ")
    if val.strip()=='':
        break
    elif val[-1] in ['C','c']:
        try:
            f = 1.8 * float(val[0:-1]) + 32
            print("转换后的温度为: %.2fF,回车退出（空输入）。"%f)
        except ValueError as e:
            print("输入有误,请重新输入，或回车退出（空输入）。")
    elif val[-1] in ['F','f']:
        try:
            c = (float(val[0:-1]) - 32) / 1.8
            print("转换后的温度为: %.2fC，回车退出（空输入）。"%c)
        except ValueError as e:
            print("输入有误,请重新输入，或回车退出（空输入）。")
    else:
        print("输入有误,请重新输入，或回车退出（空输入）。")

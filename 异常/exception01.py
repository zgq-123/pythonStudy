def fun():
    try:
        2 / 0
    except Exception as err:
        print(err)
        # raise Exception('aaaaaaa')
        return 1
    finally:
        print('基数')
        # return 2


print(fun())

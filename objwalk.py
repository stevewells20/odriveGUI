import inspect




if __name__ == '__main__':
    import odrive

    drv = odrive.find_any()

    x = inspect.getmembers(drv)

    print(x)


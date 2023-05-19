print('--decorator definition--')


def decorator(level='initial'):
    print('starting decorator, level: ', level)

    def factory(func):
        print('starting factory, level: ', level)

        def wrapper(msg=f'wrapper default msg, level: {level}'):
            print('starting wrapper, level: ', level, f'calling {func.__name__}')
            func(msg=f'exec from wrapper, level: {level}, func: '
                     f'{func.__name__}')

            def other_func(_msg=f'other func default message'):
                print(f'executing other function from level {level} with '
                      f'message {_msg}')

            other_func(msg)
            print('finishing wrapper, level: ', level)

        print('finishing factory, level: ', level)
        return wrapper

    print('finishing decorator, level: ', level)
    return factory


print('--base func definition--')


@decorator('2')
@decorator('1')
def base_func(msg):
    print(f'executing base function with message {msg}')


print('--base func call--')
base_func('call message')

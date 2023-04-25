try: 
    from . import messages
except ImportError:
    import messages


def main():
    print(messages.CAMEL)


if __name__ == "__main__":
    main()

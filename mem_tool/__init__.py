from .controller import controller


def main():
    command = ["print", "menu", "main"]
    while True:
        try:
            command = controller(command)
        except SystemExit:
            break


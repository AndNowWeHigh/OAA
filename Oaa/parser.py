"""
    version 1

    a beta version of the parser containing handler calls
"""

from handlers import Handles


class CommandParser:
    def __init__(self):
        self.state = 'START'  # Початковий стан
        self.commands = ['CREATE', 'INSERT', 'PRINT_INDEX', 'SEARCH']  # Доступні команди
        self.stack = []  # Стек для управління станами
        self.handlers = Handles()

    def parse(self, command):
        tokens = command.split()

        if not tokens:
            print("Error: Empty command.")
            return

        self.state = 'START'
        for token in tokens:
            if self.state == 'START':
                if token in self.commands:
                    self.state = f"{token}_COMMAND"
                else:
                    print(f"Error: Unknown command '{token}'.")
                    return

            elif self.state == 'CREATE_COMMAND':
                self.handlers.create(token)
                self.state = 'END'

            elif self.state == 'INSERT_COMMAND':
                if len(tokens) < 3 or not tokens[2].startswith('"') or not tokens[-1].endswith('"'):
                    print("Error: Invalid syntax for INSERT. Correct format: INSERT collection_name \"document\"")
                    return
                self.handlers.insert(tokens[1], ' '.join(tokens[2:]))
                self.state = 'END'

            elif self.state == 'PRINT_INDEX_COMMAND':
                self.handlers.print_index(token)
                self.state = 'END'

            elif self.state == 'SEARCH_COMMAND':
                if 'WHERE' in tokens:
                    where_index = tokens.index('WHERE')
                    if where_index != 2 or len(tokens) < 4:
                        print("Error: Invalid syntax for SEARCH with WHERE clause.")
                        return
                    self.handlers.search(tokens[1], ' '.join(tokens[3:]))
                else:
                    self.handlers.search(tokens[1])
                self.state = 'END'

        if self.state != 'END':
            print(f"Error: Incomplete command.")


# Основний цикл для командної строки
def command_loop():
    parser = CommandParser()
    print("Enter your command (or 'exit' to quit):")

    while True:
        try:
            # Читання команди з командної строки
            command = input("> ").strip()
            if command.lower() == 'exit':
                break
            parser.parse(command)
        except KeyboardInterrupt:
            print("\nExiting.")
            break

if __name__ == "__main__":
    command_loop()

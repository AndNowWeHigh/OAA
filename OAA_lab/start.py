import sys
from parser_1 import parse_command

def command_loop():
    print("Enter your command (type ; to finish):")
    command = []
    try:
        while True:
            line = input("> ")
            if ";" in line:
                command.append(line.split(";")[0])  # Ігноруємо текст після `;`
                full_command = " ".join(command)
                result = parse_command(full_command)
                print(result)
                command = []  # Очищуємо введення
            else:
                command.append(line)
    except KeyboardInterrupt:
        print("\nExiting program. Goodbye!")
        sys.exit()

if __name__ == "__main__":
    command_loop()

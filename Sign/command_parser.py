class CommandParser:

    @staticmethod
    def parse_data(data, state):
        decoded = "".join(map(chr, data))
        print("CommandParser: {}".format(decoded))

        commands = decoded.split(";")

        for command_string in commands:
            command_data = command_string.split("=")


            command = command_data[0]
            content = command_data[1]


            if command == "phrase":
                return content
            elif command == "artist":
                state.set_artist(content)

            elif command == "stage":
                state.set_stage(content)
                # return "Welcome to the {}".format(content)

            elif command == "takeover":
                state.set_stage(content)
                # return "Welcome to the {} takeover".format(content)

            else:
                print("unrecognized command")

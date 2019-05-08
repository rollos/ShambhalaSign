class CommandParser:

    @staticmethod
    def parse_data(data, state):
        decoded = "".join(map(chr, data))
        print("CommandParser: {}".format(decoded))

        data = decoded.split(":")

        command = data[0]
        content = data[1]

        print(command)

        if command == "phrase":
            return content
        elif command == "artist":
            state.set_artist(content)
            return None

        elif command == "stage":
            state.set_stage(content)
            return None
            # return "Welcome to the {}".format(content)

        elif command == "takeover":
            state.set_stage(content)
            return None
            # return "Welcome to the {} takeover".format(content)

        else:
            print("unrecognized command")

        return decoded
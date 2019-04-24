class CommandParser:

    @staticmethod
    def parse_data(data):
        decoded = "".join(map(chr, data))
        print("CommandParser: {}".format(decoded))

        data = decoded.split(":")

        command = data[0]
        content = data[1]

        if command == "phrase":
            return content
        elif command == "artist":
            return "Artist: " + content
        else:
            print("unrecognized command")



        return decoded
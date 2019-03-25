class CommandParser:

    @staticmethod
    def parse_data(data):
        decoded = "".join(map(chr, data))
        print("CommandParser: {}".format(decoded))
        return decoded
from db_service import DatabaseService


class CommandParser:

    @staticmethod
    def decode(data):
        return "".join(map(chr, data))

    @staticmethod
    def parse_data(data, state):

        print("CommandParser: {}".format(data))


        if data[:4] == "sync":
            CommandParser.sync_phrases(data[5:])
            return

        commands = data.split(";")

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


    @staticmethod
    def sync_phrases(sync_data):
        phrases = filter(None, sync_data.split('|'))

        for phrase_arg_string in phrases:

            args = filter(None, phrase_arg_string.split(";"))

            arg_dict = {}

            for arg in args:

                kv_pair = list(filter(None, arg.split("=", 2)))

                key = kv_pair[0]
                value = kv_pair[1]

                arg_dict[key] = value

            DatabaseService().insert_phrase(arg_dict)


        DatabaseService().select_all_phrases()


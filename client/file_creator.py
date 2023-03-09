import random

class FileCreator:

    def create_json(self, s1, s2, method):

        params = [s1, s2]
        param_types = [type(s1), type(s2)]
        id = random.randint(1, 1024)

        context = """
        {
            "method": "{}",
            "params": "{}",
            "param_types": {},
            "id": {}
        }        
        """.format(method, params, param_types, id)

        file = open("./json/request.json", "w")
        file.write(context)
        file.close()

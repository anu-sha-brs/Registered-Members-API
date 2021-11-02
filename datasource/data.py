import requests

DATA_SOURCE = "https://reqres.in/"

class DataSource():
    """ Data Source Class contains the functionality to send requests to a Data Source api. 

    Attributes:
      data_source (str): Base Url of the data source api
    """
    def __init__(self, data_source):
        self.__data_source = data_source
    
    def check_for_registered_user(self, user_id):
        """
        Checks if the users are registered in the datasource 
        """
        response = requests.get(self.__data_source + "api/users/" + str(user_id))
        resp = response.json()
        if (resp == {}):
            return False
        return True

    def get_all_users(self):
        """
        Fetches all the users that are registered in the datasource 
        """
        response = requests.get(self.__data_source + "api/users")
        print(response.json())
        resp = response.json()
        pages  = resp['total_pages']
        counter = 1
        data = resp["data"]
        while counter < pages:
            counter += 1
            resp = (requests.get(self.__data_source + "api/users?" + "page=" + str(counter))).json()
            data += resp["data"]
        return data

    def get_single_user(self, user_id):
        """
        Fetches a single user registered in the datasource 
        """
        print("api/" + 'user_id')
        response = requests.get(self.__data_source + "api/users/" + str(user_id))
        resp = response.json()
        data = resp["data"]
        return data

    def get_all_users_names(self):
        """
        Fetches all the user names list who are registered in the datasource 
        """
        names = []
        response = requests.get(self.__data_source + "api/users")
        res = response.json()
        pages  = res['total_pages']
        counter = 1
        data = res["data"]
        while counter < pages:
            counter += 1
            resp = (requests.get(self.__data_source + "api/users?" + "page=" + str(counter))).json()
            data += resp["data"]
        for i in range(len(data)):
            print("The name is: {}".format(data[i]["first_name"]))
            names.append(data[i]["first_name"])
        return names


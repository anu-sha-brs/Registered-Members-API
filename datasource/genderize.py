import requests
import json
import pandas as pd

class GenderStatistics():
    """ GenderStatics Class contains the functionality to send requests to a Genderize api and fetch statistics. 
    """
    def __init__(self) -> None:
        pass

    def get_names_gender_statistics(self, names):
        request_url = ""
        counter = 0
        responses = {}
         
        if not isinstance(names, list):
            names = [names, ]

        for name in names:
            if request_url == "":
                request_url = "name[]=" + name
                counter += 1
            else:
                request_url = request_url + "&name[]=" + name
                counter += 1

        req = requests.get("https://api.genderize.io?" + request_url)
        results = json.loads(req.text)

        #convert to a dataframe to perform statistical analysis
        df = pd.DataFrame(results)

        male_probability = round(
            df.loc[df['gender'] == 'male', 'probability'].sum()/counter, 2)

        male_percentage = str(
            int((df.loc[df['gender'] == 'male', 'probability'].count()/counter)*100)) + "%"

        female_probability = round(
            df.loc[df['gender'] == 'female', 'probability'].sum()/counter, 2)

        female_percentage = str(
            int((df.loc[df['gender'] == 'female', 'probability'].count()/counter)*100)) + "%"

        divers_probability = round(
            df.loc[df['gender'] == 'divers', 'probability'].sum()/counter, 2)

        divers_percentage = str(
            int((df.loc[df['gender'] == 'divers', 'probability'].count()/counter)*100)) + "%"

        data = {'gender': ['male', 'female', 'divers'],

                'percentage': [male_percentage, female_percentage, divers_percentage],

                'average_probability': [male_probability, female_probability, divers_probability]}

        res = pd.DataFrame(
            data, columns=['gender',  'percentage',  'average_probability'])

        responses["total_number"] = counter

        responses["data"] = res.to_dict('records')

        return responses

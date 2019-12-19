import twitter  # python-twitter api
import Twitter.config
import json


def init_twitter_api():
    api_key = init_key()
    api_secret_key = init_secret_key()
    api_token = init_token()
    api_secret_token = init_secret_token()

    api = twitter.Api(
        consumer_key=api_key,
        consumer_secret=api_secret_key,
        access_token_key=api_token,
        access_token_secret=api_secret_token
    )
    return api


def init_key():
    print("Gathering user developer Key...")
    with open('a_data_processing/config/Twitter/Key.txt', 'r') as key:
        api_key = key.read()
    return api_key


def init_secret_key():
    print("Gathering secret user developer Key...")
    with open('a_data_processing/config/Twitter/Key_secret.txt', 'r') as key:
        api_secret_key = key.read()
    return api_secret_key


def init_token():
    print("Gathering user developer Token...")
    with open('a_data_processing/config/Twitter/Token.txt', 'r') as token:
        api_token = token.read()
    return api_token


def init_secret_token():
    print("Gathering secret user developer Token...")
    with open('a_data_processing/config/Twitter/Token_secret.txt', 'r') as token:
        api_secret_token = token.read()
    return api_secret_token


# ---------------------------------------------------------------------------------------------------------------------


def api_manager():
    process = init_twitter_api()
    data = get_woeid_trends(process)
    return data


def get_global_trends(process):
    pass


def get_woeid_trends(process):

    # variable which will be hold the data
    data = {"Data": []}

    # opening the WOEID made by the Yahoo Weather API into a dictionary
    with open("C:a_data_processing/config/woeid_BR.json", "r") as code:
        states = json.load(code)

    states = states["Brasil"]

    # creating an index
    index = 1

    # accessing the WOEID data
    for i in range(len(states)):

        # calling to get trends and creating dictionary
        for j, k in states[i].items():
            data["Data"].append({})

            for m, n in states[i][j].items():
                if m == "WOEID":
                    trends = process.GetTrendsCurrent(n)

                    # accessing twitter list of "Model"s object data type
                    for p in range(len(trends)):
                        print(f"Getting trending information - {index}")
                        data["Data"][i].update({index: {}})
                        data["Data"][i][index].update({"State Name": j})
                        data["Data"][i][index].update({"Position": p+1})
                        data["Data"][i][index].update({"Trend Name": trends[p].name})
                        data["Data"][i][index].update({"Time Query": trends[p].timestamp})
                        data["Data"][i][index].update({"URL": trends[p].url})
                        index += 1

    return data



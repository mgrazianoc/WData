import yweather  # python module to use Yahoo! API
import pycountry


def api_manager(parser):

    # get_states_from_country returns a dict of states
    states = get_states_from_country(parser.country)

    print(states)

    data = get_woeid(states, parser.country)

    return data


def get_states_from_country(code):

    states = pycountry.subdivisions.get(country_code=code)
    data = {"Brasil": []}
    count = 0
    for j in states:
        state = j
        data["Brasil"].append({})
        data["Brasil"][count].update({state.code: state.name})
        count += 1
    return data


def get_woeid(states, country):

    # Initializing Yahoo Weather API
    client = yweather.Client()

    data = {"Brasil": []}

    for i in range(len(states["Brasil"])):
        for j, k in states["Brasil"][i].items():
            data["Brasil"].append({k: {}})
            data["Brasil"][i][k].update({"Code": j})
            data["Brasil"][i][k].update({"WOEID": int(client.fetch_woeid(f"{k}, Brasil"))})

    return data

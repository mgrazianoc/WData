def filter_manager(data):
    filtered_data = get_trends(data)
    final_fata = time_construct(filtered_data)
    return final_fata


def get_trends(data):
    trends = {"Data": []}

    index = 0
    for i in range(len(data["Data"])):
        for j, k in data["Data"][i].items():
            trends["Data"].append({"Index": index+1})
            for m, n in k.items():
                trends["Data"][index].update({m: n})
            index += 1

    return trends


def time_construct(data):
    trends = {"Data": []}

    for i in range(len(data["Data"])):
        trends["Data"].append({})
        for j, k in data["Data"][i].items():
            if j != "Time Query":
                trends["Data"][i].update({j: k})
            else:
                trends["Data"][i].update({"Date Query": k[:10]})

                # adjusting time zone, with less three hours. UGLY, I know...
                time = k[11:19]
                hour = int(time[:2])
                hour = (hour-3) % 24
                if hour < 10:
                    time = f"0{hour}" + time[2:]
                else:
                    time = f"{hour} " + time[2:]
                trends["Data"][i].update({"Time Query": time})

    return trends

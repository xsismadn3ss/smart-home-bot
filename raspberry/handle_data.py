from data import humidity_queries, temperature_queries

def avg(mesures):
    avg = sum(mesures)/ len(mesures)
    return avg

async def save_data(h_list, t_list, count):
    if count == 5:
        print("Guardando datos...")
        h_avg = avg(h_list)
        t_avg = avg(t_list)

        await humidity_queries.insert(h_avg)
        await temperature_queries.insert(t_avg)
        h_list = []
        t_list = []
        i = 0
        return h_list, t_list, count
    else:
        return h_list, t_list, count
# import requests

# resp_hulk = requests.get("https://superheroapi.com/api/2619421814940190/search/Hulk")
# resp_id_hulk = requests.get('https://superheroapi.com/api/2619421814940190/547/powerstats')
# # print(resp_hulk.text)
# hulk = resp_id_hulk.json()['intelligence']
# resp_america = requests.get("https://superheroapi.com/api/2619421814940190/search/Captain America")
# resp_id_america = requests.get('https://superheroapi.com/api/2619421814940190/149/powerstats')
# # print(resp_america.text)
# america = resp_id_america.json()['intelligence']
# resp_Thanos = requests.get("https://superheroapi.com/api/2619421814940190/search/Thanos")
# resp_id_Thanos = requests.get('https://superheroapi.com/api/2619421814940190/655/powerstats')
# #print(resp_Thanos.text)
# thanos = resp_id_Thanos.json()['intelligence']
# #print(thanos)

# # max_int = [hulk, america, thanos]
# # print(max(max_int))






import requests

hero_list_data = ['Hulk', 'Captain', 'America', 'Thanos']


def get_data(hero_list):
    result_data = {}
    for hero in hero_list:
        result = requests.get(f'https://www.superheroapi.com/api.php/2619421814940190/search/{hero}')
        result_data[result.json()['results'][0]['name']] = result.json()['results'][0]['powerstats']['intelligence']


    return result_data

result = get_data(hero_list_data)
# print(result) 

max_result = [(a,b) for a, b in result.items()]
print (max(max_result)[0])
import pprint

pp = pprint.PrettyPrinter()

#validation that variables are defined
def vars_exist(player):
    attributes = ['age', 'firstname', 'id', 'lastname', 'position']
    for attr in attributes:
        if attr not in player: return False
        if not player[attr]: return False     
    return True

#return format for name brief for specific sport
def get_name_brief(sport, player):
    firstname = player['firstname']
    lastname = player['lastname']
    if(sport == 'baseball'):    return firstname[0] + '. ' + lastname[0] + '.'
    if(sport == 'basketball'):  return firstname +' ' + lastname[0] + '.'
    if(sport == 'football'):    return firstname[0] + '. ' + lastname

#check for duplicate data inside the databases collection and only insert if its not there
def insert(collection, data, query):
    info = collection.find_one(query)

    if info == None: 
        collection.insert(data)
        return True

    return False        

#updates position info that already exists
def update_position(collection, query, player):
    position_object = collection.find_one(query) 
    position_info = position_object['position_info']

    identifier = {'_id':position_object['_id']}
    update = {
        '$inc' : { 'position_info.players': 1, 'position_info.age_total': player['age']},
        '$set' : { 'position_info.avg_age': (position_info['avg_age']*position_info['players'] + player['age'])//(position_info['players'] + 1) }
    }

    #update document in mongo collection
    collection.update(identifier, update)

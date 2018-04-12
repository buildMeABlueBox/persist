#validation that variables are defined
def vars_exist(player):
    attributes = ['age', 'firstname', 'id', 'lastname', 'position']
    for attr in attributes:
        if attr not in player: return False
        if not player[attr]: return False     
    return True

#return format for name brief for specific sport
def get_name_brief(sport, player):
    firstname = player.firstname
    lastname = player.lastname
    if(sport == 'baseball'):    return firstname[0] + '. ' + lastname[0] + '.'
    if(sport == 'basketball'):  return firstname +' ' + lastname[0] + '.'
    if(sport == 'football'):    return firstname[0] + '. ' + lastname

#check for duplicate data inside the databases collection and only insert if its not there
def insert(collection, data):
    identifier = data.keys[0]
    info = collection.find(identifier) #found unique object

    if info.count() == 0: 
        collection.insert(data)        
    
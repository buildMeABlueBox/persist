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
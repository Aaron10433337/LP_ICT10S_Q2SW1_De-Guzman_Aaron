from pyscript import document

def candidate_checker(e):
    club_members = {'kyle delacalzada','aaron deguzman','river datils','gilliah tabaldo','franco sulla',
                    'millicent menesses','angelica del rosario','lexie uaje'
                    ,'rafael dawinan','zachary tan', 'belle serdena', 'antonio salonga',
                    'calvin justo', 'agatha palico', 'prince berces', 'luis villafranca', 'radika evangelio', 'lan aguilar','mara fado'}


    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name
    member_checker = candidate.lower() in club_members
    messages = (f'Sorry {candidate}, your name is not on the list', f'Congratulations {candidate}! You are now part of the Band' )
    document.getElementById('result').innerHTML=messages[member_checker]
#Shake processing
import json
def match_shakes(json_shake1,json_shake2):
    shake1=json.loads(json_shake1)
    shake2=json.loads(json_shake2)
    timeframe=1000
    quick_match_threshold=50  #0-100
    if quick_match(shake1,shake2,quick_match_threshold)>quick_match_threshold:
        return precise_match_shakes(shake1, shake2, timeframe)
    else:
        return "not even close"

def quick_match(shake1, shake2,threshold):
    time_const=1  #Change this
    length_const=1 #change this
    rank=100
    rank-=length_const*(abs(len(shake1)-len(shake2))**2)
    rank-=time_const*(abs(shake1[0]['time']-shake2[-1]['time'])**2)
    return rank

def precise_match_shakes(shake1, shake2, timeframe):
    match_threshold=10
    min_diff=10000  #change this
    min_diff_index=-1
    for x in range(timeframe):
        diff=0
        for y in range(min(len(shake1),len(shake2))):
            diff+=(abs(shake1[y]['time']-shake2[y]['time'])**2)
        if diff<match_threshold:
            if magnitude_match(shake1, shake2):
                min_diff=diff
                min_diff_index=x
    if min_diff_index==-1:
        return "No match!"
    return min_diff_index

def magnitude_match(shake1, shake2):
    diff=0
    magnitude_threshold=100   #change this
    for x in range(min(len(shake1),len(shake2))):
        diff+=abs(shake1[y]['mag']-shake2[y]['mag'])**2
    if diff<magnitude_threshold:
        return True
    else:
        return False

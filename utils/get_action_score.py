import data
import math

def get_action_score(action_type):
    """
    Given the action_type of a session return a score to assign to the reference id house
    :param action_type: string of the action type
    :return: score
    """
    dict = {
        'clickout item': 1,
        'interaction item rating': 2,
        'interaction item info': 3,
        'interaction item image': 4,
        'interaction item deals': 5,
        'search for item': 6,
        'search for destination': 'reset',
        'change of sort order': None,
        'filter selection': None,
        'search for poi': None
    }

    if action_type not in dict.keys():
        print("error: WRONG ACTION TYPE")
        exit(0)
    return dict[action_type]


def time_weight(weight_function, session_length):
    """
    :param weight_function:
    :param session_lenght:
    :return:
    """
    weight_array = []
    if weight_function == 'exp':
        pass
    if weight_function == 'lin':
        for i in range(session_length):
            weight_array.append((i+1)/session_length)
        return weight_array
    print('error: weight function not defined')
    exit(0)



if __name__ == '__main__':
    #print(get_action_score('clickout_item'))
    print(time_weight('lin', 3522))


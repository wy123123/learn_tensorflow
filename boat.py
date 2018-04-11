import pandas as pd
import itertools
import random
bank = {'a_to_b':[1,2,3,4],'b_to_a':[]}
boat = {'trip':[],'boat_value':[]}
df = pd.DataFrame(columns=['counter','trip','numbers'])


def current_rule(boat):
    boat_value = sum(boat['boat_value'])
    return [boat_value-1,boat_value,boat_value+1]


def boat_value(boat):
    return sum(boat)


def update_bank(bank,boat):
    if boat['trip'] == 'a_to_b':
        bank['a_to_b'] = list(set(bank['a_to_b'])-set(boat['boat_value']))
        bank['b_to_a'] = bank['b_to_a'] + list(boat['boat_value'])
        return bank
    if boat['trip']:
        bank['b_to_a'] = list(set(bank['b_to_a'])-set(boat['boat_value']))
        bank['a_to_b'] = bank['a_to_b'] + list(boat['boat_value'])
        return bank


def trip(start=None, trip=None, bank=None):
    if start == True:
    # randomly pick two nunmber
        boat['trip'] = 'a_to_b'
        boat['boat_value'] = (random.choice(list(itertools.combinations([1,2,3,4],2))))
        return boat
    else:
        v = random.choice(list(itertools.combinations(bank[trip],2))+[bank[trip]])
        boat['trip'] = trip
        boat['boat_value'] = v
        return boat


def validate_trip(trip, rule):
    if type(trip['boat_value']) == int:
        v = trip['boat_value']
    else:
        v= sum(list(trip['boat_value']))
    if v in rule:
        return True
    else:
        return False


def main():
    counter = 0
    NewTrip = True
    restart = False
    stop = False
    trip_counter = 0
    while stop == False:
        # start a trip
        if NewTrip:
            print '###### New trip'
            current_trip = trip(start=NewTrip)
            is_validate_trip = True
            bank = {'a_to_b':[1,2,3,4],'b_to_a':[]}
            boat = {'trip':[],'boat_value':[]}
            c_trip = 'a_to_b'
            NewTrip = False
        else:
            print 'generating a new trip'
            current_trip = trip(trip=next_trip,bank=bank)
            is_validate_trip = validate_trip(current_trip, c_rule)

        if is_validate_trip:
            df = df.append({'counter':counter,
                            'trip':current_trip['trip'],
                            'numbers':current_trip['boat_value']},
                           ignore_index=True)
            bank = update_bank(bank,current_trip)
            if current_trip['trip'] == 'a_to_b':
                next_trip = 'b_to_a'
            else:
                next_trip = 'a_to_b'
            c_rule = current_rule(current_trip)
            print 'new rule' , c_rule
            trip_counter += 1
        else:
            print '{}_trip ends.'.format(counter)
            counter += 1
            trip_counter = 0
            NewTrip = True
            continue

        if len(bank['b_to_a']) == 4:
            print '{}_trip_success.'.format(counter)
            stop = True
        else:
            print '{}_{}_current_trip : '.format(counter,trip_counter), current_trip
            print '{}_{}_current_bank : '.format(counter,trip_counter), bank
            print '_____________'
            print 'starting next trip:'

    df.to_csv("./found_it.csv",index=False)

if __name__ == '__main__':
    main()
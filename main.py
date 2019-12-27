from tweet_functions import post_tweet, setup_api, get_last_tweet
from marine_traffic import get_last_port_call, get_port_name, get_local_time, get_ship_name, \
    get_time_difference_of_port

# Test vessels
SCHLESWIG_HOLSTEIN = 211190000
SEAROAD_MERSEY = 345040031
WHYDAH_OF_BRISTOL = 211682490

def main(request):
    tweet_last_port_call(WHYDAH_OF_BRISTOL)


def tweet_last_port_call(vessel_id):
    last_port_call = get_last_port_call(vessel_id)
    if last_port_call:
        tweet(last_port_call)
    else:
        print('No port call received')


def tweet(last_port_call):
    port = get_port_name(last_port_call)
    time = get_local_time(last_port_call)
    ship_name = get_ship_name(last_port_call)
    time_difference = get_time_difference_of_port(last_port_call)
    if time_difference == 0:
        content = 'Die ' + ship_name + ' hat um ' + time.strftime("%H:%M") + ' den Hafen ' + port + ' erreicht.'
    else:
        content = 'Die ' + ship_name + ' hat um ' + time.strftime(
            "%H:%M") + ' lokaler Zeit den Hafen ' + port + ' erreicht. Der Zeitunterschied zu Deutschland beträgt ' + str(
            time_difference) + ' Stunden'
    last_tweet = get_last_tweet()
    if content != last_tweet:
        post_tweet(content)
    else:
        print('Nothing changed ' + last_tweet)


if __name__ == '__main__':
    main("request")

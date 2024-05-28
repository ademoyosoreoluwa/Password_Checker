import tweepy
import time


def authenticate_twitter_app():
    auth = tweepy.OAuthHandler('dpLb3HY7kMqhBUW4ndhaxrqzR', 'ufQ6CpU9F2gMqXXv8Q7cCJjlXwZHzKJp8fdXckd10HeQdWbbsm')
    auth.set_access_token('228654225-OCMop8zYFqskWIjCyuqbsATWDJjo1iwdjzDCopQA',
                          'JrFBdI7Wvklh0KQph1MG9pgVfbftmZzILZjW9ljq2vW7v')
    api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except tweepy.TweepError as e:
        print(f"Error during authentication: {e}")
        return None

    return api


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


def main():
    api = authenticate_twitter_app()
    if api is None:
        return

    user = api.me()
    print("Username:", user.screen_name)
    print("Number of followers:", user.followers_count)

    search_string = 'python'
    numbersoftweet = 2

    for tweet in tweepy.Cursor(api.search_tweets, q=search_string).items(numbersoftweet):
        try:
            tweet.favorite()
            print('I liked that tweet')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

    for follower in limit_handler(tweepy.Cursor(api.followers).items()):
        if follower.followers_count > 5:
            follower.follow()
            print(f'Followed {follower.name}')

    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)



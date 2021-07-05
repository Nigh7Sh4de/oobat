import json
from random_word import RandomWords

def lambda_handler(event, context):

    word = r.get_random_word(includePartOfSpeech="noun")

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps({'word': word})
    }
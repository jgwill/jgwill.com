
import boto3
import json

with open('config.json') as json_file:
    config = json.load(json_file)

key = config['key']
secret = config['secret']
region = config['region']

polly = boto3.client('polly', aws_access_key_id=key, aws_secret_access_key=secret, region_name=region)
text="""

## Quels sont les effets à long terme des troubles de l'attachement sur le développement de l'enfant?


Les troubles de l'attachement peuvent avoir des effets à long terme sur le développement de l'enfant. Selon les documents consultés, ces troubles peuvent désorienter et éloigner l'enfant de son orientation créative. Les réactions à la réalité, telles que celles provoquées par un choc post-traumatique, peuvent perturber sa capacité à maintenir une focalisation sur ses valeurs et aspirations personnelles. Ces réactions peuvent être des mécanismes de défense ou des réponses conditionnées qui peuvent entraver son potentiel créatif.

Il est important de reconnaître que les troubles de l'attachement peuvent créer une tension entre la réalité vécue par l'enfant et ce qu'il désire créer dans sa vie. Cette tension peut générer des énergies et un mouvement vers la résolution de cette tension. Il est donc essentiel d'aider l'enfant à reconnaître cette tension et à la transformer en une force motrice pour ses actions.

La pratique de la tension structurelle peut être utile dans ce processus. Elle consiste à se concentrer pendant quelques instants sur ce que l'enfant désire créer, puis sur la réalité de sa situation actuelle et enfin sur le moment où il souhaite réaliser son désir. Cette pratique permet de créer une charte de tension structurelle qui aide à visualiser le chemin à parcourir pour atteindre le résultat souhaité.

Il est également important de noter que la créativité n'est pas la même chose que la création. La créativité est une qualité humaine qui peut être présente chez une personne, mais cela ne signifie pas qu'elle est automatiquement un créateur. La création est une orientation qui nécessite un travail spécifique pour maîtriser son processus créatif. Les troubles de l'attachement peuvent affecter cette orientation et demander un travail supplémentaire pour se libérer des schémas de réaction conditionnés.

En conclusion, les troubles de l'attachement peuvent avoir des effets à long terme sur le développement de l'enfant en perturbant son orientation créative. Il est important de reconnaître cette réalité et d'aider l'enfant à transformer cette tension en une force motrice pour ses actions.




"""
en="Joanna"
fr='Celine'

vid=fr
outfile='t_CoAiARR-Attachement240405-002-Impact.mp3'
response = polly.synthesize_speech(Text=text,
                                   OutputFormat="mp3",
                                   VoiceId=vid)

file = open(outfile, 'wb')
file.write(response['AudioStream'].read())
file.close()


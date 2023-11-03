import boto3
from boto3.dynamodb.conditions import Attr
tableName = 'users'

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
db = dynamodb.Table(tableName)

  
# create table 
table = dynamodb.create_table(
    TableName=tableName,
    KeySchema=[
        {
            'AttributeName': 'last_name',
            'KeyType': 'HASH' 
        },
        {
            'AttributeName': 'age',
            'KeyType': 'RANGE' 
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'age',
            'AttributeType': 'N' 
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

#insert items
item1 = db.put_item(
    Item={
        'last_name': 'Johnson',
        'first_name': 'Benjamin',
        'age': 28,
        'id': 49387266
        }
    )
print(item1)
item2 = db.put_item(
    Item={
        'last_name': 'Jones',
        'first_name': 'Mary',
        'age': 42,
        'id': 49387267
        }
    )
print(item2)

item3 = db.put_item(
    Item={
        'last_name': 'Johnson',
        'first_name': 'Joe',
        'age': 33,
        'id': 49387268
        }
    )
print(item3)

allUsers = db.scan()
print(allUsers)

#Get all users with last name of Johnson
johnsons = db.scan(
    FilterExpression=Attr('last_name').eq("Johnson")
)
print(johnsons)

#Get all users over the age of 30
overThirty = db.scan(
    FilterExpression=Attr('age').gt(30)
)
print(overThirty['Items'])

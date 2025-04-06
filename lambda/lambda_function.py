
import boto3
import os
import json

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        card_number = event.get('queryStringParameters', {}).get('bin')
        print(f"[DEBUG] Received card_number: {card_number}")

        # Directly get item by BIN
        response = table.get_item(Key={'bin': card_number})
        item = response.get('Item')

        if item:
            print(f"[DEBUG] Match found for BIN: {card_number}")
            return {
                'statusCode': 200,
                'body': json.dumps({'coupon': 1})
            }
        else:
            print(f"[DEBUG] No match found for BIN: {card_number}")
            return {
                'statusCode': 200,
                'body': json.dumps({'coupon': 2})
            }

    except Exception as e:
        print(f"[ERROR] Lambda execution failed: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal server error. Please try again later.'})
        }

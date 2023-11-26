import boto3

def lambda_handler(event, context):
    ecs_region = 'ap-southeast-2'
    cluster_name = 'prods'  # Replace with your ECS cluster name
    service_name = 'dots'  # Replace with your ECS service name

    desired_count = 0 if event['status'] == 'stop' else 1

    params = {
        'cluster': cluster_name,
        'service': service_name,
        'desiredCount': desired_count
    }

    ecs = boto3.client('ecs', region_name=ecs_region)

    try:
        response = ecs.update_service(**params)
        print('Service updated successfully:', response)
        return {
            'statusCode': 200,
            'body': 'Service updated successfully'
        }
    except Exception as e:
        print('Error updating service:', e)
        return {
            'statusCode': 500,
            'body': f'Error updating service: {str(e)}'
        }
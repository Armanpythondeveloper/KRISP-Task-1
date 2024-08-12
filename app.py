import psycopg2
import json
from datetime import datetime

def get_db_connection():
    conn = psycopg2.connect(
        dbname='metrics_db',
        user='postgres',
        password='testpassword1234',
        host='db',
        port="5432"
    )
    return conn

def insert_metric(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO user_metrics (user_id, metric_type, talked_time, microphone_used, speaker_used, voice_sentiment, timestamp, session_metadata)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        data['user_id'],
        data['metric_type'],
        data.get('talked_time'),
        data.get('microphone_used'),
        data.get('speaker_used'),
        data.get('voice_sentiment'),
        datetime.utcnow(),
        json.dumps(data.get('session_metadata', {}))
    ))

    conn.commit()
    cursor.close()
    conn.close()

sample_data = {
    'user_id': 'user123',
    'metric_type': 'talked_time',
    'talked_time': 120,
    'microphone_used': True,
    'speaker_used': False,
    'voice_sentiment': 'positive',
    'session_metadata': {'session_id': 'session456'}
}

insert_metric(sample_data)

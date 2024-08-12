
CREATE TABLE user_metrics (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    metric_type VARCHAR(50) NOT NULL,
    talked_time INT,
    microphone_used BOOLEAN,
    speaker_used BOOLEAN,
    voice_sentiment VARCHAR(50),
    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    session_metadata JSONB
);

CREATE INDEX idx_user_id ON user_metrics(user_id);
CREATE INDEX idx_metric_type ON user_metrics(metric_type);
CREATE INDEX idx_timestamp ON user_metrics(timestamp);

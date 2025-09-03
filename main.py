from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello, DataOS!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050)


# #!/usr/bin/env python3
# import os
# import sys
# from modules.data_processor import DataProcessor

# def main():
#     # Access environment variables
#     log_level = os.getenv('LOG_LEVEL', 'INFO')
#     batch_size = int(os.getenv('BATCH_SIZE', '100'))
    
#     # Access DataOS secrets (if configured)
#     secret_path = os.getenv('DATAOS_SECRET_MOUNT_PATH', '/etc/dataos/secrets')
    
#     print(f"Starting application with log level: {log_level}")
    
#     # Your application logic
#     processor = DataProcessor(batch_size=batch_size)
#     processor.run()
    
#     print("Application completed successfully")

# if __name__ == "__main__":
#     main()

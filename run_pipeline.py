from data_pipeline_sdk import DataPipelineSDK

if __name__ == "__main__":
    sdk = DataPipelineSDK(config_file='config.json')
    sdk.process_data()

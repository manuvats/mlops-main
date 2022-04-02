import os
import argparse
import yaml
import logging

if __name__=="__main__":
    args = argparse.ArgumentParser()
    default_config_path = os.path.join("config", "params.yaml")
    args.add_argument("--config", default="default")
    args.add_argument("--datasource", default=None)

    parsed_args = args.parse_args()
    print(parsed_args.config, parsed_args.datasource)


    
    

    
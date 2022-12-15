import configparser
import logging


config = configparser.ConfigParser()
config.read(".config")

API_TOKEN=config["API_TOKEN"]

print(API_TOKEN)


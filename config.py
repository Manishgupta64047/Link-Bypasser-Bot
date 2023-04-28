# To get values from Environment (True/False)
Get_ENV = True

# Required if Get_ENV == False
Vars = [
    # Bot API Token
    "",
    # GdToT Crypt
    "",
    # Laravel Session
    "",
    # XSRF_TOKEN 
    "",
    # KOLOP_CRYPT
    "",
    # DRIVEFIRE_CRYPT
    "",
    # HUBDRIVE_CRYPT
    "",
    # KATDRIVE_CRYPT
    "",
    # UPTOBOX_TOKEN
    ""
]

# AppDrive or DriveApp Account credentials
# To bypass limits imposed on Anonymous users
# Will also work/used for look-a-like sites

Creds = [
    # AppDrive/DriveApp Email ID
    "",
    # AppDrive/DriveApp Password
    ""
]

APIs = [
    "https://us-central1-my-apps-server.cloudfunctions.net/r?shortid=",
    "https://api.emilyx.in/api",
    "https://api.bypass.vip/",
    "https://api.gofile.io"
]

import os, sys
import logging as log

# Setup Logger
log.basicConfig(
    level=log.INFO,
    datefmt="%d/%m/%Y %H:%M:%S",
    format="[%(asctime)s][%(levelname)s] => %(message)s",
    handlers=[log.StreamHandler(stream=sys.stdout),
              log.FileHandler("runtime-log.txt", mode="a", encoding="utf-8")],)

def check():
    if not Vars[0]:
        log.error("Bot API Token not found!")
        raise ValueError('Bot API Token cannot be empty!')
    else:
        log.info("Found Bot API Token.")

    if not Vars[1]:
        log.warning("GdToT Crypt not provided!")
    else:
        log.info("Found GdToT Crypt.")

    if not Vars[2]:
        log.warning("Laravel Session not provided!")
    else:
        log.info("Found Laravel Session.")

    if not Vars[3]:
        log.warning("XSRF_TOKEN not provided!")
    else:
        log.info("Found XSRF_TOKEN.")

    if not Vars[4]:
        log.warning("KOLOP_CRYPT not provided!")
    else:
        log.info("Found KOLOP_CRYPT.")

    if not Vars[5]:
        log.warning("DRIVEFIRE_CRYPT not provided!")
    else:
        log.info("Found DRIVEFIRE_CRYPT.")

    if not Vars[6]:
        log.warning("HUBDRIVE_CRYPT not provided!")
    else:
        log.info("Found HUBDRIVE_CRYPT.")

    if not Vars[7]:
        log.warning("KATDRIVE_CRYPT not provided!")
    else:
        log.info("Found KATDRIVE_CRYPT.")

    if not Vars[8]:
        log.warning("UPTOBOX_TOKEN not provided!")
    else:
        log.info("Found UPTOBOX_TOKEN.")
        
    log.info("Now checking for Credentials...")
    
    if not Creds[0] or not Creds[1]:
        log.warning("AppDrive or DriveApp Credentials not found! Limit will be imposed on Anonymous user.")
    else:
        log.info("AppDrive or DriveApp Credentials found.")
    
    if Get_ENV == False:
        log.info("Got Values from config file!")
    else:
        log.info("Got Values from System Environment!")

if Get_ENV == False:
    log.info("Getting Values from config file...")
    check()
elif Get_ENV == True:
    log.info("Getting Values from System Environment...")
    TOKEN = os.environ.get("TOKEN","5830686309:AAGDqbnwi7XqAeYA69Pfm-f9ersIPyoLQZk")
    GDTot_Crypt = os.environ.get("Crypt","")
    Laravel_Session = os.environ.get("Laravel_Session","")
    XSRF_TOKEN = os.environ.get("XSRF_TOKEN","")
    KCRYPT = os.environ.get("KOLOP_CRYPT","from re import match as rematch, findall, sub as resub

import requests

from requests import get as rget

import base64

from urllib.parse import unquote, urlparse, parse_qs, quote

import time

import cloudscraper

from bs4 import BeautifulSoup, NavigableString, Tag

from lxml import etree

import hashlib

import json

from dotenv import load_dotenv

load_dotenv()

from asyncio import sleep as asleep

import os

import ddl

##########################################################

# ENVs

GDTot_Crypt = os.environ.get("CRYPT","b0lDek5LSCt6ZjVRR2EwZnY4T1EvVndqeDRtbCtTWmMwcGNuKy8wYWpDaz0%3D")

Laravel_Session = os.environ.get("Laravel_Session","")

XSRF_TOKEN = os.environ.get("XSRF_TOKEN","")

DCRYPT = os.environ.get("DRIVEFIRE_CRYPT","")

KCRYPT = os.environ.get("KOLOP_CRYPT","aWFicnVaNWh4TThRbzFqdkE2U2FKNmJOTWhvWkZmbWswaUFadTB5NXJ3RT0%3D")
    DCRYPT = os.environ.get("DRIVEFIRE_CRYPT","")
    HCRYPT = os.environ.get("HUBDRIVE_CRYPT","Q29hdlpLUEZTSEJLUjVZRkZQSExLODFuWGVudUlNK0ZPZlZmS1hENWxZVT0")
    KATCRYPT = os.environ.get("KATDRIVE_CRYPT","")
    UPTOBOX = os.environ.get("UPTOBOX_TOKEN","")
    AD_EMAIL = os.environ.get("AD_EMAIL","")
    AD_PASS = os.environ.get("AD_PASS","")
    
    Vars = [
        TOKEN,
        GDTot_Crypt,
        Laravel_Session,
        XSRF_TOKEN,
        KCRYPT,
        DCRYPT,
        HCRYPT,
        KATCRYPT,
        UPTOBOX
    ]
    
    Creds = [
        AD_EMAIL,
        AD_PASS
    ]
    check()
else:
    log.error(r"Unable to undestand from where to get values?¯\_(ツ)_/¯")
    raise ValueError("Get_ENV value is invalid & should be True or False only!")

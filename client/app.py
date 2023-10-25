from flask import request
from flask import Flask, render_template, jsonify, get_template_attribute, make_response,redirect
from flask import abort
from flask import session, url_for
# from werkzeug import secure_filename
# import numpy as np
import json
import time
from python.client import Client
import copy
import os
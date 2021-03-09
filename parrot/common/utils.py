#!/usr/bin/env python
# -*- coding: utf-8 -*-


import uuid
import string
from pytz import timezone
import datetime
import random
import os
from parrot.common import config
from parrot import app, db
from parrot.users.models import *




def time_now():

    "return dattime in UTC"

    UTC = timezone('UTC')
    return datetime.datetime.now(UTC)





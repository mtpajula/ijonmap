#!/usr/bin/env python
# -*- coding: utf-8 -*-
from settings import Settings
from messages import Messages
from projects import Projects
from users.users import Users
from files.filemanager import Filemanager


class Controller(object):
    
    def __init__(self):
        self.projects = Projects()
        self.messages = Messages()
        self.users = Users()
        self.settings = Settings()
        self.filemanager = Filemanager(self.messages, self.settings, self.projects)
        self.projects.new_project()

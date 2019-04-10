# -*- coding: utf-8 -*-
__author__ = 'bars'

import configparser


class ParseConfig(object):

    """Docstring for ParseConfig. """

    def __init__(self, pipeline_config, read_from='file'):
        """TODO: to be defined1. """
        self.pipeline_config = pipeline_config
        self.read_from = read_from

    @property
    def config(self):
        if self.read_from == 'configparser':
            _config = self.pipeline_config
        else:
            _config = configparser.ConfigParser()
            _config._interpolation = configparser.ExtendedInterpolation()
            if self.read_from == 'string':
                _config.read_string(self.pipeline_config)
            else:
                _config.read(self.pipeline_config)
        return _config

    @property
    def task_list(self):
        task_list = [task for task in self.config['PIPELINE']['pipeline'].split(' ')]
        return task_list

    @property
    def task_args(self):
        task_args = {task: {arg: self.config[task][arg] for arg in list(
            self.config[task])} for task in self.task_list}
        return task_args

    @property
    def pipeline_args(self):
        return {arg: self.config['PIPELINE'][arg] for arg in self.config['PIPELINE']}

    @property
    def general_args(self):
        return {arg: self.config['GENERAL'][arg] for arg in self.config['GENERAL']}

    @property
    def default_args(self):
        return {arg: self.config['DEFAULT'][arg] for arg in self.config['DEFAULT']}

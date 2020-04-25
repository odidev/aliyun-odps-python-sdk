#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 1999-2018 Alibaba Group Holding Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from mars.worker import ProcessHelperActor as WorkerProcessHelperActor
from mars.scheduler.utils import SchedulerActor


class CupidSchedulerProcessHelperActor(SchedulerActor):
    def __init__(self):
        super(CupidSchedulerProcessHelperActor, self).__init__()
        self._cupid_context = None

    def post_create(self):
        super(CupidSchedulerProcessHelperActor, self).post_create()

    def start_channel(self, envs):
        from cupid import context

        os.environ.update(envs)
        self._cupid_context = context()


class CupidWorkerProcessHelperActor(WorkerProcessHelperActor):
    def __init__(self):
        super(CupidWorkerProcessHelperActor, self).__init__()
        self._cupid_context = None

    def post_create(self):
        super(CupidWorkerProcessHelperActor, self).post_create()

    def start_channel(self, envs):
        from cupid import context

        os.environ.update(envs)
        self._cupid_context = context()

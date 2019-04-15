# -*- coding: utf-8 -*-
# Copyright (C) 2014-2017 Andrey Antukh <niwi@niwi.nz>
# Copyright (C) 2014-2017 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014-2017 David Barragán <bameda@dbarragan.com>
# Copyright (C) 2014-2017 Alejandro Alonso <alejandro.alonso@kaleidos.net>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.utils import timezone

from . import models
import datetime



def calculate_milestone_is_closed(milestone):
    now = datetime.datetime.now().date()
    sprint_end_date = milestone.estimated_finish

    return (milestone.user_stories.all().count() >= 0 and
            all([task.status is not None and task.status.is_closed for task in milestone.tasks.all()]) and
            all([user_story.is_closed for user_story in milestone.user_stories.all()]) and (now >= sprint_end_date))


def close_milestone(milestone):
    if not milestone.closed:
        milestone.closed = True
        milestone.save(update_fields=["closed",])


def open_milestone(milestone):
    if milestone.closed:
        milestone.closed = False
        milestone.save(update_fields=["closed",])

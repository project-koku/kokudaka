#
# Copyright 2018 Red Hat, Inc.
#
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

"""Configuration loader for Kokudaka application."""

import os


# pylint: disable=too-few-public-methods
class Config(object):
    """Configuration for app."""

    DEBUG = os.getenv('KOKUDAKA_DEBUG', False)
    if isinstance(DEBUG, str) and DEBUG.lower() in ('f', 'false'):
        DEBUG = False

    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

    # Data directory for processing incoming data
    TMP_DIR = '/var/tmp/kokudaka'

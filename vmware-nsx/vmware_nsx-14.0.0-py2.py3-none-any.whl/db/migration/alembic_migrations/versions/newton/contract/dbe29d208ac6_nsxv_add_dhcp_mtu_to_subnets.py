# Copyright 2016 VMware, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""NSXv add DHCP MTU to subnets

Revision ID: dbe29d208ac6
Revises: 081af0e396d7
Create Date: 2016-07-21 05:03:35.369938

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'dbe29d208ac6'
down_revision = '081af0e396d7'


def upgrade():
    # Add a new column and make the previous column nullable,
    # because it is enough that one of them is non-null
    op.add_column('nsxv_subnet_ext_attributes',
                  sa.Column('dhcp_mtu', sa.Integer, nullable=True))
    op.alter_column('nsxv_subnet_ext_attributes', 'dns_search_domain',
                    nullable=True, existing_type=sa.String(length=255),
                    existing_nullable=False)

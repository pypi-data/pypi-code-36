# Generated by Django 2.1.5 on 2019-01-30 14:17

from django.db import migrations
import migrate_sql.operations


class Migration(migrations.Migration):

    dependencies = [
        ('pyfb_endpoint', '0004_auto_20181219_1402'),
    ]

    operations = [
        migrate_sql.operations.CreateSQL(
            name='subscriber_view',
            sql="DROP VIEW IF EXISTS subscriber CASCADE; CREATE OR REPLACE VIEW subscriber AS  SELECT row_number() OVER () AS id,  c.name AS username,  CAST('' AS VARCHAR) AS domain,  c.password FROM pyfb_endpoint_customer c WHERE c.enabled=True and c.registration=True;",
            reverse_sql='DROP subscriber',
        ),
        migrate_sql.operations.CreateSQL(
            name='address_view',
            sql='DROP VIEW IF EXISTS address CASCADE; CREATE OR REPLACE VIEW address AS SELECT row_number() OVER () AS id, * FROM (  SELECT  1 AS grp,  CAST(LEFT(CAST(c.sip_ip AS VARCHAR), LENGTH(CAST(c.sip_ip AS VARCHAR)) - 3) AS VARCHAR) AS ip_addr,  CAST(RIGHT(CAST(c.sip_ip AS VARCHAR), 2) AS INTEGER) AS mask,  CAST(c.sip_port AS INTEGER) AS port,  CAST(c.name AS VARCHAR) AS tag FROM pyfb_endpoint_customer c WHERE c.enabled=True and c.registration=False UNION ALL SELECT  10 AS grp,  CAST(sg.sip_proxy AS VARCHAR) AS ip_addr,  32 AS mask,  CAST(sg.sip_port AS INTEGER) AS port,  sg.name AS tag FROM pyfb_endpoint_provider sg WHERE sg.enabled=True and sg.register=False) v;',
            reverse_sql='DROP VIEW IF EXISTS address CASCADE ',
        ),
        migrate_sql.operations.CreateSQL(
            name='usrpref_view',
            sql="DROP VIEW IF EXISTS usr_preferences CASCADE; CREATE OR REPLACE VIEW usr_preferences AS SELECT row_number() OVER () AS id, * FROM (  SELECT DISTINCT  c.name AS uuid,  c.name AS username,  CAST('' AS VARCHAR) AS domain,  CAST('grpnormcallee' AS VARCHAR) AS attribute,  CAST(1 AS INT) AS type,  CAST(nrg.dpid_id AS VARCHAR) AS value,  CAST(now() AS timestamp without time zone) AS last_modified FROM pyfb_endpoint_customer c INNER JOIN pyfb_normalization_grp ng   ON ng.id = c.callee_norm_id INNER JOIN pyfb_normalization_rule_grp nrg  ON nrg.dpid_id = ng.id WHERE c.enabled=True UNION ALL   SELECT DISTINCT  c.name AS uuid,  c.name AS username,  CAST('' AS VARCHAR) AS domain,  CAST('grpnormcaller' AS VARCHAR) AS attribute,  CAST(1 AS INT) AS type,  CAST(nrg.dpid_id AS VARCHAR) AS value,  CAST(now() AS timestamp without time zone) AS last_modified FROM pyfb_endpoint_customer c INNER JOIN pyfb_normalization_grp ng   ON ng.id = c.callerid_norm_id INNER JOIN pyfb_normalization_rule_grp nrg  ON nrg.dpid_id = ng.id WHERE c.enabled=True UNION ALL   SELECT DISTINCT  c.name AS uuid,  c.name AS username,  CAST('' AS VARCHAR) AS domain,  CAST('grpnormcalleein' AS VARCHAR) AS attribute,  CAST(1 AS INT) AS type,  CAST(nrg.dpid_id AS VARCHAR) AS value,  CAST(now() AS timestamp without time zone) AS last_modified FROM pyfb_endpoint_customer c INNER JOIN pyfb_normalization_grp ng   ON ng.id = c.callee_norm_in_id INNER JOIN pyfb_normalization_rule_grp nrg  ON nrg.dpid_id = ng.id WHERE c.enabled=True UNION ALL   SELECT DISTINCT  c.name AS uuid,  c.name AS username,  CAST('' AS VARCHAR) AS domain,  CAST('grpnormcallerin' AS VARCHAR) AS attribute,  CAST(1 AS INT) AS type,  CAST(nrg.dpid_id AS VARCHAR) AS value,  CAST(now() AS timestamp without time zone) AS last_modified FROM pyfb_endpoint_customer c INNER JOIN pyfb_normalization_grp ng   ON ng.id = c.callerid_norm_in_id INNER JOIN pyfb_normalization_rule_grp nrg  ON nrg.dpid_id = ng.id WHERE c.enabled=True UNION ALL   SELECT DISTINCT  c.name AS uuid,  c.name AS username,  CAST('' AS VARCHAR) AS domain,  CAST('routinggrp' AS VARCHAR) AS attribute,  CAST(1 AS INT) AS type,  CAST(r.routinggroup_id AS VARCHAR) AS value,  CAST(now() AS timestamp without time zone) AS last_modified FROM pyfb_endpoint_customer c INNER JOIN pyfb_routing_c_routinggrp r   ON r.customer_id = c.customer_id WHERE c.enabled=True) v; ",
            reverse_sql='DROP VIEW IF EXISTS usr_preferences CASCADE; ',
        ),
    ]

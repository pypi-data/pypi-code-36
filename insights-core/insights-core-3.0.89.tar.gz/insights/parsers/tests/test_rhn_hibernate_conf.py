from insights.tests import context_wrap
from insights.parsers.rhn_hibernate_conf import RHNHibernateConf

conf_content = """
############################################################################
## HIBERNATE CONFIGURATION
##
## This is not the only way to configure hibernate.  You can
## create a hibernate.cfg.xml file or you can create your own
## custom file which you parse and create a new Configuration object.
##
## We're using the hibernate.properties file because it's simple.
############################################################################
hibernate.dialect=org.hibernate.dialect.Oracle10gDialect
hibernate.connection.driver_class=oracle.jdbc.driver.OracleDriver
hibernate.connection.driver_proto=
hibernate.connection.provider_class=org.hibernate.connection.C3P0ConnectionProvider

hibernate.use_outer_join=true
hibernate.jdbc.batch_size=0
#hibernate.show_sql=true

hibernate.c3p0.min_size=5
hibernate.c3p0.max_size=20
hibernate.c3p0.timeout=300
#
# This should always be 0.
#
hibernate.c3p0.max_statements=0

# test period value in seconds
hibernate.c3p0.idle_test_period=300
hibernate.c3p0.testConnectionOnCheckout=true
hibernate.c3p0.connectionCustomizerClassName=com.redhat.rhn.common.db.RhnConnectionCustomizer
hibernate.c3p0.preferredTestQuery=select 'c3p0 ping' from dual

hibernate.cache.provider_class=org.hibernate.cache.OSCacheProvider
hibernate.cache.use_query_cache=true
hibernate.bytecode.use_reflection_optimizer=false
hibernate.jdbc.batch_size=0
""".strip()


def test_rhn_hibernate_conf():
    result = RHNHibernateConf(context_wrap(conf_content))
    assert result.get("hibernate.c3p0.max_statements") == "0"
    assert result.get("hibernate.connection.driver_proto") == ""
    assert result.get("hibernate.c3p0.preferredTestQuery") == "select 'c3p0 ping' from dual"

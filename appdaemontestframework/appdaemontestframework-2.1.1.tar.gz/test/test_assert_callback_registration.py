from datetime import time

import appdaemon.plugins.hass.hassapi as hass
import pytest
from pytest import mark

from appdaemontestframework import automation_fixture


class MockAutomation(hass.Hass):
    should_listen_state = False
    should_listen_event = False
    should_register_run_daily = False

    def initialize(self):
        if self.should_listen_state:
            self.listen_state(self._my_listen_state_callback, 'some_entity', new='off')
        if self.should_listen_event:
            self.listen_event(self._my_listen_event_callback, 'zwave.scene_activated', scene_id=3)
        if self.should_register_run_daily:
            self.run_daily(self._my_run_daily_callback, time(hour=3, minute=7), extra_param='ok')

    def _my_listen_state_callback(self, entity, attribute, old, new, kwargs):
        pass

    def _my_listen_event_callback(self, event_name, data, kwargs):
        pass

    def _my_run_daily_callback(self, kwargs):
        pass

    def _some_other_function(self, entity, attribute, old, new, kwargs):
        pass

    def enable_listen_state_during_initialize(self):
        self.should_listen_state = True

    def enable_listen_event_during_initialize(self):
        self.should_listen_event = True

    def enable_register_run_daily_during_initialize(self):
        self.should_register_run_daily = True


@automation_fixture(MockAutomation)
def automation():
    pass


@mark.only
class TestAssertListenState:
    def test_success(self, automation: MockAutomation, assert_that):
        automation.enable_listen_state_during_initialize()

        assert_that(automation) \
            .listens_to.state('some_entity', new='off') \
            .with_callback(automation._my_listen_state_callback)

    def test_failure__not_listening(self, automation: MockAutomation, assert_that):
        with pytest.raises(AssertionError):
            assert_that(automation) \
                .listens_to.state('some_entity', new='off') \
                .with_callback(automation._my_listen_state_callback)

    def test_failure__wrong_entity(self, automation: MockAutomation, assert_that):
        automation.enable_listen_state_during_initialize()

        with pytest.raises(AssertionError):
            assert_that(automation) \
                .listens_to.state('WRONG', new='on') \
                .with_callback(automation._my_listen_state_callback)

    def test_failure__wrong_kwargs(self, automation: MockAutomation, assert_that):
        automation.enable_listen_state_during_initialize()

        with pytest.raises(AssertionError):
            assert_that(automation) \
                .listens_to.state('some_entity', new='WRONG') \
                .with_callback(automation._my_listen_state_callback)

        with pytest.raises(AssertionError):
            assert_that(automation) \
                .listens_to.state('some_entity', wrong='off') \
                .with_callback(automation._my_listen_state_callback)

    def test_failure__wrong_callback(self, automation: MockAutomation, assert_that):
        automation.enable_listen_state_during_initialize()

        with pytest.raises(AssertionError):
            assert_that(automation) \
                .listens_to.state('some_entity', new='on') \
                .with_callback(automation._some_other_function)


@mark.only
class TestAssertListenEvent:
    def test_success(self, automation: MockAutomation, assert_that):
        automation.enable_listen_event_during_initialize()

        assert_that(automation) \
            .listens_to.event('zwave.scene_activated', scene_id=3) \
            .with_callback(automation._my_listen_event_callback)

    def test_failure__not_listening(self, automation: MockAutomation, assert_that):
        with pytest.raises(AssertionError):
            assert_that(automation) \
                .listens_to.event('zwave.scene_activated', scene_id=3) \
                .with_callback(automation._my_listen_event_callback)

    def test_failure__wrong_event(self, automation: MockAutomation, assert_that):
        automation.enable_listen_state_during_initialize()

        with pytest.raises(AssertionError):
            assert_that(automation) \
                .listens_to.event('WRONG', scene_id=3) \
                .with_callback(automation._my_listen_event_callback)

    def test_failure__wrong_kwargs(self, automation: MockAutomation, assert_that):
        automation.enable_listen_state_during_initialize()

        with pytest.raises(AssertionError):
            assert_that(automation) \
                .listens_to.event('zwave.scene_activated', scene_id='WRONG') \
                .with_callback(automation._my_listen_event_callback)

        with pytest.raises(AssertionError):
            assert_that(automation) \
                .listens_to.event('zwave.scene_activated', wrong=3) \
                .with_callback(automation._my_listen_event_callback)

    def test_failure__wrong_callback(self, automation: MockAutomation, assert_that):
        automation.enable_listen_state_during_initialize()

        with pytest.raises(AssertionError):
            assert_that(automation) \
                .listens_to.event('zwave.scene_activated', scene_id=3) \
                .with_callback(automation._some_other_function)


@mark.only
class TestRegisteredRunDaily:
    def test_success(self, automation: MockAutomation, assert_that):
        automation.enable_register_run_daily_during_initialize()

        assert_that(automation) \
            .registered.run_daily(time(hour=3, minute=7), extra_param='ok') \
            .with_callback(automation._my_run_daily_callback)

    def test_failure__not_listening(self, automation: MockAutomation, assert_that):
        with pytest.raises(AssertionError):
            assert_that(automation) \
                .registered.run_daily(time(hour=3, minute=7), extra_param='ok') \
                .with_callback(automation._my_run_daily_callback)

    def test_failure__wrong_time(self, automation: MockAutomation, assert_that):
        automation.enable_register_run_daily_during_initialize()

        with pytest.raises(AssertionError):
            assert_that(automation) \
                .registered.run_daily(time(hour=4), extra_param='ok') \
                .with_callback(automation._my_run_daily_callback)

    def test_failure__wrong_kwargs(self, automation: MockAutomation, assert_that):
        automation.enable_register_run_daily_during_initialize()

        with pytest.raises(AssertionError):
            assert_that(automation) \
                .registered.run_daily(time(hour=3, minute=7), extra_param='WRONG') \
                .with_callback(automation._my_run_daily_callback)

        with pytest.raises(AssertionError):
            assert_that(automation) \
                .registered.run_daily(time(hour=3, minute=7), wrong='ok') \
                .with_callback(automation._my_run_daily_callback)

    def test_failure__wrong_callback(self, automation: MockAutomation, assert_that):
        automation.enable_register_run_daily_during_initialize()

        with pytest.raises(AssertionError):
            assert_that(automation) \
                .registered.run_daily(time(hour=3, minute=7), extra_param='ok') \
                .with_callback(automation._some_other_function)

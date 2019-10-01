from unittest import TestCase

from hamcrest import assert_that, equal_to

from pytest_reference_formatter.formatter import handling_references


class TestFormatter(TestCase):
    def test_single_reference_can_be_formatted(self):
        """ when user input has one parameter """
        single_reference_input = \
            ['paessler.license.tests.admin_testcases.test_activation.DeactivateSystemIDScenario.'
             'test_deactivating_systemid_creates_sales_comment']
        single_reference_input_with_django_sites_and_py = \
            ['django-sites.paessler.license.tests.admin_testcases.test_activation.py.DeactivateSystemIDScenario.'
             'test_deactivating_systemid_creates_sales_comment']
        single_reference_expected_output = \
            ['django-sites/paessler/license/tests/admin_testcases/test_activation.py::'
             'DeactivateSystemIDScenario::test_deactivating_systemid_creates_sales_comment']

        assert_that(handling_references(single_reference_input),
                    equal_to(single_reference_expected_output), 'identifier')
        assert_that(handling_references(single_reference_input_with_django_sites_and_py),
                    equal_to(single_reference_expected_output), 'identifier')

    def test_multiple_reference_can_be_formatted(self):
        """ when user input has more than one parameter """
        multiple_reference_input = \
            ['paessler.license.tests.admin_testcases.test_activation.DeactivateSystemIDScenario.'
             'test_deactivating_systemid_creates_sales_comment',
             'django-sites.paessler.license.tests.admin_testcases.test_activation.'
             'ChangeExpirationOfSystemIDGrantScenario.'
             'test_changing_expiration_for_systemid_creates_sales_comment']

        multiple_reference_expected_output = \
            ['django-sites/paessler/license/tests/admin_testcases/test_activation.py::'
             'DeactivateSystemIDScenario::'
             'test_deactivating_systemid_creates_sales_comment',
             'django-sites/paessler/license/tests/admin_testcases/test_activation.py::'
             'ChangeExpirationOfSystemIDGrantScenario::'
             'test_changing_expiration_for_systemid_creates_sales_comment']

        assert_that(handling_references(multiple_reference_input), equal_to(multiple_reference_expected_output))

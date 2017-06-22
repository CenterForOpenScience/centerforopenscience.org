import pytest # noqa

from django.test import TestCase
import common.blocks.codes as common


class CodeBlockTest(TestCase):

    def setUp(self):
        """ Establishes necessary variables """
        super(CodeBlockTest, self).setUp()
        self.block = common.CodeBlock()

    def test_render_template(self):
        """ Tests that the right template renders """
        template = self.block.meta.template
        self.assertEqual(template, 'common/blocks/code_block.html', 'The templates were not the same')

    def test_render_icon(self):
        """ Checks that the right icon renders """
        icon = self.block.meta.icon
        self.assertEqual(icon, 'edit', 'The icons did not match')

    def test_render_label(self):
        """ Tests the label """
        label = self.block.meta.label
        self.assertEqual(label, 'Codes', 'The labels were not the same')

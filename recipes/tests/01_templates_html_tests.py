import pytest
from django.test import TestCase
import django.template
from django.template.loader import get_template


class TemplatesHtmlTest(TestCase):
    @staticmethod
    def test_page_home_template_existence():
        template_name = 'recipes/pages/home.html'
        try:
            # Tentativa de carregar o template
            get_template(template_name)
        except django.template.TemplateDoesNotExist:
            # Se o template não existir, o teste falha
            pytest.fail(f"O template {template_name} não existe.")

    @staticmethod
    def test_page_recipe_view_template_existence():
        template_name = 'recipes/pages/recipe-view.html'
        try:
            # Tentativa de carregar o template
            get_template(template_name)
        except django.template.TemplateDoesNotExist:
            # Se o template não existir, o teste falha
            pytest.fail(f"O template {template_name} não existe.")

    @staticmethod
    def test_partial_footer_template_existence():
        template_name = 'recipes/partials/footer.html'
        try:
            # Tentativa de carregar o template
            get_template(template_name)
        except django.template.TemplateDoesNotExist:
            # Se o template não existir, o teste falha
            pytest.fail(f"O template {template_name} não existe.")

    @staticmethod
    def test_partial_head_template_existence():
        template_name = 'recipes/partials/head.html'
        try:
            # Tentativa de carregar o template
            get_template(template_name)
        except django.template.TemplateDoesNotExist:
            # Se o template não existir, o teste falha
            pytest.fail(f"O template {template_name} não existe.")

    @staticmethod
    def test_partial_header_template_existence():
        template_name = 'recipes/partials/header.html'
        try:
            # Tentativa de carregar o template
            get_template(template_name)
        except django.template.TemplateDoesNotExist:
            # Se o template não existir, o teste falha
            pytest.fail(f"O template {template_name} não existe.")

    @staticmethod
    def test_partial_reciep_template_existence():
        template_name = 'recipes/partials/recipe.html'
        try:
            # Tentativa de carregar o template
            get_template(template_name)
        except django.template.TemplateDoesNotExist:
            # Se o template não existir, o teste falha
            pytest.fail(f"O template {template_name} não existe.")

    @staticmethod
    def test_partial_search_form_template_existence():
        template_name = 'recipes/partials/search-form.html'
        try:
            # Tentativa de carregar o template
            get_template(template_name)
        except django.template.TemplateDoesNotExist:
            # Se o template não existir, o teste falha
            pytest.fail(f"O template {template_name} não existe.")

    @staticmethod
    def test_base_template_global_base_template_existence():
        template_name = 'global/base.html'
        try:
            # Tentativa de carregar o template
            get_template(template_name)
        except django.template.TemplateDoesNotExist:
            # Se o template não existir, o teste falha
            pytest.fail(f"O template {template_name} não existe.")

    @staticmethod
    def test_page_search_template_existence():
        template_name = 'recipes/pages/search.html'
        try:
            # Tentativa de carregar o template
            get_template(template_name)
        except django.template.TemplateDoesNotExist:
            # Se o template não existir, o teste falha
            pytest.fail(f"O template {template_name} não existe.")

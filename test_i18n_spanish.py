"""
Comprehensive test suite for i18n Spanish language configuration.
"""
import os
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from acouz.utils.i18n import tr, _STRINGS
from acouz.utils.config import ConfigManager

def test_module_import():
    """Test 1: Module Import"""
    print("TEST 1: Module Import")
    print("✓ i18n module loaded successfully")
    print()
    return True

def test_spanish_default():
    """Test 2: Spanish as Default Language"""
    print("TEST 2: Spanish as Default Language")
    os.environ['UI_LANGUAGE'] = 'es'

    tests_es = {
        'home.title': 'Panel de control',
        'general.title': 'Configuración',
        'nav.home': 'Inicio',
        'api.title': 'Clave API Groq',
        'audio.title': 'Audio',
        'about.tagline': 'Dictado de voz de código abierto. Rápido, privado, gratuito.',
    }

    all_pass = True
    for key, expected in tests_es.items():
        result = tr(key)
        status = '✓' if result == expected else '✗'
        if result != expected:
            all_pass = False
            print(f"  {status} {key}: '{result}' (expected: '{expected}')")
        else:
            print(f"  {status} {key}: {result}")

    print(f"  Result: {'PASS' if all_pass else 'FAIL'}")
    print()
    return all_pass

def test_english_switch():
    """Test 3: English Language Switch"""
    print("TEST 3: English Language Switch")
    os.environ['UI_LANGUAGE'] = 'en'

    tests_en = {
        'home.title': 'Dashboard',
        'general.title': 'Settings',
        'nav.home': 'Home',
        'api.title': 'Groq API Key',
        'audio.title': 'Audio',
    }

    all_pass = True
    for key, expected in tests_en.items():
        result = tr(key)
        status = '✓' if result == expected else '✗'
        if result != expected:
            all_pass = False
            print(f"  {status} {key}: '{result}' (expected: '{expected}')")
        else:
            print(f"  {status} {key}: {result}")

    print(f"  Result: {'PASS' if all_pass else 'FAIL'}")
    print()
    return all_pass

def test_french_switch():
    """Test 4: French Language Switch"""
    print("TEST 4: French Language Switch")
    os.environ['UI_LANGUAGE'] = 'fr'

    tests_fr = {
        'home.title': 'Tableau de bord',
        'general.title': 'Paramètres',
        'nav.home': 'Accueil',
        'api.title': 'Clé API Groq',
        'audio.title': 'Audio',
    }

    all_pass = True
    for key, expected in tests_fr.items():
        result = tr(key)
        status = '✓' if result == expected else '✗'
        if result != expected:
            all_pass = False
            print(f"  {status} {key}: '{result}' (expected: '{expected}')")
        else:
            print(f"  {status} {key}: {result}")

    print(f"  Result: {'PASS' if all_pass else 'FAIL'}")
    print()
    return all_pass

def test_translation_coverage():
    """Test 5: Translation Coverage"""
    print("TEST 5: Translation Coverage")
    total = len(_STRINGS)
    es_count = sum(1 for v in _STRINGS.values() if 'es' in v)
    en_count = sum(1 for v in _STRINGS.values() if 'en' in v)
    fr_count = sum(1 for v in _STRINGS.values() if 'fr' in v)

    print(f"  Total keys: {total}")
    print(f"  Spanish translations: {es_count}/{total}")
    print(f"  English translations: {en_count}/{total}")
    print(f"  French translations: {fr_count}/{total}")
    print(f"  Coverage: {100*es_count/total:.1f}%")

    missing_es = [k for k, v in _STRINGS.items() if 'es' not in v]
    if missing_es:
        print(f"  Missing Spanish translations:")
        for k in missing_es:
            print(f"    - {k}")

    passed = es_count == total
    print(f"  Result: {'PASS' if passed else 'FAIL'}")
    print()
    return passed

def test_ui_language_list():
    """Test 6: UI Language List"""
    print("TEST 6: UI Language List")
    from acouz.ui.pages.general import _UI_LANGS

    expected_langs = [('es', 'Español'), ('en', 'English'), ('fr', 'Français')]
    print(f"  Expected: {expected_langs}")
    print(f"  Actual:   {_UI_LANGS}")

    passed = _UI_LANGS == expected_langs
    print(f"  Result: {'PASS' if passed else 'FAIL'}")
    print()
    return passed

def test_config_defaults():
    """Test 7: Configuration Defaults"""
    print("TEST 7: Configuration Defaults")
    from acouz.ui.pages.general import GeneralPage

    # Test that the default is Spanish
    ConfigManager.initialize()
    default_lang = ConfigManager.get("UI_LANGUAGE", "es")

    print(f"  Default UI_LANGUAGE: {default_lang}")
    passed = default_lang == "es"
    print(f"  Result: {'PASS' if passed else 'FAIL'}")
    print()
    return passed

if __name__ == "__main__":
    print("=" * 60)
    print("COMPREHENSIVE I18N TEST SUITE")
    print("=" * 60)
    print()

    ConfigManager.initialize()

    results = []
    results.append(("Module Import", test_module_import()))
    results.append(("Spanish Default", test_spanish_default()))
    results.append(("English Switch", test_english_switch()))
    results.append(("French Switch", test_french_switch()))
    results.append(("Translation Coverage", test_translation_coverage()))
    results.append(("UI Language List", test_ui_language_list()))
    results.append(("Config Defaults", test_config_defaults()))

    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    for name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{status} - {name}")

    all_passed = all(passed for _, passed in results)
    print()
    print(f"Overall Result: {'✓ ALL TESTS PASSED' if all_passed else '✗ SOME TESTS FAILED'}")
    print("=" * 60)

    sys.exit(0 if all_passed else 1)

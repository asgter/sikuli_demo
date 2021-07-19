from unittest import TestCase

from jpype import JClass

from core.initialize_jvm import EnvInitializer


class TestScreenObj(TestCase):
    def test_screen_attrs(self):
        with EnvInitializer():
            Screen = JClass("org.sikuli.script.Screen")
            screen = Screen()
            print(dir(screen))


class TestLocationObj(TestCase):
    def test_location_attrs(self):
        with EnvInitializer():
            Location = JClass("org.sikuli.script.Location")
            print(dir(Location))


class TestPatternObj(TestCase):
    def test_pattern_attrs(self):
        with EnvInitializer():
            Pattern = JClass("org.sikuli.script.Pattern")
            pattern = Pattern()
            print(dir(pattern))


class TestRegionObj(TestCase):
    def test_region_attrs(self):
        with EnvInitializer():
            Region = JClass("org.sikuli.script.Region")
            print(dir(Region))


class TestFinderObj(TestCase):
    def test_finder_attrs(self):
        with EnvInitializer():
            Finder = JClass("org.sikuli.script.Finder")
            print(dir(Finder))

class TestSikuliEventObj(TestCase):
    def test_event_attrs(self):
        with EnvInitializer():
            sikuli_event = JClass("org.sikuli.script.SikuliEvent")
            print(dir(sikuli_event))

    def test_type_method(self):
        with EnvInitializer():
            sikuli_event = JClass("org.sikuli.script.SikuliEvent")
            print(dir(sikuli_event.Type))

class TestKeyObj(TestCase):
    def test_event_attrs(self):
        with EnvInitializer():
            key = JClass("org.sikuli.script.Key")
            print(dir(key))
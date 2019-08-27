import os
import yaml
import rasa_metaform
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

THIS_DIR = os.path.abspath(os.path.dirname(__file__))
domain_pre_file = os.path.join(THIS_DIR, "domain-pre.yml")
domain_file = os.path.join(THIS_DIR, "domain-post.yml")


class SampleForm(
    rasa_metaform.MetaFormAction,
    form_yml_file_path=os.path.join(THIS_DIR, "sample.yml"),
):
    pass


form = SampleForm()


def test_name():
    assert SampleForm.name() == "sample_form"


def test_extract_requested_slot_default():
    tracker = Tracker(
        "default",
        {"requested_slot": "some_slot"},
        {"entities": [{"entity": "some_slot", "value": "some_value"}]},
        [],
        False,
        None,
        {},
        "action_listen",
    )

    slot_values = form.extract_requested_slot(CollectingDispatcher(), tracker, {})
    assert slot_values == {"some_slot": "some_value"}


def test_extract_requested_slot_from_text_no_intent():
    tracker = Tracker(
        "default",
        {"requested_slot": "user_name"},
        {"text": "Foo Bar"},
        [],
        False,
        None,
        {},
        "action_listen",
    )

    slot_values = form.extract_requested_slot(CollectingDispatcher(), tracker, {})
    assert slot_values == {"user_name": "Foo Bar"}


def test_extract_requested_slot_from_button():
    tracker = Tracker(
        "default",
        {"requested_slot": "is_in_spain"},
        {"intent": {"name": "deny", "confidence": 1.0}},
        [],
        False,
        None,
        {},
        "action_listen",
    )

    slot_values = form.extract_requested_slot(CollectingDispatcher(), tracker, {})
    assert slot_values == {"is_in_spain": False}


def test_get_all_slots():
    slots = []
    rasa_metaform.get_all_slots(form.yml, slots)
    assert slots == ["user_name", "is_in_spain", "user_city"]


def test_update_domain():
    form.update_domain(domain_file, domain_pre_file)


def test_update_domain_name():
    with open(domain_file) as f:
        domain = yaml.load(f, Loader=yaml.Loader)
    assert form.name() in domain["forms"]


def test_update_domain_slots():
    with open(domain_file) as f:
        domain = yaml.load(f, Loader=yaml.Loader)
    slots = []
    slots = rasa_metaform.get_all_slots(form.yml, slots)
    for slot in slots:
        assert slot in domain["slots"]


def test_update_domain_templates():
    with open(domain_file) as f:
        domain = yaml.load(f, Loader=yaml.Loader)
    slots = []
    slots = rasa_metaform.get_all_slots(form.yml, slots)
    for slot in slots:
        assert f"utter_ask_{slot}" in domain["templates"]

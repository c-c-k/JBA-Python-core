from io import StringIO
import sys

import pytest

from zookeeper import zookeeper, messages


@pytest.mark.parametrize(
    ('habitat_id', 'animal'),
    (
        ('0', 'camel '),
        ('1', 'lion '),
        ('2', 'deer '),
        ('3', 'goose '),
        ('4', 'bat '),
        ('5', 'rabbit '),
        ('-1', 'exit'),
        ('text input\n-1', 'number'),
        ('999\n-1', 'not found'),
        ('text input\n-1', '-1'),
        ('999\n-1', '-1'),
    )
)
def test_main_output(capsys, monkeypatch, habitat_id, animal):
    stdin_override = StringIO(initial_value=habitat_id)
    with monkeypatch.context() as m:
        m.setattr(sys, 'stdin', stdin_override)
        zookeeper.main()
    captured = capsys.readouterr()
    assert animal in captured.out.strip()
    assert 'Please enter' in captured.out.strip()
    assert 'restart' in captured.out.strip()

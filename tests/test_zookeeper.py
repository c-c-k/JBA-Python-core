from io import StringIO
import sys

import pytest

from zookeeper import zookeeper, messages


@pytest.mark.parametrize(
    ('commands', 'output'),
    (
        ([], ['later']),
        (['0'], ['camel']),
        (['1'], ['lion']),
        (['2'], ['deer']),
        (['3'], ['goose']),
        (['4'], ['bat']),
        (['5'], ['rabbit']),
        (['bad input'], ['number']),
        (['999'], ['not found']),
        (['1', '5'], ['lion', 'rabbit']),
    )
)
def test_main_output(capsys, monkeypatch, commands, output):
    stdin_override = StringIO(initial_value='\n'.join((*commands, 'exit')))
    with monkeypatch.context() as m:
        m.setattr(sys, 'stdin', stdin_override)
        zookeeper.main()
    captured = capsys.readouterr()
    assert 'Please enter' in captured.out.strip()
    assert 'exit' in captured.out.strip()
    for string in output:
        assert string in captured.out.strip()

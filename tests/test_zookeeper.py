from zookeeper import zookeeper, messages


def test_main_output(capsys):
    zookeeper.main()
    captured = capsys.readouterr()
    assert captured.out.strip() == messages.CAMEL.strip()

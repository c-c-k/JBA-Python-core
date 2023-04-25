from zookeeper.zookeeper import main

TEST_OUTPUT = """I love animals!
Let's check on the animals...
The deer looks fine.
The bat looks happy.
The lion looks healthy.
"""


def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    for (prog_line, test_line) in zip(
            captured.out.splitlines(), TEST_OUTPUT.splitlines()):
        assert prog_line == test_line

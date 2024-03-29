import os

from TTS.TTS.utils.generic_utils import get_cuda


def get_device_id():
    use_cuda, _ = get_cuda()
    if use_cuda:
        GPU_ID = "0"
    else:
        GPU_ID = ""
    return GPU_ID


def get_tests_path():
    """Returns the path to the test directory."""
    return os.path.dirname(os.path.realpath(__file__))


def get_tests_input_path():
    """Returns the path to the test data directory."""
    return os.path.join(get_tests_path(), "inputs")


def get_tests_output_path():
    """Returns the path to the directory for test outputs."""
    return os.path.join(get_tests_path(), "outputs")


def run_cli(command):
    exit_status = os.system(command)
    assert exit_status == 0, f" [!] command `{command}` failed."

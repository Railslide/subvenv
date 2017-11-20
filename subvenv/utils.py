import sys


def deprecation_warning(command, replacement):
    message = (
        "Warning: `{}` is going to be deprecated, use `{}` instead.\n"
    ).format(command, replacement)

    sys.stderr.write(message)

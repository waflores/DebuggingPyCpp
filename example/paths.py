import pathlib

TEMPORARY_PATH = pathlib.Path("/tmp")
PROGRAM_BINARY_DIRECTORY = TEMPORARY_PATH / pathlib.Path("program")
SHARED_PROGRAM_PATH = PROGRAM_BINARY_DIRECTORY / pathlib.Path("shared")
PROGRAM_BINARY_PATH = PROGRAM_BINARY_DIRECTORY / pathlib.Path("bin/executable")

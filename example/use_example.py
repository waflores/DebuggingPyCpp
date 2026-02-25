import argparse
import example


def main():
    parser = argparse.ArgumentParser(
                    description='PyCpp Example program',
                    epilog='An example of how run a mix of languages with Bazel')
    parser.parse_args()  # assign args to use later on

    print(dir(example))
    print(f"running the example: {example.add(1, 2)}")


if __name__ == "__main__":
    main()

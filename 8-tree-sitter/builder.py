"""build parser"""

from tree_sitter import Language


def main():
    Language.build_library(
        # Store the library in the `build` directory
        "build/python.so",
        # Include one or more languages
        [
            "pygram",
        ],
    )


if __name__ == "__main__":
    main()

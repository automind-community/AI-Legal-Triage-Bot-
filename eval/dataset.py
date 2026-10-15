"""Module for loading and preparing the reglab/housing_qa evaluation dataset."""

from typing import Any


def load_housing_qa(split: str = "test") -> list[dict[str, Any]]:
    """Fetch reglab/housing_qa questions split (6,853 Q&A pairs) from HuggingFace.

    Args:
        split: Dataset split to fetch.

    Returns:
        List of benchmark dictionaries with question, golden context/statute, and answer.
    """
    raise NotImplementedError("Dataset loader stub.")

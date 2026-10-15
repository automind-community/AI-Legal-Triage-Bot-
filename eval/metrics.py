"""Module defining RAG evaluation metrics: Hit@k, MRR, Precision@k, and Faithfulness."""

from typing import Any


def compute_hit_at_k(retrieved_ids: list[str], ground_truth_id: str, k: int = 8) -> float:
    """Calculate binary Hit@k metric indicating whether the relevant statute was retrieved.

    Args:
        retrieved_ids: List of retrieved section IDs.
        ground_truth_id: Expected statutory section ID.
        k: Cutoff rank.

    Returns:
        1.0 if ground_truth_id is within top-k, else 0.0.
    """
    raise NotImplementedError("Hit@k metric stub.")


def compute_mrr(retrieved_ids: list[str], ground_truth_id: str) -> float:
    """Calculate Mean Reciprocal Rank (MRR) for the ground truth statute.

    Args:
        retrieved_ids: List of retrieved section IDs ordered by rank.
        ground_truth_id: Expected statutory section ID.

    Returns:
        Reciprocal rank score (1.0 / rank) or 0.0 if not found.
    """
    raise NotImplementedError("MRR metric stub.")

# -*- coding: utf-8 -*-
"""
pytest configuration for the LLM Wiki test suite.

Registers the `slow` marker so that `pytest -m "not slow"` (the default used
by the pre-commit hook) cleanly skips external URL reachability checks.
"""
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--run-slow",
        action="store_true",
        default=False,
        help="Also run @pytest.mark.slow tests (external URL reachability).",
    )


def pytest_collection_modifyitems(config, items):
    if not config.getoption("--run-slow"):
        skip_slow = pytest.mark.skip(reason="slow URL check — run with --run-slow")
        for item in items:
            if item.get_closest_marker("slow"):
                item.add_marker(skip_slow)


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "slow: external URL reachability checks — skipped by default; "
        "opt-in with --run-slow or -m slow",
    )

import pytest

pytest.importorskip('PySide6')
from PySide6.QtWidgets import QApplication, QPushButton

from src.utils.helpers import block_signals


def test_block_signals_restores_state():
    app = QApplication.instance() or QApplication([])
    btn = QPushButton()

    # If the button starts blocked it should remain blocked after the context
    btn.blockSignals(True)
    with block_signals(btn):
        assert btn.signalsBlocked()
    assert btn.signalsBlocked()

    # When starting unblocked it should return to unblocked
    btn.blockSignals(False)
    with block_signals(btn):
        assert btn.signalsBlocked()
    assert not btn.signalsBlocked()

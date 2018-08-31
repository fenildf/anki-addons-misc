"""
Works for Anki2.1 ONLY

Print context menu into right-click mene in Anki Reviewer

Copyright: (c) KyleHwang(Kuang) <https://github.com/upday7>
License: GNU AGPLv3 or later <https://www.gnu.org/licenses/agpl.html>
"""
from anki.hooks import addHook
from aqt import mw


def _reviewerContextMenu(view, menu):
    if mw.state != "review":
        return

    self = mw.reviewer
    opts = [
        [_("Flag Card"), [
            [_("Red Flag"), "Ctrl+1", lambda: self.setFlag(1)],
            [_("Purple Flag"), "Ctrl+2", lambda: self.setFlag(2)],
            [_("Green Flag"), "Ctrl+3", lambda: self.setFlag(3)],
            [_("Blue Flag"), "Ctrl+4", lambda: self.setFlag(4)],
            None,
            [_("Clear Flag"), "Ctrl+0", lambda: self.setFlag(0)],
        ]],
        [_("Mark Note"), "*", self.onMark],
        [_("Bury Card"), "-", self.onBuryCard],
        [_("Bury Note"), "=", self.onBuryNote],
        [_("Suspend Card"), "@", self.onSuspendCard],
        [_("Suspend Note"), "!", self.onSuspend],
        [_("Delete Note"), "Ctrl+Delete", self.onDelete],
        [_("Options"), "O", self.onOptions],
        None,
        [_("Replay Audio"), "R", self.replayAudio],
        [_("Record Own Voice"), "Shift+V", self.onRecordVoice],
        [_("Replay Own Voice"), "V", self.onReplayRecorded],
    ]

    self._addMenuItems(menu, [None, ])
    self._addMenuItems(menu, opts)


addHook('AnkiWebView.contextMenuEvent', _reviewerContextMenu)

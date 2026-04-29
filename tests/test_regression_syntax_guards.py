from pathlib import Path


def _read(path: str) -> str:
    return Path(path).read_text()


def test_curriculum_engine_has_single_school_name_and_version_block():
    content = _read("src/last_dices_terminal_school/services/curriculum_engine.py")
    assert content.count('school_name=str(manifest.get("school_name", "LAST DICES // TERMINAL SCHOOL OS"))') == 1
    assert content.count('version=str(manifest.get("version", "1.0"))') == 1
    assert 'school_name=manifest.get("school_name", "LAST DICES // TERMINAL SCHOOL OS")' not in content
    assert 'version=manifest.get("version", "1.0")' not in content


def test_reporting_has_single_next_actions_line():
    content = _read("src/last_dices_terminal_school/services/reporting.py")
    assert content.count('"NEXT ACTIONS\\n- " + "\\n- ".join(report.next_actions)') == 1


def test_tui_uses_descriptive_lesson_variable():
    content = _read("src/last_dices_terminal_school/app/tui.py")
    assert 'self.repo.save_lessons([lesson.model_dump() for lesson in lessons])' in content
    assert 'self.repo.save_lessons([l.model_dump() for l in lessons])' not in content


def test_assignment_service_no_unused_json_or_lambda_contains():
    content = _read("src/last_dices_terminal_school/services/assignment_service.py")
    assert 'import json' not in content
    assert 'def contains(term: str) -> int:' in content
    assert 'contains = lambda s: 1 if s in content.lower() else 0' not in content


def test_theme_has_no_media_query_block():
    content = _read("src/last_dices_terminal_school/app/theme.tcss")
    assert '@media' not in content

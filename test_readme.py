"""Checks for rohachevsk Junior QA profile README. Run: python test_readme.py"""
import pathlib, sys

ROOT = pathlib.Path(__file__).parent
README = ROOT / "README.md"

def main():
    ok = True
    if not README.exists():
        print("FAIL: README.md not found")
        return 1
    text = README.read_text(encoding="utf-8")

    checks = [
        ("Vanya" in text, "intro with Vanya"),
        ("QA" in text, "QA positioning in header"),
        ("Manual" in text, "Manual testing mentioned"),
        ("API" in text, "API testing mentioned"),
        ("Postman" in text, "Postman in skills"),
        (("SQL" in text or "PostgreSQL" in text), "SQL/PostgreSQL mentioned"),
        (("DevTools" in text or "DevTools" in text.lower() or "Chrome DevTools" in text), "DevTools mentioned"),
        ("rohachevsk/room-booking-qa-portfolio" in text, "link room-booking-qa-portfolio"),
        ("rohachevsk/weather-forecast-qa" in text, "link weather-forecast-qa"),
        (("41" in text and "8" in text), "room-booking numbers (41 TC, 8 bugs)"),
        ("Retest" in text or "retest" in text, "retest mentioned"),
        ("Regression" in text or "regression" in text, "regression mentioned"),
        ("JavaScript" in text, "JavaScript badge/skill"),
        ("React" in text, "React badge/skill"),
        (("Node" in text and "js" in text.lower()), "Node.js badge/skill"),
        ("Nest" in text, "NestJS badge/skill"),
        ("rohachevsk/todo-listReact" in text, "link todo-listReact"),
        ("rohachevsk/my-appNextJs" in text, "link my-appNextJs"),
        ("rohachevsk/project-nest" in text, "link project-nest"),
        ("rohachevsk/nodejsUni" in text, "link nodejsUni"),
        ("rohachevsk/NotesApp" in text, "dev background NotesApp kept"),
        ("rohachevsk/movieSearch" in text, "dev background movieSearch kept"),
        ("username=rohachevsk" in text, "stats images with username=rohachevsk"),
        ("Contact" in text, "section Contacts"),
        ("TODO" not in text, "no TODO placeholders"),
        (len(text.strip()) > 800, f"length >800 (now {len(text.strip())})"),
    ]
    for passed, name in checks:
        print(("PASS" if passed else "FAIL") + f": {name}")
        ok = ok and passed
    return 0 if ok else 1

if __name__ == "__main__":
    sys.exit(main())

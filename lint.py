# lint.py
import sys
from pylint import lint

THRESHOLD = 9.0

# Run without do_exit (removed in Pylint 3.x)
results = lint.Run(["factorial.py"])

# In 3.x, stats is an object, not a dict
score = results.linter.stats.global_note

print(f"Pylint score: {score:.2f}/10")

if score < THRESHOLD:
    print("Linter failed: Score < threshold value")
    sys.exit(1)

sys.exit(0)

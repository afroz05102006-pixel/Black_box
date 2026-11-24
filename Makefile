setup:
	python3 -m venv .venv
	source .venv/bin/activate && pip install -r requirements.txt

test:
	source .venv/bin/activate && pytest

demo:
	source .venv/bin/activate && python3 eval/run_eval.py

run:
	source .venv/bin/activate && uvicorn api.main:app --reload

VENV = venv
PYTHON = python3
PIP = $(VENV)/bin/pip
VENV_PYTHON = $(VENV)/bin/python

all: run

$(VENV)/bin/activate: requerimientos.txt
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requerimientos.txt
	touch $(VENV)/bin/activate

install: $(VENV)/bin/activate

run:
	@if [ -z "$(FILE)" ]; then \
  		echo "Debes especificar una ruta de la forma make run FILE=ejemplos/3.txt"; \
  	else \
  		$(PYTHON) code/tp2.py $(FILE); \
  	fi

mediciones: install
	$(VENV_PYTHON) code/mediciones.py

clean:
	rm -rf $(VENV)
	rm -rf __pycache__
	rm -rf code/__pycache__

.PHONY: all install run clean

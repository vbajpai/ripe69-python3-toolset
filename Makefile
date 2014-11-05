make:
	pip install -r requirements.txt

update:
	pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | \
	xargs pip install -U

run:
	ipython notebook --no-browser --pylab=inline --ip=0.0.0.0 \
	--notebook-dir=`pwd` --port=7777

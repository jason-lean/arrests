all:
	cd data/blotter; make
	cd data/maps; make
	python -m SimpleHTTPServer 8888 &

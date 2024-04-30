import argparse

def parse_cli_args():
	parser = argparse.ArgumentParser(
		prog="app_name",
		description="dummy desc",
	)
	parser.add_argument("-f", "--file")
	args = vars(parser.parse_args())

	return args

from cli.args import parse_cli_args

def main():
	cli_args = parse_cli_args()
	if cli_args["file"]:
		print(f"Doing something with the file: {cli_args['file']}")

if __name__ == "__main__":
	main()
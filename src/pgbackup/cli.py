from argparse import ArgumentParser, Action

class DriverAction(Action):
	def __call__(self, parser, namespace, values, option_string=None):
		driver, destination = values
		namespace.driver = driver.lower()
		namespace.destination = destination

def create_parser():
	parser = ArgumentParser(description="""
		Backup PostgreSQL
		""")
	parser.add_argument("url", help="URL of the database")
	parser.add_argument("--driver", '-d'
		help="How and where to store a backup",
		nargs=2,
		metavar=("DRIVER", "DESTINATION")
		action=DriverAction,
		required=True)

	return parser

def main():
	import boto3
	import time
	from pgbackup import pgdump, storage

	args = create_parser().parse_args()
	dump = pgdump.dump(args.url)
	if args.driver == s3:
		client = boto3.client('s3')
		timestamp = time.strftime("%Y-%m-%dT%H-%M", time.localtime())
		file_name = pgdump.dump_file_name(args.url, timestamp)
		print(f"Backing database up to {args.destination} in s3 as {file_name}")
		storage.s3(client, dump.stdout, args.destination, file_name)
	else:
		outfile = open(args.destination, 'wb')
		print(f"Backing database up locally to {outfile.name}")
		storage.local(dump.stdout, outfile)

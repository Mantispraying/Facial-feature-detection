import click
@click.command()
@click.option("--name","-n",default='mantis',help='Your first name')
def cli(name):
    print("My name is "+name)
if __name__ == "__main__":
    cli()
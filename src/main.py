import args_cli
 

if __name__ == '__main__':

    ClasCli = args_cli.ArgsCli()
    args = ClasCli.Cli()

    print(f"Theme Name -> {args.theme}\nFont Name -> {args.font}")

        for line in f:
            if line_is_command(line):
                cwd = perform_command(line, tree_nodes, cwd)
            else:
                check_output(line, tree_nodes, cwd)
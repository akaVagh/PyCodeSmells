import ast
import logging
from metrics import cc, loc, nof, nom, pc, wmc
from log_config import setup_logging

setup_logging()


def analyze_code(file_path):
    logging.info(f"Starting analysis of the file: {file_path}")
    try:
        with open(file_path, 'r') as file:
            node = ast.parse(file.read())

        metrics_data = []
        # Your existing analysis logic...
        for class_node in [n for n in ast.walk(node) if isinstance(n, ast.ClassDef)]:
            class_metrics = {
                'type': 'class',
                'name': class_node.name,
                'number_of_fields': nof.number_of_fields(class_node),
                'number_of_methods': nom.number_of_methods(class_node),
                'wmc': wmc.weighted_methods_per_class(class_node),
                'loc': loc.class_loc(class_node)
            }
            metrics_data.append(class_metrics)

        # Analyze each function/method in the file
        for func_node in [n for n in ast.walk(node) if isinstance(n, ast.FunctionDef)]:
            function_metrics = {
                'type': 'function',
                'name': func_node.name,
                'cyclomatic_complexity': cc.cyclomatic_complexity(func_node),
                'parameter_count': pc.parameter_count(func_node),
                'loc': loc.method_loc(func_node)
            }
            metrics_data.append(function_metrics)
        logging.info("Successfully completed analysis")
        return metrics_data

    except Exception as e:
        logging.error(f"Error occurred during analysis: {e}", exc_info=True)
        raise

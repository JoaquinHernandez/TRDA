import importlib
import pkgutil
import logging

CHECKS = []

def register_check(check_cls):
    """Decorator to register a new security check."""
    CHECKS.append(check_cls)
    return check_cls

def load_all_modules(package_name="rda.modules"):
    """Dynamically traverse and load all python files in the modules directory."""
    try:
        package = importlib.import_module(package_name)
        for _, module_name, _ in pkgutil.iter_modules(package.__path__):
            try:
                importlib.import_module(f"{package_name}.{module_name}")
            except Exception as e:
                logging.error(f"Failed to load module {module_name}: {e}")
    except ModuleNotFoundError:
        logging.error(f"Package {package_name} not found.")

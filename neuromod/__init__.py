# neuromod/__init__.py

# Importing core modules
from .memory_module import MemorySimulator, clear_memory
from .decision_module import DecisionMaker, reset_decisions
from .attention_module import AttentionMechanism, clear_attention_weights

# Optionally, you can define the version of your library here
__version__ = '0.1.0'

# Optionally, you can include other metadata or utility functions
def get_library_info():
    return f"NeuroMod version {__version__}"


from .videohelpersuite.nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
import folder_paths
from .videohelpersuite.server import server
from .videohelpersuite import documentation
from .videohelpersuite import latent_preview
from .videohelpersuite.utils import get_comfyui_version, is_comfyui_version_compatible

# Package version
__version__ = "1.7.9"

# ComfyUI compatibility
_version = get_comfyui_version()
_compatible = is_comfyui_version_compatible()

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]

# Format node documentation
documentation.format_descriptions(NODE_CLASS_MAPPINGS)

# ComfyUI-VideoHelperSuite Compatibility

This document details the compatibility of ComfyUI-VideoHelperSuite with different versions of ComfyUI.

## Version Support

### ComfyUI 0.9.2
**Status**: ✅ Fully Supported

Key features verified:
- ProgressBar API: Supports both old and new progress tracking methods
- Prompt Queue Structure: Handles 6-element queue format with `sensitive` field
- Server Routes: Compatible with updated asyncio patterns
- Node Input Types: Full validation and type checking support

### ComfyUI 0.8.x - 0.9.1
**Status**: ✅ Backward Compatible

The extension includes compatibility handling for older versions:
- Prompt queue structure detection (5 vs 6 elements)
- Progressive API compatibility checks
- Fallback support for legacy ProgressBar implementations

## Key API Changes Handled

### 1. Prompt Queue Structure
**Change**: ComfyUI evolved from 5-element to 6-element queue tuples

**Handling in VHS**:
```python
# Handle both old (5 values) and new (6 values) ComfyUI versions
if len(value) == 6:
    (_, prompt_id, prompt, extra_data, outputs_to_execute, sensitive) = value
else:
    (_, prompt_id, prompt, extra_data, outputs_to_execute) = value
```

**Files affected**:
- `videohelpersuite/utils.py`: `requeue_workflow()`, `requeue_workflow_unchecked()`

### 2. ProgressBar API
**Supported methods**:
- `ProgressBar(max_value)`: Constructor
- `pbar.update(step)`: Incremental progress
- `pbar.update_absolute(current, total)`: Absolute progress position

**Files affected**:
- `videohelpersuite/nodes.py`: VideoCombine, LoadAudio nodes
- `videohelpersuite/load_video_nodes.py`: Video loading generators

### 3. Server Routes
**Pattern**: Decorator-based route registration
```python
@server.PromptServer.instance.routes.get("/vhs/viewvideo")
async def view_video(request):
    ...
```

**Files affected**:
- `videohelpersuite/server.py`: All video/audio preview routes

### 4. Node Input Type Definitions
**Format**: ComfyUI 0.9.2 enforces stricter type validation

**Verified patterns in VHS**:
- `INPUT_TYPES` as `@classmethod` returning dict
- `RETURN_TYPES` and `RETURN_NAMES` tuple definitions
- Optional and hidden input types with proper metadata
- Custom type handling (e.g., `imageOrLatent`, `VHS_FILENAMES`)

**Files with verified nodes**:
- `videohelpersuite/nodes.py`: 13 node classes
- `videohelpersuite/image_latent_nodes.py`: Latent/image utility nodes
- `videohelpersuite/load_images_nodes.py`: Image loading nodes
- `videohelpersuite/batched_nodes.py`: Batch processing nodes
- `videohelpersuite/load_video_nodes.py`: Video loading nodes

## Installation & Setup

### Requirements
- Python 3.8+
- ComfyUI 0.8.x or later (tested on 0.9.2)
- Dependencies: opencv-python, imageio-ffmpeg

### Installation Steps

1. Clone into ComfyUI custom_nodes directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git
```

2. Install dependencies:
```bash
pip install -r ComfyUI-VideoHelperSuite/requirements.txt
```

3. Restart ComfyUI

## Migration Guide

### For Existing Workflows

If you're updating from an older version of ComfyUI-VideoHelperSuite to version 1.7.9+:

1. **No breaking changes**: Existing workflows will continue to work
2. **Enhanced compatibility**: The extension automatically detects your ComfyUI version
3. **Improved stability**: Better error handling for version mismatches

### For Custom Extensions Extending VHS

If you're developing custom nodes that depend on VHS:

1. Ensure your nodes are compatible with ComfyUI 0.9.2 node format
2. Use `INPUT_TYPES` as a classmethod
3. Define `RETURN_TYPES` and `RETURN_NAMES` explicitly
4. Test with both older and newer ComfyUI versions if supporting multiple versions

## Troubleshooting

### Issue: "ImportError: cannot import name 'ProgressBar'"
**Solution**: Ensure ComfyUI is installed and in the Python path. Update ComfyUI to latest version.

### Issue: "KeyError: 'sensitive' in prompt queue"
**Solution**: This is automatically handled. If you see this error, it indicates a ComfyUI version issue. Please report with ComfyUI version number.

### Issue: Workflows not loading
**Solution**: 
1. Check ComfyUI version compatibility (0.8.x+)
2. Verify all dependencies are installed: `pip install -r requirements.txt`
3. Check server logs for specific errors

## Testing

VHS includes test workflows for verification:
- `tests/simple.json`: Basic video combination workflow
- `tests/audio.json`: Audio processing workflow
- `tests/batch4x4.json`: Batch processing workflow

Run with ComfyUI's built-in test framework or manually through the web UI.

## Version History

- **1.7.9**: Full ComfyUI 0.9.2 support added
  - Enhanced prompt queue handling
  - Improved type validation
  - Better error messages for version mismatches

## Getting Help

- **GitHub Issues**: https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite/issues
- **ComfyUI Community**: Check the ComfyUI discord or forums
- **Version Info**: Include your ComfyUI and Python versions in bug reports

## Contributing

If you encounter compatibility issues with specific ComfyUI versions:

1. Note the ComfyUI version and error message
2. Check if it's listed as known issue in this document
3. Submit an issue with reproduction steps
4. Include output from: `comfyui --version` (if available)

import os
import json
import tifffile
from pathlib import Path
from napari_plugin_engine import napari_hook_implementation

from bg_atlasapi.bg_atlas import BrainGlobeAtlas


@napari_hook_implementation
def napari_get_reader(path):
    """A basic implementation of the napari_get_reader hook specification.

    Parameters
    ----------
    path : str or list of str
        Path to file, or list of paths.

    Returns
    -------
    function or None
        If the path is a recognized format, return a function that accepts the
        same path or list of paths, and returns a list of layer data tuples.
    """

    if isinstance(path, str) and is_brainreg_dir(path):
        return reader_function


def is_brainreg_dir(path):
    """Determines whether a path is to a brainreg output directory

    Parameters
    ----------
    path : str
        Path to file.

    Returns
    -------
    function or None
        If the path is a recognized format, return a function that accepts the
        same path or list of paths, and returns a list of layer data tuples.
    """
    path = os.path.abspath(path)
    if os.path.isdir(path):
        filelist = os.listdir(path)
    else:
        return False
    for fname in filelist:
        if fname == "brainreg.json":
            return True
    return False


def load_additional_downsampled_channels(
    path, layers, extension=".tiff", search_string="downsampled_standard",
):

    # Get additional downsampled channels

    for file in path.iterdir():
        if (
            (file.suffix == extension)
            and file.name.startswith(search_string)
            and file.name != "downsampled_standard.tiff"
        ):

            print(
                f"Found additional downsampled image: {file.name}, "
                f"adding to viewer"
            )
            name = file.name.strip(search_string).strip(extension) + (
                " (downsampled)"
            )
            layers.append(
                (
                    tifffile.imread(file),
                    {"name": name, "visible": False},
                    "image",
                )
            )

    return layers


def load_atlas(atlas, layers):
    atlas_image = BrainGlobeAtlas(atlas).annotation
    layers.append((atlas_image, {"name": atlas, "visible": False}, "labels",))
    return layers


def reader_function(path):
    """Take a path or list of paths and return a list of LayerData tuples.

    Readers are expected to return data as a list of tuples, where each tuple
    is (data, [add_kwargs, [layer_type]]), "add_kwargs" and "layer_type" are
    both optional.

    Parameters
    ----------
    path : str or list of str
        Path to file, or list of paths.

    Returns
    -------
    layer_data : list of tuples
        A list of LayerData tuples where each tuple in the list contains
        (data, metadata, layer_type), where data is a numpy array, metadata is
        a dict of keyword arguments for the corresponding viewer.add_* method
        in napari, and layer_type is a lower-case string naming the type of layer.
        Both "meta", and "layer_type" are optional. napari will default to
        layer_type=="image" if not provided
    """

    print("Loading brainreg directory")
    path = Path(os.path.abspath(path))
    with open(path / "brainreg.json") as json_file:
        metadata = json.load(json_file)

    layers = []
    layers = load_additional_downsampled_channels(path, layers)
    layers.append(
        (
            tifffile.imread(path / "downsampled_standard.tiff"),
            {"name": "Image (downsampled)", "metadata": metadata},
            "image",
        )
    )
    layers = load_atlas(metadata["atlas"], layers)

    return layers

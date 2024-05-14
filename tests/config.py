from pathlib import Path
from ai_diffusion.resources import SDVersion, default_checkpoints


test_dir = Path(__file__).parent
root_dir = test_dir.parent
server_dir = test_dir / "server"
data_dir = test_dir / "data"
image_dir = test_dir / "images"
result_dir = test_dir / "results"
reference_dir = test_dir / "references"
benchmark_dir = test_dir / "benchmark"

default_checkpoint = {
    SDVersion.sd15: "realisticVisionV51_v51VAE.safetensors",
    SDVersion.sdxl: "juggernautXL_version6Rundiffusion.safetensors",
}

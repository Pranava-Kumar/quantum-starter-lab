from dataclasses import dataclass
from typing import Any, Dict, Mapping, Optional

@dataclass
class DemoResult:
  name: str
  n_qubits: int
  circuit_ascii: str
  circuit_native: Any
  counts: Mapping[str, int]
  prob_ideal: Optional[Mapping[str, float]]
  prob_noisy: Optional[Mapping[str, float]]
  metrics: Dict[str, float]
  explanation: str
  figures: Dict[str, Any]
  metadata: Dict[str, Any]
  
def plot(self, side_by_side: bool = True, show: bool = True, savepath: Optional[str] = None) -> Any:
    try:
        import matplotlib.pyplot as plt  # optional
    except Exception:
        print('plot(): matplotlib not installed. Install with: uv pip install -e ".[plots]"')
        return None
    keys = list(self.counts.keys())
    vals = [self.counts[k] for k in keys]
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(keys, vals, color="#4C78A8")
    ax.set_title(self.name)
    ax.set_xlabel("bitstring (big-endian)")
    ax.set_ylabel("counts")
    if savepath:
        fig.savefig(savepath, bbox_inches="tight", dpi=200)
    if show:
        plt.show()
    return fig

def show_circuit(self) -> str:
    return self.circuit_ascii
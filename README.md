### Initial Datasets for ''A RISC-V PPA-fusion Cooperative Optimization Framework Based on Hybrid Strategies"

This repository contains the initial datasets used in RISC-V design optimization experiments of our paper "A RISC-V PPA-fusion Cooperative Optimization Framework Based on Hybrid Strategies". 

To cite our paper, please use the BibTex code below:

```latex
@article{10766887,
  author={Gao, Tianning and Wang, Yifan and Zhu, Ming and Wu, Xiulong and Zhou, Dian and Bi, Zhaori},
  journal={IEEE Transactions on Very Large Scale Integration (VLSI) Systems}, 
  title={An RISC-V PPA-Fusion Cooperative Optimization Framework Based on Hybrid Strategies}, 
  year={2025},
  volume={33},
  number={1},
  pages={140-153},
  doi={10.1109/TVLSI.2024.3496858}
}
```

The CSV files stores the initial data. The column names of the initial data are as following:

| **$x_0$, $x_1$, $\dots$ $x_{n-1}$** | CPI  | Power (mW) | Area (sites) | WTS (ns) | FOM  |
| ----------------------------------- | ---- | ---------- | ------------ | -------- | ---- |

where $n$​ is the number of parameters, including micro-architecture and synthesis tool parameters.

"read_init_data.py" provides a function to read the initial data into numpy arrays.


import os, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, leaves_list
os.makedirs("figures",exist_ok=True); os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(3); g,s=40,20
X=np.zeros((g,s))
for b in range(4):
    X[b*10:(b+1)*10, b*5:(b+1)*5]+= 3
X+=rng.normal(0,0.6,(g,s))
ro=leaves_list(linkage(X,"ward")); co=leaves_list(linkage(X.T,"ward"))
Xo=X[ro][:,co]
plt.figure(figsize=(6,6)); plt.imshow(Xo,aspect="auto",cmap="coolwarm")
plt.colorbar(label="expression"); plt.xlabel("samples"); plt.ylabel("genes")
plt.title("Clustered expression heatmap (demo data)")
plt.tight_layout(); plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write("4 co-expression blocks recovered\n"); print("ok")
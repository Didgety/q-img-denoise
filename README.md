# Binary image denoising with RBMs and QAOA

Jai Veilleux · University of Southern California · EE 513 Application of Quantum Computing final project

Can a shallow quantum circuit recover a clean image after some of its pixels have flipped? This project tests that question on 3 × 3 Bars-and-Stripes images. I adapted the restricted Boltzmann machine (RBM) denoising objective of Kerger and Miyazaki to a gate-model circuit and compared exact classical optimization, the Quantum Approximate Optimization Algorithm (QAOA) in Qiskit Aer, and QAOA on IBM Quantum hardware.

[Read the report (PDF)](paper/qaoa-rbm-image-denoising-report.pdf) · [Explore the experiment notebook](qaoa-rbm-image-denoising.ipynb)

## Experiment and results

The RBM learns a prior over clean images. For each noisy input, the denoising objective balances the RBM energy of a candidate reconstruction and a penalty for changing observed pixels. The notebook maps this objective to an Ising Hamiltonian and optimizes QAOA angles separately for each input. It selects the lowest-energy measured sample and scores the reconstruction by the fraction of pixels that match the clean image.

| Experiment | Finding |
| --- | --- |
| Exact optimization | Minimizing the binary objective generally improved pixel agreement over the noisy input. Among the contrastive divergence models tested, CD-10 gave the most consistent improvement and was used for QAOA. |
| Ideal Aer simulation | With two QAOA layers, the lowest-energy sample improved on the noisy input at low and moderate noise levels. The improvement was less consistent at higher noise. |
| IBM Quantum hardware | Even one QAOA layer required hundreds of two-qubit gates after transpilation. The hardware samples gave poorer reconstructions than Aer samples from the corresponding circuits. |

## Run locally

1. Open a terminal in `q-img-denoise/` and run `python setup_env.py` with Python 3.14. On Windows, you can also use `py -3.14 setup_env.py`. The script creates `.venv` and installs the notebook dependencies.
2. Use the created virtual environment as the kernel for the Jupyter notebook.
3. Leave `RUN_HARDWARE = False` and select **Run All**. The notebook generates the images locally, trains the RBMs, and runs the classical and Aer experiments. The QAOA benchmark performs repeated optimizations across images and noise levels.

## Optional IBM Quantum run

To submit the hardware experiments, copy `.env.example` to `.env` in `q-img-denoise/`. Set `QISKIT_IBM_TOKEN` to your IBM Cloud API key and `QISKIT_IBM_INSTANCE` to your instance CRN. With that directory as the notebook working directory, set `RUN_HARDWARE = True` in the optional hardware section. Running that section submits both the single-circuit example and the batch used for the overlap comparison.

FROM continuumio/anaconda3

# Copy environment.yml (if found) to a temp location so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
RUN conda install jupyter -y --quiet

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
# Various Python and C/build deps
RUN apt-get update -y
RUN apt-get install -y g++ make pkg-config libopencv-dev libgomp1
RUN apt-get install libffi7

RUN conda create -n new-base python=3.10

RUN conda init bash
SHELL ["conda", "run", "-n", "new-base", "/bin/bash", "-c"]


COPY requirements.txt /workspace/
WORKDIR /workspace
RUN pip install --no-cache-dir -r requirements.txt

#Install jupyter notebook
RUN conda install jupyter -y --quiet
#CMD ["jupyter notebook", "--ip='0.0.0.0'", "--port=8888", "--no-browser", "--allow-root"]
#!/bin/bash -e

ROOT=$(realpath $(dirname ${BASH_SOURCE[0]}))
# source $HERE/__init__.sh
# ROOT=$(realpath $HERE/..)

# source $ROOT/.anaconda3/bin/activate

if [ -e $ROOT/src/ompl/py-bindings/ompl/base/_base.so ]; then
  echo "==> OMPL is already installed"
  exit 0
fi

echo "==> Installing dependencies"

conda install cmake boost eigen

pip install pyplusplus castxml

echo "==> Installing OMPL"

mkdir -p $ROOT/src
cd $ROOT/src
if [ ! -d ompl ]; then
  git clone https://github.com/ompl/ompl.git
fi
cd ompl


mkdir -p build
cd build
cmake .. -DOMPL_BUILD_PYBINDINGS=TRUE -DCMAKE_PREFIX_PATH=$CONDA_PREFIX
make -j4 update_bindings
make -j4

cd ..
cat << EOF > setup.py
import setuptools


setuptools.setup(
    name="ompl",
    version="1.5.1",
    packages=setuptools.find_packages("py-bindings"),
    package_dir={"": "py-bindings"},
)
EOF
# source $ROOT/.anaconda3/bin/activate
pip install -e .

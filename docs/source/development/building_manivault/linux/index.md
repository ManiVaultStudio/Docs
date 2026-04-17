# Building on Linux

Tried on Ubuntu 24.04 using gcc 13.3.0 and CMake 3.28.3. 
Install build dependencies (building infrastructure, Qt packages, zlib):
```bash
sudo apt install build-essential cmake qt6-base-dev qt6-base-private-dev qt6-webengine-dev qt6-wayland qt6-svg-dev qt6-5compat-dev zlib1g libgl1-mesa-dev libxkbcommon-dev libtbb-dev libxcursor-dev libxcomposite-dev libxi-dev libnss3-dev libnspr4-dev libfreetype-dev libfontconfig1-dev libxtst-dev libasound2-dev libdbus-1-dev libxkbfile-dev libxcb-cursor0
```

<details closed>
   
<summary>Ubuntu 22.04 (not recommended)</summary>

On Ubuntu 22.04 you'll additionally need `libxkbfile-dev libglew-dev`. 
```bash
sudo apt install build-essential libxkbcommon-dev libxkbfile-dev libtbb-dev libglew-dev fonts-font-awesome libgomp1 libgl1 libegl1 libcups2 libopengl0 libnss3-dev libasound2-dev libxkbcommon-x11-dev
```

Also, the standard repository does not provide Qt 6.3 or a nice modern cmake version. 
You can install Qt like this, using [aqtinstall](https://github.com/miurahr/aqtinstall):
```bash
cd ~
mkdir micromamba && cd micromamba
sudo apt install -y curl
curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj bin/micromamba
./bin/micromamba shell init -s bash -r ~/micromamba
source ~/.bashrc
micromamba create -n qt -y python=3.12
micromamba activate qt
pip install aqtinstall
aqt list-qt linux desktop --arch 6.8.2
aqt list-qt linux desktop --modules 6.8.2 gcc_64
mkdir -p ~/qt6
aqt install-qt -O ~/qt6 linux desktop 6.8.2 gcc_64 -m all
echo -e '\n# Custom qt\nexport PATH=$HOME/qt6/6.8.2/gcc_64/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

We might as well build cmake from scratch
```bash
cd ~
sudo apt purge cmake -y
sudo apt install -y build-essential gfortran libssl-dev
mkdir cmake && cd cmake
mkdir cmake_install
git clone https://gitlab.kitware.com/cmake/cmake.git
mv cmake cmake_source
cd cmake_source
git checkout v3.31.5
./bootstrap --prefix=$HOME/cmake/cmake_install
make -j4 && make install
echo -e '\n# Custom cmake\nexport PATH=$HOME/cmake/cmake_install/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

```{toctree}
:maxdepth: 1

clion
vscode
```
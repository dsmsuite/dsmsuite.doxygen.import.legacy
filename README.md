# Example usage under Fedora

## Download c++ sample project

From https://github.com/jmuijsenberg/UnderstandApi

## Install doyxygen

On fedora sudo dnf install doxygen

## Create dsm analysis folder output folder and doxygen output folder

mkdir ~/DsmAnalysis
cd ~/DsmAnalysis
mkdir doxygen_output

## Copy dixygen config file and adapt

Copy Doxygen file from archive and place it in ~/DsmAnalysis
Update the INPUT path

## Create doxygen config file for c++ sample project using doxygen confifg found in this archive

doxygen ~/DsmAnalysis/Doxyfile

## On window PC open dsi file



#
# this action runs when tag name starts with t and upload file to testpypi
#
name: testrelease_binary

on:
  push:
    #branches: [ action_test ]
    tags: ["t*"]

jobs:
  vm:
    runs-on: ubuntu-latest
    container: quay.io/pypa/manylinux2010_x86_64    
    steps:
      - name: build_sdist
        run: |
          echo This job does not specify a container.
          echo It runs directly on the virtual machine.
          #
          git clone https://github.com/mfem/PyMFEM.git
          #git clone https://github.com/sshiraiwa/PyMFEM.git
          cd PyMFEM	  
          #git checkout action_test
          #
          export PATH=/opt/python/cp36-cp36m/bin:$PATH	  
          pip3 install wheel	  
          pip3 install six
          pip3 install auditwheel
          pip3 install twine
          if [ -f requirements.txt ]; then
             pip3 install -r requirements.txt
          fi	  
          rm -rf dist/*
          python3 setup.py sdist
          ls -l dist/
          python3 -m twine upload --repository-url https://test.pypi.org/legacy/ --password ${{ secrets.TEST_PYPI_TOKEN }} --username __token__ --verbose dist/*
          #python3 -m twine upload --password ${{ secrets.PYPI_TOKEN }} --username __token__ --verbose dist/*   	  
  container:
    needs: vm
    strategy:
      matrix:
        #pythonpath:  ["cp36-cp36m"]
        pythonpath: ["cp36-cp36m", "cp37-cp37m", "cp38-cp38", "cp39-cp39"]
 
    runs-on: ubuntu-latest
    container: quay.io/pypa/manylinux2010_x86_64
    #container: node:10.16-jessie
    steps:
      - name: build package
        run: |
          echo It runs in the container instead of the VM.
          #
          git clone https://github.com/mfem/PyMFEM.git
          #git clone https://github.com/sshiraiwa/PyMFEM.git
          cd PyMFEM	  
          #git checkout action_test
          #
          ls -l /opt/python/
          export PATH=/opt/python/${{ matrix.pythonpath }}/bin:$PATH
          pip3 install six
          pip3 install auditwheel
          pip3 install twine	
          if [ -f requirements.txt ]; then
             pip3 install -r requirements.txt
          fi	  
          CWD=$PWD
          ls -l 
          python3 setup.py install
          rm -rf dist/*
          python3 setup.py bdist_wheel
          export LD_LIBRARY_PATH=${CWD}/PyMFEM/external/mfem/cmbuild_ser/:$LD_LIBRARY_PATH
          rm -rf wheelhouse/*
          auditwheel repair dist/*.whl
          rm -rf dist/*
          #python3 setup.py sdist
          mv wheelhouse/* dist/
          ls -l dist/
          python3 -m twine upload --repository-url https://test.pypi.org/legacy/ --password ${{ secrets.TEST_PYPI_TOKEN }} --username __token__ --verbose dist/*
          #python3 -m twine upload --password ${{ secrets.PYPI_TOKEN }} --username __token__ --verbose dist/*   	  

g++ ./tmvamethod.cpp -I/home/dphan/TMVA-v4.2.0/ -pthread -std=c++11 -Wno-deprecated-declarations -m64 -I/home/dphan/ROOT-system/root-5.34.34/include -L/home/dphan/TMVA-v4.2.0/lib -lTMVA.1 -L/home/dphan/ROOT-system/root-5.34.34/lib -lCore -lCint -lRIO -lNet -lHist -lGraf -lGraf3d -lGpad -lTree -lRint -lPostscript -lMatrix -lPhysics -lMathCore -lThread -pthread -lm -ldl -rdynamic -lMLP -lTreePlayer -lMinuit -g -o TMVATest

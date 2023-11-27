# MLpihole

**An extension of Pi-hole with Machine Learning Features.**

This project integrates a machine learning model directly into Pi-hole's gravity.sh, enabling real-time ad classification as part of the routine blacklists update process.

The gravity.sh script is a part of the Pi-hole software, responsible for updating the blocklists used for ad blocking. Pi-hole works by maintaining a list of domains known to serve advertisements, and this list is updated regularly to ensure effectiveness in blocking ads.

Since identifying ad domains can be seen as a pattern matching problem pi-holes features can be extended with Machine Learning.

## Installation

To integrate MLpihole with your Pi-hole installation, follow these steps:

1. **Navigate to your Pi-hole directory:**
   
   ```bash
   cd Pi-Hole
   ```
   
   Ensure that gravity.sh is present in this directory

2. **Clone the MLpihole repository:**



   ```bash
   git clone https://github.com/som14159/MLpihole
   ```
   You might also need to install other dependencies like symspell , nltk etc .
   
3. **Update gravity.sh file to execute the Prediction Script:**
   ```bash
   echo 'bash /MLpihole/predict.sh' >> gravity.sh
   ```
   



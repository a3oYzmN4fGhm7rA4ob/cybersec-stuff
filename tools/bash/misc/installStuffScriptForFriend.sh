# A script i made for a friend to help them install stuff quick on Ubuntu systems

cd ~

# Tools installed via apt
sudo apt install git nmap wireshark aircrack-ng nikto python3-full python3-scapy hping3 wafw00f exiftool gobuster hydra arp-scan hashcat kleopatra ghostwriter

# Other tools installed automatically

# mitmproxy
echo !Notice! Downloading and unpacking mitmproxy. Please see the docs at https://docs.mitmproxy.org/stable/overview/installation to learn how to set it up and run it properly, ideally with a second browser for proxying. The executables will not be setup for running, you\'ll need to chmod them yourself or something.
curl --output mitmproxy-12.2.0-linux-x86_64.tar.gz https://downloads.mitmproxy.org/12.2.0/mitmproxy-12.2.0-linux-x86_64.tar.gz
tar -zxvf mitmproxy-12.2.0-linux-x86_64.tar.gz

# torctl
git clone https://github.com/a3oYzmN4fGhm7rA4ob/linuxmint-torctl-installer && cd linuxmint-torctl-installer && sudo bash install_torctl.sh && cd ~

# my funny tooling doc idk
https://raw.githubusercontent.com/a3oYzmN4fGhm7rA4ob/cybersec-stuff/refs/heads/main/misc/tooling.md.tar.gz
tar -zxvf tooling.md.tar.gz

# sqlmap
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev

# EvilLimiter
git clone https://github.com/bitbrute/evillimiter.git
cd evillimiter
sudo python3 setup.py install
cd ~

# veracrypt
curl --output VeraCrypt-1.26.24-x86_64.AppImage https://launchpad.net/veracrypt/trunk/1.26.24/+download/VeraCrypt-1.26.24-x86_64.AppImage
echo !Notice! VeraCrypt standalone AppImage downloaded.

# element
sudo apt install -y wget apt-transport-https
‍sudo wget -O /usr/share/keyrings/element-io-archive-keyring.gpg https://packages.element.io/debian/element-io-archive-keyring.gpg
‍echo "deb [signed-by=/usr/share/keyrings/element-io-archive-keyring.gpg] https://packages.element.io/debian/ default main" | sudo tee /etc/apt/sources.list.d/element-io.list
sudo apt update
sudo apt install element-desktop

# tor browser
echo !Notice! Tor Browser is being downloaded. You\'ll want to unpack the file itself later. I\'m too lazy to do it rn.
wget -O tor-browser-linux-x86_64-14.5.8.tar.xz https://www.torproject.org/dist/torbrowser/14.5.8/tor-browser-linux-x86_64-14.5.8.tar.xz

# finally, install metasploit
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
  chmod 755 msfinstall && \
  ./msfinstall

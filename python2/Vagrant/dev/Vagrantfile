Vagrant.configure("2") do |config|
  # Choix de l'image CentOS la plus stable
  config.vm.box = "centos/7"

  # Configuration du réseau
  config.vm.network "private_network", type: "dhcp"

  # Provisionnement optionnel (décommentez pour utiliser)
  # config.vm.provision "shell", inline: <<-SHELL
  #   yum install -y net-tools
  #   yum install -y iproute
  #   # Ajoutez d'autres paquets nécessaires ici
  # SHELL
end

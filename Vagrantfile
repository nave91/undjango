Vagrant.configure(2) do |config|
  config.vm.box = "hashicorp/precise32"
  config.vm.network "forwarded_port", guest: 8000, host: 9876
  config.vm.network "private_network", ip: "10.1.2.250"
  config.vm.synced_folder ".", "/home/vagrant/", id: "vagrant-root", type: "nfs", mount_options: ['nfsvers=3', 'actimeo=1']

end

from paramiko import SSHClient
class pythoncloud:
    def __init__(self,host:str,username:str):
        self.client = SSHClient()
        self.host = host
        self.username = username
        
    def execute_command(self,command:str,sudo=False):
        """ Execute a command on the server"""
        stdin, stdout, stderr = self.client.exec_command(command)
        if(sudo):
            stdin.write(self.password)
            stdin.channel.shutdown_write()
        
    def deploy(self,port:int,local_path:str,remote_path:str):
        """ 
        
        """
        
        self.execute_command('sudo apt update',sudo=True)
        self.execute_command('sudo python3 -m pip install --upgrade pip',sudo=True)
        self.execute_command('pip3 install Jupyter',sudo=True)
        self.execute_command('sudo jupyter notebook --no-browser --port={}'.format(port),sudo=True)
        
       
        
        #ssh -N -f -L localhost:YYYY:localhost:XXXX remoteuser@remotehost
    def login_with_password(self,password:str):
        """Login to the server using a password
        
           Args:
            key_filename (str): ssh password
        """
            
        #client.load_system_host_keys()
        #client.load_host_keys('~/.ssh/known_hosts')
        #client.set_missing_host_key_policy(AutoAddPolicy())
        
        self.client.connect(self.host, username=self.username, password=password)
        self.client.close()
        
    def login_with_key(self,key_filename:str):
        
        """ Login to the server using a key file

        Args:
            key_filename (str): file path to the key file
        """
        self.client.connect(self.host, username=self.username, key_filename=key_filename)
        self.client.close()
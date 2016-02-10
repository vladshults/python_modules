'''
Created on 
@author: vlad
'''


class Generate:
    '''
    classdocs
    '''
    
    def __init__(self, param_list):
        self.ip_tun_list = []
        self.ip_receive_tun_list = []
        self.src_network_list = []
        self.param_list = param_list
        self.netw_range = range(param_list[0], param_list[1])
        self.ip_range = range(param_list[2], param_list[3])
        self.single_ip = str(param_list[4]) + '0.1'
        self.single_receive_ip = str(param_list[4]) + '100.1'
        self.src_network = str(param_list[6])
        self.cn_serial = str(param_list[7])
        
    
    def generate_ip_lists(self):
        for y in self.netw_range:
                for z in self.ip_range:
                    adr = str(self.param_list[4]) + str(y) + '.' + str(z)
                    self.ip_tun_list.append(adr)
                    src_adr = str(self.param_list[5]) + str(y) + '.' + str(z)
                    self.src_network_list.append(src_adr)
                    
        
    def generate_many_to_one(self):
        with open(r"secondary_ips.txt", "w") as f:
            for ip in self.ip_tun_list:
                s = ' ip secondary-address ' + ip + '/16\n'
                f.write(s)
        f.close()
        
        with open(r"tunnels_from_many_ips.txt", "w") as f:
            counter = 0
            for ip in self.ip_tun_list:
                counter = counter + 1
                c_id = str(counter + 10000)
                conn_id = 't' + c_id
                s1  = 'crypto disec conn ' + conn_id + '\n'
                s2  = ' alg encryption' + '\n'
                s3  = ' id ' + str(c_id) + '\n'
                s4  = ' local ip ' + ip + '\n'
                s5  = ' remote ip ' + self.single_ip + '\n'
                s6  = ' serial 4150' + '\n'
                s7  = ' local cn 2' + '\n'
                s8  = ' remote cn 1' + '\n'
                s9  = ' permit src ' + self.src_network_list[counter - 1] + '/32 ' + 'dst ' + self.src_network + '0.0/24' + '\n'
                s10 = '\n'
                s11 = 'crypto disec enable conn ' + conn_id + '\n'
                s12 = '\n'
                f.writelines([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12])
        f.close()
        
        with open(r"tunnels_from_single_ip.txt", "w") as f:
            counter = 0
            for ip in self.ip_tun_list:
                counter = counter + 1
                c_id = str(counter + 10000)
                conn_id = 't' + c_id
                s1  = 'crypto disec conn ' + conn_id + '\n'
                s2  = ' alg encryption' + '\n'
                s3  =  ' id ' + str(c_id) + '\n'
                s4  = ' local ip ' + self.single_ip + '\n'
                s5  = ' remote ip ' + ip + '\n'
                s6  = ' serial 4150' + '\n'
                s7  = ' local cn 1' + '\n'
                s8  = ' remote cn 2' + '\n'
                s9  = ' permit src ' + self.src_network + '0.0/24 ' + 'dst ' + self.src_network_list[counter - 1] + '/32 '  + '\n'
                s10 = '\n'
                s11 = 'crypto disec enable conn ' + conn_id + '\n'
                s12 = '\n'
                f.writelines([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12])
        f.close()        
        
        
    def generate_many_to_many(self):
        pass
    

#param_list = [ 1, 11, 0, 256, '172.16.', '10.100.', '10.200.', '4150' ]
param_list = [ 1, 21, 0, 256, '172.16.', '10.100.', '10.200.', '4150' ]


if __name__ == "__main__":
    g = Generate(param_list)
    g.generate_ip_lists()
    g.generate_many_to_one()
    
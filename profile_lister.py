#!/usr/bin/env python

from __future__ import absolute_import, division, print_function

import netmiko
from getpass import getpass


device_type = 'f5_ltm'
device = raw_input('device: ')
username = raw_input('username: ')
password = getpass()

# pre-define lists for each profile type
client_ssl_list = []
http_list = []
http_compression_list = []
one_connect_list = []
rewrite_list = []
server_ssl_list = []
stream_list = []
tcp_list = []
web_acceleration_list = []
certificate_authority_list = []
client_ldap_list = []
dhcpv4_list = []
dhcpv6_list = []
diameter_list = []
dns_list = []
dns_logging_list = []
fasthttp_list = []
fastl4_list = []
fix_list = []
ftp_list = []
gtp_list = []
html_list = []
http2_list = []
icap_list = []
iiop_list = []
ipother_list = []
mblb_list = []
mssql_list = []
ntlm_list = []
ocsp_stapling_params_list = []
pptp_list = []
qoe_list = []
radius_list = []
request_adapt_list = []
request_log_list = []
response_adapt_list = []
rtsp_list = []
sctp_list = []
server_ldap_list = []
sip_list = []
smtp_list = []
smtps_list = []
socks_list = []
spdy_list = []
statistics_list = []
tcp_analytics_list = []
tftp_list = []
udp_list = []
web_security_list = []
websocket_list = []
xml_list = []

# Don't really need to pre-define this, but it keeps sanity checks happy if we do
connection = []

# catchall - nothing should end up in here
misc_list = []


try:
    print('~'*79)
    print('Connecting to device', device)
    connection = netmiko.ConnectHandler(ip=device, device_type=device_type, username=username, password=password)

except netmiko.ssh_exception.NetMikoAuthenticationException:
    print('authentication failed to ', device)

if connection:
    print('Connected!')

command = 'list ltm profile one-line\n'
data = connection.send_command(command)

for line in data.split('\n'):
    if line.split()[2] == 'client-ssl':
        client_ssl_list.append(line)
    elif line.split()[2] == 'http':
        http_list.append(line)
    elif line.split()[2] == 'http-compression':
        http_compression_list.append(line)
    elif line.split()[2] == 'one-connect':
        one_connect_list.append(line)
    elif line.split()[2] == 'rewrite':
        rewrite_list.append(line)
    elif line.split()[2] == 'server-ssl':
        server_ssl_list.append(line)
    elif line.split()[2] == 'stream':
        stream_list.append(line)
    elif line.split()[2] == 'tcp':
        tcp_list.append(line)
    elif line.split()[2] == 'web-acceleration':
        web_acceleration_list.append(line)
    elif line.split()[2] == 'certificate-authority':
        certificate_authority_list.append(line)
    elif line.split()[2] == 'client-ldap':
        client_ldap_list.append(line)
    elif line.split()[2] == 'dhcpv4':
        dhcpv4_list.append(line)
    elif line.split()[2] == 'dhcpv6':
        dhcpv6_list.append(line)
    elif line.split()[2] == 'diameter':
        diameter_list.append(line)
    elif line.split()[2] == 'dns':
        dns_list.append(line)
    elif line.split()[2] == 'dns-logging':
        dns_logging_list.append(line)
    elif line.split()[2] == 'fasthttp':
        fasthttp_list.append(line)
    elif line.split()[2] == 'fastl4':
        fastl4_list.append(line)
    elif line.split()[2] == 'fix':
        fix_list.append(line)
    elif line.split()[2] == 'ftp':
        ftp_list.append(line)
    elif line.split()[2] == 'gtp':
        gtp_list.append(line)
    elif line.split()[2] == 'html':
        html_list.append(line)
    elif line.split()[2] == 'http2':
        http2_list.append(line)
    elif line.split()[2] == 'icap':
        icap_list.append(line)
    elif line.split()[2] == 'iiop':
        iiop_list.append(line)
    elif line.split()[2] == 'ipother':
        ipother_list.append(line)
    elif line.split()[2] == 'mblb':
        mblb_list.append(line)
    elif line.split()[2] == 'mssql':
        mssql_list.append(line)
    elif line.split()[2] == 'ntlm':
        ntlm_list.append(line)
    elif line.split()[2] == 'ocsp-stapling-params':
        ocsp_stapling_params_list.append(line)
    elif line.split()[2] == 'pptp':
        pptp_list.append(line)
    elif line.split()[2] == 'qoe':
        qoe_list.append(line)
    elif line.split()[2] == 'radius':
        radius_list.append(line)
    elif line.split()[2] == 'request-adapt':
        request_adapt_list.append(line)
    elif line.split()[2] == 'request-log':
        request_log_list.append(line)
    elif line.split()[2] == 'response-adapt':
        response_adapt_list.append(line)
    elif line.split()[2] == 'rtsp':
        rtsp_list.append(line)
    elif line.split()[2] == 'sctp':
        sctp_list.append(line)
    elif line.split()[2] == 'server-ldap':
        server_ldap_list.append(line)
    elif line.split()[2] == 'sip':
        sip_list.append(line)
    elif line.split()[2] == 'smtp':
        smtp_list.append(line)
    elif line.split()[2] == 'smtps':
        smtps_list.append(line)
    elif line.split()[2] == 'socks':
        socks_list.append(line)
    elif line.split()[2] == 'spdy':
        spdy_list.append(line)
    elif line.split()[2] == 'statistics':
        statistics_list.append(line)
    elif line.split()[2] == 'tcp-analytics':
        tcp_analytics_list.append(line)
    elif line.split()[2] == 'tftp':
        tftp_list.append(line)
    elif line.split()[2] == 'udp':
        udp_list.append(line)
    elif line.split()[2] == 'web-security':
        web_security_list.append(line)
    elif line.split()[2] == 'websocket':
        websocket_list.append(line)
    elif line.split()[2] == 'xml':
        xml_list.append(line)

    else:
        misc_list.append(line)

# if a list has data in it, display it
if client_ssl_list:
    print('\n')
    print('~'*79)
    print('client-ssl')
    print('~'*79)
    for element in client_ssl_list:
        profile_name = element.split()
        print(profile_name[3])

if http_list:
    print('\n')
    print('~'*79)
    print('http')
    print('~'*79)
    for element in http_list:
        profile_name = element.split()
        print(profile_name[3])

if http_compression_list:
    print('\n')
    print('~'*79)
    print('http-compression')
    print('~'*79)
    for element in http_compression_list:
        profile_name = element.split()
        print(profile_name[3])

if one_connect_list:
    print('\n')
    print('~'*79)
    print('one-connect')
    print('~'*79)
    for element in one_connect_list:
        profile_name = element.split()
        print(profile_name[3])

if rewrite_list:
    print('\n')
    print('~'*79)
    print('rewrite')
    print('~'*79)
    for element in rewrite_list:
        profile_name = element.split()
        print(profile_name[3])

if server_ssl_list:
    print('\n')
    print('~'*79)
    print('server-ssl')
    print('~'*79)
    for element in server_ssl_list:
        profile_name = element.split()
        print(profile_name[3])

if stream_list:
    print('\n')
    print('~'*79)
    print('stream\n')
    print('~'*79)
    for element in stream_list:
        profile_name = element.split()
        print(profile_name[3])

if tcp_list:
    print('\n')
    print('~'*79)
    print('tcp')
    print('~'*79)
    for element in tcp_list:
        profile_name = element.split()
        print(profile_name[3])

if web_acceleration_list:
    print('\n')
    print('~'*79)
    print('web-acceleration')
    print('~'*79)
    for element in web_acceleration_list:
        profile_name = element.split()
        print(profile_name[3])

if misc_list:
    print('\n')
    print('~'*79)
    print('MISC')
    print('~'*79)
    for element in misc_list:
        profile_name = element.split()
        print(element)

if certificate_authority_list:
    print('\n')
    print('~'*79)
    print('certificate-authority')
    print('~'*79)
    for element in certificate_authority_list:
        profile_name = element.split()
        print(profile_name[3])


if client_ldap_list:
    print('\n')
    print('~'*79)
    print('client-ldap')
    print('~'*79)
    for element in client_ldap_list:
        profile_name = element.split()
        print(profile_name[3])


if dhcpv4_list:
    print('\n')
    print('~'*79)
    print('dhcpv4')
    print('~'*79)
    for element in dhcpv4_list:
        profile_name = element.split()
        print(profile_name[3])


if dhcpv6_list:
    print('\n')
    print('~'*79)
    print('dhcpv6')
    print('~'*79)
    for element in dhcpv6_list:
        profile_name = element.split()
        print(profile_name[3])


if diameter_list:
    print('\n')
    print('~'*79)
    print('diameter')
    print('~'*79)
    for element in diameter_list:
        profile_name = element.split()
        print(profile_name[3])


if dns_list:
    print('\n')
    print('~'*79)
    print('dns')
    print('~'*79)
    for element in dns_list:
        profile_name = element.split()
        print(profile_name[3])


if dns_logging_list:
    print('\n')
    print('~'*79)
    print('dns-logging')
    print('~'*79)
    for element in dns_logging_list:
        profile_name = element.split()
        print(profile_name[3])


if fasthttp_list:
    print('\n')
    print('~'*79)
    print('fasthttp')
    print('~'*79)
    for element in fasthttp_list:
        profile_name = element.split()
        print(profile_name[3])


if fastl4_list:
    print('\n')
    print('~'*79)
    print('fastl4')
    print('~'*79)
    for element in fastl4_list:
        profile_name = element.split()
        print(profile_name[3])


if fix_list:
    print('\n')
    print('~'*79)
    print('fix')
    print('~'*79)
    for element in fix_list:
        profile_name = element.split()
        print(profile_name[3])


if ftp_list:
    print('\n')
    print('~'*79)
    print('ftp')
    print('~'*79)
    for element in ftp_list:
        profile_name = element.split()
        print(profile_name[3])


if gtp_list:
    print('\n')
    print('~'*79)
    print('gtp')
    print('~'*79)
    for element in gtp_list:
        profile_name = element.split()
        print(profile_name[3])


if html_list:
    print('\n')
    print('~'*79)
    print('html')
    print('~'*79)
    for element in html_list:
        profile_name = element.split()
        print(profile_name[3])


if http2_list:
    print('\n')
    print('~'*79)
    print('http2')
    print('~'*79)
    for element in http2_list:
        profile_name = element.split()
        print(profile_name[3])


if icap_list:
    print('\n')
    print('~'*79)
    print('icap')
    print('~'*79)
    for element in icap_list:
        profile_name = element.split()
        print(profile_name[3])


if iiop_list:
    print('\n')
    print('~'*79)
    print('iiop')
    print('~'*79)
    for element in iiop_list:
        profile_name = element.split()
        print(profile_name[3])


if ipother_list:
    print('\n')
    print('~'*79)
    print('ipother')
    print('~'*79)
    for element in ipother_list:
        profile_name = element.split()
        print(profile_name[3])


if mblb_list:
    print('\n')
    print('~'*79)
    print('mblb')
    print('~'*79)
    for element in mblb_list:
        profile_name = element.split()
        print(profile_name[3])


if mssql_list:
    print('\n')
    print('~'*79)
    print('mssql')
    print('~'*79)
    for element in mssql_list:
        profile_name = element.split()
        print(profile_name[3])


if ntlm_list:
    print('\n')
    print('~'*79)
    print('ntlm')
    print('~'*79)
    for element in ntlm_list:
        profile_name = element.split()
        print(profile_name[3])


if ocsp_stapling_params_list:
    print('\n')
    print('~'*79)
    print('ocsp-stapling-params')
    print('~'*79)
    for element in ocsp_stapling_params_list:
        profile_name = element.split()
        print(profile_name[3])


if pptp_list:
    print('\n')
    print('~'*79)
    print('pptp')
    print('~'*79)
    for element in pptp_list:
        profile_name = element.split()
        print(profile_name[3])


if qoe_list:
    print('\n')
    print('~'*79)
    print('qoe')
    print('~'*79)
    for element in qoe_list:
        profile_name = element.split()
        print(profile_name[3])


if radius_list:
    print('\n')
    print('~'*79)
    print('radius')
    print('~'*79)
    for element in radius_list:
        profile_name = element.split()
        print(profile_name[3])


if request_adapt_list:
    print('\n')
    print('~'*79)
    print('request-adapt')
    print('~'*79)
    for element in request_adapt_list:
        profile_name = element.split()
        print(profile_name[3])


if request_log_list:
    print('\n')
    print('~'*79)
    print('request-log')
    print('~'*79)
    for element in request_log_list:
        profile_name = element.split()
        print(profile_name[3])


if response_adapt_list:
    print('\n')
    print('~'*79)
    print('response-adapt')
    print('~'*79)
    for element in response_adapt_list:
        profile_name = element.split()
        print(profile_name[3])


if rtsp_list:
    print('\n')
    print('~'*79)
    print('rtsp')
    print('~'*79)
    for element in rtsp_list:
        profile_name = element.split()
        print(profile_name[3])


if sctp_list:
    print('\n')
    print('~'*79)
    print('sctp')
    print('~'*79)
    for element in sctp_list:
        profile_name = element.split()
        print(profile_name[3])


if server_ldap_list:
    print('\n')
    print('~'*79)
    print('server-ldap')
    print('~'*79)
    for element in server_ldap_list:
        profile_name = element.split()
        print(profile_name[3])


if sip_list:
    print('\n')
    print('~'*79)
    print('sip')
    print('~'*79)
    for element in sip_list:
        profile_name = element.split()
        print(profile_name[3])


if smtp_list:
    print('\n')
    print('~'*79)
    print('smtp')
    print('~'*79)
    for element in smtp_list:
        profile_name = element.split()
        print(profile_name[3])


if smtps_list:
    print('\n')
    print('~'*79)
    print('smtps')
    print('~'*79)
    for element in smtps_list:
        profile_name = element.split()
        print(profile_name[3])


if socks_list:
    print('\n')
    print('~'*79)
    print('socks')
    print('~'*79)
    for element in socks_list:
        profile_name = element.split()
        print(profile_name[3])


if spdy_list:
    print('\n')
    print('~'*79)
    print('spdy')
    print('~'*79)
    for element in spdy_list:
        profile_name = element.split()
        print(profile_name[3])


if statistics_list:
    print('\n')
    print('~'*79)
    print('statistics')
    print('~'*79)
    for element in statistics_list:
        profile_name = element.split()
        print(profile_name[3])


if tcp_analytics_list:
    print('\n')
    print('~'*79)
    print('tcp-analytics')
    print('~'*79)
    for element in tcp_analytics_list:
        profile_name = element.split()
        print(profile_name[3])


if tftp_list:
    print('\n')
    print('~'*79)
    print('tftp')
    print('~'*79)
    for element in tftp_list:
        profile_name = element.split()
        print(profile_name[3])


if udp_list:
    print('\n')
    print('~'*79)
    print('udp')
    print('~'*79)
    for element in udp_list:
        profile_name = element.split()
        print(profile_name[3])


if web_security_list:
    print('\n')
    print('~'*79)
    print('web-security')
    print('~'*79)
    for element in web_security_list:
        profile_name = element.split()
        print(profile_name[3])


if websocket_list:
    print('\n')
    print('~'*79)
    print('websocket')
    print('~'*79)
    for element in websocket_list:
        profile_name = element.split()
        print(profile_name[3])


if xml_list:
    print('\n')
    print('~'*79)
    print('xml')
    print('~'*79)
    for element in xml_list:
        profile_name = element.split()
        print(profile_name[3])

if misc_list:
    print('\n')
    print('~'*79)
    print('*** WARNING *** Misc list. Nothing should be in here. Check profile categories.')
    print('~'*79)
    for element in misc_list:
        profile_name = element.split()
        print(profile_name[3])

connection.disconnect()

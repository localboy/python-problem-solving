"""
Hosts and the Total Number of Requests
In this challenge, you will write a program to analyze a log file
and summarize the results. You will be given a text file of an
http requests log and must list the number of requests from
each host. Output should be directed to a file as described in
the Program Description below.
The format of the log file, a text file with a .txt extension,
follows. Each line contains a single log record with the
following columns (in order):
1. The hostname of the host making the request.
2. This column's values are missing and were replaced by a
hyphen.
3. This column's values are missing and were replaced by a
hyphen.
4. A timestamp enclosed in square brackets following theformat [DD/mmm/YYYY:HH:MM:SS -0400] , where DD is the
day of the month, mmm is the name of the month, YYYY is
the year, HH:MM:SS is the time in 24-hour format, and -
0400 is the time zone.
5. The request, enclosed in quotes (e.g., "GET /images/NASA-
logosmall.gif HTTP/1.0" ).
6. The HTTP response code.
7. The total number of bytes sent in the response.
Example log file entry
Function Description
Your function must create a unique list of hostnames with their
number of requests and output to a file named
records_ filename where filename is replaced with the input
filename. Each hostname should be followed by a space then
the number of requests and a newline. Order doesn't matter.
Constraints
The log file has a maximum of 2 × 10 5 lines of records.
Input Format
Sample Case 0
Sample Input 0
hosts_access_log_00.txt
Sample Output 0
Given filename = "hosts_access_log_00.txt", we process the
records in hosts_access_log_00.txt and create an output file
named records_hosts_access_log_00.txt containing the
following rows:
burger.letters.com 3
d104.aa.net 3
unicomp6.unicomp.net 4
Explanation 0
The log file hosts_access_log_00.txt contains the following
log records:
unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400]
"GET /shuttle/countdown/ HTTP/1.0" 200 3985
burger.letters.com - - [01/Jul/1995:00:00:11 -0400] "GET
/shuttle/countdown/liftoff.html HTTP/1.0" 304 0
burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET
/images/NASA-logosmall.gif HTTP/1.0" 304 0
burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET
/shuttle/countdown/video/livevideo.gif HTTP/1.0" 200 0
d104.aa.net - - [01/Jul/1995:00:00:13 -0400] "GET
/shuttle/countdown/ HTTP/1.0" 200 3985
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400]
"GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400]
"GET /images/NASA-logosmall.gif HTTP/1.0" 200 786
unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400]
"GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204
d104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET
/shuttle/countdown/count.gif HTTP/1.0" 200 40310
d104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET
/images/NASA-logosmall.gif HTTP/1.0" 200 786
When we consolidate the data above, we confirm the
following:
1. The host unicomp6.unicomp.net made 4 requests.
2. The host burger.letters.com made 3 requests.
3. The host d104.aa.net made 3 requests.
"""

if __name__ == '__main__':
    filename = input('Enter a filename: ')

    try:
        with open(filename) as f:
            variable=f.readlines()
        hosts = [v.split()[0] for v in variable]
        new_file = 'record_' + filename
        
        with open(new_file, 'w') as nf:
            nf.write('\n'.join(list([i + ' ' + str(hosts.count(i)) for i in set(sorted(hosts))])))
    except FileNotFoundError:
        print('File not found')
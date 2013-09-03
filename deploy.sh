#!/bin/bash
rm mysite.tar.gz
tar czvf mysite.tar.gz mysite
scp mysite.tar.gz ec2-user@ec2-54-213-47-138.us-west-2.compute.amazonaws.com:/home/ec2-user/mysite.tar.gz
rm mysite.tar.gz

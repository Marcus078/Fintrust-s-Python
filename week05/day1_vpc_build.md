# Week 5 Day 1: Amazon VPC Deep Dive

## Overview

Today focused on Amazon VPC, the networking foundation of AWS. We learned how to design secure, scalable, and highly available network architectures using VPCs, subnets, route tables, gateways, and security controls.

Using the FinTrust Bank scenario, we designed and built a production-style Multi-AZ VPC architecture in the Cape Town AWS Region (`af-south-1`).

## AM Session: Amazon VPC Deep Dive

Topics covered:

- Amazon VPC fundamentals
- CIDR notation and IP addressing
- Public and Private Subnets
- Route Tables
- Internet Gateways (IGW)
- NAT Gateways
- Security Groups
- Network ACLs (NACLs)
- Multi-AZ architecture design

## PM Session: Multi-AZ VPC Build Lab

During the practical lab, I built the FinTrust VPC architecture in AWS.

Tasks completed:

- Created a VPC
- Created six subnets
- Attached an Internet Gateway
- Created public and private route tables
- Created NAT Gateways
- Configured Security Groups
- Verified connectivity

## Reflection

The concept that stood out most was understanding that route tables determine whether a subnet is public or private. I also learned the importance of deploying resources across multiple Availability Zones to improve availability and fault tolerance.
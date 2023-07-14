# Security in Computer Networks
## Principles of Cryptography
### Symmetric Key Cryptography
#### Block Ciphers
2 broad classes of symmetric encryption techniques:
 * stream cipher
 * block cipher

Popular block ciphers:
 * *DES* - Data Encryption Standard
 * *AES* - Advanced Encryption Standard

### Public Key Encryption
#### Session Key
*Session key* is *shared symmetric key* so that block cipher such as *DES* or *AES* can be used 

## Message Integrity and Digital Signatures
### Digital Signatures
#### Public Key Certification
> An important application of digital signatures is *public key certification*, that is, certifying that a public key belongs to a specific entity. Public key certification is
used in many popular secure networking protocols, including IPsec and SSL.

SELF COMMENT: The short paragraph above indicates that a *certification* contains:

* public key
* cerfitication information of the entity, to which this certification belongs

In the context of *https*, this certificate is intially sent from the server to the client, then

*CA (Certificate Authority)*


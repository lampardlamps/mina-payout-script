## Supercharged Pool Payout Script

This is a fork of Minaexplorer's script: https://github.com/garethtdavies/mina-payout-script (with thanks to him!). The main purpose of this script is to implement the payout logic of the Supercharged Pool (https://minaexplorer.com/wallet/B62qif7HxYzQCb8v2FN3KgZkS8oevDG2zqYqzkdjSV1Smf6jbEcPVEc): any wallet with locked tokens will NOT be paid, and all the rewards are shared with the wallets with ONLY unlocked tokens.

```
pip3 install -r requirements.txt
python3 payout.py
```

Will output:

```
Using ledger hash: jxRySSfk8kJZVj46zveaToDUJUC2GtprmeK7poqWymEzB6d2Tun
This script will payout from blocks 15107 to 20000 in epoch 3

The pool's total staking balance is: 12959594.201637622.
However, only 34897.996031090006 of it is unlocked,
and the block rewards are shared by the 24 unlocked accounts.

We won these 88 blocks:
+-------------+--------------+------------------------+---------------------+------------------------+
| BlockHeight |   Coinbase   | Producer Fee Transfers | Snark Fee Transfers | Coinbase Fee Transfers |
+-------------+--------------+------------------------+---------------------+------------------------+
|    19819    | 720000000000 |        3000000         |          0          |           0            |
|    19796    | 720000000000 |        6000000         |          0          |           0            |
|    19768    | 720000000000 |        3000000         |          0          |           0            |
|    19662    | 720000000000 |        2000000         |          0          |           0            |
|    19628    | 720000000000 |       102000000        |          0          |           0            |
|    19535    | 720000000000 |        9000000         |          0          |           0            |
|    19510    | 720000000000 |        8000000         |          0          |           0            |
|    19460    | 720000000000 |        2000000         |          0          |           0            |
|    19459    | 720000000000 |        9000000         |          0          |           0            |
|    19440    | 720000000000 |        2000000         |          0          |           0            |
|    19433    | 720000000000 |        3000000         |          0          |           0            |
|    19339    | 720000000000 |        8000000         |          0          |           0            |
|    19303    | 720000000000 |        15000000        |          0          |           0            |
|    19275    | 720000000000 |        2000000         |          0          |           0            |
|    19238    | 720000000000 |        12000000        |          0          |           0            |
|    19175    | 720000000000 |        3000000         |          0          |           0            |
|    19164    | 720000000000 |        2000000         |          0          |           0            |
|    19084    | 720000000000 |        1000000         |          0          |           0            |
|    19026    | 720000000000 |        1000000         |          0          |           0            |
|    19025    | 720000000000 |        4000000         |          0          |           0            |
|    19012    | 720000000000 |        2000000         |          0          |           0            |
|    19007    | 720000000000 |        2000000         |          0          |           0            |
|    18999    | 720000000000 |        61000000        |          0          |           0            |
|    18981    | 720000000000 |        5000000         |          0          |           0            |
|    18953    | 720000000000 |        2000000         |          0          |           0            |
|    18904    | 720000000000 |        4000000         |          0          |           0            |
|    18790    | 720000000000 |        4000000         |          0          |           0            |
|    18767    | 720000000000 |        1000000         |          0          |           0            |
|    18757    | 720000000000 |        4000000         |          0          |           0            |
|    18669    | 720000000000 |        16000000        |          0          |           0            |
|    18622    | 720000000000 |           0            |          0          |           0            |
|    18609    | 720000000000 |        1000000         |          0          |           0            |
|    18601    | 720000000000 |        1000000         |          0          |           0            |
|    18391    | 720000000000 |        3000000         |          0          |           0            |
|    18346    | 720000000000 |           0            |          0          |           0            |
|    18334    | 720000000000 |        2000000         |          0          |           0            |
|    18331    | 720000000000 |        3000000         |          0          |           0            |
|    18243    | 720000000000 |        1000000         |          0          |           0            |
|    18151    | 720000000000 |        2000000         |          0          |           0            |
|    17968    | 720000000000 |        2000000         |          0          |           0            |
|    17912    | 720000000000 |        1000000         |          0          |           0            |
|    17867    | 720000000000 |        4000000         |          0          |           0            |
|    17741    | 720000000000 |        1000000         |          0          |           0            |
|    17738    | 720000000000 |        3000000         |          0          |           0            |
|    17447    | 720000000000 |        10000000        |          0          |           0            |
|    17362    | 720000000000 |        11000000        |          0          |           0            |
|    17091    | 720000000000 |        23000000        |          0          |           0            |
|    17068    | 720000000000 |        36000000        |          0          |           0            |
|    17000    | 720000000000 |        11000000        |          0          |           0            |
|    16991    | 720000000000 |        11000000        |          0          |           0            |
|    16948    | 720000000000 |        2000000         |          0          |           0            |
|    16892    | 720000000000 |        24000000        |          0          |           0            |
|    16817    | 720000000000 |        12000000        |          0          |           0            |
|    16666    | 720000000000 |        34000000        |          0          |           0            |
|    16661    | 720000000000 |       234500000        |          0          |           0            |
|    16644    | 720000000000 |        12000000        |          0          |           0            |
|    16597    | 720000000000 |        11000000        |          0          |           0            |
|    16554    | 720000000000 |        33000000        |          0          |           0            |
|    16553    | 720000000000 |        11000000        |          0          |           0            |
|    16517    | 720000000000 |        11000000        |          0          |           0            |
|    16509    | 720000000000 |        32000000        |          0          |           0            |
|    16476    | 720000000000 |        13000000        |          0          |           0            |
|    16293    | 720000000000 |        12000000        |          0          |           0            |
|    16275    | 720000000000 |        12000000        |          0          |           0            |
|    16261    | 720000000000 |        33000000        |          0          |           0            |
|    16229    | 720000000000 |       112000000        |          0          |           0            |
|    16160    | 720000000000 |        11000000        |          0          |           0            |
|    16054    | 720000000000 |        12000000        |          0          |           0            |
|    16042    | 720000000000 |        15000000        |          0          |           0            |
|    15999    | 720000000000 |        12000000        |          0          |           0            |
|    15911    | 720000000000 |        11000000        |          0          |           0            |
|    15817    | 720000000000 |        11000000        |          0          |           0            |
|    15814    | 720000000000 |        12000000        |          0          |           0            |
|    15798    | 720000000000 |        11000000        |          0          |           0            |
|    15795    | 720000000000 |        22000000        |          0          |           0            |
|    15784    | 720000000000 |        11000000        |          0          |           0            |
|    15776    | 720000000000 |        11000000        |          0          |           0            |
|    15711    | 720000000000 |        12000000        |          0          |           0            |
|    15689    | 720000000000 |        12000000        |          0          |           0            |
|    15647    | 720000000000 |        11000000        |          0          |           0            |
|    15645    | 720000000000 |        24000000        |          0          |           0            |
|    15520    | 720000000000 |        35000000        |          0          |           0            |
|    15488    | 720000000000 |        11000000        |          0          |           0            |
|    15413    | 720000000000 |        10000000        |          0          |           0            |
|    15376    | 720000000000 |        10000000        |          0          |           0            |
|    15357    | 720000000000 |        12000000        |          0          |           0            |
|    15272    | 720000000000 |        11000000        |          0          |           0            |
|    15222    | 720000000000 |       122000000        |          0          |           0            |
+-------------+--------------+------------------------+---------------------+------------------------+
We have received grand total of 63361.431500000 mina in this window.
Our fee at 2.5% is 1584.035787500 mina, and the total payout amount is 61777.395712500
+---------------------------------------------------------+-------------------+-----------+-----------------+-----------------+
|                        PublicKey                        |  Staking Balance  | Unlocked? | Payout nanomina |   Payout mina   |
+---------------------------------------------------------+-------------------+-----------+-----------------+-----------------+
| B62qpge4uMq4Vv5Rvc8Gw9qSquUYd6xoW1pz7HQkMSHm6h1o7pvLPAN |    0.010000000    |   True    |    17702230     |   0.017702230   |
| B62qkPnVJoYjB6AB4hXg5LA3LDxTGJKJJfV8HZDu3SdJbzDvGUBnhDm |    0.100000000    |   True    |    177022714    |   0.177022714   |
| B62qrYDn9gjvt4PGN9rPjnHiGnstJrYo2oHtJ7tbWYNsLtWk4WLZMXt |  4389.917417867   |   True    |  7771152968972  | 7771.152968972  |
| B62qmaatVU8sTcRTYWr7vmhYjCRWvNoKVf3Te7Cks6iWJ3ZNpjUwcVK |   612.393000000   |   True    |  1084074989790  | 1084.074989790  |
| B62qkNJPMFTJdgXDxb9YLgAvGiRSrcoU1TnQTQYKMh8wqZ2rkUynns4 |    1.100000000    |   True    |   1947250313    |   1.947250313   |
| B62qk9WYHu2PBYv4EyEubnVQURcwpiV2ysuYYoMdwi8YTnwZQ7H4bLM |  5899.312757818   |   True    | 10443126257034  | 10443.126257034 |
| B62qmBVAArv7jDvKKcWv4dhdPrqcti4C7XUM93ThCfaHdnfemXfHYTx |    1.400000000    |   True    |   2478318580    |   2.478318580   |
| B62qnJjx96oDkfA4rcDog7whcyHB19XfG6yYi8fekgXge9N9m9uax6U |    0.195000000    |   True    |    345194339    |   0.345194339   |
| B62qpzJgthynVQcXLePPDnKBAWc196b7fforhqeHCYncafYZPTZJfik |  4450.090000000   |   True    |  7877672134511  | 7877.672134511  |
| B62qkQJWnnDeWaqmBHsJ9ikLxsZfcdCtNhhRtrUnDfCe2Hzsqsu3RkV |  1675.947484894   |   True    |  2966808491634  | 2966.808491634  |
| B62qjt5GzHKrNZNx5gNBn9ebrAhHRQ62BmwvS5BvcLRUb2R1zqch28s |  11889.851000000  |   True    | 21047742384226  | 21047.742384226 |
| B62qkXNkRLUJj91VcFBFgCctdpgwfMXPe8fUHWDQtfL8TqRkR4TkdDT |    0.100000000    |   True    |    177022714    |   0.177022714   |
| B62qrXynZY4AKszEybHwcx1r9BkrroueBU6nGc2idCHnw5tQEjvpAHi |    0.000000000    |   True    |        0        |   0.000000000   |
| B62qjE4MrihFWPiBcm77JrbrQrycNwTbV6vv9utJFiMhBktnAQY2qUL |   612.850369124   |   True    |  1084884637237  | 1084.884637237  |
| B62qmPxdtJAufkMVG5xtNNmkrFoLH4Z1P3itV1SBAGXHnHexgozX4bi |   612.850369124   |   True    |  1084884637237  | 1084.884637237  |
| B62qrrMbZwJW5Nka86Q81xwq1Tx21kcLWqqVUPwCzz4GdasN8icD4Gs |    1.200000000    |   True    |   2124273068    |   2.124273068   |
| B62qjGXKTmoJGPPZuzYDzJwzdkjeFN8LvWRVKdEiMAGP4UoWYRs7AZx |    1.191000000    |   True    |   2108341023    |   2.108341023   |
| B62qrwpHTcLUq9epwFLbhu45hUjy7wjSjkwqcXuChbyGSBtHu5Ah5GY |    0.079000000    |   True    |    139847933    |   0.139847933   |
| B62qkd36WgsePzNcxN5dnkdpupB8H7BvfnZ7XMyGgWEBHVYdHcNYeb6 |   612.599000000   |   True    |  1084439656676  | 1084.439656676  |
| B62qpDBqtnDJT3jaC18ih7SZgbQ3BhNZ2CNg4b4fr2viLuGua3Y6ix6 |   612.537528296   |   True    |  1084330837771  | 1084.330837771  |
| B62qq7jDazmvSkXj8WWsoW2tg7fMm1zwZXKnNEmMd9qZ4t7nC7YGKcK |   612.190000000   |   True    |  1083715633587  | 1083.715633587  |
| B62qj5pJ7ZLKauDhhviYNpV8B6BpmZ3a9mXBjZMVJNNsQy3rpmnudoN |   612.113103967   |   True    |  1083579510108  | 1083.579510108  |
| B62qj8wH9YcKdzHu6NXbZpWqyZrYKYGeATh5o2UFZxC45KNYcTMvNoY |  1100.970000000   |   True    |  1948967479263  | 1948.967479263  |
| B62qjZBFstncJwSJ15HQZXfY9agDMs2uWiFo9dATRBYWVGm4ffJ7MRE |  1198.999000000   |   True    |  2122501120528  | 2122.501120528  |
| B62qkbdgRRJJfqcyVd23s9tgCkNYuGMCmZHKijnJGqYgs9N3UdjcRtR |  6697.563753375   |   False   |        0        |   0.000000000   |
| B62qqMo7X8i2NnMxrtKf3PAWfbEADk4V1ojWhGeH6Gvye9hrMjBiZjM |  32558.703045112  |   False   |        0        |   0.000000000   |
| B62qqomhidaLc7wbYPeaHkGkzXVNA9z7pqf8nL7UjiSZKmLmVT1mPEB |  32558.990000000  |   False   |        0        |   0.000000000   |
| B62qoB8RRURcit5keJXvq7uXzYkgN4Lsz5GFaVpGYdA9vAiASy3iBcD |  66000.471816426  |   False   |        0        |   0.000000000   |
| B62qrJb5c4yaeL5fDCrEU5tGsmJWbcfnkdW1pMQbGT1rAnnA2JjAP6h |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qowpMhZ2Ww7b8xQxcK7rrpfsL5Nt5Yz5uxaizUBKqpeZUqBETa31 |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qkrhfb1e3fV2HCsFxvnjKp1Yu4UyVpytucWDW16Ri3rzG9Ew2cF4 |  7065.114656873   |   False   |        0        |   0.000000000   |
| B62qqrn3yzWRDJrUni6cRva4t51AcnY1o1pM4xpB78MfHUH3ajZu1Ko |  65329.909092470  |   False   |        0        |   0.000000000   |
| B62qrdiTDeX3AP6aHn62WUsQ3dT7mH7zA6YUGmJ5R9FJDTac4j6DmPA |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qraStik5h6MHyJdB39Qd2gY2pPHaKsZFLWVNEv2h3F85T4DmtjC7 |  19378.600201813  |   False   |        0        |   0.000000000   |
| B62qqb9QnByFcRQ2BGY6LjogXvsbknCxUPbBzhbrB1rpFoKR9Ys5VpE |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qjW8gnXUWZH4zeMmHGgj73BRPt7bYkWQPcw3VG28QvfDJC2gvQvn |  66000.811089930  |   False   |        0        |   0.000000000   |
| B62qiWir45GBE9PWWoySrVnB8ERdL7QiykkfwjyzytuDSQTbibigSuw |  66002.733000000  |   False   |        0        |   0.000000000   |
| B62qrR8VjjKrijdZ9HgUg5D33CrNCWhDdJr8gvmdFFCizCGgaeANhXT |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qj5TbymjFWUsjHnCDNfzbFbacKzXwnHdgDJDoAZwcs5GD2sacGMc |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qrkCaGXGWJC7JWzdg1nJv7Y1opgWDTDi6XknSYwTdrkMpTrg9AXc |  66000.900000000  |   False   |        0        |   0.000000000   |
| B62qj49ZC1dvWzGNMd5VVxSVQhZv4rzoKd7TdsVSUAsHZ7x4mHXAWjH |  66000.000193897  |   False   |        0        |   0.000000000   |
| B62qrN1MZnXy15VXkh3D5XiNPQVKQLr4UXqBPFv3E4NHNFrzANC4wFb |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qrAJ7wiP6sJwjM3RsZX3Xzp21BpfkF3yXA49TxPNBHAKrjPLbx4J |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qrYkGp44a78p3t6uifiBq2wwctJw3k8u88sKLLAgdAZFK1G8UGcH |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qoWeaz5bDeo7Zt7ckkXnWEYTdNRUGQGgMNofUJ3hZcAG1KKbo4Ky |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qoSqKkE5B4HPxWtidWGDty12o95nicTb81fW6HbUDPycQvDBs1cD |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qmLHunUCqVvXShJD6Qtg353wtM5fvDnJJu3F1AkeiwEMmbrnhVjg |  66000.010000000  |   False   |        0        |   0.000000000   |
| B62qpuQzCRgYUH7Ehi8gsLdRWVc75uKHwTUmsbsqTUMeMF7DcgpEJbb |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qrzTgzDJ6n1UojoypnHx4P1onR61r3RZkFaqFcgQ1mVUPY6cJzSr |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qmgDU4ygtzV5ZueVWgSFjYtkatqjSTmj4z2jbjN5XjfLMrmK9zkx |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qmAgjG13dd7gH5HZVaFRXZMFsLUVhs6qyqJdzQbhFs8SU9rycSX5 |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qowSjKkwtESnVZtaZpvuPJFbkygn5CZo5Ym9AKTHX7hMjMEhGGKY |  66000.067824773  |   False   |        0        |   0.000000000   |
| B62qp7Poht74axa1BJMWmN6MzAwEAnr2uRhi444YDvE4KAm57LEBKET |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qo5HvEcc98R9N1Y19hpsvkyvHbgFc2f4Dg3EnDAaFo1N3MG3xWJx |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qp5dgv9tGSdD2DJDgJC8m5K3ah3mazxVagMm6pM5pJzX5QuPp8H6 |  66000.186000000  |   False   |        0        |   0.000000000   |
| B62qkag9ybmAzG9areQNg5oFNrsKjMc71q6nVnRDRDVo2XBxBcuzrA3 |  66000.000000000  |   False   |        0        |   0.000000000   |
| B62qixTkfYwADQSS9SHL9NRBoNKvmfCYxQAPhoLiZDA5RsrzqiRPLHp |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qpwAqAJ5HaJT3iJgoFM5vC9gSJ1u2b9tvpRXx3Ns8mVoZTUDgGSL |  66001.100000000  |   False   |        0        |   0.000000000   |
| B62qmbwRekMF7vGprxsSXT6XEPYVQcYN4dMdRZeZmAkPWwq1g4zV33Q |  66000.090000000  |   False   |        0        |   0.000000000   |
| B62qjV8B1C3nbRqKXEiREjNQCLuCL4Y75PPpwcFqWBAvFWN3X2iJJJD |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qpymA2yno7Qawq6vaK4aXtnNttAcvG4Nt23tFvbMPyG5yhEKMUSu |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qj8oSkVyBfVim9JWehGAa8eN43Q9RU5HQdzPSiy4XmS5uVAG7dJy |  66000.090000000  |   False   |        0        |   0.000000000   |
| B62qpH4BktZFp5in5jKcfFrUqAYKbpU2RhH8iHmLKdraVWxjdbUMbpG |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qrJr7qJF5VJRrChgJj9QsskoGdJzVNJoMk6dEtnEBNKci4faYWfe |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qmmjvVdhd2VBRyh5PJHiQkYkqLDgqa9uq5nfC2dM2MdfWt4ennHW |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qqL6UUFFPkM7m3j2mmuEfjQvQdsKSGTu2CqYeYftb4sr5ji9DiHu |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qmVkhfGqvfYrybuY3pgGjbLifcC1Wy1hLC7VtKHmvypuhancbueR |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qkes2AXQFszcXKtS9ZHVofoPRZJXiXzSfYVpH48vs14LVQXPoBfY |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qjBp3TgwngdrKkK69NjrhTFS9KSTriLFiv2FKvnhGfjbYFFZCT9M |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qnAkxbs4gqZVnqzpQ6vbuoAD4VQSzYLydjt1d7eV9na7kXky6vV3 |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qprj7x2ByZHbVAf8r7k4fZKR4f745ysQA3fYgZh3gSdPoWXCDry7 |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qjNN4wmuSdk6sS47Kpfi7CzdSEsf8Qm3HtmNCyxFhE8zxufycgQ6 |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qjDdeNBAc1AemCQ8fGYcLTCuqZGimzGUb4pXdzYws3wCmYFCDTQe |  66000.090000000  |   False   |        0        |   0.000000000   |
| B62qr2CgfiqKX2pVNkKTBKnHK8SAwqhHW1KUcszTp5Maivq1inYhRea |  66000.000000000  |   False   |        0        |   0.000000000   |
| B62qpHpeTCVYbnuhZexBqz5tCSAWKT1izgCFHs8n9EqvrLzppLGKXqJ |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qjKEsfg8hiRVUEcUjW1RstNtyhMes6hb5wfcgSZizfXU26SLk4cT |  66000.000000000  |   False   |        0        |   0.000000000   |
| B62qoo5DaMn4iZeVijjm2XnoiNhQTMCdWixHtNMGaD9kcGd1z988toe |  66332.738193897  |   False   |        0        |   0.000000000   |
| B62qpza4Xqp9GTDcsdjGJabz5M682oy7AudCD1jkqsMWHuzynLMfcKz |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qngpchppH4j7gtkHWnZfAzRm2ak2p2mBjNHtWssoEvhK2Ev4u167 |  66002.390000000  |   False   |        0        |   0.000000000   |
| B62qiWSe63weqBN3vpnUyagnMkYmvRwKKQJ4dKckuJFsojUAYY56mfx |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qj9MASPt6AcfxHawZcwkjFEfQqRVTn6HghdBmtEKvudWuRnhyEvG |  66000.000000000  |   False   |        0        |   0.000000000   |
| B62qqAmP51fjPJ1FFVXP8i48f4zhEyhRr47v2X4iVfSVtMiMG489HAH |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qpoqqu8Rhc6E5GN1McsT6VxL5i3DGuQkt3k23JVKZrNWxqGM4mDn |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qreVP6TddxX5CySuko7gqxVwzRmQyYzraHp85dzYG9g9ixPbVL3D |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qndynjUPACSp1Y9T6RppW6CU3K34wYXarR435Shbm2FD9un5AZjg |  66000.067824773  |   False   |        0        |   0.000000000   |
| B62qou778MhEYT3qzuUL6LhsmSVMpB7FQn9ZkWPsYcHNV6LgCLDHcoP |  66000.490000000  |   False   |        0        |   0.000000000   |
| B62qknJSP3q28HrstZ8trCWQR3DGaSWzYuNQSi1JkZxgbyuxGdp3Fw5 |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qqS4q8Lk8uCWBK6xsJcHpXSqpabvgNWm3gHaXAEaFGANU5Eqs3KP |  66000.000000000  |   False   |        0        |   0.000000000   |
| B62qjmwNZgQq5s757XqHqtQxiXWQECqan9bUFAQaRVFYP8tnFKQKRjY |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qopUvFqDi7UHtMtJyVsBPGGUKSmsaVr5C7qadxFQB5PJNxVan9R2 |  66000.000665601  |   False   |        0        |   0.000000000   |
| B62qid7mcNh29WVifR2qWQDLJ9dRu94EUcbsgrTr9fdFMGsPQzWv8Qo |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qnkCQqXyeXvbMavAG9U9cZ8JJi5XB7fwKMJoSEemzhqCWHQxpe5j |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qodJCdovJawjWjeYyttgjqJXfE9cn4UqZHqPtj74N4zrDZB4X7Gi |  66001.100000000  |   False   |        0        |   0.000000000   |
| B62qo5tnoVeYMWW7EwNHCeUVvBU6ffxog6zJa9CZemj3XBL3adbrQTp |  66000.090000000  |   False   |        0        |   0.000000000   |
| B62qrD4yGS7R7SutQnL4QqG28uwnRvX6hxAbyyAKiNn2HTkAv9x1BYq |  66000.066000000  |   False   |        0        |   0.000000000   |
| B62qjJPwZ81Z39Sg2WJ5tNPcCFBqwSeYZd68w8579eggnSyhFgGscuY |  66010.481000000  |   False   |        0        |   0.000000000   |
| B62qkUcq8Tt1h5PMXWoc9n4Jk6zsbG1YZoTeB8jQzS9JLrtL2HP6dyt |  66000.090000000  |   False   |        0        |   0.000000000   |
| B62qmvmCN8qzDBKAD6M89hvGQeundPcDHhq5DrU57orGGKyT8NtrrRe |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qm4AZDUA99AekfUfk1jufXR5KnaY7XFNUhd5tdV256voGdvwPFGR |  66003.928193897  |   False   |        0        |   0.000000000   |
| B62qmXi6YMzGmKhw7CK1M8VAybRyErq7VytkXULkjTjiB1FjTdoYxX1 |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qjGmBJWG5oP95zVCik6TZJ7HfoZpNLuEY2Ddy2ZBGWXsfm56zUqV |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qiwepAfGCvyDBMx8acQ2wTwEDLN4ZkAK4VEwtuDqawKfvs2Y2Ej6 |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qqa9zE4zcqLx2emeoeCp59f9iKBMiLtcQRDpBsqrxGvhrVciwB7G |  66110.897193897  |   False   |        0        |   0.000000000   |
| B62qrUAu3VZ2JUA2Z8kbFVWcd5vGehomxCnM2LptvpKbuu3y5GNxbb7 |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qowXgtSfrWgMwvP6yxe3Z3JnpRHKZhsWCRLETNvMnT7ezeT6rA4c |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qofdXQKEMyb1CzTCHopwZGWQ2etmhwvF66Ukm4d9FkzHB71qPUT5 |  66000.388000000  |   False   |        0        |   0.000000000   |
| B62qjYZCaRMB7cXWvCowkhEHiHmyhwu7AnDvQhHeDUfuaZ3c6y4JLgF |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qm6XTALQy15eQPvpdietiVAJ5QBU5WGRugAxRpsvbiXn6iSdNqzu |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qrKhDiFPNc1VgfVVvmxwTa6oDwv4DPXNwSxC1kvY7nqYDc1LcZXq |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qnXGNL44878HmkoTvkmjDHRxReHPFFjBcf4qjWDjUxjMoLmuJVWw |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qne2bgd34Fayvg6JjXtqULn1YyuFYfPWRqounqx6DH9Ju9Q99HRX |  66000.000000000  |   False   |        0        |   0.000000000   |
| B62qqja2YnsyBoDvMrpkHFCwJpSjEn47biEhm4QKZEUVFBxQZYZmv6w |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qjQ5cHbShm31do3N9wmRu1AVDBV1AaAQnxM9VoKq5aV8EERtnYB8 |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qpcGGx2UxNMgxqM9DrJuzkoB8Q6KrGifTVT6hdq4pwMUAsEtduQJ |  66000.090000000  |   False   |        0        |   0.000000000   |
| B62qrP5fybkeKbRpLRf2CFmnAjLEnZf36DT5CT6h8fMtxTJfYCzXqiW |  66610.888193897  |   False   |        0        |   0.000000000   |
| B62qo3VjJHcjPh8TEzWXajHfC4pXCHisnHEaAajkHEeMTQ62XYY24KM |  66251.188844466  |   False   |        0        |   0.000000000   |
| B62qp8TJyLYVFR6FnQAZ4A3aBKCMkEZzWBo3VSuGkyhBMdFAgjhTtE9 |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qikygSmv245hJZQzAhAqxfqeNiyPDZUS9MME4HkP9oFNhij85XUp |  66000.708193897  |   False   |        0        |   0.000000000   |
| B62qoa7ihzF5PiP66kFYctKKqmBy3JyVFYfHkaXBHJ1xKF3XdjvEzzV |  66000.217193897  |   False   |        0        |   0.000000000   |
| B62qkmLi1Th94fnNgqKYubXTtdbcXnNEEARgMcTNcyagCm9Dx7pUbHy |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qpGALWoNczLHTwTwhgxjj2qjNqdof2wzxFoZgxqyX1uaccnQ4Hnb |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qpdPvGHBe2ceij4GEZYAarqTdrWEi97trdZLRBoJHLxu1W2mqBG9 |  66000.090000000  |   False   |        0        |   0.000000000   |
| B62qpRa7iZ64Ws7aH971V32TRmDAcLBfuxppxx6s4CAvmC3NZfBjxeq |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qqRtCkFNBtAzB9D82ay94iFxU1RCtTXYQ4miqH6xrTiwEJ25T8sR |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qnuHogQxCbENFXYJdhyxz6dYCJDVVgjkvGxQyzxTVFN71vAyJGYQ |  66000.010000000  |   False   |        0        |   0.000000000   |
| B62qmCvy7LUqfZ6uZYPn6MY6pofWJntJdjx85RQRmL73jaEKpqe1Jv4 |  66002.390000000  |   False   |        0        |   0.000000000   |
| B62qkjHJXHXpqrdVsoM8JPQ9CGjimZzZzx73Wth8MyNyqmdkEMdGAxo |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qkqNhtDFa5ZDYGrUqn9CEB6aGrgMyj1JLeEPX4tmM6cdWnrH6rRo |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qqnTQYi2ZdDaeePDxmrgcporgoFMcTMbxPmzpwQn31VSXMHawzyU |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qjhfxnFVwmeeM2sQS6JFNKqQQjU6vh6aRx65rj2kLNYctTwGNZ6e |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qrCS5D3bvY9rJ7QLfkkiFF1Gq3S87q7qa72d6VbCwC1UjwxykHTF |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qooHQvsHsqfudGFU6wcK2YfCz7EuUd8cUT9qxfkEbt5uvTA4481Z |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qiU5Mc96FNQJQwv8JrE9LB8RkvummZ5MKnWTPCiY2E6KHnVppujV |  66721.010000000  |   False   |        0        |   0.000000000   |
| B62qjjXbygJnetM7hm8kC5T6rxTCZHzQL9SSxDaQopS6fVLwJUNYUan |  66000.090000000  |   False   |        0        |   0.000000000   |
| B62qjET9m1YnNPcgdFZCBiacwGAo3nXZY7GdLdvVsa6cNCPPk5FTc9d |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qnYnbEvsgp6XxhniNMSJWA43S1KhWFTa5yj8eNxesUT4oy1SC7r3 |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qqg8tqdhUx9K9borozHQanZpRs7zGPsRZYt3tXVMuuMYjUtaCvU1 |  66000.000000000  |   False   |        0        |   0.000000000   |
| B62qknwJHQU7EwT9NcvUbqwq95oHx8fFMQiGpEeiq2hKkfKWor3zdnQ |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qkaLCKizSR2XFYFK22jVPuxSjJKXPhm8b9QxsGmW5K15eYFq7ZNH |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qqBjKoZYj1A7AAigACJZjwr7Fx2wYLGwc4z7a2WpHhsxfLu15mzH |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qieizHWA2zusWh8y9eCzqA6dvgGNSs5RJGHPmAGcBtdgr8BRSfEg |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qpqKh6G14cd8HdnXw8xk5kZhRLywjJkPChRBXh16J69dtkWhtw1K |  66000.090000000  |   False   |        0        |   0.000000000   |
| B62qoKgbZLxduRtXiWrfM4zhmkicPQwsNtd4eqcizd7WPwD18aDH5hj |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qmW3eMFnZkFPEkqz35KvuRfEJdx4U5PydcUmbs2P3ioV8c3qZCuR |  66000.000000000  |   False   |        0        |   0.000000000   |
| B62qjwTD8QKpffkzNEvtJVqRfK9gT1APcvAu6PkV2nD4PLTbvzx9KTM |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qjJ8mNz65hUKWTh5wYbaHDa9nqfhz21JbY4ts69xBNYhTQxbQzCJ |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qrGdW3pGKhs8BRGrjom3WzTFShfAobatkyKwqw7Yrn6NEYDDpH9C |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qpGyTotKHjKuT9GNb9SG2gH44RwkdpzfFSpvrTLTNx77onpvwfpE |  66612.937193897  |   False   |        0        |   0.000000000   |
| B62qmQ7bj2w7PsKUkhicKKYCP3FpaGRExYVZm1EPLrniABscEELzgSz |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qqkhvx6FtK5D5Z7K1x7ebVjoxd28NtSCRacYTqueWCWQERqtEDPb |  66613.938193897  |   False   |        0        |   0.000000000   |
| B62qrAjwKEug5bXehb1WoxPrDf7heb2VSy8yEmKHVp1dAfseYHhBmfk |  5046.510469181   |   False   |        0        |   0.000000000   |
| B62qoSKy5LTX48VRcvVuCfWLMeuHNqsqPZXXeYwHVkxshneaeW1rKPh |  2018.604187613   |   False   |        0        |   0.000000000   |
| B62qkwrHj3YCKgQsXRktpwhVFij19RiwYDgMmiwp7iggNBi8712a4W4 |  10000.244820647  |   False   |        0        |   0.000000000   |
| B62qn519rweP51hpDGQYqCZ8JRPkpxHd2JzDoBFQcupGppuwkpGBHp9 |  2018.604187613   |   False   |        0        |   0.000000000   |
| B62qm8BBqTFCc1KKiDU6wuqjZf6n65dasH8jAHSrLZiNyzhQJLZUizQ |  2722.290000000   |   False   |        0        |   0.000000000   |
| B62qrSiA6i3HQRDS2boxepfMaXQeof88YLTJBEr3qjCNZerNfrZkEYs |  3002.390000000   |   False   |        0        |   0.000000000   |
| B62qo1EYgARevAzQyNDxhNmKwZAdHg4j65Sr4JnJwtoLGXt6ustog1n |  2018.604187613   |   False   |        0        |   0.000000000   |
| B62qrQMPSJpee1NnxVb4cr1qBtH3kMNpXaHVj4oVxNhqadCMBk6wELy | 309677.012160129  |   False   |        0        |   0.000000000   |
| B62qmQAFPta1Q3c7wXHxXRKnE3uWyBYZCLb8frdHEgavi3BbBVkpeC1 | 507454.463072188  |   False   |        0        |   0.000000000   |
| B62qoUiAHZZ9xY7BibT84iwMtgQidQByE7tCuNhn6DmyKhUPAzpnJAd | 309677.012160129  |   False   |        0        |   0.000000000   |
| B62qouqyiJfmysbVqgXZJy7rDvh2ZT1w5vmEQXqKAkpfvk37xQePyYL | 203053.176619445  |   False   |        0        |   0.000000000   |
| B62qiX7wCtUbpzgJavPKbfBcLJ6nyYB88cWjfwjWZiyZZLS7weCDxwm | 203053.176619445  |   False   |        0        |   0.000000000   |
| B62qn71s63yywMUCcFhP4iCata7HpgyrvmGjpKa1D9544vGW6FBZ6a1 | 909354.049955700  |   False   |        0        |   0.000000000   |
| B62qqEV4oP7w2jLQGckvZzdWjfdLKySKHJ3tNU5niRjpPD7beYumWTB | 613559.297664572  |   False   |        0        |   0.000000000   |
| B62qmsYXFNNE565yv7bEMPsPnpRCsMErf7J2v5jMnuKQ1jgwZS8BzXS | 1709737.537593210 |   False   |        0        |   0.000000000   |
+---------------------------------------------------------+-------------------+-----------+-----------------+-----------------+


```

Take the output to a different machine to sign - see `sign.ts` for an example.

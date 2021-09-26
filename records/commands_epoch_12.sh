export $(cat ~/.mina-env | xargs)

mina accounts import -privkey-path ~/cb_keys/my-wallet

export SUPERCHARGED_POOL=B62qmvHQzJmT2rKE1F9RemenGRG8BfXT1Kurve3eT4iC2HMrWiaVG3H

mina accounts unlock -public-key $SUPERCHARGED_POOL 

mina client send-payment -amount 811.723531619 -receiver B62qp5779JznHu89EpPxwmB1DLuY5aucG385GGXhodzQ18KJNLJG5cY -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 285
sleep 1s 
mina client send-payment -amount 208.467048194 -receiver B62qkP2wF1xfiMy6zpdaJEsDojjp6stmpAn6speYW57iaFr2bUthhpA -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 286
sleep 1s 
mina client send-payment -amount 194.172754503 -receiver B62qmMkbajiY3bdVRjv5bx3yxjp5sBHHQuu8M11sDdjtBy5VdgWdgTr -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 287
sleep 1s 
mina client send-payment -amount 174.732799266 -receiver B62qiefFsu75RVCL8cBjz1iq8d1p5X1wbX8iddmEUsq9UwuDrimPuo5 -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 288
sleep 1s 
mina client send-payment -amount 162.634265489 -receiver B62qkFa1sHgmFi5u5kW5oG4iPvycp6komoSNLn5TT8uKGfsmh1EnAjZ -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 289
sleep 1s 
mina client send-payment -amount 155.474925058 -receiver B62qkGVCPGHrLHV9r3G9NqD9du2Wcb5uKBfDvLwbxDKnyjMppHoN6gi -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 290
sleep 1s 
mina client send-payment -amount 110.125363523 -receiver B62qpUpEH7ivz61Sxo3PuTxntUNswmiHo2jwE2HvqmSVYW7q8xoStkx -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 291
sleep 1s 
mina client send-payment -amount 90.718029683 -receiver B62qnYVJSEPGrVtUvECksn4cRDBa8c4QhLQ7dzoHxqB6kPcAZvY41ui -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 292
sleep 1s 
mina client send-payment -amount 87.100400717 -receiver B62qmkmSCiTvayykE34nVjvyGdYDvFhx1iHV94rHgkESSNiApTzixj9 -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 293
sleep 1s 
mina client send-payment -amount 83.071999245 -receiver B62qiYihpWA6auBZun2ayZZhnf5bsT1qyq5LvDCk1piokgykeWM7j5M -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 294
sleep 1s 
mina client send-payment -amount 59.495833401 -receiver B62qrqZUXMccumSmoPExAjxkyUQVm5pCQpsECB4GtkRohEGiFMiMQJN -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 295
sleep 1s 
mina client send-payment -amount 38.094962874 -receiver B62qqysUvMRJ8Pyc135g9dRPj5CGDrcGTpWS4KGgH1Nr9yp12i3VDaa -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 296
sleep 1s 
mina client send-payment -amount 33.941787153 -receiver B62qjSEK49kPcp1PPKPjynWCG7rBz69nqdXGk7aNtDUxxj6qiwi6kDq -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 297
sleep 1s 
mina client send-payment -amount 33.696716625 -receiver B62qmKTP2kpPvCmjiaN1Qt3U6JxQm4opxZzmjvyRwwihDV2CLsSTxzg -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 298
sleep 1s 
mina client send-payment -amount 29.039823619 -receiver B62qpn3hY83x3acuJ4XTFqZmbYfAim76AXjfduxbrn1uEJv8YGafNz2 -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 299
sleep 1s 
mina client send-payment -amount 20.228357739 -receiver B62qkHAZshmphiL13WYgXN55FFPfrQA7jGWPaobVwvgYmq7eZnaL62e -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 300
sleep 1s 
mina client send-payment -amount 19.243283768 -receiver B62qrUfmK7TrJwNXPiAk5FL3Q3GB8zaYQBY8CqUBoSy2s7b4VCHNZHV -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 301
sleep 1s 
mina client send-payment -amount 19.241343712 -receiver B62qmErVtaUFVio5wH2w4NEYyXXBWf1dEPgcW5i4Be5groik8js5sbS -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 302
sleep 1s 
mina client send-payment -amount 16.991580246 -receiver B62qj6jtkWLVTaQeWBrey5pkBBgA8Vwonn8gXACuW44YD59CHY6gxzS -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 303
sleep 1s 
mina client send-payment -amount 16.991580246 -receiver B62qnE6ZeP7wdhWxPDpJvpwTN4LLEW6f5JAbgaaYRFuUk8abK27v4wE -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 304
sleep 1s 
mina client send-payment -amount 16.980342754 -receiver B62qrPnUQcCmQ1XPypTkSG7c2YhRkU2mvdWr9uGLS9S8eBvuWZYdnSu -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 305
sleep 1s 
mina client send-payment -amount 16.974093983 -receiver B62qoNX2W5k8gijbV8A6CbotR8rssgfGo99U2oNYRqtKvd14QSg2d9Q -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 306
sleep 1s 
mina client send-payment -amount 16.922137044 -receiver B62qp6cZQWwJZfyjuPzNDaXxc6BnwxMzjEYWGxxko43k3mx2VitrZBP -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 307
sleep 1s 
mina client send-payment -amount 16.903244865 -receiver B62qnQQaf736WgHyds2UaMb41CzCqZfDDNSmqfjDx6mcAxGxoGJd2tW -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 308
sleep 1s 
mina client send-payment -amount 15.916901614 -receiver B62qrgVUFe9bJCpsBBjP6SnBdSZTNYsiYdHn1mfudd7d8QPQcoYb3fn -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 309
sleep 1s 
mina client send-payment -amount 13.182918501 -receiver B62qmrmcKaKhFYNV8m6vnShQzuVF7enwRRyM6ESv4tFKmPKjXwMhPMW -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 310
sleep 1s 
mina client send-payment -amount 12.106688887 -receiver B62qkBMtTuTguHAmjABKGfX2C4ca6WZuTj2yXFB7B5VsB7aSxFz7gnG -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 311
sleep 1s 
mina client send-payment -amount 10.188060882 -receiver B62qjsiS7ynezJPc3FnzPe9isRh53xqftuQ7H2TRK3vanGFr76m7Uyx -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 312
sleep 1s 
mina client send-payment -amount 8.671340047 -receiver B62qoytoZPzr7QxkwsrfhkRat1np2ghRygHnw4AVMuYtJodsRiSHxvo -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 313
sleep 1s 
mina client send-payment -amount 6.968877283 -receiver B62qm4HceSuB9Pds5TgEipa4bhThvezuoDozJmY4SfeNodD4WgqXNge -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 314
sleep 1s 
mina client send-payment -amount 6.956842460 -receiver B62qpoEqFGy8mqeV23u3tc9kN9iuuUkdQfKvycRqXCuunF6GfxsrfDY -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 315
sleep 1s 
mina client send-payment -amount 6.052423240 -receiver B62qmdQ8VwCh4o2WFJUtx4behatPR1bsTiZqZMkpfvLL5SBG6cF7TEE -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 316
sleep 1s 
mina client send-payment -amount 4.921547189 -receiver B62qmu46DVv9f86QkJtvdP5dNbzeCeYNy91jqDM4ysDttfrqn3xnGpp -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 317
sleep 1s 
mina client send-payment -amount 4.488875505 -receiver B62qrbhYaFqVRj3TGvEJXkHbrd4yPHgd3nABwLCGm48g9W3VcV1emBw -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 318
sleep 1s 
mina client send-payment -amount 3.391633473 -receiver B62qkLdEr6XTWAcFxrdMcHfrQmMeLwZ1AJi7piw6sJvLV33vu2uK3V7 -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 319
sleep 1s 
mina client send-payment -amount 1.383835013 -receiver B62qpjieFM2nJdeTpnkvcN5FUuzwNxsMkWAGsW9eYdTXdGvfMrkHC9d -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 320
sleep 1s 
mina client send-payment -amount 1.002587712 -receiver B62qkSAN6FX99nguNJNQW3fdXh5yEv5PtMZwW6KWyUZrSRdTyHpdC6r -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 321
sleep 1s 
mina client send-payment -amount 0.605632777 -receiver B62qqur5M47Z6t7FJL476L2DHJQEARmNYRbDoX1Sm3zzD7VF6CDfbLp -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 322
sleep 1s 
mina client send-payment -amount 0.498055810 -receiver B62qiab7PzuV56zkmiBoyN7rX3rxtPebDd65aTzPnwYUfyf2aWFKUy8 -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 323
sleep 1s 
mina client send-payment -amount 0.180174786 -receiver B62qiwkRmsD8T2zbkSjvadmbJ5EpuaGebvD3pMDQ5gqsRj5bgTjdmCM -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 324
sleep 1s 
mina client send-payment -amount 0.120746583 -receiver B62qmB9LAADE42yVjXqqGSSMJeZGANC7PWcL7VthYwBr7DJnrePP8fW -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 325
sleep 1s 
mina client send-payment -amount 0.062106167 -receiver B62qiUCGYVUykUk5e2uK2hvrDx4CQ6Z1DQRxE4DFNXArE7KYD1ngq8f -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 326
sleep 1s 
mina client send-payment -amount 0.028617429 -receiver B62qjt5GzHKrNZNx5gNBn9ebrAhHRQ62BmwvS5BvcLRUb2R1zqch28s -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 327
sleep 1s 
mina client send-payment -amount 0.022280994 -receiver B62qivJW8U6V6VCj2xAqT8JqW4VoNucQqhcFLStnKsFyjiuA9UJ3Acp -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 328
sleep 1s 
mina client send-payment -amount 0.007803059 -receiver B62qmJeVUiEkcr9CcfGmuEzqELAmeoSRpN9KZrbrzXdb9WCGZGjY7Dz -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 329
sleep 1s 
mina client send-payment -amount 0.004909787 -receiver B62qieZHH1wHfv4PkSBhyttENUSV34ywjBP1LoedSiaz6sePMqy6ik3 -fee 0.001 -sender $SUPERCHARGED_POOL -memo Supercharged_pool -nonce 330
sleep 1s 

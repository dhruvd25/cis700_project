# Face Aging using an Encoder - Conditional DCGAN Network

Since 2014, GANs (Generative Adversarial Networks) have gained great popularity in generating data. Conditional GANs work as an extension to the GAN framework as many times we want to generate data based on a particular condition/label. In this case, that condition is **age**. Our end goal is to be able to take a person's face image and then be able to generate how they would look at a different age. 

## High Level Idea 
Our idea consisted of two main steps:
* Training a cGAN to be able to generate images of people at different ages
* Training an Encoder to learn a mapping between generator outputs and noise vectors to be able to generate images of a paritcular person at different ages.

We will explain these steps in more detail.

## Step 1: cGAN

Sadly, as people age, they start to look different i.e same people at different ages have different features. 

## Step 2: Encoder
Clearly, there exists a mapping between the noise vectors and what the Generator outputs. However, the GAN does not learn this inverse mapping. In order for us to produce images of a person of a different age, we have to be able to generate the respective noise vector for that person. Once we have this vector, we can concatentate the age we want to see this person at and run it to through the generator. 

## Results

## Improvements
* Based on the results of the cGAN, we can see that there seems to be very little difference between most people of ages between 20-30 and 40-50. Adding more age groups as well older age groups should help the Generator learn more discerning features between them.
* We can see that we lose information in mapping the generator outputs to their respective noise vectors. Optimization techniques can be used reduce this loss.



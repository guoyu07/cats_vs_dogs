# Hello World!
This repository contains the code for a computer-vision program. Using a convolutional
neural-network (made with [TensorFlow](https://www.tensorflow.org/)), this program can tell
whether a cat or dog is in a given picture.

The data used to train the model was [Kaggle's dataset.](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/data)
# Want to use and modify this program?
### If you have no idea what you're doing here...
If you want to use and modify this program to your fullest potential, you'll need to have *a lot*
of background knowledge about artificial neural-networks and machine-learning in general. There's
no way around these requirements, unfortunately. You have to put in the time, read lots of books
and blog-posts, take online-courses, etc. Going beyond this point, I'll assume you have that
knowledge, since I do not have anywhere near the time to explain everything. I will list a few
resources, however:

* http://neuralnetworksanddeeplearning.com/
    * Awesome online book. Many people will list this as a resource if you ask around, and I can
      tell you it's a damn fine one. I learned so much from this book.
* http://cs231n.github.io/
    * Lecture-notes and other resources from a course at Stanford University. Helped me out a ton!
* https://www.coursera.org/learn/machine-learning
    * Another well-respected resource like the first one I listed. Haven't gone through it myself
      but people who have say it's good.
* http://www.deeplearningbook.org/
    * A bit of a newbie on the field, but has some top-notch authors behind it. They're well-known
      in the field of AI and well-respected too.
* https://www.youtube.com/watch?v=aircAruvnKk
    * This video was created by 3Blue1Brown as part of a series, which is actually being created as
      I speak (October 15th, 2017). 3Blue1Brown is fucking amazing, that's all I have to say. He
      teaches things in an intuitive manner with lots of nice visualizations. Whatever comes out of
      this series, I'm sure it'll be good. He also has series' on linear algebra and calculus too.

Even having a solid background in machine-learning, you still need to (obviously) know how to
program in Python and how to use the TensorFlow framework. There are so many tutorials for both of
these that I won't even bother to list any, as a google-search will yield everything you seek.
### If you do have an idea of what you're doing...
*...follow these steps:*
1. Go to the aforementioned dataset and download the data to your directory of choice.
2. Set up your directory in the following way:
    * model.py (the file in `src`)
    * layers (my custom TensorFlow-wrapper, also in `src`)
    * data
        * train
            * cats (will contain the images of cats from Kaggle)
            * dogs (will contain the images of dogs from Kaggle)
        * test (will contain test-images from Kaggle)
3. Now you need to learn how to use `model.py`, which acts as the interface by which you'll train
and test the model. There are three main commands you'll need to know.
    * `python model.py -tr -s 25000`
        * The `-tr` tells the program to train the model, and the `-s` tells the program how many
          "steps" it should take. By steps, I mean parameter-updates, which are performed
          image-after-image. In more technical terms, I'm doing stochastic gradient-descent with
          `batch_size=1`. Why did I not implement minibatch gradient-descent? Lack of computing
          resources. I don't personally have a lot of RAM on my machine, so I didn't bother.
        * In this example, I train on all 25000 images from Kaggle's training-set. You can tell
          because of the `-s 25000`. But what if I used something like `-s 26000`? The Kaggle
          dataset only contains 25000 images total! Simple, my preprocessing-function that I wrote
          in `layers/preprocessing` will simply start over at the beginning of the directory. It's
          seamless, so don't worry about it.
        * After the training is complete, the program generate (or overwrite if exists) two
          directories:
            * saved_model (self-explanatory)
            * tensorboard
                * See https://www.tensorflow.org/get_started/summaries_and_tensorboard for details.
    * `python model.py -tr -r -s 25000`
        * Almost identical to the first command. Only thing different is the `-r` flag.
        * `-r` tells the program that it's *resuming* training.
        * With this flag, the training will start where it left off from your `saved_model`
          directory. It will overwrite `saved_model` and `tensorboard`.
    * `python model.py -te -i data/test/1.jpg`
        * The `-te` tells the program to test the model on an image, whose path is given by
          `-i data/test/1.jpg`.
4. That's all there is to it! I highly encourage you to tinker around with my code and change it as
it suits your purposes—it currently suits mine very well, but for you, it may not!

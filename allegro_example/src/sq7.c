#define ALLEGRO_STATICLINK
#include "sq7.h"

/*
So this is an example I put together quickly in ANSI C, using the allegro 5
library. The allegro 5 libary is an open source library with easy windowing,
graphics, and input handling. I personally like it, although there are many
other libraries like it. It is available for C++ and C, and I'm sure someone
has made a native wrapper for Java, but I'm not sure why we would want that
since we could just use Swing or LWJGL if we were programming in Java.

This example is in ANSI C so it is not object oriented, but as this is very
barebones, there is no real example where things could have been object
oriented. If we were to use this example as a starting place, a good place to
really flex our OOP skills would be the Model and View in the MVC architecture
pattern, especially in the implementation of the questions. As C++ is a superset
of C, this code is fully compatible with C++.

Throughout this file I use certain terms you should be aware of.

pthread is a standard library for multithreading. While there are others, this
one is POSIX compliant. It is available by default on every UNIX based system I
have seen, and there are many different ports to Windows available.

critical region refers to a region of memory (think variables) which is shared
by multiple threads. This is important to think about because what would happens
if there are multiple threads accessing the memory at the same time. Imagine a
variable with a value of 5. One thread wants to increment it by one, another
wants to decrement it by one. Logically, this is pretty simple, but if both
threads run at the same time the result might actually end up being 4 or 6
instead of the expected 5. This is known as a race condition.

mutex, short for mutual exclusion, is a simple way to prevent a race condition.
The core idea is that only one thread is allowed to acccess the critical region
at a given time, and others must wait until the first thread is done.

*/

//allegro globals
ALLEGRO_DISPLAY* display;

//critical regions and their locks
pthread_mutex_t ioMutex;
int shouldQuit; //should be true if window is closed or other conditions

/*
Allegro uses an event system to make it easier to handle IO. After registering
at least one event source, we can call al_wait_for_event() to block the current
execution thread until an event occurs on a registered source. The type
ALLEGRO_EVENT is a union capable of holding any possible allegro event.

Be careful when setting input flags. As they are a critical region shared
between multiple threads, you must lock a mutex first to avoid a race condition.
Remember to unlock the mutex when you are done.

Do not be alarmed if you haven't covered multithreading in detail yet. I will be
happy to explain anything necessary, and I think you will find it not too
difficult to understand.

In MVC architecture pattern, this would be the controller.
*/
void* eventLoop(void* param) {
  //create a queue to hold incoming events
  ALLEGRO_EVENT_QUEUE* queue = al_create_event_queue();
  ALLEGRO_EVENT e;

  //register potential sources of events
  al_register_event_source(queue, al_get_display_event_source(display));
  al_register_event_source(queue, al_get_keyboard_event_source());

  while(!shouldQuit) {
    //block if no event, or store event in e
    al_wait_for_event(queue, &e);

    //handle the event
    if (e.type == ALLEGRO_EVENT_DISPLAY_CLOSE) {
      //pthread_mutex_lock() locks a mutex, or waits until it is unlocked, and
      //then locks it.
      pthread_mutex_lock(&ioMutex);

      shouldQuit = 1;

      //Unlock the mutex when we are done with the critical region.
      pthread_mutex_unlock(&ioMutex);
    }
  }

  return NULL;
}

/*
A loop that executes  while the game it is running. It is responsible for
overseeing the Model and View (in the MVC architecture pattern), but not the
controller.

It is of course possible to fully seperate Model, View, And controller into
different threads, but it is much easier to put Model and View together.
*/
void* mainLoop(void* param) {
  
  while (!shouldQuit) {
    //TODO add main loop code here
  }

  return NULL;
}

int main(int argc, char** argv) {
  //intiallize allegro and its modules
  al_init(); //initialize allegro base
  al_install_keyboard(); //tell allegro that we want to use the keybaord
  al_install_audio(); //tell allegro that we want to use audio
  al_init_acodec_addon(); //initialize the codec addon so we can load audio
  al_reserve_samples(1); //reserve an audio sample for playback
  al_init_image_addon(); //initialize the image addon for drawing & loading

  //create display
  display = al_create_display(800, 600); //800 * 600
  al_set_window_title(display, "SQ7's TOP SECRET PROTOTYPE");

  //declare threads and attr objects
  pthread_t eventThread;
  pthread_attr_t eventThreadAttr;

  //init attr and mutex objects
  pthread_attr_init(&eventThreadAttr);
  pthread_mutex_init(&ioMutex, NULL);

  //start threads
  pthread_create(&eventThread, &eventThreadAttr, eventLoop, NULL);

  //load questions from db file
  //TODO

  //run main loop in this thread
  mainLoop(NULL);

  //save changes to db file

  //join threads
  pthread_join(eventThread, NULL);

  //clean up allegro and its addons
  al_destroy_display(display);
  al_uninstall_keyboard();
  al_uninstall_audio();

  //clean up other resources
  pthread_attr_destroy(&eventThreadAttr);
  pthread_mutex_destroy(&ioMutex);

  return 0;
}


#ifndef sq7_h
#define sq7_h

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <pthread.h>

#include <allegro5/allegro.h>
#include <allegro5/allegro_image.h>
#include <allegro5/allegro_audio.h>
#include <allegro5/allegro_acodec.h>

#define SMOOTHSTEP(x) ((x) * (x) * (3 - 2 * (x)))

/*
eventLoop should be a loop that polls for input events. Upon receiving events
it should access a critical region and set flags.
*/
void* eventLoop(void*);

/*
mainLoop updates every tick as needed and also renders output to the window.
Remember to lock the mutex when accessing the critical region! Also, do not
forget to unlock it when you are done.
*/
void* mainLoop(void*);

#endif


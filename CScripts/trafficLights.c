#include <bcm2835.h>
#include <stdio.h>

#define RED RPI_GPIO_P1_15
//Standard mapping was not correct for the pi board I have. Using V2 mapping for yellow light instead. 
#define YELLOW RPI_V2_GPIO_P1_13
#define GREEN RPI_GPIO_P1_11 

int main(int argc, char **argv) {

        //This initilises the bcm library. If it ballses itself, the program ends.
        if (!bcm2835_init()) return 1; 

        //Set the pins as outputs (sends a signal to a peripheral=.
        bcm2835_gpio_fsel(RED, BCM2835_GPIO_FSEL_OUTP);
        bcm2835_gpio_fsel(YELLOW, BCM2835_GPIO_FSEL_OUTP);
        bcm2835_gpio_fsel(GREEN, BCM2835_GPIO_FSEL_OUTP);

        //Time between flashes in milliseconds.
        unsigned int delay = 1000;

        //On, off, on, off, on, off, on, off, on, off, on, off
        while(1) {
		bcm2835_gpio_set(RED);
                bcm2835_delay(delay);
                bcm2835_gpio_clr(RED);
                bcm2835_delay(delay);#
                bcm2835_gpio_set(YELLOW);
                bcm2835_delay(delay);
                bcm2835_gpio_clr(YELLOW);
                bcm2835_delay(delay);
                bcm2835_gpio_set(GREEN);
                bcm2835_delay(delay);
                bcm2835_gpio_clr(GREEN);
                bcm2835_delay(delay);
        }
}
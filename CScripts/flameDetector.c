#include <bcm2835.h>
#include <stdio.h>

#define PIN RPI_GPIO_P1_07

int main(void) {
	if (!bcm2835_init))
		return 1;
	
	//Set RPI pin 7 to be an input
	bcm2835_gpio_fsel(PIN, BCM2835_GPIO_FSEL_INPT);

	//Set with a pull up. No flame is 1, flame is 0. Ambiguous readings should default to no flame.
	bcm2835_gpio_set_pud(PIN, BCM2835_GPIO_PUD_UP)

	printf("Show me that flame!\n");

	while(1) 
	{
		//Poll for a reading from the pin.
		uint8_t value = bcm2835_gpio_lev(PIN);
		if (value == 0)
			printf("FIRE!\n");

		//chwila
		delay(500);	
	}
	bcm2835_close();
	return 0;
}
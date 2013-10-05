
#include <stdio.h>
#include "nrlmsise-00.h"

int
main()
{
     struct nrlmsise_output output;
     struct nrlmsise_input input;
     struct nrlmsise_flags flags;
//     struct ap_array aph;
     int i;

     //   for (i=0;i<7;i++)
     //  aph.a[i]=100;
     flags.switches[0]=0;
     for (i=1;i<24;i++)
	  flags.switches[i]=1;
     
     int doy = 200;
     int sec = 12*3600 + 0 * 60 + 0;
     double g_lat = 52.44;
     double g_long = -0.11;
     double alt;
     printf("Altitude, He, N2, O2, Ar, Total, T\n");
     for (alt=0.0;alt<150.000;alt+=0.005) {
	  input.doy = doy;
	  input.year = 0; // Not used
	  input.sec = sec;
	  input.alt = alt;
	  input.g_lat = g_lat;
	  input.g_long = g_long;
	  input.lst = sec + g_long/15.0;

	  input.f107A = 150; // These should be set to 150, 150, 4 according to the docs
	  input.f107 = 150;
	  input.ap = 4;

	  gtd7(&input, &flags, &output);

	  printf("%g, %g, %g, %g, %g, %g, %g\n", alt*1000.0, output.d[0], output.d[2], 
		output.d[3], output.d[4], output.d[5], output.t[1]);
     }


     return 0;
}

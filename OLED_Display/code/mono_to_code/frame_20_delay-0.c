
/*******************************************************************************
* image
* filename: unsaved
* name: frame_20_delay-0
*
* preset name: Monochrome
* data block size: 8 bit(s), uint8_t
* RLE compression enabled: no
* conversion type: Monochrome, Diffuse Dither 128
* bits per pixel: 1
*
* preprocess:
*  main scan direction: top_to_bottom
*  line scan direction: forward
*  inverse: no
*******************************************************************************/

/*
 typedef struct {
     const uint8_t *data;
     uint16_t width;
     uint16_t height;
     uint8_t dataSize;
     } tImage;
*/
#include <stdint.h>



static const uint8_t image_data_frame_20_delay0[512] = {
    0x00, 0x0f, 0xfc, 0x00, 0x00, 0x00, 0x00, 0x70, 
    0x00, 0x1f, 0xfc, 0x00, 0x00, 0x00, 0x00, 0x78, 
    0x00, 0x3f, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x7e, 
    0x00, 0x7f, 0xfc, 0x00, 0xd7, 0xc0, 0x00, 0x7f, 
    0x00, 0xff, 0xfc, 0x0f, 0xff, 0xfd, 0x00, 0xff, 
    0x00, 0xff, 0xfe, 0xff, 0xff, 0xff, 0xa0, 0xff, 
    0x01, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf9, 0xff, 
    0x01, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfd, 0xff, 
    0x03, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0x03, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0x03, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0x03, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0x07, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0x07, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0x0f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0x0f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0x0f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0x0f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0x1f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0x1f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0x1f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0x1f, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0x3e, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0x1e, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0x3c, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0x3e, 0x7f, 0xff, 0xf7, 0xff, 0xff, 0xff, 0xff, 
    0x3b, 0x7d, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0x3e, 0x5f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
    0x3b, 0x8f, 0xff, 0xff, 0xff, 0xfb, 0xff, 0xff, 
    0x3f, 0x2f, 0xff, 0x7f, 0xff, 0xff, 0xff, 0xff, 
    0x3e, 0x4f, 0xff, 0xfb, 0xff, 0xff, 0xff, 0x7c, 
    0x3c, 0x1f, 0xff, 0xff, 0xff, 0xf6, 0xff, 0xf9, 
    0x3d, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfa, 
    0x1c, 0x1f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfc, 
    0x3c, 0x1f, 0xbf, 0x7f, 0xbf, 0xff, 0xff, 0xfe, 
    0x3c, 0x1b, 0xef, 0x0f, 0xff, 0xdf, 0xff, 0xfe, 
    0x78, 0x1f, 0xb8, 0x43, 0xff, 0xff, 0x1f, 0xfe, 
    0x78, 0x1f, 0xf3, 0xbd, 0xfe, 0xe0, 0x1f, 0xee, 
    0xf9, 0x5f, 0xe7, 0xcf, 0xff, 0xdf, 0xc5, 0xfe, 
    0xf8, 0x1b, 0xcf, 0xc7, 0xff, 0xfe, 0x77, 0x56, 
    0xf9, 0x4f, 0xec, 0xe3, 0xff, 0xee, 0x3b, 0xfe, 
    0xf0, 0x5f, 0xfd, 0x53, 0xff, 0xee, 0x39, 0xfd, 
    0xf8, 0x8f, 0xff, 0xbf, 0xff, 0xee, 0x9d, 0xf6, 
    0xf1, 0x57, 0xff, 0xff, 0xff, 0xfa, 0xdb, 0xfd, 
    0xf8, 0x2b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf4, 
    0xf0, 0x8d, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfd, 
    0xf0, 0x2b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf8, 
    0xf4, 0x4e, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf1, 
    0xf0, 0x8b, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf4, 
    0xf2, 0x57, 0x7b, 0xff, 0xff, 0xff, 0xfb, 0xf5, 
    0xf4, 0xa3, 0xfd, 0xff, 0xd7, 0xff, 0xf7, 0xec, 
    0xb2, 0x17, 0xd8, 0xff, 0xd7, 0xff, 0xeb, 0xfa, 
    0xf4, 0xab, 0x88, 0x7f, 0xff, 0xff, 0xc3, 0xc9, 
    0xf5, 0x47, 0xc0, 0x0f, 0xff, 0xff, 0x83, 0xba, 
    0x50, 0x2b, 0xc0, 0x03, 0xff, 0xfc, 0x03, 0x18, 
    0xff, 0x03, 0xc0, 0x01, 0xb5, 0x00, 0x00, 0x3a, 
    0xff, 0xc1, 0xc0, 0x01, 0x87, 0x00, 0x00, 0x39, 
    0xff, 0x81, 0xc0, 0x03, 0xef, 0x00, 0x00, 0x32, 
    0xff, 0xc1, 0x80, 0x04, 0x7d, 0x00, 0x00, 0x74, 
    0xff, 0x81, 0x80, 0x08, 0x00, 0xc0, 0x00, 0x30, 
    0xff, 0xff, 0x80, 0x18, 0x48, 0xc0, 0x00, 0x10, 
    0xff, 0xff, 0xc0, 0x10, 0xfc, 0x60, 0x00, 0x00, 
    0xff, 0xff, 0xc0, 0x31, 0xee, 0x60, 0x00, 0x00, 
    0xff, 0xff, 0x80, 0x3f, 0xff, 0x60, 0x00, 0x00
};
const tImage frame_20_delay0 = { image_data_frame_20_delay0, 64, 64,
    8 };


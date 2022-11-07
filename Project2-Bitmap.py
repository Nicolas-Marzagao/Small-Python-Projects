import sys

bitmap = ' '

def bitmapSel:
    global bitmap
    print('''Select which bitmap you wish to display with your message:
    
    [ 1 ] World Map
    sorry couldnt find any more lol :p''')
    
    opt = int(input('> '))
    
    if opt == 1:
        bitmap = '''
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................''' 


def main:
    print('Bitmap Message, by Nicolas Marzagão')
    print('Enter the message to display with the bitmap.')
    message = input('> ')
    if message == '':
        sys.exit()

    # Loop over each line in the bitmap:
    for line in bitmap.splitlines():
        # Loop over each character in the line:
        for i, bit in enumerate(line):
            if bit == ' ':
                # Print an empty space since there's a space in the bitmap:
                print(' ', end='')
            else:
                # Print a character from the message:
                print(message[i % len(message)], end='')
        print()

if __name__ == "__main__"
    main()
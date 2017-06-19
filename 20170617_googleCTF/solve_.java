public class solve_ {

    private static byte[] flag = new byte[]{(byte) -19, (byte) 116, (byte) 58, (byte) 108, (byte) -1, (byte) 33, (byte) 9, (byte) 61, (byte) -61, (byte) -37, (byte) 108, (byte) -123, (byte) 3, (byte) 35, (byte) 97, (byte) -10, (byte) -15, (byte) 15, (byte) -85, (byte) -66, (byte) -31, (byte) -65, (byte) 17, (byte) 79, (byte) 31, (byte) 25, (byte) -39, (byte) 95, (byte) 93, (byte) 1, (byte) -110, (byte) -103, (byte) -118, (byte) -38, (byte) -57, (byte) -58, (byte) -51, (byte) -79};
    
    private static byte[] flag_xor = new byte[]{(byte) 0x13, (byte) 0x11, (byte) 0x13, (byte) 3, (byte) 4, (byte) 3, (byte) 1, (byte) 5};

    String[] strArr = new String[]{"\ud83c\udf55", "\ud83c\udf6c", "\ud83c\udf5e", "\ud83c\udf4e", "\ud83c\udf45", "\ud83c\udf59", "\ud83c\udf5d", "\ud83c\udf53", "\ud83c\udf48", "\ud83c\udf49", "\ud83c\udf30", "\ud83c\udf57", "\ud83c\udf64", "\ud83c\udf66", "\ud83c\udf47", "\ud83c\udf4c", "\ud83c\udf63", "\ud83c\udf44", "\ud83c\udf4a", "\ud83c\udf52", "\ud83c\udf60", "\ud83c\udf4d", "\ud83c\udf46", "\ud83c\udf5f", "\ud83c\udf54", "\ud83c\udf5c", "\ud83c\udf69", "\ud83c\udf5a", "\ud83c\udf68", "\ud83c\udf3e", "\ud83c\udf3d", "\ud83c\udf56"};

    public static byte[] m0(byte[] bArr, byte[] bArr2) {
        byte[] bArr3 = new byte[256];
        byte[] bArr4 = new byte[256];
        int i = 0;
        int i2 = 0;
        while (i2 != 256) {
            bArr3[i2] = (byte) i2;
            bArr4[i2] = bArr2[i2 % bArr2.length];
            i2++;
        }
        int i3 = i2 ^ i2;
        i2 = 0;
        while (i3 != 256) {
            i2 = ((i2 + bArr3[i3]) + bArr4[i3]) & 255;
            bArr3[i2] = (byte) (bArr3[i2] ^ bArr3[i3]);
            bArr3[i3] = (byte) (bArr3[i3] ^ bArr3[i2]);
            bArr3[i2] = (byte) (bArr3[i2] ^ bArr3[i3]);
            i3++;
        }
        bArr4 = new byte[bArr.length];
        i3 ^= i3;
        i2 ^= i2;
        while (i != bArr.length) {
            i3 = (i3 + 1) & 255;
            i2 = (i2 + bArr3[i3]) & 255;
            bArr3[i2] = (byte) (bArr3[i2] ^ bArr3[i3]);
            bArr3[i3] = (byte) (bArr3[i3] ^ bArr3[i2]);
            bArr3[i2] = (byte) (bArr3[i2] ^ bArr3[i3]);
            bArr4[i] = (byte) (bArr[i] ^ bArr3[(bArr3[i3] + bArr3[i2]) & 255]);
            i++;
        }
        System.out.println(new String(bArr4));
        return bArr4;
    }

    static public void main (String test[]){
        byte[] bArr = new byte[]{(byte) 26, (byte) 27, (byte) 30, (byte) 4, (byte) 21, (byte) 2, (byte) 18, (byte) 7};
        for (int i = 0; i < 8; i++) {
            bArr[i] = (byte) (bArr[i] ^ flag_xor[i]);
        }

        System.out.println(new String(m0(flag,bArr)));
        }
}

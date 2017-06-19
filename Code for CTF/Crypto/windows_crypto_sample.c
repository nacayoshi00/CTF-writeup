#include <windows.h>
#include <wincrypt.h>
#include <stdio.h>

#define PASSWORD_LENGTH 100
#define BLOCK_LEN 2000

int main() {
	HCRYPTPROV hProv;
	HCRYPTKEY hKey;
	HCRYPTHASH hHash;
//	7ZfKiuNbDcmXJvzRuVHRiD4pH6EEApCmb4ciUmzbH6TXEh7nmuQ3LghuGx38t2BT
	CHAR sPassword[PASSWORD_LENGTH] = "7ZfKiuNbDcmXJvzRuVHRiD4pH6EEApCmb4ciUmzbH6TXEh7nmuQ3LghuGx38t2BX";
	DWORD dwStatus = 0;
    BOOL bResult = FALSE;
    BOOL isDecrypt = TRUE;
    int key_len = lstrlen(sPassword);
    printf("key_len: %d\n", key_len);

	HANDLE hInpFile = CreateFile("notdroids.jpg", GENERIC_READ, 0, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
	HANDLE hOutFile = CreateFile("output.jpg", GENERIC_WRITE, 0,  NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);    

	CryptAcquireContext(&hProv, NULL, "Microsoft Enhanced Cryptographic Provider v1.0", 1, 0);
	CryptCreateHash(hProv, 0x8003, 0, 0, &hHash);
	CryptHashData(hHash, sPassword, key_len, 0);
	CryptDeriveKey(hProv, 0x6801, hHash, 0x800000, &hKey);

	const size_t chunk_size = BLOCK_LEN;
	BYTE chunk[chunk_size];
    DWORD read = 0;
    DWORD written = 0;
    printf("Start!\n");
    while (bResult = ReadFile(hInpFile, chunk, chunk_size, &read, NULL)) {
        if (0 == read){
            printf("no read!\n");
            break;
        }
        DWORD ciphertextLen = BLOCK_LEN;

        if (isDecrypt) {
            printf("decrypt read: %d\n", read);
            if (!CryptDecrypt(hKey, 0, FALSE, 0,chunk, &ciphertextLen)) {
                printf("Decrypt failed!\n");
                break;
            }
        } else {
            printf("encrypt read: %d\n", read);
            if (!CryptEncrypt(hKey, 0, FALSE, 0,chunk, &ciphertextLen, read)) {
                printf("failed!\n");
                break;
            }
        }
        if (!WriteFile(hOutFile, chunk, ciphertextLen, &written, NULL)) {
            printf("writing failed!\n");
            break;
        }
        memset(chunk, 0, chunk_size);
    }
	printf("end!:%d\n", bResult);
//	MessageBox(NULL, sBuffer, "FLAG", MB_OK);
    CryptDestroyKey(hKey);
    CryptDestroyHash(hHash);
    CloseHandle(hInpFile);
    CloseHandle(hOutFile);

	return 0;
}



from wallet_pass.apple.main import ApplePass
from wallet_pass.apple.schemas import AppleBarcode, AppleGenericTemplate, AppleField, ApplePassSchema, FileSchema


def read_file(path: str) -> bytes:
    with open(path, 'rb') as f:
        return f.read()


if __name__ == '__main__':
    pass_schema = ApplePassSchema(
        teamIdentifier='teamIdentifier',
        passTypeIdentifier='passTypeIdentifier',
        serialNumber='serialNumber',
        organizationName='organizationName',
        description='description',
        logoText='logoText',
        # webServiceURL='https://yourpasshost.example.com/',
        # authenticationToken='authenticationToken',
        backgroundColor='rgb(240, 66, 5)',
        foregroundColor='rgb(0, 0, 0)',
        labelColor='rgb(0, 0, 0)',
        barcodes=[AppleBarcode(message='TestQRData')],
        generic=AppleGenericTemplate(
            headerFields=[AppleField(
                key='hf1',
                value='HeaderField1',
                label='HF1'
            )],
            primaryFields=[AppleField(
                key='pf1',
                value='PrimaryField1',
                label='PF1'
            )],
            secondaryFields=[AppleField(
                key='sf1',
                value='SecondaryField1',
                label='SF1'
            ), AppleField(
                key='sf2',
                value='SecondaryField2',
                label='SF2'
            )],
            auxiliaryFields=[AppleField(
                key='af1',
                value='AuxiliaryField1',
                label='AF1'
            ), AppleField(
                key='af2',
                value='AuxiliaryField2',
                label='AF2'
            )],
            backFields=[AppleField(
                key='bf1',
                value='BackField1',
                label='BF1'
            )],
        )
    )

    files = [
        FileSchema(file=read_file('./icon.png'), filename='icon.png'),
        FileSchema(file=read_file('./icon@2x.png'), filename='icon@2x.png'),
        FileSchema(file=read_file('./logo.png'), filename='logo.png'),
        FileSchema(file=read_file('./logo@2x.png'), filename='logo@2x.png'),
        FileSchema(file=read_file('./thumbnail.png'), filename='thumbnail.png'),
        FileSchema(file=read_file('./thumbnail@2x.png'), filename='thumbnail@2x.png'),
    ]

    apple_pass = ApplePass(
        read_file('path/to/cert.pem'),
        read_file('path/to/key.pem'),
        'some_key_password',
        read_file('path/to/wwdr.pem'),
        pass_schema,
        files
    )
    pkpass = apple_pass.get_pkpass_file()
    with open('./pass.pkpass', 'wb') as f:
        f.write(pkpass)

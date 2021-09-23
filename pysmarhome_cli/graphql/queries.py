devs_query = '''
{
    devices {
        id
        name
        state {
            power
            ...on RgbLampState {
                color
                brightness
            }
            ...on TvState {
                mute
                volume
            }
            ...on AcState {
                temp
            }
        }
    }
}
'''

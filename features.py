STRIP_BINARY = {
    'autocorr': False,
    'gaussian': True,
}

FEATURES = {
    'autocorr':
        (
            'id',
            'resultid',
            'peak_power',
            'mean_power',
            'time',
            'ra',
            'dec',
            'q_pix',
            'delay',
            'freq',
            'detection_freq',
            'barycentric_freq',
            'fft_len',
            'chirp_rate',
            'rfi_checked',
            'rfi_found',
            'reserved'
        ),
    'gaussian':
        (
            'id',
            'resultid',
            'peak_power',
            'mean_power',
            'time',
            'ra',
            'dec',
            'q_pix',
            'freq',
            'detection_freq',
            'barycentric_freq',
            'fft_len',
            'chirp_rate',
            'rfi_checked',
            'rfi_found',
            'reserved'
            'sigma',
            'chisqr',
            'null_chisqr',
            'score',
            'max_power',
        )
}

GOOD_FEATURES = {
    'autocorr':
        (
            'peak_power',
            #'time',
            #'ra',
            #'dec',
            'delay',
            'freq',
            'detection_freq',
            'barycentric_freq',
            'chirp_rate',
        )
}

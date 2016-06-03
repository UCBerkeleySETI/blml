
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
        )
}

GOOD_FEATURES = {
    'autocorr':
        (
            'peak_power',
            'mean_power',
            'time',
            'ra',
            'dec',
            'delay',
            'freq',
            'detection_freq',
            'barycentric_freq',
            'fft_len',
            'chirp_rate',
        )
}

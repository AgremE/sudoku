class Hyperparams:
    '''Hyper parameters'''
    # data
    train_fpath = '../data/sudoku.csv'
    val_fpath = '../data/validation.csv'
    sound_fpath = 'WEB/'
    max_len = 150 # maximum length of text
    max_duration = 5.0 # maximum duration of a sound file. seconds.
    
    # signal processing
    sr = 22050 # Sampling rate
    n_fft = 2048 # fft points (samples)
    frame_shift = 0.0125 # seconds
    frame_length = 0.05 # seconds
    hop_length = int(sr*frame_shift) # samples 
    win_length = int(sr*frame_length) # samples
    n_mels = 80 # Number of Mel banks to generate
    power = 1.2 # Exponent for the magnitude melspectrogram
    n_iter = 30 # Number of inversion iterations 
    
    # model
    embed_size = 256
    num_blocks = 10
    num_filters = 512
    filter_size = 3
    decoder_num_banks = 8
    num_highwaynet_blocks = 4
    r = 5 # Reduction factor
    
    # training scheme
    lr = 0.001
    logdir = "log"
    save_path = 'log/model.ckpt'
    batch_size = 32
    num_epochs = 10

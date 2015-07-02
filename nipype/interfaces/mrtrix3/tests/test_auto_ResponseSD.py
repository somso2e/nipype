# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.mrtrix3.preprocess import ResponseSD

def test_ResponseSD_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    bval_scale=dict(argstr='-bvalue_scaling %s',
    ),
    disp_mult=dict(argstr='-dispersion_multiplier %f',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    grad_file=dict(argstr='-grad %s',
    ),
    grad_fsl=dict(argstr='-fslgrad %s %s',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    in_mask=dict(argstr='-mask %s',
    ),
    int_mult=dict(argstr='-integral_multiplier %f',
    ),
    iterations=dict(argstr='-max_iters %d',
    ),
    max_change=dict(argstr='-max_change %f',
    ),
    max_sh=dict(argstr='-lmax %d',
    ),
    out_file=dict(argstr='%s',
    mandatory=True,
    position=-1,
    usedefault=True,
    ),
    out_sf=dict(argstr='-sf %s',
    ),
    shell=dict(argstr='-shell %s',
    sep=',',
    ),
    terminal_output=dict(nohash=True,
    ),
    test_all=dict(argstr='-test_all',
    ),
    vol_ratio=dict(argstr='-volume_ratio %f',
    ),
    )
    inputs = ResponseSD.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_ResponseSD_outputs():
    output_map = dict(out_file=dict(),
    out_sf=dict(),
    )
    outputs = ResponseSD.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value


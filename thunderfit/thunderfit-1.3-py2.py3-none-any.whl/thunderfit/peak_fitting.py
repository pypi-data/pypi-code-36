from lmfit import models

def fit_peaks(x_data, y_data, peak_types, peak_centres, peak_amps, peak_widths, bounds):
    model_specs = build_specs(peak_types, peak_centres, peak_amps, peak_widths, bounds)
    model, peak_params = generate_model(model_specs)
    peaks = model.fit(y_data, peak_params, x=x_data)
    if not peaks.success:
        print('peaks failed to fit')
    peak_params = peaks.best_values

    return model_specs, model, peak_params, peaks

def make_bounds(tightness, no_peaks, bounds_dict, peak_widths, peak_centres, peak_amps):
    bounds = {}

    if not bounds_dict['centers'] or len(bounds_dict['centers']) != no_peaks:
        l_cent_bounds = [cent - tightness['centre_bounds'] * peak_widths[i] for i, cent in enumerate(peak_centres)]
        u_cent_bounds = [cent + tightness['centre_bounds'] * peak_widths[i] for i, cent in enumerate(peak_centres)]
        cent_bounds = list(zip(l_cent_bounds, u_cent_bounds))
        bounds['centers'] = cent_bounds

    if not bounds_dict['widths'] or len(bounds_dict['widths']) != no_peaks:
        l_width_bounds = [width / tightness['width_bounds'][0] for width in peak_widths]
        u_width_bounds = [width * tightness['width_bounds'][1] for width in peak_widths]
        width_bounds = list(zip(l_width_bounds, u_width_bounds))
        bounds['widths'] = width_bounds

    if not bounds_dict['amps'] or len(bounds_dict['amps']) != no_peaks:
        l_amp_bounds = [amp / tightness['amps_bounds'][0] for amp in peak_amps]
        u_amp_bounds = [amp * tightness['amps_bounds'][1] for amp in peak_amps]
        amp_bounds = list(zip(l_amp_bounds, u_amp_bounds))
        bounds['amps'] = amp_bounds

    return bounds

def build_specs(peak_types, peak_centres, peak_amps, peak_widths, bounds):
    specs = [
        {
            'type': peak_types[i],
            'params': {'center': peak_centres[i], 'amp': peak_amps[i] ,'sigma': peak_widths[i],
                       'gamma' :peak_widths[i]
                       },
            'bounds': {'centers': bounds['centers'][i], 'amps': bounds['amps'][i],
                       'widths': bounds['widths'][i]
                       }
        }
        for i, _ in enumerate(peak_centres)
    ]

    return specs

def generate_model(model_specs):
    """
    https://chrisostrouchov.com/post/peak_fit_xrd_python/
    :param model_specs:
    :return:
    """
    composite_model = None
    params = None
    for i, basis_func in enumerate(model_specs):
        prefix = f'm{i}_'
        model = getattr(models, basis_func['type'])(prefix=prefix)
        if basis_func['type'] in ['GaussianModel', 'LorentzianModel' ,'VoigtModel']:
            # for now VoigtModel has gamma constrained to sigma
            w_min = basis_func['bounds']['widths'][0]
            w_max = basis_func['bounds']['widths'][1]
            x_min = basis_func['bounds']['centers'][0]
            x_max = basis_func['bounds']['centers'][1]
            y_min = basis_func['bounds']['amps'][0]
            y_max = basis_func['bounds']['amps'][1]

            model.set_param_hint('sigma', min=w_min, max=w_max)
            model.set_param_hint('center', min=x_min, max=x_max)
            model.set_param_hint('height', min=y_min, max=y_max)
            model.set_param_hint('amplitude', min=1e-6)

            # default guess is horrible!! do not use guess()
            default_params = {
                prefix + 'center': basis_func['params']['center'],
                prefix + 'height': basis_func['params']['amp'],
                prefix + 'sigma': basis_func['params']['sigma']
            }
        else:
            raise NotImplemented(f'model {basis_func["type"]} not implemented yet')

        model_params = model.make_params(**default_params, **basis_func.get('params', {}))

        if params is None: # first loop
            params = model_params
            composite_model = model
        else: # subsequent loops
            params.update(model_params)
            composite_model = composite_model + model

    return composite_model, params
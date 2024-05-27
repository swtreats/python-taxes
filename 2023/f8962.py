from form import Form, FilingStatus
from typing import Optional


class F8962(Form):
    """Form 8962, Premium Tax Credit"""
    POVERTY_LINE_ALASKA = [
        16990, 22890, 28790, 34690, 40590, 46490, 52390, 58290]
    POVERTY_LINE_ALASKA_EXTRA = 5900
    POVERTY_LINE_HAWAII = [
        15630, 21060, 26490, 31920, 37350, 42780, 48210, 53640]
    POVERTY_LINE_HAWAII_EXTRA = 5430
    POVERTY_LINE_OTHER48 = [
        13590, 18310, 23030, 27750, 32470, 37190, 41910, 46630]
    POVERTY_LINE_OTHER48_EXTRA = 4270

    # from 150 to 400
    APPLICABLE_FIGURE: list[float] = [
        0,
        0.0004,
        0.0008,
        0.0012,
        0.0016,
        0.002,
        0.0024,
        0.0028,
        0.0032,
        0.0036,
        0.004,
        0.0044,
        0.0048,
        0.0052,
        0.0056,
        0.006,
        0.0064,
        0.0068,
        0.0072,
        0.0076,
        0.008,
        0.0084,
        0.0088,
        0.0092,
        0.0096,
        0.01,
        0.0104,
        0.0108,
        0.0112,
        0.0116,
        0.012,
        0.0124,
        0.0128,
        0.0132,
        0.0136,
        0.014,
        0.0144,
        0.0148,
        0.0152,
        0.0156,
        0.016,
        0.0164,
        0.0168,
        0.0172,
        0.0176,
        0.018,
        0.0184,
        0.0188,
        0.0192,
        0.0196,
        0.02,
        0.0204,
        0.0208,
        0.0212,
        0.0216,
        0.022,
        0.0224,
        0.0228,
        0.0232,
        0.0236,
        0.024,
        0.0244,
        0.0248,
        0.0252,
        0.0256,
        0.026,
        0.0264,
        0.0268,
        0.0272,
        0.0276,
        0.028,
        0.0284,
        0.0288,
        0.0292,
        0.0296,
        0.03,
        0.0304,
        0.0308,
        0.0312,
        0.0316,
        0.032,
        0.0324,
        0.0328,
        0.0332,
        0.0336,
        0.034,
        0.0344,
        0.0348,
        0.0352,
        0.0356,
        0.036,
        0.0364,
        0.0368,
        0.0372,
        0.0376,
        0.038,
        0.0384,
        0.0388,
        0.0392,
        0.0396,
        0.04,
        0.0404,
        0.0408,
        0.0412,
        0.0416,
        0.042,
        0.0424,
        0.0428,
        0.0432,
        0.0436,
        0.044,
        0.0444,
        0.0448,
        0.0452,
        0.0456,
        0.046,
        0.0464,
        0.0468,
        0.0472,
        0.0476,
        0.048,
        0.0484,
        0.0488,
        0.0492,
        0.0496,
        0.05,
        0.0504,
        0.0508,
        0.0512,
        0.0516,
        0.052,
        0.0524,
        0.0528,
        0.0532,
        0.0536,
        0.054,
        0.0544,
        0.0548,
        0.0552,
        0.0556,
        0.056,
        0.0564,
        0.0568,
        0.0572,
        0.0576,
        0.058,
        0.0584,
        0.0588,
        0.0592,
        0.0596,
        0.06,
        0.0603,
        0.0605,
        0.0608,
        0.061,
        0.0613,
        0.0615,
        0.0618,
        0.062,
        0.0623,
        0.0625,
        0.0628,
        0.063,
        0.0633,
        0.0635,
        0.0638,
        0.064,
        0.0643,
        0.0645,
        0.0648,
        0.065,
        0.0653,
        0.0655,
        0.0658,
        0.066,
        0.0663,
        0.0665,
        0.0668,
        0.067,
        0.0673,
        0.0675,
        0.0678,
        0.068,
        0.0683,
        0.0685,
        0.0688,
        0.069,
        0.0693,
        0.0695,
        0.0698,
        0.07,
        0.0703,
        0.0705,
        0.0708,
        0.071,
        0.0713,
        0.0715,
        0.0718,
        0.072,
        0.0723,
        0.0725,
        0.0728,
        0.073,
        0.0733,
        0.0735,
        0.0738,
        0.074,
        0.0743,
        0.0745,
        0.0748,
        0.075,
        0.0753,
        0.0755,
        0.0758,
        0.076,
        0.0763,
        0.0765,
        0.0768,
        0.077,
        0.0773,
        0.0775,
        0.0778,
        0.078,
        0.0783,
        0.0785,
        0.0788,
        0.079,
        0.0793,
        0.0795,
        0.0798,
        0.08,
        0.0803,
        0.0805,
        0.0808,
        0.081,
        0.0813,
        0.0815,
        0.0818,
        0.082,
        0.0823,
        0.0825,
        0.0828,
        0.083,
        0.0833,
        0.0835,
        0.0838,
        0.084,
        0.0843,
        0.0845,
        0.0848,
        0.085]
    # if pct of poverty < first, then use second.
    # if greater than all, no limitation.
    LIMITATION_TABLE = [
        # (pct < x, limitation_amount)
        (200, 350),
        (300, 900),
        (400, 1500)]

    def compute_poverty_line(self, table: list[int], extra: int,
                             size: int):
        table_len = len(table)
        if size > table_len:
            return table[-1] + extra * (size - table_len)
        return table[size-1]

    def compute_poverty_line_for_state(self, state: str, size: int):
        if state == 'AK':
            table = self.POVERTY_LINE_ALASKA
            extra = self.POVERTY_LINE_ALASKA_EXTRA
        elif state == 'HI':
            table = self.POVERTY_LINE_HAWAII
            extra = self.POVERTY_LINE_HAWAII_EXTRA
        else:
            table = self.POVERTY_LINE_OTHER48
            extra = self.POVERTY_LINE_OTHER48_EXTRA
        return self.compute_poverty_line(table, extra, size)

    def compute_applicable_figure(self, pct_of_poverty: int):
        pct_in_range = min(400,
                           max(150, pct_of_poverty))
        idx = pct_in_range - 150
        figure = self.APPLICABLE_FIGURE[idx-1]
        if pct_of_poverty > 150:
            assert (figure != 0)
        return figure

    def compute_repayment_limitation(
            self, pct_of_poverty: int,
            is_single_filer: bool) -> Optional[int]:
        multiplier = 1
        if not is_single_filer:
            multiplier = 2
        for (pct, amount) in self.LIMITATION_TABLE:
            if pct_of_poverty < pct:
                return amount * multiplier
        return None

    def __init__(f, inputs: dict, f1040: Form):
        super(F8962, f).__init__(inputs)
        if 'aca_premium' not in inputs:
            f.must_file = False
            return
        tax_family_size = 1
        if inputs['status'] == FilingStatus.JOINT:
            tax_family_size = 2
        if 'qualifying_children' in inputs:
            tax_family_size += inputs['qualifying_children']
        f['1'] = tax_family_size
        # modified AGI is AGI +
        #  foreign earned income, tax-exempt interest,
        #  and the portion of social security benefits that is not taxable
        modified_agi = f1040.get('11')
        # TODO fix this if/when f2555 is needed and available.
        foreign_earned_income = 0
        tax_exempt_interest = inputs['tax_exempt_interest']
        nontax_ss_income = inputs['ssec_income'] \
            - inputs['ssec_income_taxable']
        modified_agi = modified_agi + foreign_earned_income \
            + tax_exempt_interest + nontax_ss_income
        # TODO: fix this
        dependants_modified_agi = 0
        f['2a'] = modified_agi
        f['2b'] = dependants_modified_agi
        f['3'] = f.rowsum(['2a', '2b'])
        ptc_state = 'OTHER'
        if 'ptc_state' in inputs:
            ptc_state = inputs['ptc_state']
        poverty_line = f.compute_poverty_line_for_state(
            ptc_state, tax_family_size)
        if ptc_state == 'AK':
            f['4a'] = True
        elif ptc_state == 'HI':
            f['4b'] = True
        else:
            f['4c'] = True
        f['4'] = poverty_line
        pct_of_poverty = f['3'] / f['4'] * 100
        if pct_of_poverty > 400:
            pct_of_poverty = 401
        else:
            pct_of_poverty = int(pct_of_poverty)
        f['5'] = pct_of_poverty

        applicable_figure = f.compute_applicable_figure(
            pct_of_poverty
        )
        old_disable_rounding = f.disable_rounding
        f.disable_rounding = True
        f['7'] = applicable_figure
        f.disable_rounding = old_disable_rounding
        f['8a'] = round(f['3'] * applicable_figure)
        f['8b'] = round(f['8a']/12)
        f['11a'] = inputs['aca_premium']
        f['11b'] = inputs['aca_slcsp']
        f['11c'] = f['8a']
        f['11d'] = max(f['11b'] - f['11c'], 0)
        f['11e'] = min(f['11a'], f['11d'])
        ptc_advance = 0
        if 'ptc_advance' in inputs:
            ptc_advance = inputs['ptc_advance']
        f['11f'] = ptc_advance
        # TODO: monthly values
        f['24'] = f['11e']
        f['25'] = f['11f']
        f['26'] = max(f['24'] - f['25'], 0)
        # if > 0: add f26 to schedule 3 line 9.
        if f['24'] < f['25']:
            # TODO: repayment of tax credit
            f['27'] = f['25'] - f['24']
            is_single_filer = inputs['status'] == FilingStatus.SINGLE
            repayment_limitation = f.compute_repayment_limitation(
                f['5'], is_single_filer)
            if repayment_limitation is not None:
                f['28'] = repayment_limitation
                f['29'] = min(f['27'], f['28'])
            else:
                f['29'] = f['27']
            # place f29 on schedule 2 line 2 of 1040.

        if ptc_advance != 0 or f['24'] != 0:
            f.must_file = True
        f.must_file = True

    def title(self):
        return 'Form 8962'

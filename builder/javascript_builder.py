

class FILTERS:
    deviationStandard = 'Witnet.Types.FILTERS.deviationStandard'
    mode = 'Witnet.Types.FILTERS.mode'


class REDUCERS:
    ...


aggregator = '''// Filters out any value that is more than 1.5 times the standard
// deviation away from the average, then computes the average mean of the
// values that pass the filter.
const aggregator = new Witnet.Aggregator({
  filters: [
    [Witnet.Types.FILTERS.deviationStandard, 1.5],
  ],
  reducer: Witnet.Types.REDUCERS.averageMean,
})'''

tally = '''// Filters out any value that is more than 1.5 times the standard
// deviation away from the average, then computes the average mean of the
// values that pass the filter.
const tally = new Witnet.Tally({
  filters: [
    [Witnet.Types.FILTERS.deviationStandard, 1.5],
  ],
  reducer: Witnet.Types.REDUCERS.averageMean,
})'''


def build_dr_js(sources, token_0, token_1):
    _request_sources = ''.join([f'  .source({x(token_0, token_1)[0]})\n' for x in sources])
    _sources = ''.join([f'\n{x(token_0, token_1)[1]}\n' for x in sources])
    req = f'''// This is the Witnet.Request object that needs to be exported
const request = new Witnet.Request()
{_request_sources[:-1]}
  .setAggregator(aggregator) // Set the aggregator function
  .setTally(tally) // Set the tally function
  .setQuorum(10, 51) // Set witness count and minimum consensus percentage
  .setFees(10 ** 6, 10 ** 6) // Set economic incentives
  .setCollateral(5 * 10 ** 9) // Require 5 wits as collateral'''
    footer = '''// Do not forget to export the request object
export { request as default }'''
    tmp = f'''import * as Witnet from "witnet-requests"
{_sources}

{aggregator}

{tally}

{req}

{footer}'''

    # print(tmp)
    file_name = f'data/requests/{token_0.capitalize()}{token_1.capitalize()}Price.js'
    print(f'   ├ Creating {file_name}.')
    with open(file_name, 'w') as f:
        f.write(tmp)

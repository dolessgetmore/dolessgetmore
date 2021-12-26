###########################################
### 추가 기능 개발
###########################################
import pandas as pd
import pandas_datareader as pdr
import datetime
###########################################
### 사용하는 모듈
import yfinance as yf
import get_all_tickers
###########################################

class data:
    pass

class YahooFinance:
        
    def get_daily_data(self, tickers, start, end):
        def data(ticker):
            return pdr.DataReader( ticker , 'yahoo' , start,end )
        datas = map(data, tickers)
        datas = pd.concat(datas, keys = tickers, names = ['Tickers', 'Date'])
        datas.reset_index(level=[0,1], inplace=True)

        df_records = datas.to_dict('records')

        # if start < datetime.date.today():
        #     model_instances = [models.daily_data(
        #         ticker=models.ticker.objects.get(ticker=record['Tickers']),
        #         date=record['Date'],
        #         high=record['High'],
        #         low=record['Low'],
        #         open=record['Open'],
        #         close=record['Close'],
        #         volume=record['Volume'],
        #         adj_close=record['Adj Close'],
        #     ) for record in df_records]

            # for obj in model_instances:
            #     if obj.date < datetime.date.today():
            #         obj.is_closed = True

            # models.daily_data.objects.bulk_create(model_instances, ignore_conflicts=True)
        return datas



    def get_recent(self, tickers, start, end):
        for i in range(20):
            try:
                start = start - datetime.timedelta(days=1)
                end = start
                return self.get_daily_data(tickers, start, end)
            except:
                start = start - datetime.timedelta(days=1)
                end = start

    def get_ticker():
        import pandas as pd
        import yahooquery as yq

        def get_symbol(query, preferred_exchange='AMS'):
            try:
                data = yq.search(query)
            except ValueError: # Will catch JSONDecodeError
                print(query)
            else:
                quotes = data['quotes']
                if len(quotes) == 0:
                    return 'No Symbol Found'

                symbol = quotes[0]['symbol']
                for quote in quotes:
                    if quote['exchange'] == preferred_exchange:
                        symbol = quote['symbol']
                        break
                return symbol

        companies = ['Abbott Laboratories', 'ABBVIE', 'Abercrombie', 'Abiomed', 'Accenture Plc']
        df = pd.DataFrame({'Company name': companies})
        df['Company symbol'] = df.apply(lambda x: get_symbol(x['Company name']), axis=1)


if __name__ == '__main__':
    # print(get_all_tickers.get_tickers())
    print(get_all_tickers.get_tickers_by_region(get_all_tickers.Region.ASIA))
    
    # print(get_all_tickers.Region)
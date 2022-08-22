

class ReportAnalytics(object):
    def __init__(self, book_names, start_date, end_date, full_report=False):
        self.fpdf = FPDF()
        self.book_names = book_names
        self.start_date = start_date
        self.end_date = end_date
        self.full_report = full_report
        

    def future_payment_PDF_generator(self):
        # Generate the pdf:
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font('Helvetica', 'B', 14)
        pdf.set_text_color(83, 83, 81)
        text = "        The graph represents the number of payers in each hour for each channel, as well as the amount of commitment."
        pdf.set_xy(x=50, y=20)
        pdf.cell(w=40, h=19, txt=f'Commitment per hour', border=0, align='L', fill=False)
        pdf.set_font('Helvetica', 'B', 8)
        plot_sms = multiple_lines_plot(dataframe[dataframe['Channel'] == 'sms'], 'sms', color='#FB6276')
        plot_email = multiple_lines_plot(dataframe[dataframe['Channel'] == 'email'], 'email', color='#129DA4')
        plot_whatsapp = multiple_lines_plot(dataframe[dataframe['Channel'] == 'whatsapp'], 'whatsapp', color='#75485E')
        pdf.set_xy(x=0, y=20)
        pdf.cell(w=200, h=40, txt=text, border=0, align='L', fill=False)
        pdf.set_xy(x=0, y=26)
        pdf.cell(w=200, h=40, txt=f'        Books Names:  {books}', border=0, align='L', fill=False)
        pdf.set_xy(x=0, y=30)
        pdf.cell(w=200, h=40, txt=f'        Dates: {start_date} - {end_date}', border=0, align='L', fill=False)
        pdf.image(plot_sms, x=38, y=53, w=130, h=70)
        pdf.image(plot_email, x=38, y=123, w=130, h=70)
        pdf.image(plot_whatsapp, x=38, y=193, w=130, h=70)
        
        return pdf
        
    
    def create_payment_by_the_hour_grpah(self):
        """
        The function generates a pdf with a graph that presents the distribution of payments per hour per channel.
        :param books: name of the books that presented in the graph.
        :param start_date: The graph will show only the information of customers who paid after this date.
        :param end_date: The graph will show only the information of customers who paid before this date.
        :param output_path: Output path for the pdf.
        :return: A PDF with the graph.
        """
        data_frames = queries(self.books, self.start_date, self.end_date)
        final_data = preprocessing(data_frames[0], data_frames[1], data_frames[2], data_frames[3])

        if self.full_report:
            return PDF_generator(final_data, books, start_date, end_date, output_path)
        else:
            pdf = PDF_generator(final_data, books, start_date, end_date, output_path)
            return pdf.output(f'{output_path}hours_payment_per_channel.pdf')
    
    
    def create_futuer_payment_graph(self):
        """
        The function generates a pdf with a graph that presents the distribution of payments per hour per channel.
        :param books: name of the books that presented in the graph.
        :param start_date: The graph will show only the information of customers who paid after this date.
        :param end_date: The graph will show only the information of customers who paid before this date.
        :param output_path: Output path for the pdf.
        :return: A PDF with the graph.
        """
        data_frames = queries(self.books, self.start_date, self.end_date)
        final_data = preprocessing(data_frames[0], data_frames[1], data_frames[2], data_frames[3])
        return PDF_generator(final_data, books, start_date, end_date, output_path)

    def produce_full_report(self):
        
        self.create_futuer_payment_graph(self.fpddf, self.book_names)
        self.fpdf.add_page()
        self.create_payment_by_the_hour_grpah(self.fpddf, self.book_names)
        self.fpdf.add_page()

        # Save PDF
        pdf.output(f'{output_path}hours_payment_per_channel.pdf')
    
    
    
    
    
    
    

    
report_analytics = ReportAnalytics(book_names, start_date, end_date)

#report_analytics.produce_full_report()

report_analytics.create_futuer_payment_graph()
class Invoice:
    def __init__(self, client=None):
        self.client = client
        self.service = 'Invoice'

    def order_states(self):
        api = self.client.get_client(self.service)
        state = api.factory.create('OrderSlipStateType')
        return state

    def search_params(self):
        api = self.client.get_client(self.service)
        params = api.factory.create('InvoiceSearchParameters')
        return params

    def get_document(self, **kwargs):
        """
        Valid parameters are InvoiceSearchParameters

        - ChangedAfter
        - InvoiceIds
        - OrderIds
        - CustomerIds
        - OrderStates
        """
        api = self.client.get_client(self.service)

        params = api.factory.create('InvoiceDocumentSearchParameters')
        for key, value in kwargs.iteritems():
            setattr(params, key, value)

        status, result = api.service.GetInvoiceDocument(params)
        return result
        # return self.client.get(method, params)

    def get_document_with_zeep(self, **kwargs):
        """
        Valid parameters are InvoiceSearchParameters

        - ChangedAfter
        - InvoiceIds
        - OrderIds
        - CustomerIds
        - OrderStates
        """
        import zeep
        from requests import Session
        from zeep.transports import Transport

        session = Session()
        session.headers['Cookie'] = self.client._headers['Cookie']
        transport = Transport(session=session)
        wsdl = self.client._services[self.service]
        client = zeep.Client(wsdl, transport=transport)

        params = client.get_type('ns0:InvoiceDocumentSearchParameters')

        # call the api
        doc = client.service.GetInvoiceDocument(params(**kwargs))

        return doc

    def changed_after(self, changed, **options):
        api = self.client.get_client(self.service)

        # searchParams
        params = api.factory.create('InvoiceSearchParameters')
        params.ChangedAfter = changed

        invoiceReturnProperties = api.factory.create('ArrayOfString')  # noqa
        invoiceReturnProperties.string.extend(['OrderId', 'CustomerId', 'CustomerName', 'OrderStatus', 'InvoiceId', 'DateOrdered', 'DateInvoiced', 'PaymentTime', 'CustomerReferenceNo', 'ProjectId', 'OurReference', 'IncludeVAT', 'InvoiceTitle', 'InvoiceText', 'OrderTotalIncVat'])

        rowReturnProperties = api.factory.create('ArrayOfString')  # noqa
        rowReturnProperties.string.extend(['ProductId', 'RowId', 'Price', 'Name', 'AccrualDate', 'ChangeState'])

        options['invoiceReturnProperties'] = invoiceReturnProperties
        options['rowReturnProperties'] = rowReturnProperties

        method = api.service.GetInvoices

        return self.client.get_collection(method, params, **options)

    def from_invoiceids(self, invoiceids, **options):
        api = self.client.get_client(self.service)

        # searchParams
        params = api.factory.create('InvoiceSearchParameters')
        params.InvoiceIds = invoiceids

        invoiceReturnProperties = api.factory.create('ArrayOfString')  # noqa
        invoiceReturnProperties.string.extend(['OrderId', 'CustomerId', 'CustomerName', 'OrderStatus', 'InvoiceId', 'DateOrdered', 'DateInvoiced', 'PaymentTime', 'CustomerReferenceNo', 'ProjectId', 'OurReference', 'IncludeVAT', 'InvoiceTitle', 'InvoiceText', 'OrderTotalIncVat'])

        rowReturnProperties = api.factory.create('ArrayOfString')  # noqa
        rowReturnProperties.string.extend(['ProductId', 'RowId', 'Price', 'Name', 'AccrualDate', 'ChangeState'])

        options['invoiceReturnProperties'] = invoiceReturnProperties
        options['rowReturnProperties'] = rowReturnProperties

        method = api.service.GetInvoices

        return self.client.get_collection(method, params, **options)

    def from_orderids(self, orderids, **options):
        api = self.client.get_client(self.service)

        # searchParams
        params = api.factory.create('InvoiceSearchParameters')
        if type(orderids) is list:
            params.OrderIds.int.extend(orderids)
        else:
            params.OrderIds.int.append(orderids)

        invoiceReturnProperties = api.factory.create('ArrayOfString')  # noqa
        invoiceReturnProperties.string.extend(['OrderId', 'CustomerId', 'CustomerName', 'OrderStatus', 'InvoiceId', 'DateOrdered', 'DateInvoiced', 'PaymentTime', 'CustomerReferenceNo', 'ProjectId', 'OurReference', 'IncludeVAT', 'InvoiceTitle', 'InvoiceText', 'OrderTotalIncVat'])

        rowReturnProperties = api.factory.create('ArrayOfString')  # noqa
        rowReturnProperties.string.extend(['ProductId', 'RowId', 'Price', 'Name', 'AccrualDate', 'ChangeState'])

        options['invoiceReturnProperties'] = invoiceReturnProperties
        options['rowReturnProperties'] = rowReturnProperties

        method = api.service.GetInvoices

        return self.client.get_collection(method, params, **options)

    def from_customerids(self, customerids, **options):
        api = self.client.get_client(self.service)

        # searchParams
        params = api.factory.create('InvoiceSearchParameters')
        if type(customerids) is list:
            params.CustomerIds.int.extend(customerids)
        else:
            params.CustomerIds.int.append(customerids)

        invoiceReturnProperties = api.factory.create('ArrayOfString')  # noqa
        invoiceReturnProperties.string.extend(['OrderId', 'CustomerId', 'CustomerName', 'OrderStatus', 'InvoiceId', 'DateOrdered', 'DateInvoiced', 'PaymentTime', 'CustomerReferenceNo', 'ProjectId', 'OurReference', 'IncludeVAT', 'InvoiceTitle', 'InvoiceText', 'OrderTotalIncVat'])

        rowReturnProperties = api.factory.create('ArrayOfString')  # noqa
        rowReturnProperties.string.extend(['ProductId', 'RowId', 'Price', 'Name', 'AccrualDate', 'ChangeState'])

        options['invoiceReturnProperties'] = invoiceReturnProperties
        options['rowReturnProperties'] = rowReturnProperties

        method = api.service.GetInvoices

        return self.client.get_collection(method, params, **options)

    def from_orderstate(self, orderstates, **options):
        api = self.client.get_client(self.service)

        # searchParams
        params = api.factory.create('InvoiceSearchParameters')
        if type(orderstates) is list:
            params.OrderStates.OrderSlipStateType.extend(orderstates)
        else:
            params.OrderStates.OrderSlipStateType.append(orderstates)

        invoiceReturnProperties = api.factory.create('ArrayOfString')  # noqa
        invoiceReturnProperties.string.extend(['OrderId', 'CustomerId', 'CustomerName', 'OrderStatus', 'InvoiceId', 'DateOrdered', 'DateInvoiced', 'PaymentTime', 'CustomerReferenceNo', 'ProjectId', 'OurReference', 'IncludeVAT', 'InvoiceTitle', 'InvoiceText', 'OrderTotalIncVat'])

        rowReturnProperties = api.factory.create('ArrayOfString')  # noqa
        rowReturnProperties.string.extend(['ProductId', 'RowId', 'Price', 'Name', 'AccrualDate', 'ChangeState'])

        options['invoiceReturnProperties'] = invoiceReturnProperties
        options['rowReturnProperties'] = rowReturnProperties

        method = api.service.GetInvoices

        return self.client.get_collection(method, params, **options)

    def search(self, params, **options):
        api = self.client.get_client(self.service)

        invoiceReturnProperties = api.factory.create('ArrayOfString')  # noqa
        invoiceReturnProperties.string.extend(['OrderId', 'CustomerId', 'CustomerName', 'OrderStatus', 'InvoiceId', 'DateOrdered', 'DateInvoiced', 'PaymentTime', 'CustomerReferenceNo', 'ProjectId', 'OurReference', 'IncludeVAT', 'InvoiceTitle', 'InvoiceText', 'OrderTotalIncVat'])

        rowReturnProperties = api.factory.create('ArrayOfString')  # noqa
        rowReturnProperties.string.extend(['ProductId', 'RowId', 'Price', 'Name', 'AccrualDate', 'ChangeState'])

        options['invoiceReturnProperties'] = invoiceReturnProperties
        options['rowReturnProperties'] = rowReturnProperties

        method = api.service.GetInvoices

        return self.client.get_collection(method, params, **options)

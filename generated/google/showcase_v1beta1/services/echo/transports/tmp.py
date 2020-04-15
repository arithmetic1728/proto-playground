class EchoClient(metaclass=EchoClientMeta):
    DEFAULT_OPTIONS = ClientOptions.ClientOptions(api_endpoint="localhost:7469")

    def __init__(
        self,
        *,
        credentials: credentials.Credentials = None,
        transport: Union[str, EchoTransport] = None,
        client_options: ClientOptions = DEFAULT_OPTIONS,
    ) -> None:
        if isinstance(client_options, dict):
            client_options = ClientOptions.from_dict(client_options)

        api_mtls_endpoint = None
        client_cert_callback = None
        if hasattr(client_options, "api_mtls_endpoint"):
            api_mtls_endpoint = client_options["api_mtls_endpoint"]
        if hasattr(client_options, "client_cert_callback"):
            client_cert_callback = client_options["client_cert_callback"]
        if api_mtls_endpoint or client_cert_callback:
            # we will create the mTLS transport, ignore the given transport.
            transport = None

        if isinstance(transport, EchoTransport):
            if credentials:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            self._transport = transport
        else:
            Transport = type(self).get_transport_class(transport)

            self._transport = Transport(
                credentials=credentials,
                host=client_options.api_endpoint or "localhost:7469",
                api_mtls_endpoint=api_mtls_endpoint,
                client_cert_callback=client_cert_callback,
            )

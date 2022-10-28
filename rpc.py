# from SimpleXMLRPCServer import SimpleXMLRPCServer
# from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
# import OpenOPC
# 
# chemicalsMain = OpenOPC.open_client('172.30.246.210')
# chemicalsMain.connect('SWToolbox.TOPServer.V5')
# print(chemicalsMain.info())
# print(chemicalsMain.list())
# print('\n')
# 
# chemicalsRedundant = OpenOPC.open_client('172.30.246.211')
# chemicalsRedundant.connect('SWToolbox.TOPServer.V5')
# print(chemicalsRedundant.info())
# print(chemicalsRedundant.list())
# print('\n')
# 
# smeltingMain = OpenOPC.open_client('172.30.246.212')
# smeltingMain.connect('SWToolbox.TOPServer.V5')
# print(smeltingMain.info())
# print(smeltingMain.list())
# print('\n')
# 
# smeltingRedundant = OpenOPC.open_client('172.30.246.213')
# smeltingRedundant.connect('SWToolbox.TOPServer.V5')
# print(smeltingRedundant.info())
# print(smeltingRedundant.list())
# print('\n')
# 
# #for i in range(0,32000):
#     #pass
#     #chemicalsMain.write(('plc18c.plc18d.D25000', i))
#     #print(chemicalsMain.read('plc18.D25000'))
# 
# # Restrict to a particular path.
# class RequestHandler(SimpleXMLRPCRequestHandler):
#     rpc_paths = ()
#     
#     """def do_GET(self):
#         # Check that the path is legal
#         if not self.is_rpc_path_valid():
#             self.report_404()
#             return
#     
#         response = 'hello world!'
#         self.send_response(200)
#         self.send_header("Content-type", "text/xml")
#         self.send_header("Content-length", str(len(response)))
#         self.end_headers()
#         self.wfile.write(response)
#     
#         # shut down the connection
#         self.wfile.flush()"""
# 
# # Create server
# server = SimpleXMLRPCServer(("0.0.0.0", 8000), requestHandler=RequestHandler)
# server.register_introspection_functions()
# 
# # Register pow() function; this will use the value of
# # pow.__name__ as the name, which is just 'pow'.
# #server.register_function(pow)
# 
# # Register a function under a different name
# def adder_function(x,y):
#     return x + y
# server.register_function(adder_function, 'add')
# 
# def returnString(s):
#     return s + 'random string stuff'
# server.register_function(returnString, 'string')
# 
# def getIO(sIOServer, plc, address):
#     if sIOServer == 'chemM':
#         ioServer = chemicalsMain
#     if sIOServer == 'chemR':
#         ioServer = chemicalsRedundant
#     if sIOServer == 'smeltingM':
#         ioServer = smeltingMain
#     if sIOServer == 'smeltingR':
#         ioServer = smeltingRedundant
#     return ioServer.read(plc + '.' + address)
# server.register_function(getIO, 'getIO')
# 
# # Register an instance; all the methods of the instance are
# # published as XML-RPC methods (in this case, just 'div').
# class MyFuncs:
#     def div(self, x, y):
#         return x // y
#     
# server.register_instance(MyFuncs())
# 
# # Run the server's main loop
# server.serve_forever()
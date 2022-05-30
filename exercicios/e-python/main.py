import medicos 

menu = str(input('Deseja agendar uma consulta? (S ou N)')).upper().strip()

if menu == 'S':
    paciente = input('Por favor digite seu nome: ')
    print(f'{paciente}, escolha com qual médico deseja consultar:')
    print('1.Dra Zileide')
    print('2.Dr Anhanguarte')
    medico = int(input('com qual médico deseja agendar uma consulta?'))
    if medico ==1:
        print(f'Sua consulta com o(a) {medicos.medicos[0]} será agendada')
    
    if medico ==2:
        print(f'Sua consulta com o(a) {medicos.medicos[1]} será agendada.')
else:
    print('Agradecemos o seu contato!')


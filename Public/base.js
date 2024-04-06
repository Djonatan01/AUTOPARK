
// Função para aplicar máscara ao campo de entrada celular
function applyMaskToPhoneInput() {
    $("#celular").mask("(00) 00000-0000");
 }

 // Função para aplicar máscara ao campo de entrada CEP
 function applyMaskToZipCodeInput() {
    $("#cep").mask("00000-000");
 }

 // Função para aplicar máscara ao campo de entrada CPF
 function applyMaskToCPFInput() {
    $("#cpf").mask("000.000.000-00");
 }
 // Aplicar as máscaras quando o documento estiver pronto
 $(document).ready(function () {
    applyMaskToPhoneInput();
    applyMaskToZipCodeInput();
    applyMaskToCPFInput();
 });

// Função para pegar o valor do select e atualizar o campo NumVaga
function getSelectedValue() {
   // Acessa o elemento select pelo seu ID
   var selectElement = document.getElementById('tipoVaga');
   // Pega o valor do option selecionado
   var selectedValue = selectElement.value;
   // Obtém o valor atual do campo NumVaga
   var ultimaVaga = (document.getElementById('NumVaga').value).split('-') ;
   // Construindo o novo valor para NumVaga com base no tipo de vaga selecionado
   var novoValorNumVaga = ultimaVaga[0] + "-" + selectedValue;
   // Atualiza o campo NumVaga com o novo valor
   document.getElementById('NumVaga').value = novoValorNumVaga;
   // Retorna o valor selecionado
   return selectedValue;
}

// Adiciona um ouvinte de evento 'change' ao elemento select
document.getElementById('tipoVaga').addEventListener('change', function() {
   // Chama a função getSelectedValue() quando o valor do select é alterado
   getSelectedValue();
});

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

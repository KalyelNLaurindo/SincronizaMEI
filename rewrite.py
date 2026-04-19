import re

with open('ImplantaionsPlanTasks.md', 'r', encoding='utf-8') as f:
    text = f.read()

epic_pattern = re.compile(r'(# [🔴🟠🟡🟢] E[0-9] — .*?)(?=(?:\n# [🔴🟠🟡🟢] E[0-9] — )|\Z)', re.DOTALL)
epics = epic_pattern.findall(text)

header_pattern = re.compile(r'^(.*?)(?=# [🔴🟠🟡🟢] E[0-9] — )', re.DOTALL)
header_match = header_pattern.search(text)
header = header_match.group(1) if header_match else ''

epics_dict = {}
for e in epics:
    m = re.search(r'# [🔴🟠🟡🟢] E([0-9])', e)
    if m:
        num = int(m.group(1))
        epics_dict[num] = e

# Reorder: 1, 2, then 7 goes to 3, then 3,4,5,6 go to 4,5,6,7, then 8,9
new_order = [1, 2, 7, 3, 4, 5, 6, 8, 9]

# Counter for global task renumbering
task_counter = 1

def process_epic(epic_text, is_feature_epic):
    global task_counter
    parts = re.split(r'(## TASK-[0-9]{3} .*?(?:\n(?:(?!(?:## TASK-)|(?:---)).)*)*)', epic_text, flags=re.DOTALL)
    
    epic_head = parts[0]
    result_text = epic_head

    for p in parts[1:]:
        if p.startswith('## TASK-'):
            title_match = re.search(r'## TASK-[0-9]{3} · (.*)', p)
            title = title_match.group(1).strip() if title_match else 'Tarefa'
            
            content = p[p.find('\n')+1:]
            
            # Remove artifacts of previous auto-replace
            content = re.sub(r'### Critérios de Aceite \(TDD Lifecycle\).*?(?=#### Regras de Negócio)', '### Critérios de Aceite\n', content, flags=re.DOTALL)
            content = content.replace('#### Regras de Negócio (a serem validadas nos testes):\n', '')

            if is_feature_epic and ('Implementar' in title or 'Configurar' in title) and not 'test' in title.lower():
                # Create Test Task
                test_title = f'## TASK-{task_counter:03d} · [TDD RED] Escrever testes falhando para: {title}\n'
                test_content = (
                    f"**Prioridade:** 🔴 P0\n\n"
                    f"### O que fazer\n"
                    f"Implementar as suítes de testes unitários ou de integração **falhando** (mocked features) que validam as regras descritas para '{title}'. Essa tarefa obrigatoriamente vem antes da respectiva implementação da funcionalidade.\n\n"
                    f"### Critérios de Aceite\n"
                    f"- [ ] Configurar os scaffolds do teste usando as abstrações base.\n"
                    f"- [ ] Injetar os mocks necessários nas dependências do projeto.\n"
                    f"- [ ] Garantir que ao rodar a suíte, todas as validações de regra de negócio abaixo resultem em erro RED.\n\n"
                    f"---\n\n"
                )
                result_text += test_title + test_content
                task_counter += 1

                # Create Implementation Task
                impl_title = f'## TASK-{task_counter:03d} · [TDD GREEN/REFACTOR] Escrever funcionalidade MVC (POO) para: {title}\n'
                result_text += impl_title + content
                task_counter += 1
            else:
                new_title = f'## TASK-{task_counter:03d} · {title}\n'
                result_text += new_title + content
                task_counter += 1
        else:
            result_text += p

    return result_text

final_epics = []
epic_counter = 1
for old_num in new_order:
    if old_num not in epics_dict:
        continue
    e_text = epics_dict[old_num]
    
    e_text = re.sub(r'# [🔴🟠🟡🟢] E[0-9] — ', f'# 🔴 E{epic_counter} — ', e_text, 1)
    e_text = re.sub(r'\*Épico:\*\* E[0-9] —', f'**Épico:** E{epic_counter} —', e_text)
    
    is_feature_epic = epic_counter in [4, 5, 6, 7]
    final_epics.append(process_epic(e_text, is_feature_epic))
    epic_counter += 1

with open('ImplantaionsPlanTasks.md', 'w', encoding='utf-8') as f:
    f.write(header + ''.join(final_epics))

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

new_order = [1, 2, 7, 3, 4, 5, 6, 8, 9]

task_counter = 1

def process_epic(epic_text, is_feature_epic):
    global task_counter
    parts = re.split(r'(## TASK-[0-9]{3} .*?(?:\n(?:(?!(?:## TASK-[0-9]{3} )|(?:---)).)*)*)', epic_text, flags=re.DOTALL)
    
    epic_head = parts[0]
    result_text = epic_head

    for p in parts[1:]:
        if p.startswith('## TASK-'):
            title_match = re.search(r'## TASK-[0-9]{3} · (.*?)\n', p)
            title = title_match.group(1).strip() if title_match else 'Funcionalidade'
            
            first_newline = p.find('\n')
            content = p[first_newline+1:] if first_newline != -1 else ""

            is_test_task = 'teste' in title.lower() or 'jacoco' in title.lower() or 'archunit' in title.lower() or 'testcontainers' in title.lower()
            
            if is_feature_epic and not is_test_task:
                test_title = f'## TASK-{task_counter:03d} · [TDD RED] Criar testes falhos para: {title}\n\n'
                test_content = (
                    f"**Prioridade:** 🔴 P0\n"
                    f"**Estimativa:** 2h\n\n"
                    f"### O que fazer\n"
                    f"Implementar testes unitários e de integração (com features mockadas) verificando os limites das regras da funcionalidade '{title}'. Esta task OBRIGATORIAMENTE precede o desenvolvimento do código da aplicação.\n\n"
                    f"### Critérios de Aceite\n"
                    f"- [ ] Configurar fixtures e abstrações do ambiente teste.\n"
                    f"- [ ] Injetar os Mocks nas dependências que ainda não foram criadas.\n"
                    f"- [ ] Garantir que os testes falham corretamente (RED).\n\n"
                    f"---\n\n"
                )
                result_text += test_title + test_content
                task_counter += 1

                impl_title = f'## TASK-{task_counter:03d} · [TDD GREEN/REFACTOR] Implementar lógica: {title}\n'
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
    
    if old_num == 7:
        e_text = re.sub(r'# [🔴🟠🟡🟢] E7 — .*', f'# 🔴 E3 — FUNDAÇÃO TDD & QUALIDADE (Shift-Left)', e_text, 1)
    else:
        e_text = re.sub(r'# [🔴🟠🟡🟢] E[0-9] — ', f'# 🔴 E{epic_counter} — ', e_text, 1)
    
    e_text = re.sub(r'\*\*Épico:\*\* E[0-9] —', f'**Épico:** E{epic_counter} —', e_text)
    
    is_feature_epic = epic_counter in [4, 5, 6, 7]
    final_epics.append(process_epic(e_text, is_feature_epic))
    epic_counter += 1

new_content = header + ''.join(final_epics)
new_content = re.sub(r'\| E3 \| Backend.*?\| 10 tasks \|', '| E3 | Fundação TDD & Qualidade | 🔴 P0 | 6 tasks |', new_content)
new_content = re.sub(r'\| E7 \| Testes \& Qualidade \| 🟠 P1 \| 6 tasks \|', '| E7 | Frontend React PWA | 🟡 P2 | X tasks |', new_content)

new_content = re.sub(r'\*\*Total: 55 tasks\*\*', f'**Total: {task_counter-1} tasks**', new_content)

with open('ImplantaionsPlanTasks.md', 'w', encoding='utf-8') as f:
    f.write(new_content)

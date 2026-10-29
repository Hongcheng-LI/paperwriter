import { readFileSync } from "node:fs";
import { readFile } from "node:fs/promises";
import { join, sep } from "node:path";
import { fileURLToPath } from "node:url";

const name = "paperwriter";
const inject = ["skills"];
const FM = /^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/u;
const directory = join(fileURLToPath(new URL("./assets/", import.meta.url)), name);

const description = (() => {
  const fm = FM.exec(readFileSync(join(directory, "SKILL.md"), "utf8"))?.[1] ?? "";
  const raw = fm.match(/^description:\s*"((?:\\.|[^"\\])*)"/m)?.[1] ?? "";
  return JSON.parse(`"${raw}"`);
})();

const candidate = {
  name,
  description,
  invocation: { modelInvocable: true, userInvocable: true },
  provider: "dsh-paperwriter",
  source: "bundled",
  rank: 600, // same tier as official bundled skills (dsh-skill BUNDLED_SKILL_RANK)
  resourceBase: { kind: "directory", path: directory.split(sep).join("/") },
  locator: join(directory, "SKILL.md"),
};

export function apply(ctx) {
  ctx.skills.registerProvider(() => ({
    name,
    list: () => Promise.resolve([candidate]),
    async get(candidate) {
      const body = await readFile(candidate.locator, "utf8");
      const content = FM.test(body) ? body.replace(FM, "").trim() : body;
      return { ...candidate, content };
    },
  }));
}

export { inject, name };

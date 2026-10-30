# Play-Annotation-Generator Annotation Review — FieldGoalBlock_86

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_86`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 389
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 220
- **Validation Warnings:** 239
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 195
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `8` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `3` | `3` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `7` | `7` |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher4 | defense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `12` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `13` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `14` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `15` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `16` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `17` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `18` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `20` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `3` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `7` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `8` | `Group` | 0 | START | 0 | 21 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `3` | `3` | 15 | START | 15 | 23 |
| ✅ EXACT | `Action_KickBall` | Kicker | `7` | `7` | 34 | START | 34 | 41 |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher4 | `9` | `9` | 40 | START | 40 | 57 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PlaceBall` | 15 | 23 | 9 | inferred_complete_timeline |
| `Action_None` | 24 | 74 | 51 | inferred_complete_timeline |
| `Action_None` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_None` | 87 | 178 | 92 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_None` | 226 | 228 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_KickBall` | 34 | 41 | 8 | inferred_complete_timeline |
| `Action_None` | 42 | 42 | 1 | inferred_complete_timeline |
| `Action_None` | 50 | 89 | 40 | inferred_complete_timeline |
| `Action_None` | 99 | 132 | 34 | inferred_complete_timeline |
| `Action_None` | 138 | 174 | 37 | inferred_complete_timeline |
| `Action_None` | 184 | 186 | 3 | inferred_complete_timeline |
| `Action_None` | 188 | 194 | 7 | inferred_complete_timeline |
| `Action_None` | 197 | 203 | 7 | inferred_complete_timeline |
| `Action_None` | 205 | 212 | 8 | inferred_complete_timeline |
| `Action_None` | 218 | 237 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–24
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 24 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–116
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 20 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 33 | 12 | inferred_complete_timeline |
| `Action_None` | 34 | 50 | 17 | inferred_complete_timeline |
| `Action_None` | 53 | 116 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 27 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 33 | 3 | inferred_complete_timeline |
| `Action_None` | 34 | 41 | 8 | inferred_complete_timeline |
| `Action_None` | 49 | 50 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 33 | 9 | inferred_complete_timeline |
| `Action_None` | 34 | 48 | 15 | inferred_complete_timeline |
| `Action_None` | 59 | 146 | 88 | inferred_complete_timeline |
| `Action_None` | 149 | 300 | 152 | inferred_complete_timeline |
| `Action_None` | 323 | 389 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–276
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 23 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 33 | 8 | inferred_complete_timeline |
| `Action_None` | 38 | 78 | 41 | inferred_complete_timeline |
| `Action_None` | 87 | 91 | 5 | inferred_complete_timeline |
| `Action_None` | 120 | 193 | 74 | inferred_complete_timeline |
| `Action_None` | 197 | 200 | 4 | inferred_complete_timeline |
| `Action_None` | 202 | 243 | 42 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 250 | 258 | 9 | inferred_complete_timeline |
| `Action_None` | 260 | 276 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–341
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 33 | 18 | inferred_complete_timeline |
| `Action_None` | 34 | 341 | 308 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 68 | 71 | 4 | inferred_complete_timeline |
| `Action_None` | 90 | 101 | 12 | inferred_complete_timeline |
| `Action_None` | 103 | 166 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–35
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_None` | 34 | 35 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 33 | 20 | inferred_complete_timeline |
| `Action_None` | 34 | 37 | 4 | inferred_complete_timeline |
| `Action_None` | 56 | 186 | 131 | inferred_complete_timeline |
| `Action_None` | 188 | 198 | 11 | inferred_complete_timeline |
| `Action_None` | 227 | 245 | 19 | inferred_complete_timeline |
| `Action_None` | 250 | 255 | 6 | inferred_complete_timeline |
| `Action_None` | 258 | 271 | 14 | inferred_complete_timeline |
| `Action_None` | 275 | 286 | 12 | inferred_complete_timeline |
| `Action_None` | 288 | 299 | 12 | inferred_complete_timeline |
| `Action_None` | 302 | 304 | 3 | inferred_complete_timeline |
| `Action_None` | 315 | 389 | 75 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 159 | 126 | inferred_complete_timeline |
| `Action_None` | 164 | 180 | 17 | inferred_complete_timeline |
| `Action_None` | 183 | 193 | 11 | inferred_complete_timeline |
| `Action_None` | 196 | 208 | 13 | inferred_complete_timeline |
| `Action_None` | 216 | 242 | 27 | inferred_complete_timeline |
| `Action_None` | 251 | 267 | 17 | inferred_complete_timeline |
| `Action_None` | 276 | 291 | 16 | inferred_complete_timeline |
| `Action_None` | 295 | 296 | 2 | inferred_complete_timeline |
| `Action_None` | 298 | 304 | 7 | inferred_complete_timeline |
| `Action_None` | 324 | 389 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 74 | 41 | inferred_complete_timeline |
| `Action_None` | 82 | 107 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 33 | 4 | inferred_complete_timeline |
| `Action_None` | 34 | 34 | 1 | inferred_complete_timeline |
| `Action_None` | 36 | 42 | 7 | inferred_complete_timeline |
| `Action_None` | 48 | 64 | 17 | inferred_complete_timeline |
| `Action_None` | 68 | 100 | 33 | inferred_complete_timeline |
| `Action_None` | 103 | 248 | 146 | inferred_complete_timeline |
| `Action_None` | 250 | 275 | 26 | inferred_complete_timeline |
| `Action_None` | 299 | 300 | 2 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_None` | 306 | 389 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 63 | 30 | inferred_complete_timeline |
| `Action_None` | 106 | 115 | 10 | inferred_complete_timeline |
| `Action_None` | 117 | 147 | 31 | inferred_complete_timeline |
| `Action_None` | 166 | 204 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–360
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_BlockKick` | 40 | 57 | 18 | inferred_complete_timeline |
| `Action_None` | 58 | 96 | 39 | inferred_complete_timeline |
| `Action_None` | 148 | 218 | 71 | inferred_complete_timeline |
| `Action_None` | 222 | 236 | 15 | inferred_complete_timeline |
| `Action_None` | 238 | 242 | 5 | inferred_complete_timeline |
| `Action_None` | 251 | 360 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–31
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 23 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 31 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 97 | 64 | inferred_complete_timeline |
| `Action_None` | 99 | 101 | 3 | inferred_complete_timeline |
| `Action_None` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_None` | 107 | 179 | 73 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 242 | 54 | inferred_complete_timeline |
| `Action_None` | 251 | 253 | 3 | inferred_complete_timeline |
| `Action_None` | 255 | 272 | 18 | inferred_complete_timeline |
| `Action_None` | 288 | 290 | 3 | inferred_complete_timeline |
| `Action_None` | 292 | 293 | 2 | inferred_complete_timeline |
| `Action_None` | 298 | 304 | 7 | inferred_complete_timeline |
| `Action_None` | 307 | 311 | 5 | inferred_complete_timeline |
| `Action_None` | 313 | 367 | 55 | inferred_complete_timeline |
| `Action_None` | 372 | 389 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 65 | 32 | inferred_complete_timeline |
| `Action_None` | 68 | 194 | 127 | inferred_complete_timeline |
| `Action_None` | 196 | 197 | 2 | inferred_complete_timeline |
| `Action_None` | 200 | 211 | 12 | inferred_complete_timeline |
| `Action_None` | 224 | 227 | 4 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 156 | 123 | inferred_complete_timeline |
| `Action_None` | 159 | 181 | 23 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 135 | 102 | inferred_complete_timeline |
| `Action_None` | 138 | 199 | 62 | inferred_complete_timeline |
| `Action_None` | 201 | 213 | 13 | inferred_complete_timeline |
| `Action_None` | 216 | 218 | 3 | inferred_complete_timeline |
| `Action_None` | 221 | 228 | 8 | inferred_complete_timeline |
| `Action_None` | 230 | 245 | 16 | inferred_complete_timeline |
| `Action_None` | 250 | 273 | 24 | inferred_complete_timeline |
| `Action_None` | 275 | 286 | 12 | inferred_complete_timeline |
| `Action_None` | 288 | 296 | 9 | inferred_complete_timeline |
| `Action_None` | 298 | 303 | 6 | inferred_complete_timeline |
| `Action_None` | 320 | 369 | 50 | inferred_complete_timeline |
| `Action_None` | 372 | 381 | 10 | inferred_complete_timeline |
| `Action_None` | 383 | 389 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 199 | 166 | inferred_complete_timeline |
| `Action_None` | 202 | 211 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 32–345 | 294 | 9 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 39–72 | 28 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 39–194 | 83 | 5 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 56–389 | 271 | 9 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 100–268 | 165 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 115–122 | 8 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 129–130 | 2 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 134–384 | 251 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 135–186 | 49 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 166–178 | 13 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 189–212 | 14 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 229–389 | 146 | 3 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 230–389 | 103 | 5 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 238–389 | 145 | 3 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 242–389 | 118 | 7 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 256–268 | 13 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 271–272 | 2 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 288–311 | 24 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 295–334 | 12 | 3 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 304–373 | 62 | 3 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 328–368 | 41 | 1 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 330–331 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 194 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_None' range [34-159] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-193] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-208] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-242] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-267] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-291] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-304] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-199] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-211] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-74] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-107] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-74] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-178] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-156] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-181] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-199] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-213] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-228] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-245] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-273] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-286] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-296] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-303] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-369] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-381] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-65] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-194] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-211] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '7' starts at frame 42, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [42-42] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-89] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-132] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-174] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-194] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-203] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-212] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-48] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-146] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-300] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-96] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-218] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-236] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-242] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-360] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-23] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-31] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-63] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-115] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-147] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-204] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-71] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-101] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-166] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-35] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-23] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-33] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-78] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-193] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-243] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-258] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-276] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-20] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-50] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-116] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-27] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-33] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-41] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-24] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-37] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-186] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-198] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-245] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-255] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-271] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-286] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-299] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-304] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 34, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [34-34] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-42] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-64] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-100] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-248] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-275] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-341] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-97] for track '21' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-242] for track '21' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-272] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-304] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-311] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-367] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-36] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-51] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-125] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-307] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-317] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-345] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-42] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-50] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-69] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-46] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-113] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-170] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-184] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-194] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-101] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-181] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-243] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-274] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-305] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-389] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-153] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-248] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-257] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-268] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-122] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-384] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-170] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-186] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-178] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-194] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-212] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-242] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-258] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-389] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-245] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-305] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-389] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-254] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-263] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-277] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-287] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-300] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-268] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-311] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-334] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-350] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-358] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-373] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-368] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.

</details>
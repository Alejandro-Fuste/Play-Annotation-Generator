# Play-Annotation-Generator Annotation Review — Counter_295

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_295`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 154
- **Validation Warnings:** 168
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 127
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `18` | `17` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 137 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 135 | START | 135 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `15` | `14` | 138 | START | 138 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `21` | `20` | 138 | START | 153 | 172 |
| ✅ EXACT | `Action_PullBlock` | RG | `18` | `17` | 138 | START | 138 | 234 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `8` | `7` | 138 | START | 138 | 234 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 152 | END | 135 | 152 |
| ✅ EXACT | `Action_Handoff` | QB | `20` | `19` | 164 | START | 164 | 181 |
| ✅ EXACT | `Action_BallCarry` | RB | `14` | `13` | 182 | START | 182 | 208 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 234 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–337
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_SnapReceive` | 135 | 152 | 18 | inferred_complete_timeline |
| `Action_None` | 153 | 163 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 164 | 181 | 18 | inferred_complete_timeline |
| `Action_None` | 182 | 337 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 181 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 182 | 208 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–337
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 290 | 156 | inferred_complete_timeline |
| `Action_None` | 292 | 306 | 15 | inferred_complete_timeline |
| `Action_None` | 309 | 337 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 371 | 237 | inferred_complete_timeline |
| `Action_None` | 373 | 389 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–327
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 196 | 62 | inferred_complete_timeline |
| `Action_None` | 198 | 276 | 79 | inferred_complete_timeline |
| `Action_None` | 280 | 327 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 138 | 234 | 97 | inferred_complete_timeline |
| `Action_None` | 235 | 245 | 11 | inferred_complete_timeline |
| `Action_None` | 249 | 251 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–386
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_DownBlock` | 138 | 167 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 171 | 205 | 35 | inferred_complete_timeline |
| `Action_DownBlock` | 215 | 234 | 20 | inferred_complete_timeline |
| `Action_None` | 235 | 243 | 9 | inferred_complete_timeline |
| `Action_None` | 245 | 276 | 32 | inferred_complete_timeline |
| `Action_None` | 279 | 293 | 15 | inferred_complete_timeline |
| `Action_None` | 300 | 383 | 84 | inferred_complete_timeline |
| `Action_None` | 385 | 386 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 15 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 134 | 115 | inferred_complete_timeline |
| `Action_None` | 135 | 142 | 8 | inferred_complete_timeline |
| `Action_None` | 198 | 206 | 9 | inferred_complete_timeline |
| `Action_None` | 208 | 389 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_BallSnap` | 135 | 152 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 153 | 172 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 191 | 220 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 224 | 234 | 11 | inferred_complete_timeline |
| `Action_None` | 235 | 238 | 4 | inferred_complete_timeline |
| `Action_None` | 240 | 242 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_PullBlock` | 138 | 234 | 97 | inferred_complete_timeline |
| `Action_None` | 235 | 389 | 155 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 202 | 68 | inferred_complete_timeline |
| `Action_None` | 211 | 218 | 8 | inferred_complete_timeline |
| `Action_None` | 220 | 223 | 4 | inferred_complete_timeline |
| `Action_None` | 230 | 276 | 47 | inferred_complete_timeline |
| `Action_None` | 279 | 351 | 73 | inferred_complete_timeline |
| `Action_None` | 353 | 354 | 2 | inferred_complete_timeline |
| `Action_None` | 360 | 363 | 4 | inferred_complete_timeline |
| `Action_None` | 373 | 389 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 203 | 69 | inferred_complete_timeline |
| `Action_None` | 205 | 228 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 144 | 10 | inferred_complete_timeline |
| `Action_None` | 148 | 156 | 9 | inferred_complete_timeline |
| `Action_None` | 158 | 188 | 31 | inferred_complete_timeline |
| `Action_None` | 196 | 212 | 17 | inferred_complete_timeline |
| `Action_None` | 215 | 219 | 5 | inferred_complete_timeline |
| `Action_None` | 221 | 230 | 10 | inferred_complete_timeline |
| `Action_None` | 233 | 235 | 3 | inferred_complete_timeline |
| `Action_None` | 274 | 293 | 20 | inferred_complete_timeline |
| `Action_None` | 299 | 300 | 2 | inferred_complete_timeline |
| `Action_None` | 302 | 308 | 7 | inferred_complete_timeline |
| `Action_None` | 313 | 389 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 165 | 31 | inferred_complete_timeline |
| `Action_None` | 173 | 201 | 29 | inferred_complete_timeline |
| `Action_None` | 246 | 254 | 9 | inferred_complete_timeline |
| `Action_None` | 267 | 283 | 17 | inferred_complete_timeline |
| `Action_None` | 293 | 313 | 21 | inferred_complete_timeline |
| `Action_None` | 315 | 316 | 2 | inferred_complete_timeline |
| `Action_None` | 322 | 389 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 230 | 96 | inferred_complete_timeline |
| `Action_None` | 238 | 276 | 39 | inferred_complete_timeline |
| `Action_None` | 279 | 290 | 12 | inferred_complete_timeline |
| `Action_None` | 294 | 315 | 22 | inferred_complete_timeline |
| `Action_None` | 319 | 320 | 2 | inferred_complete_timeline |
| `Action_None` | 325 | 389 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 389 | 255 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 280 | 146 | inferred_complete_timeline |
| `Action_None` | 286 | 389 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–304
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 233 | 99 | inferred_complete_timeline |
| `Action_None` | 256 | 279 | 24 | inferred_complete_timeline |
| `Action_None` | 283 | 284 | 2 | inferred_complete_timeline |
| `Action_None` | 287 | 288 | 2 | inferred_complete_timeline |
| `Action_None` | 299 | 300 | 2 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 319 | 185 | inferred_complete_timeline |
| `Action_None` | 322 | 389 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–309
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 309 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_None` | 135 | 243 | 109 | inferred_complete_timeline |
| `Action_None` | 247 | 389 | 143 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–186 | 179 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 17–20 | 4 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 81–86 | 6 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 141–367 | 153 | 6 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 197–389 | 193 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 202–203 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 208–259 | 30 | 8 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 209–389 | 174 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 231–389 | 159 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 235–237 | 3 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 265–389 | 125 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 284–389 | 106 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 291–293 | 3 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 295–296 | 2 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 317–322 | 6 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 322–325 | 4 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 322–389 | 65 | 3 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 332–360 | 28 | 2 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 336–360 | 25 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 354–356 | 3 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 357–389 | 31 | 2 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 358–389 | 30 | 2 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 364–365 | 2 | 1 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 366–389 | 24 | 1 | Undefined position; Undefined team |
| `45` | `61` | Position_Unknown | Team_Unknown | 384–385 | 2 | 1 | Undefined position; Undefined team |
| `46` | `62` | Position_Unknown | Team_Unknown | 385–389 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 110 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 592: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '14' (LT) duration 97 frames exceeds threshold 90 frames [start=138, end=234].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '17' (RG) duration 97 frames exceeds threshold 90 frames [start=138, end=234].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '20' (C) duration 97 frames exceeds threshold 90 frames [start=138, end=234].
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [135–152], lower_priority='Action_DownBlock' annotated_start=138, effective_Action_DownBlock_start=153.
- ⚠️ Action 'Action_None' range [135-290] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-306] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-337] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-202] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-218] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-223] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-276] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-351] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-363] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-280] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-196] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-276] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-327] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-371] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-389] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-173] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-245] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-233] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-279] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-165] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-201] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-254] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-283] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-313] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-389] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-319] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-309] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-230] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-276] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-290] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-315] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [182-208] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [138-167] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [171-205] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-243] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-276] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-293] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-383] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-144] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-188] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-212] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-219] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-230] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-293] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-308] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-243] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [138-234] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-203] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-228] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-337] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [153-172] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [191-220] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [224-234] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-15] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-134] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-142] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-206] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-20] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-86] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-153] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-166] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-238] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-367] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-259] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-247] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-389] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-322] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-330] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-374] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-333] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-360] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-360] for track '39' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-356] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-371] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-360] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-389] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.

</details>
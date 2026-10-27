# Play-Annotation-Generator Annotation Review — Counter_206

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_206`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 111
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `16` | `15` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `11` | `10` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 130 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 131 | START | 131 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `10` | `9` | 132 | START | 145 | 184 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `12` | `11` | 132 | START | 132 | 158 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | Position_Unknown | `16` | `15` | 132 | START | N/A | N/A |
| ✅ EXACT | `Action_PullBlock` | RG | `15` | `14` | 132 | START | 132 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `11` | `10` | 132 | START | 132 | 163 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `4` | `3` | 137 | START | 137 | 168 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 144 | END | 131 | 144 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `4` | 162 | START | 162 | 171 |
| ✅ EXACT | `Action_BallCarry` | RB | `4` | `3` | 172 | START | 172 | 195 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 220 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_SnapReceive` | 131 | 144 | 14 | inferred_complete_timeline |
| `Action_None` | 145 | 161 | 17 | inferred_complete_timeline |
| `Action_Handoff` | 162 | 171 | 10 | inferred_complete_timeline |
| `Action_None` | 172 | 195 | 24 | inferred_complete_timeline |
| `Action_None` | 197 | 320 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 136 | 70 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 137 | 168 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 172 | 195 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–353
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 132 | 163 | 32 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 165 | 220 | 56 | inferred_complete_timeline |
| `Action_None` | 221 | 353 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–250
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 225 | 95 | inferred_complete_timeline |
| `Action_None` | 230 | 250 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_DownBlock` | 132 | 158 | 27 | inferred_complete_timeline |
| `Action_DownBlock` | 162 | 171 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 175 | 178 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 184 | 220 | 37 | inferred_complete_timeline |
| `Action_None` | 221 | 225 | 5 | inferred_complete_timeline |
| `Action_None` | 227 | 229 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_BallSnap` | 131 | 144 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 145 | 184 | 40 | inferred_complete_timeline |
| `Action_DownBlock` | 186 | 192 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 196 | 198 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 202 | 203 | 2 | inferred_complete_timeline |
| `Action_None` | 225 | 230 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |
| `Action_PullBlock` | 132 | 143 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–253
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 156 | 26 | inferred_complete_timeline |
| `Action_None` | 218 | 246 | 29 | inferred_complete_timeline |
| `Action_None` | 250 | 253 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 75 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 93 | 17 | inferred_complete_timeline |
| `Action_None` | 163 | 168 | 6 | inferred_complete_timeline |
| `Action_None` | 187 | 359 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 222 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 176 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_None` | 131 | 226 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 130 | 83 | inferred_complete_timeline |
| `Action_None` | 131 | 167 | 37 | inferred_complete_timeline |
| `Action_None` | 169 | 202 | 34 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_None` | 227 | 240 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–76
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 22–96 | 75 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 40–164 | 125 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 76–343 | 250 | 5 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 143–184 | 42 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 151–166 | 10 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 174–193 | 19 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 178–221 | 44 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 185–359 | 174 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 198–200 | 3 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 226–245 | 20 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 236–249 | 14 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 242–253 | 12 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 253–256 | 4 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 292–359 | 68 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 302–325 | 24 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 307–359 | 51 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 323–359 | 37 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 324–359 | 36 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 336–359 | 23 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 353–355 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (4 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `16` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [131–144], lower_priority='Action_DownBlock' annotated_start=132, effective_Action_DownBlock_start=145.
- ⚠️ Segment 'Action_DownBlock' for track '15' has invalid range: start=132, end=96. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-76] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-222] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [137-168] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [172-195] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-130] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [162-171] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-195] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-320] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-225] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-250] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-226] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-156] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-246] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-253] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-46] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-167] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-202] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-240] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [145-184] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [186-192] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [196-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [202-203] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-230] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-131] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [132-163] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [165-220] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-353] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [132-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [162-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [175-178] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-75] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-359] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-176] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [132-143] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-96] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-164] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-104] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-184] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-328] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-343] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-184] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-188] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-193] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-221] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-222] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-359] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-245] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-249] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-253] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-256] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-325] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-331] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-359] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-343] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-355] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>
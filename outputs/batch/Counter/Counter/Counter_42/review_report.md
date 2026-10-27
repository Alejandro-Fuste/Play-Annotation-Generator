# Play-Annotation-Generator Annotation Review — Counter_42

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_42`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 32
- **Ball Tracks:** 1
- **Action Segments:** 98
- **Validation Warnings:** 104
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `1` | `0` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 151 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 152 | START | 152 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `1` | `0` | 152 | START | 152 | 173 |
| ✅ EXACT | `Action_DownBlock` | LT | `4` | `3` | 152 | START | 152 | 258 |
| ✅ EXACT | `Action_PullBlock` | LG | `9` | `8` | 152 | START | 152 | 258 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `6` | `5` | 152 | START | 152 | 179 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | `3` | `2` | 155 | START | 155 | 198 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 166 | END | 152 | 166 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `12` | 174 | START | 174 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `2` | 202 | START | 202 | 315 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 258 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–318
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_SnapReceive` | 152 | 166 | 15 | inferred_complete_timeline |
| `Action_None` | 167 | 173 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 174 | 201 | 28 | inferred_complete_timeline |
| `Action_None` | 202 | 318 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 155 | 198 | 44 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 202 | 315 | 114 | inferred_complete_timeline |
| `Action_BallCarry` | 317 | 318 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 321 | 323 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 329 | 329 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 152 | 179 | 28 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 185 | 258 | 74 | inferred_complete_timeline |
| `Action_None` | 259 | 267 | 9 | inferred_complete_timeline |
| `Action_None` | 276 | 285 | 10 | inferred_complete_timeline |
| `Action_None` | 288 | 329 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–301
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_DownBlock` | 152 | 258 | 107 | inferred_complete_timeline |
| `Action_None` | 259 | 301 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_PullBlock` | 152 | 258 | 107 | inferred_complete_timeline |
| `Action_None` | 259 | 329 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_BallSnap` | 152 | 166 | 15 | inferred_complete_timeline |
| `Action_None` | 173 | 200 | 28 | inferred_complete_timeline |
| `Action_None` | 202 | 329 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_DownBlock` | 152 | 173 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 178 | 194 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 201 | 251 | 51 | inferred_complete_timeline |
| `Action_DownBlock` | 256 | 258 | 3 | inferred_complete_timeline |
| `Action_None` | 259 | 278 | 20 | inferred_complete_timeline |
| `Action_None` | 281 | 292 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 329 | 178 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–228
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 93 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 148 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 228 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 163 | 12 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 152 | 1 | inferred_complete_timeline |
| `Action_None` | 156 | 158 | 3 | inferred_complete_timeline |
| `Action_None` | 161 | 184 | 24 | inferred_complete_timeline |
| `Action_None` | 187 | 191 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 170 | 19 | inferred_complete_timeline |
| `Action_None` | 196 | 325 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–322
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 274 | 123 | inferred_complete_timeline |
| `Action_None` | 281 | 322 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–292
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 151 | 44 | inferred_complete_timeline |
| `Action_None` | 152 | 241 | 90 | inferred_complete_timeline |
| `Action_None` | 246 | 292 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_None` | 152 | 220 | 69 | inferred_complete_timeline |
| `Action_None` | 222 | 262 | 41 | inferred_complete_timeline |
| `Action_None` | 268 | 271 | 4 | inferred_complete_timeline |
| `Action_None` | 274 | 306 | 33 | inferred_complete_timeline |
| `Action_None` | 313 | 327 | 15 | inferred_complete_timeline |
| `Action_None` | 329 | 329 | 1 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 31–102 | 72 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 56–58 | 3 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 174–329 | 152 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 183–329 | 147 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 184–329 | 146 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 196–315 | 110 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 200–202 | 3 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 219–329 | 101 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 226–327 | 102 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 234–261 | 25 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 243–329 | 65 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 251–329 | 79 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 254–329 | 50 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 282–285 | 4 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 295–300 | 6 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 302–329 | 28 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 304–305 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `20` | 151 | 156 | 6 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `1` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 66 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '0' (RG) duration 107 frames exceeds threshold 90 frames [start=152, end=258].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '3' (LT) duration 107 frames exceeds threshold 90 frames [start=152, end=258].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '8' (LG) duration 107 frames exceeds threshold 90 frames [start=152, end=258].
- ⚠️ Action 'Action_DownBlock' range [152-173] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [178-194] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [201-251] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-278] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-292] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-274] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-322] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [155-198] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [202-315] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [317-318] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [321-323] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-301] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-151] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [152-179] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [181-182] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-267] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-285] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-90] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-241] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-292] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-220] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-262] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-271] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-306] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-327] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-170] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-325] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-163] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-73] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-93] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-148] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-151] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-228] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-318] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [152-166] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-200] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 152, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [152-152] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-184] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-102] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-58] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-203] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-290] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-300] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-308] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-327] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-256] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-300] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>
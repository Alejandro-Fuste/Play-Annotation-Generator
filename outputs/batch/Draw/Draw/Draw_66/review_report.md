# Play-Annotation-Generator Annotation Review — Draw_66

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_66`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `11` | `10` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 33 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `6` | 34 | START | 34 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `11` | `10` | 37 | START | 37 | 101 |
| ✅ EXACT | `Action_PassBlock` | LT | `12` | `11` | 37 | START | 37 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `4` | `3` | 37 | START | 37 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `7` | `6` | 37 | START | 49 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `8` | `7` | 37 | START | 37 | 73 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 48 | END | 34 | 48 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `9` | `8` | 51 | START | 51 | 80 |
| ✅ EXACT | `Action_BallCarry` | QB | `9` | `8` | 81 | START | 81 | 389 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 101 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_SnapReceive` | 34 | 48 | 15 | inferred_complete_timeline |
| `Action_None` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 51 | 80 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 81 | 389 | 309 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 125 | 92 | inferred_complete_timeline |
| `Action_None` | 127 | 149 | 23 | inferred_complete_timeline |
| `Action_None` | 151 | 183 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 101 | 65 | inferred_complete_timeline |
| `Action_None` | 102 | 156 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 101 | 65 | inferred_complete_timeline |
| `Action_None` | 102 | 128 | 27 | inferred_complete_timeline |
| `Action_None` | 131 | 182 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_BallSnap` | 34 | 48 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 101 | 53 | inferred_complete_timeline |
| `Action_None` | 102 | 188 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 73 | 37 | inferred_complete_timeline |
| `Action_PassBlock` | 76 | 96 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PassBlock` | 37 | 64 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 74 | 83 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 88 | 101 | 14 | inferred_complete_timeline |
| `Action_None` | 102 | 258 | 157 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 94 | 61 | inferred_complete_timeline |
| `Action_None` | 98 | 145 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 120 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–262
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 114 | 81 | inferred_complete_timeline |
| `Action_None` | 137 | 159 | 23 | inferred_complete_timeline |
| `Action_None` | 164 | 177 | 14 | inferred_complete_timeline |
| `Action_None` | 179 | 197 | 19 | inferred_complete_timeline |
| `Action_None` | 254 | 262 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 75 | 42 | inferred_complete_timeline |
| `Action_None` | 77 | 79 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 127 | 94 | inferred_complete_timeline |
| `Action_None` | 129 | 176 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 323 | 290 | inferred_complete_timeline |
| `Action_None` | 327 | 329 | 3 | inferred_complete_timeline |
| `Action_None` | 331 | 339 | 9 | inferred_complete_timeline |
| `Action_None` | 342 | 389 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–286
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 197 | 164 | inferred_complete_timeline |
| `Action_None` | 202 | 286 | 85 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `16` | Position_Unknown | Team_Unknown | 80–194 | 79 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 94–170 | 74 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 126–262 | 132 | 5 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 186–389 | 204 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 198–241 | 27 | 3 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 257–342 | 16 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 270–389 | 120 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 306–389 | 73 | 3 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 308–389 | 78 | 3 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 317–389 | 61 | 4 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 321–389 | 65 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 339–389 | 51 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 364–389 | 26 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [34–48], lower_priority='Action_PassBlock' annotated_start=37, effective_Action_PassBlock_start=49.
- ⚠️ Action 'Action_None' range [34-323] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-339] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-127] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-176] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-94] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-145] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-64] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [74-83] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-258] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-197] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-286] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-75] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-188] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [37-73] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [76-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-114] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-159] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-177] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-197] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-262] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-128] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-182] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-156] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-149] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-183] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-83] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-188] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-115] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-170] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-223] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-246] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-254] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-389] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-211] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-237] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-268] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-342] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-325] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-355] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-389] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-323] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-373] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-351] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-362] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-368] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-326] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>
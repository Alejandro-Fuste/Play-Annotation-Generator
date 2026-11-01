# Play-Annotation-Generator Annotation Review — InsideZoneRead_113

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_113`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 101
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `20` | `19` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 7 | START | 7 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 7 | START | 7 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 7 | START | 7 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `13` | `Group` | 7 | START | 7 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 7 | START | 7 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 7 | START | 7 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 7 | START | 7 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 7 | START | 7 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 7 | START | 7 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 7 | START | 7 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 7 | START | 7 | 72 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 70 | START | 70 | 80 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `9` | 73 | START | 73 | 181 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 73 | START | 73 | 168 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `22` | `21` | 73 | START | 81 | 151 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `6` | `5` | 73 | START | 73 | 181 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `9` | `8` | 73 | START | 73 | 181 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 80 | END | 70 | 80 |
| ✅ EXACT | `Action_ReadDefender` | QB | `20` | `19` | 85 | START | 85 | 103 |
| ✅ EXACT | `Action_Handoff` | QB | `20` | `19` | 104 | START | 104 | 115 |
| ✅ EXACT | `Action_BallCarry` | RB | `12` | `11` | 116 | START | 116 | 359 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 181 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 7–303
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 69 | 63 | inferred_complete_timeline |
| `Action_SnapReceive` | 70 | 80 | 11 | inferred_complete_timeline |
| `Action_None` | 81 | 84 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 85 | 103 | 19 | inferred_complete_timeline |
| `Action_Handoff` | 104 | 115 | 12 | inferred_complete_timeline |
| `Action_None` | 116 | 218 | 103 | inferred_complete_timeline |
| `Action_None` | 220 | 303 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 7–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 115 | 109 | inferred_complete_timeline |
| `Action_BallCarry` | 116 | 359 | 244 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 7–155
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 69 | 63 | inferred_complete_timeline |
| `Action_None` | 70 | 155 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 7–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 69 | 63 | inferred_complete_timeline |
| `Action_None` | 70 | 359 | 290 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 7–207
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 69 | 63 | inferred_complete_timeline |
| `Action_None` | 70 | 207 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 7–357
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 69 | 63 | inferred_complete_timeline |
| `Action_None` | 70 | 357 | 288 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 7–337
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 72 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 181 | 109 | inferred_complete_timeline |
| `Action_None` | 182 | 334 | 153 | inferred_complete_timeline |
| `Action_None` | 336 | 337 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 7–226
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 72 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 168 | 96 | inferred_complete_timeline |
| `Action_ZoneBlock` | 171 | 181 | 11 | inferred_complete_timeline |
| `Action_None` | 182 | 202 | 21 | inferred_complete_timeline |
| `Action_None` | 208 | 226 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 7–227
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 69 | 63 | inferred_complete_timeline |
| `Action_BallSnap` | 70 | 80 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 81 | 151 | 71 | inferred_complete_timeline |
| `Action_ZoneBlock` | 161 | 172 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_None` | 182 | 227 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 7–359
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 72 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 181 | 109 | inferred_complete_timeline |
| `Action_None` | 182 | 244 | 63 | inferred_complete_timeline |
| `Action_None` | 248 | 318 | 71 | inferred_complete_timeline |
| `Action_None` | 323 | 359 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 7–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 72 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 181 | 109 | inferred_complete_timeline |
| `Action_None` | 182 | 359 | 178 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 69 | 63 | inferred_complete_timeline |
| `Action_None` | 70 | 145 | 76 | inferred_complete_timeline |
| `Action_None` | 149 | 210 | 62 | inferred_complete_timeline |
| `Action_None` | 212 | 215 | 4 | inferred_complete_timeline |
| `Action_None` | 218 | 359 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 7–222
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 69 | 63 | inferred_complete_timeline |
| `Action_None` | 70 | 156 | 87 | inferred_complete_timeline |
| `Action_None` | 162 | 164 | 3 | inferred_complete_timeline |
| `Action_None` | 169 | 175 | 7 | inferred_complete_timeline |
| `Action_None` | 177 | 222 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 7–86
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 69 | 63 | inferred_complete_timeline |
| `Action_None` | 70 | 86 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 7–218
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 69 | 63 | inferred_complete_timeline |
| `Action_None` | 70 | 81 | 12 | inferred_complete_timeline |
| `Action_None` | 88 | 218 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 69 | 63 | inferred_complete_timeline |
| `Action_None` | 70 | 224 | 155 | inferred_complete_timeline |
| `Action_None` | 226 | 359 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 7–210
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 69 | 63 | inferred_complete_timeline |
| `Action_None` | 70 | 107 | 38 | inferred_complete_timeline |
| `Action_None` | 126 | 132 | 7 | inferred_complete_timeline |
| `Action_None` | 137 | 140 | 4 | inferred_complete_timeline |
| `Action_None` | 163 | 210 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 7–222
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 69 | 63 | inferred_complete_timeline |
| `Action_None` | 70 | 145 | 76 | inferred_complete_timeline |
| `Action_None` | 210 | 222 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 7–173
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 69 | 63 | inferred_complete_timeline |
| `Action_None` | 70 | 173 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 69 | 63 | inferred_complete_timeline |
| `Action_None` | 70 | 212 | 143 | inferred_complete_timeline |
| `Action_None` | 214 | 287 | 74 | inferred_complete_timeline |
| `Action_None` | 289 | 302 | 14 | inferred_complete_timeline |
| `Action_None` | 305 | 359 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 69 | 63 | inferred_complete_timeline |
| `Action_None` | 70 | 359 | 290 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 7–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 69 | 63 | inferred_complete_timeline |
| `Action_None` | 70 | 359 | 290 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 107–131 | 18 | 4 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 145–288 | 139 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 179–186 | 8 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 190–195 | 6 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 197–317 | 121 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 207–359 | 142 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 230–272 | 39 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 247–248 | 2 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 262–264 | 3 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 271–274 | 4 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 292–359 | 68 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 297–316 | 20 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 321–359 | 39 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 328–359 | 32 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 354–359 | 6 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 355–359 | 5 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (RT) duration 109 frames exceeds threshold 90 frames [start=73, end=181].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '8' (LT) duration 109 frames exceeds threshold 90 frames [start=73, end=181].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (RG) duration 109 frames exceeds threshold 90 frames [start=73, end=181].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (LG) duration 109 frames exceeds threshold 90 frames [start=73, end=181].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (C) duration 109 frames exceeds threshold 90 frames [start=73, end=181].
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [70–80], lower_priority='Action_ZoneBlock' annotated_start=73, effective_Action_ZoneBlock_start=81.
- ⚠️ Action 'Action_None' range [70-155] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-359] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-145] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-359] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-207] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-359] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-145] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-222] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-334] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-337] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-244] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-318] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-224] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-359] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-357] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-156] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-175] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-222] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-212] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-287] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-302] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-359] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-86] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-218] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-168] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [171-181] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-202] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-226] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-218] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-303] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-107] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-132] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [81-151] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [161-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-227] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-288] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-186] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-195] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-317] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-304] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-347] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-238] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-272] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-316] for track '33' has 1 frames without a visible bounding box.
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

</details>
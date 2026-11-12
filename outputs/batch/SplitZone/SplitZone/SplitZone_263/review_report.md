# Play-Annotation-Generator Annotation Review — SplitZone_263

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_263`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 66
- **Validation Warnings:** 55
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
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_SplitBlock` | WR2 | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `2` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 29 | START | 29 | 359 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 29 | START | 29 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 29 | START | 29 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 29 | START | 29 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 29 | START | 29 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 29 | START | 29 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 29 | START | 29 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 29 | START | 38 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 29 | START | 29 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 29 | START | 29 | 340 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 29 | START | 29 | 340 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `15` | `15` | 143 | START | 143 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `15` | `15` | 151 | START | 151 | 153 |
| ✅ EXACT | `Action_ZoneBlock` | C | `19` | `19` | 151 | START | 151 | 257 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `20` | `20` | 151 | START | 151 | 257 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 151 | START | 151 | 159 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `3` | `3` | 151 | START | 151 | 167 |
| ✅ EXACT | `Action_SplitBlock` | WR2 | `13` | `13` | 160 | START | 160 | 257 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 161 | END | 161 | 161 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `11` | 165 | START | 165 | 190 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `2` | `2` | 191 | START | 191 | 218 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 257 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 29–306
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 160 | 132 | inferred_complete_timeline |
| `Action_SnapReceive` | 161 | 161 | 1 | inferred_complete_timeline |
| `Action_None` | 162 | 164 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 165 | 190 | 26 | inferred_complete_timeline |
| `Action_None` | 191 | 306 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 29–359
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 190 | 162 | inferred_complete_timeline |
| `Action_BallCarry` | 191 | 218 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 220 | 224 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 227 | 359 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 29–359
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 359 | 331 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 29–359
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 159 | 131 | inferred_complete_timeline |
| `Action_SplitBlock` | 160 | 257 | 98 | inferred_complete_timeline |
| `Action_None` | 258 | 359 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 29–359
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 340 | 312 | inferred_complete_timeline |
| `Action_PreSnap` | 351 | 359 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 29–340
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 340 | 312 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 29–167
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 150 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 167 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 29–359
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 142 | 114 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 143 | 150 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 158 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 162 | 165 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 174 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 186 | 188 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 190 | 257 | 68 | inferred_complete_timeline |
| `Action_None` | 258 | 359 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 29–340
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 150 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 257 | 107 | inferred_complete_timeline |
| `Action_None` | 258 | 340 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 38–359
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 38 | 150 | 113 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 159 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 257 | 91 | inferred_complete_timeline |
| `Action_None` | 258 | 359 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 29–359
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 150 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 151 | 257 | 107 | inferred_complete_timeline |
| `Action_None` | 258 | 270 | 13 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |
| `Action_None` | 283 | 359 | 77 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 29–359
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 359 | 331 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 29–242
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 242 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 29–225
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 186 | 158 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 219 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 29–175
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 175 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 29–359
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 270 | 242 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 359 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 29–359
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 359 | 331 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 29–359
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 253 | 225 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 359 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 29–355
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 355 | 327 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 29–359
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 359 | 331 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 29–359
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 359 | 331 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 29–265
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 265 | 237 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 187–359 | 173 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 203–356 | 154 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 242–359 | 114 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 249–359 | 108 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 274–319 | 46 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 350–359 | 10 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 350–359 | 9 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (7 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 35 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (LG) duration 107 frames exceeds threshold 90 frames [start=151, end=257].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (C) duration 107 frames exceeds threshold 90 frames [start=151, end=257].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RT) duration 107 frames exceeds threshold 90 frames [start=151, end=257].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 107 frames exceeds threshold 90 frames [start=151, end=257].
- ⚠️ Action 'Action_PreSnap' range [29-355] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [191-218] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [220-224] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-167] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-340] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-186] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-219] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-222] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-270] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-242] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-340] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-359] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-306] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-153] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [155-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [162-165] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-174] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [179-181] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [186-188] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-175] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-265] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-253] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-257] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-340] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-257] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-270] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [151-159] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-356] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-270] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-359] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-315] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-319] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-356] for track '28' has 1 frames without a visible bounding box.
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

</details>
# Play-Annotation-Generator Annotation Review — SplitZone_144

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_144`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 105
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
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT | defense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `3` | `3` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `2` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 24 | START | 25 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 24 | START | 25 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 24 | START | 25 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 24 | START | 25 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 24 | START | 25 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 24 | START | 25 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 24 | START | 25 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 24 | START | 25 | 117 |
| ✅ EXACT | `Action_BallSnap` | DT | `14` | `13` | 115 | START | 115 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | `4` | `4` | 118 | START | 118 | 149 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `3` | `3` | 118 | START | 118 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `6` | `5` | 118 | START | 118 | 157 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `6` | 118 | START | 118 | 132 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `8` | `7` | 118 | START | 118 | 150 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 120 | END | 115 | 120 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 128 | START | 128 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `3` | `3` | 129 | START | 129 | 214 |
| ✅ EXACT | `Action_BallCarry` | RB | `2` | `2` | 144 | START | 144 | 153 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 225 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 25–213
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 114 | 90 | inferred_complete_timeline |
| `Action_SnapReceive` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_None` | 121 | 127 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 128 | 143 | 16 | inferred_complete_timeline |
| `Action_None` | 144 | 213 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 25–153
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 143 | 119 | inferred_complete_timeline |
| `Action_BallCarry` | 144 | 153 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 25–165
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 117 | 93 | inferred_complete_timeline |
| `Action_SplitBlock` | 118 | 149 | 32 | inferred_complete_timeline |
| `Action_SplitBlock` | 157 | 165 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 25–213
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 114 | 90 | inferred_complete_timeline |
| `Action_None` | 115 | 213 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 25–299
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 117 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 157 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 225 | 62 | inferred_complete_timeline |
| `Action_None` | 226 | 299 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 25–150
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 117 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 150 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 25–299
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 117 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 128 | 11 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 129 | 214 | 86 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 223 | 225 | 3 | inferred_complete_timeline |
| `Action_None` | 232 | 299 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 25–299
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 117 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 118 | 132 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 225 | 92 | inferred_complete_timeline |
| `Action_None` | 226 | 270 | 45 | inferred_complete_timeline |
| `Action_None` | 272 | 299 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 25–291
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 33 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 114 | 75 | inferred_complete_timeline |
| `Action_None` | 115 | 133 | 19 | inferred_complete_timeline |
| `Action_None` | 157 | 192 | 36 | inferred_complete_timeline |
| `Action_None` | 194 | 291 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 25–296
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 114 | 90 | inferred_complete_timeline |
| `Action_BallSnap` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_None` | 121 | 162 | 42 | inferred_complete_timeline |
| `Action_None` | 166 | 182 | 17 | inferred_complete_timeline |
| `Action_None` | 187 | 195 | 9 | inferred_complete_timeline |
| `Action_None` | 197 | 293 | 97 | inferred_complete_timeline |
| `Action_None` | 295 | 296 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 25–207
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 114 | 90 | inferred_complete_timeline |
| `Action_None` | 115 | 207 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 25–173
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 41 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 114 | 67 | inferred_complete_timeline |
| `Action_None` | 115 | 143 | 29 | inferred_complete_timeline |
| `Action_None` | 169 | 173 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 25–299
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 114 | 90 | inferred_complete_timeline |
| `Action_None` | 115 | 174 | 60 | inferred_complete_timeline |
| `Action_None` | 176 | 299 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 25–139
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 114 | 90 | inferred_complete_timeline |
| `Action_None` | 115 | 139 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 25–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 114 | 90 | inferred_complete_timeline |
| `Action_None` | 115 | 299 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 25–299
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 114 | 90 | inferred_complete_timeline |
| `Action_None` | 115 | 197 | 83 | inferred_complete_timeline |
| `Action_None` | 206 | 299 | 94 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `11` | Position_Unknown | Team_Unknown | 25–51 | 17 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 127–299 | 173 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 129–261 | 55 | 6 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 160–299 | 140 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 161–166 | 6 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 174–299 | 94 | 7 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 178–299 | 114 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 179–299 | 115 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 182–299 | 118 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 184–192 | 7 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 185–299 | 108 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 210–299 | 90 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 224–299 | 76 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 233–299 | 48 | 3 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 242–299 | 58 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 265–299 | 35 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 276–299 | 23 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '3' (RG) duration 97 frames exceeds threshold 90 frames [start=129, end=225].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (LT) duration 108 frames exceeds threshold 90 frames [start=118, end=225].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (RT) duration 108 frames exceeds threshold 90 frames [start=118, end=225].
- ⚠️ Action 'Action_None' range [115-197] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-213] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [144-153] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [129-214] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [216-217] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [223-225] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [118-149] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [157-165] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-157] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-132] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-225] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-270] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [118-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-207] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-33] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-133] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-192] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-291] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-38] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-51] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-213] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-162] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-182] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-195] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-293] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-139] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-41] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-114] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-143] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-299] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-143] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-158] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-181] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-226] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-299] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-166] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-195] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-213] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-258] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-275] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-193] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-299] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-188] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-218] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-248] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-280] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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

</details>
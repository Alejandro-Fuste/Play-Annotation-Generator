# Play-Annotation-Generator Annotation Review — BootPass_99

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_99`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Comp.`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 102
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 3
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `13` | `13` |
| ⚠️ START CHANGED | `Action_RunBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `21` | `21` |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `21` | `21` |
| ⚠️ START CHANGED | `Action_BootAway` | Position_Unknown | Team_Unknown | `21` | `21` |
| ⚠️ START CHANGED | `Action_RunFlatRoute` | RT | offense | `18` | `18` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `21` | `21` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 207 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 33 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 34 | START | 34 | 40 |
| ✅ EXACT | `Action_RunBlock` | LT | `13` | `13` | 40 | START | 40 | 61 |
| ⚠️ START CHANGED | `Action_RunBlock` | C | `14` | `14` | 40 | START | 41 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `16` | `16` | 40 | START | 40 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `18` | `18` | 40 | START | 40 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `20` | `20` | 40 | START | 40 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | Position_Unknown | `21` | `21` | 40 | END | 34 | 37 |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | `21` | `21` | 61 | START | 61 | 80 |
| ⚠️ START CHANGED | `Action_BootAway` | Position_Unknown | `21` | `21` | 82 | START | 83 | 120 |
| ⚠️ START CHANGED | `Action_RunFlatRoute` | RT | `18` | `18` | 88 | START | 89 | 123 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `21` | `21` | 122 | START | 122 | 130 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `0` | `0` | 208 | START | 208 | 239 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 153 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 207 | 208 | inferred_complete_timeline |
| `Action_SecureCatch` | 208 | 239 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 68 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 216 | 183 | inferred_complete_timeline |
| `Action_None` | 220 | 234 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 47 | 14 | inferred_complete_timeline |
| `Action_None` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_None` | 54 | 57 | 4 | inferred_complete_timeline |
| `Action_None` | 89 | 162 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–61
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_RunBlock` | 40 | 61 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_RunBlock` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 59 | 111 | 53 | inferred_complete_timeline |
| `Action_RunBlock` | 115 | 118 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 120 | 151 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_BallSnap` | 34 | 40 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 41 | 54 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–56
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_RunBlock` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 52 | 56 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_RunBlock` | 40 | 43 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 79 | 80 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 89 | 123 | 35 | inferred_complete_timeline |
| `Action_None` | 124 | 188 | 65 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 125 | 92 | inferred_complete_timeline |
| `Action_None` | 127 | 132 | 6 | inferred_complete_timeline |
| `Action_None` | 136 | 156 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 43 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–32
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 32 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 44 | 11 | inferred_complete_timeline |
| `Action_None` | 50 | 68 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 82 | 49 | inferred_complete_timeline |
| `Action_None` | 86 | 179 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 184 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 200 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 239 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 84 | 51 | inferred_complete_timeline |
| `Action_None` | 86 | 225 | 140 | inferred_complete_timeline |
| `Action_None` | 228 | 230 | 3 | inferred_complete_timeline |
| `Action_None` | 233 | 239 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 85 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–146 | 129 | 6 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 17–141 | 115 | 10 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 53–170 | 105 | 6 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 53–54 | 2 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 54–65 | 9 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 92–93 | 2 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 103–239 | 137 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 103–133 | 29 | 2 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 114–153 | 40 | 1 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 116–167 | 46 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 137–152 | 13 | 2 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 140–166 | 21 | 3 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 158–239 | 50 | 2 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 206–239 | 34 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 206–239 | 34 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_RunBlock` for actor_track_id `14` (C): Annotated start 40 != Inferred start 41
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `21` (2 segments found)
- ⚠️ `Action_BootAway` for actor_track_id `21` (Position_Unknown): Annotated start 82 != Inferred start 83
- ⚠️ `Action_RunFlatRoute` for actor_track_id `18` (RT): Annotated start 88 != Inferred start 89

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [34–40], lower_priority='Action_RunBlock' annotated_start=40, effective_Action_RunBlock_start=41.
- ⚠️ Action 'Action_PreSnap' range [0-207] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-125] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-132] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-156] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-84] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-225] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-153] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-85] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-43] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-68] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-200] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-82] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-179] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-216] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-234] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-44] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [40-61] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [41-54] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-47] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-51] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-162] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [40-41] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [59-111] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [115-118] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [120-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-75] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-146] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [40-43] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [79-80] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [82-84] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-188] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-32] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [40-41] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [52-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' for track '21' starts at frame 34, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_SnapReceive' range [34-37] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '21' starts at frame 41, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [41-41] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [61-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-141] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-56] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-65] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-93] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-103] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-123] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-170] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-56] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-65] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-112] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-133] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-153] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-122] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-133] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-167] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-147] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-151] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-166] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-175] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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
# Play-Annotation-Generator Annotation Review — Duo_185

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_185`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 129
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 1
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | LG | offense | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | offense | `23` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `29` | `28` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `21` | `Group` | 0 | START | 68 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `22` | `Group` | 0 | START | 68 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `23` | `Group` | 0 | START | 68 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 132 |
| ✅ EXACT | `Action_ComboBlock` | LG | `12` | `12` | 114 | START | 114 | 159 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | Position_Unknown | `16` | `16` | 114 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | `23` | `23` | 114 | START | 114 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | `29` | `28` | 114 | START | 114 | 114 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 161 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 200 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 175 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 181 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 199 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 192 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 68–196
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 68 | 132 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 186 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 196 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 68–200
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 68 | 83 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 93 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 188 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 195 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 200 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 5 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 79 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 200 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 5 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 108 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_ComboBlock` | 114 | 159 | 46 | inferred_complete_timeline |
| `Action_None` | 164 | 188 | 25 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 102 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 108 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 149 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 192 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 200 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `23`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 68–180
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 68 | 79 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 113 | 15 | inferred_complete_timeline |
| `Action_ComboBlock` | 114 | 136 | 23 | inferred_complete_timeline |
| `Action_ComboBlock` | 138 | 161 | 24 | inferred_complete_timeline |
| `Action_None` | 162 | 176 | 15 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 164 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 184 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 188 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 3 | 26 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 170 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 184 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 184 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–17 | 12 | 4 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–5 | 5 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–5 | 4 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–5 | 4 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–5 | 4 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–5 | 4 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 106–200 | 95 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 106–200 | 58 | 4 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 106–196 | 16 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 106–176 | 55 | 6 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 106–139 | 15 | 4 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 134–187 | 49 | 3 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 147–167 | 19 | 3 | Undefined position; Undefined team |
| `31` | `32` | Position_Unknown | Team_Unknown | 165–200 | 34 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ComboBlock` on target `16` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `23` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `29` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 97 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ComboBlock' for track '16' has invalid range: start=114, end=5. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-151] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-175] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-181] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-200] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-187] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-176] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-200] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-132] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-200] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-190] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-176] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-184] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-102] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-149] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-192] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-200] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-108] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [114-159] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-79] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-200] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-134] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-164] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-184] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-188] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-26] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-170] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-184] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-132] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-186] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-196] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-83] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-93] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-188] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-195] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-200] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-79] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-87] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-113] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [114-136] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [138-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-176] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-200] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-139] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-184] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-200] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-119] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-196] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-126] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-130] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-145] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-148] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-159] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-176] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-113] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' for track '28' starts at frame 114, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ComboBlock' range [114-114] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [116-117] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [136-139] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-138] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-142] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-187] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-154] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-164] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-167] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-172] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-200] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>
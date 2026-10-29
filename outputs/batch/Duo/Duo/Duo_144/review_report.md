# Play-Annotation-Generator Annotation Review — Duo_144

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_144`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | offense | `3` | `3` |
| ✅ EXACT | `Action_ComboBlock` | RG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | offense | `9` | `9` |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `14` | `Group` | 0 | START | 0 | 205 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 79 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | `12` | `12` | 80 | START | 80 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | `3` | `3` | 80 | START | 80 | 104 |
| ✅ EXACT | `Action_ComboBlock` | RG | `7` | `7` | 80 | START | 80 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | `9` | `9` | 80 | START | 80 | 80 |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | `7` | `7` | 101 | START | 101 | 123 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 130 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 126 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 209 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 170 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 185 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 194 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 205 | 206 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 208 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_ComboBlock` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_ComboBlock` | 88 | 105 | 18 | inferred_complete_timeline |
| `Action_ComboBlock` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 111 | 124 | 14 | inferred_complete_timeline |
| `Action_None` | 169 | 209 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_ComboBlock` | 80 | 80 | 1 | inferred_complete_timeline |
| `Action_ComboBlock` | 82 | 130 | 49 | inferred_complete_timeline |
| `Action_None` | 131 | 146 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–192
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_ComboBlock` | 80 | 100 | 21 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 101 | 123 | 23 | inferred_complete_timeline |
| `Action_None` | 132 | 189 | 58 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_ComboBlock` | 80 | 104 | 25 | inferred_complete_timeline |
| `Action_ComboBlock` | 107 | 130 | 24 | inferred_complete_timeline |
| `Action_None` | 131 | 133 | 3 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 198 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 206 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 163 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 209 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 175 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 157 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 194 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 207 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 159 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 206 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–209 | 206 | 2 | Undefined position; Undefined team |
| `16` | `26` | Position_Unknown | Team_Unknown | 122–209 | 88 | 1 | Undefined position; Undefined team |
| `17` | `28` | Position_Unknown | Team_Unknown | 133–139 | 5 | 2 | Undefined position; Undefined team |
| `18` | `29` | Position_Unknown | Team_Unknown | 145–209 | 59 | 2 | Undefined position; Undefined team |
| `19` | `30` | Position_Unknown | Team_Unknown | 149–209 | 57 | 3 | Undefined position; Undefined team |
| `20` | `31` | Position_Unknown | Team_Unknown | 176–209 | 34 | 1 | Undefined position; Undefined team |
| `21` | `32` | Position_Unknown | Team_Unknown | 181–185 | 5 | 1 | Undefined position; Undefined team |
| `22` | `34` | Position_Unknown | Team_Unknown | 183–209 | 27 | 1 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 185–208 | 24 | 1 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 187–209 | 4 | 2 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 207–209 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 290: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-171] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-175] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-147] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-159] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-206] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-209] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [80-104] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-139] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-170] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-185] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-194] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-209] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-153] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-157] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-194] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-207] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [101-123] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-189] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-147] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-189] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-198] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-201] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-206] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' for track '9' starts at frame 80, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ComboBlock' range [80-80] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-146] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-192] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-209] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-163] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-209] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [80-82] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [88-105] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [107-108] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [111-124] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-209] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-205] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-208] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-118] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-126] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-209] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-209] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-139] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-200] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-209] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-179] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-188] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-209] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-185] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-209] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-208] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-209] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-209] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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

</details>
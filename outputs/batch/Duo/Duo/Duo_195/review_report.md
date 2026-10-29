# Play-Annotation-Generator Annotation Review — Duo_195

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_195`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 1
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 57
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | offense | `11` | `11` |
| ⚠️ START CHANGED | `Action_ComboBlock` | LG | offense | `16` | `16` |
| ✅ EXACT | `Action_ComboBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `17` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 225 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 75 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `13` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 0 | START | 0 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | `11` | `11` | 94 | START | 96 | 116 |
| ⚠️ START CHANGED | `Action_ComboBlock` | LG | `16` | `16` | 94 | START | 104 | 110 |
| ✅ EXACT | `Action_ComboBlock` | C | `17` | `17` | 94 | START | 94 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | `18` | `18` | 94 | START | 94 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `17` | `17` | 107 | START | 107 | 122 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 145 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 141 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 158 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 41 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 139 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 170 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 184 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 225 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 83 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 113 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 123 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 43 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 82 | 22 | inferred_complete_timeline |
| `Action_ComboBlock` | 104 | 110 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_ComboBlock` | 94 | 106 | 13 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 107 | 122 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 135 | 145 | 11 | inferred_complete_timeline |
| `Action_None` | 146 | 225 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 84 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 89 | 3 | inferred_complete_timeline |
| `Action_ComboBlock` | 96 | 116 | 21 | inferred_complete_timeline |
| `Action_ComboBlock` | 138 | 142 | 5 | inferred_complete_timeline |
| `Action_None` | 219 | 225 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_ComboBlock` | 94 | 94 | 1 | inferred_complete_timeline |
| `Action_ComboBlock` | 102 | 106 | 5 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 225 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 137 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 225 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 125 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 163 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 170 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 225 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 125 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 167 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 225 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 135 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 225 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 216 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 225 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 18–187 | 156 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 43–206 | 95 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 48–49 | 2 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 51–96 | 44 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 63–225 | 141 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 141–223 | 78 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 145–148 | 4 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 151–225 | 62 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 163–197 | 35 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 189–225 | 37 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 193–225 | 33 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 202–225 | 24 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 206–225 | 20 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 211–225 | 11 | 2 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 215–225 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `11` (2 segments found)
- ⚠️ `Action_ComboBlock` for actor_track_id `16` (LG): Annotated start 94 != Inferred start 104
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 85 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-122] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-225] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-83] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-113] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-123] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-141] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-158] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-196] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-216] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-225] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-137] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-225] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-87] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-139] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-170] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-173] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-184] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-225] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-225] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-84] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-89] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [96-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [138-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-225] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-125] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-163] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-170] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-225] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-167] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-225] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-45] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-225] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-43] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-82] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [104-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [107-122] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [135-145] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-225] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' for track '18' starts at frame 94, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ComboBlock' range [94-94] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [102-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-225] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-79] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-144] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-47] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-206] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-65] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-90] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-164] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-178] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-211] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-225] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-192] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-223] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-148] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-157] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-225] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-197] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-225] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-225] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-225] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [206-225] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-217] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-225] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-225] for track '33' has 3 frames without a visible bounding box.
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

</details>
# Play-Annotation-Generator Annotation Review — Duo_152

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_152`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 1
- **Action Segments:** 75
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_ComboBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | offense | `9` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `10` | `Group` | 0 | START | 0 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 0 | START | 0 | 155 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 130 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 84 |
| ✅ EXACT | `Action_ComboBlock` | RT | `13` | `13` | 85 | START | 85 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | `17` | `17` | 85 | START | 85 | 85 |
| ✅ EXACT | `Action_ComboBlock` | LG | `19` | `19` | 85 | START | 85 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | `9` | `9` | 85 | START | 85 | 104 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 143 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–105
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 60 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 105 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 160 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 209 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 90 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 109 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 131 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 134 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 184 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ComboBlock` | 85 | 143 | 59 | inferred_complete_timeline |
| `Action_None` | 144 | 149 | 6 | inferred_complete_timeline |
| `Action_None` | 155 | 209 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_ComboBlock` | 85 | 85 | 1 | inferred_complete_timeline |
| `Action_ComboBlock` | 87 | 99 | 13 | inferred_complete_timeline |
| `Action_ComboBlock` | 101 | 110 | 10 | inferred_complete_timeline |
| `Action_ComboBlock` | 112 | 143 | 32 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_None` | 148 | 209 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_ComboBlock` | 85 | 104 | 20 | inferred_complete_timeline |
| `Action_ComboBlock` | 109 | 113 | 5 | inferred_complete_timeline |
| `Action_ComboBlock` | 120 | 124 | 5 | inferred_complete_timeline |
| `Action_ComboBlock` | 128 | 131 | 4 | inferred_complete_timeline |
| `Action_None` | 146 | 209 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_ComboBlock` | 85 | 143 | 59 | inferred_complete_timeline |
| `Action_None` | 144 | 209 | 66 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 209 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 130 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 154 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–209 | 151 | 9 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 107–176 | 66 | 3 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 152–209 | 51 | 4 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 161–162 | 2 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 163–165 | 3 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 171–199 | 29 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 176–182 | 7 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 185–209 | 25 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 190–208 | 12 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `20` | `23` | 58 | 59 | 2 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `9` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 71 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-209] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-209] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-209] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-154] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-154] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-76] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-90] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-109] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-131] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-184] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-209] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-130] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-209] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [85-104] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [109-113] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [120-124] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [128-131] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-209] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-209] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-209] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-209] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-166] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-209] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-130] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-39] for track '16' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-168] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-188] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-209] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' for track '17' starts at frame 85, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ComboBlock' range [85-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [87-99] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [101-110] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-209] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-60] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-105] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [85-143] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-134] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-176] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-155] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-159] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-166] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-209] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-162] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-165] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-199] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-182] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-209] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-202] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-208] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>
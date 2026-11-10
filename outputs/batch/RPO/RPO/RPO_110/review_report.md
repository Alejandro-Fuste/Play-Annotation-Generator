# Play-Annotation-Generator Annotation Review — RPO_110

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_110`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 1
- **Action Segments:** 95
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunFadeRoute` | actor_track_id `35` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_PullBall` | RB | offense | `11` | `11` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `16` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `5` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `0` | `0` | 67 | START | 67 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `15` | `15` | 67 | START | 67 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `18` | 67 | START | 67 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `8` | 67 | START | 67 | 96 |
| ✅ EXACT | `Action_ZoneBlock` | C | `9` | `9` | 67 | START | 67 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ReadDefender` | QB | `6` | `6` | 74 | START | 74 | 93 |
| ✅ EXACT | `Action_PullBall` | RB | `11` | `11` | 88 | START | 88 | 96 |
| ✅ EXACT | `Action_ThrowPass` | RB | `11` | `11` | 119 | START | 119 | 125 |

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
- **Visible Frames:** 0–106
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 73 | 8 | inferred_complete_timeline |
| `Action_ReadDefender` | 74 | 93 | 20 | inferred_complete_timeline |
| `Action_ReadDefender` | 104 | 106 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 87 | 22 | inferred_complete_timeline |
| `Action_PullBall` | 88 | 96 | 9 | inferred_complete_timeline |
| `Action_None` | 97 | 118 | 22 | inferred_complete_timeline |
| `Action_ThrowPass` | 119 | 125 | 7 | inferred_complete_timeline |
| `Action_None` | 126 | 204 | 79 | inferred_complete_timeline |
| `Action_None` | 216 | 233 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 82 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 86 | 21 | inferred_complete_timeline |
| `Action_None` | 141 | 228 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 66 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 97 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 125 | 22 | inferred_complete_timeline |
| `Action_None` | 126 | 238 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 66 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 84 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 125 | 40 | inferred_complete_timeline |
| `Action_None` | 126 | 126 | 1 | inferred_complete_timeline |
| `Action_None` | 134 | 223 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 66 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 122 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 66 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 74 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 82 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 66 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 96 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 104 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 125 | 14 | inferred_complete_timeline |
| `Action_None` | 126 | 148 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 98 | 33 | inferred_complete_timeline |
| `Action_None` | 102 | 181 | 80 | inferred_complete_timeline |
| `Action_None` | 186 | 229 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 112 | 47 | inferred_complete_timeline |
| `Action_None` | 114 | 239 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 90 | 25 | inferred_complete_timeline |
| `Action_None` | 94 | 116 | 23 | inferred_complete_timeline |
| `Action_None` | 118 | 230 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 101 | 36 | inferred_complete_timeline |
| `Action_None` | 133 | 224 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 171 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–218
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 114 | 49 | inferred_complete_timeline |
| `Action_None` | 118 | 141 | 24 | inferred_complete_timeline |
| `Action_None` | 146 | 195 | 50 | inferred_complete_timeline |
| `Action_None` | 197 | 202 | 6 | inferred_complete_timeline |
| `Action_None` | 204 | 212 | 9 | inferred_complete_timeline |
| `Action_None` | 214 | 218 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 232 | 167 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 239 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_None` | 66 | 72 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 69–71 | 3 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 71–101 | 31 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 105–116 | 11 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 105–225 | 121 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 119–213 | 77 | 3 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 122–233 | 108 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 126–216 | 82 | 3 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 152–161 | 9 | 2 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 154–239 | 86 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 161–219 | 53 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 164–211 | 48 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 195–237 | 43 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 223–224 | 2 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 226–231 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `19` | `19` | 0 | 57 | 58 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ReadDefender` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 202: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_ZoneBlock' range [67-97] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-238] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-171] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-232] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-112] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-114] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-141] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-195] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-212] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-218] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-82] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [74-93] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [104-106] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-96] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-104] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-148] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-122] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-224] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-204] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-233] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-98] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-181] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-229] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-90] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-230] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 126, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [126-126] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-223] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-86] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-228] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-72] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-74] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-71] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-101] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-111] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-225] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-154] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-213] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-125] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-162] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-177] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-216] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-161] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-239] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-211] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-211] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-237] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-231] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>